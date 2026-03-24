import { Job } from "../models/job.model.js";
import { Company } from "../models/company.model.js";

export const postJob = async (req, res) => {
    try {
        const { title, description, requirements, salary, jobType, position, companyId } = req.body;
        
        if (!title || !description || !requirements || !salary || !jobType || !position || !companyId) {
            return res.status(400).json({
                message: "All fields are required",
                success: false
            });
        }

        const company = await Company.findById(companyId);
        if (!company) {
            return res.status(404).json({
                message: "Company not found",
                success: false
            });
        }

        const job = await Job.create({
            title,
            description,
            requirements,
            salary: Number(salary),
            jobType,
            position,
            company: companyId,
            created_by: req.id
        });

        return res.status(201).json({
            message: "Job posted successfully",
            job,
            success: true
        });

    } catch (error) {
        console.error("Error posting job:", error);
        return res.status(500).json({
            message: "Server error while posting job",
            success: false
        });
    }
};

export const getAllJobs = async (req, res) => {
    try {
        const keyword = req.query.keyword || "";
        const query = {
            $or: [
                { title: { $regex: keyword, $options: "i" } },
                { description: { $regex: keyword, $options: "i" } }
            ]
        };

        const jobs = await Job.find(query)
            .populate({
                path: "company"
            })
            .sort({ createdAt: -1 });

        if (!jobs || jobs.length === 0) {
            return res.status(404).json({
                message: "No jobs found",
                success: false
            });
        }

        return res.status(200).json({
            jobs,
            success: true
        });

    } catch (error) {
        console.error("Error fetching jobs:", error);
        return res.status(500).json({
            message: "Server error while fetching jobs",
            success: false
        });
    }
};

export const getJobById = async (req, res) => {
    try {
        const jobId = req.params.id;
        const job = await Job.findById(jobId)
            .populate({
                path: "company"
            })
            .populate({
                path: "created_by",
                select: "fullname email"
            });

        if (!job) {
            return res.status(404).json({
                message: "Job not found",
                success: false
            });
        }

        return res.status(200).json({
            job,
            success: true
        });

    } catch (error) {
        console.error("Error fetching job:", error);
        return res.status(500).json({
            message: "Server error while fetching job",
            success: false
        });
    }
};

export const getAdminJobs = async (req, res) => {
    try {
        const adminId = req.id;
        const jobs = await Job.find({ created_by: adminId })
            .populate({
                path: "company"
            })
            .sort({ createdAt: -1 });

        if (!jobs || jobs.length === 0) {
            return res.status(404).json({
                message: "No jobs posted by you",
                success: false
            });
        }

        return res.status(200).json({
            jobs,
            success: true
        });

    } catch (error) {
        console.error("Error fetching admin jobs:", error);
        return res.status(500).json({
            message: "Server error while fetching admin jobs",
            success: false
        });
    }
};

export const updateJob = async (req, res) => {
    try {
        const jobId = req.params.id;
        const { title, description, requirements, salary, jobType, position } = req.body;

        const job = await Job.findById(jobId);
        if (!job) {
            return res.status(404).json({
                message: "Job not found",
                success: false
            });
        }

        if (job.created_by.toString() !== req.id) {
            return res.status(403).json({
                message: "You are not authorized to update this job",
                success: false
            });
        }

        const updatedJob = await Job.findByIdAndUpdate(
            jobId,
            { title, description, requirements, salary: Number(salary), jobType, position },
            { new: true, runValidators: true }
        ).populate("company");

        return res.status(200).json({
            message: "Job updated successfully",
            job: updatedJob,
            success: true
        });

    } catch (error) {
        console.error("Error updating job:", error);
        return res.status(500).json({
            message: "Server error while updating job",
            success: false
        });
    }
};

export const deleteJob = async (req, res) => {
    try {
        const jobId = req.params.id;

        const job = await Job.findById(jobId);
        if (!job) {
            return res.status(404).json({
                message: "Job not found",
                success: false
            });
        }

        if (job.created_by.toString() !== req.id) {
            return res.status(403).json({
                message: "You are not authorized to delete this job",
                success: false
            });
        }

        await Job.findByIdAndDelete(jobId);

        return res.status(200).json({
            message: "Job deleted successfully",
            success: true
        });

    } catch (error) {
        console.error("Error deleting job:", error);
        return res.status(500).json({
            message: "Server error while deleting job",
            success: false
        });
    }
};
