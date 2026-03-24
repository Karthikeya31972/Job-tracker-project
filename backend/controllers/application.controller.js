import { Application } from "../models/application.model.js";
import { Job } from "../models/job.model.js";
import { User } from "../models/user.model.js";

export const applyJob = async (req, res) => {
    try {
        const jobId = req.params.id;
        const userId = req.id;

        const job = await Job.findById(jobId);
        if (!job) {
            return res.status(404).json({
                message: "Job not found",
                success: false
            });
        }

        const existingApplication = await Application.findOne({
            job: jobId,
            applicant: userId
        });

        if (existingApplication) {
            return res.status(400).json({
                message: "You have already applied for this job",
                success: false
            });
        }

        const application = await Application.create({
            job: jobId,
            applicant: userId
        });

        await application.populate([
            { path: 'job', populate: { path: 'company' } },
            { path: 'applicant', select: 'fullname email' }
        ]);

        return res.status(201).json({
            message: "Job application submitted successfully",
            application,
            success: true
        });

    } catch (error) {
        console.error("Error applying for job:", error);
        return res.status(500).json({
            message: "Server error while applying for job",
            success: false
        });
    }
};

export const getAppliedJobs = async (req, res) => {
    try {
        const userId = req.id;
        
        const applications = await Application.find({ applicant: userId })
            .populate({
                path: 'job',
                populate: {
                    path: 'company'
                }
            })
            .sort({ createdAt: -1 });

        if (!applications || applications.length === 0) {
            return res.status(404).json({
                message: "No job applications found",
                success: false
            });
        }

        return res.status(200).json({
            applications,
            success: true
        });

    } catch (error) {
        console.error("Error fetching applied jobs:", error);
        return res.status(500).json({
            message: "Server error while fetching applied jobs",
            success: false
        });
    }
};

export const getApplicants = async (req, res) => {
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
                message: "You are not authorized to view applicants for this job",
                success: false
            });
        }

        const applications = await Application.find({ job: jobId })
            .populate({
                path: 'applicant',
                select: 'fullname email phoneNumber profile.bio profile.skills profile.resume'
            })
            .sort({ createdAt: -1 });

        if (!applications || applications.length === 0) {
            return res.status(404).json({
                message: "No applicants found for this job",
                success: false
            });
        }

        return res.status(200).json({
            applications,
            success: true
        });

    } catch (error) {
        console.error("Error fetching applicants:", error);
        return res.status(500).json({
            message: "Server error while fetching applicants",
            success: false
        });
    }
};

export const updateApplicationStatus = async (req, res) => {
    try {
        const { applicationId } = req.params;
        const { status } = req.body;

        if (!['pending', 'accepted', 'rejected'].includes(status)) {
            return res.status(400).json({
                message: "Invalid status. Must be pending, accepted, or rejected",
                success: false
            });
        }

        const application = await Application.findById(applicationId)
            .populate({
                path: 'job',
                select: 'created_by'
            });

        if (!application) {
            return res.status(404).json({
                message: "Application not found",
                success: false
            });
        }

        if (application.job.created_by.toString() !== req.id) {
            return res.status(403).json({
                message: "You are not authorized to update this application status",
                success: false
            });
        }

        const updatedApplication = await Application.findByIdAndUpdate(
            applicationId,
            { status },
            { new: true }
        ).populate([
            { path: 'job', populate: { path: 'company' } },
            { path: 'applicant', select: 'fullname email' }
        ]);

        return res.status(200).json({
            message: `Application status updated to ${status}`,
            application: updatedApplication,
            success: true
        });

    } catch (error) {
        console.error("Error updating application status:", error);
        return res.status(500).json({
            message: "Server error while updating application status",
            success: false
        });
    }
};

export const deleteApplication = async (req, res) => {
    try {
        const { applicationId } = req.params;
        const userId = req.id;

        const application = await Application.findById(applicationId);
        if (!application) {
            return res.status(404).json({
                message: "Application not found",
                success: false
            });
        }

        if (application.applicant.toString() !== userId) {
            return res.status(403).json({
                message: "You are not authorized to delete this application",
                success: false
            });
        }

        await Application.findByIdAndDelete(applicationId);

        return res.status(200).json({
            message: "Application deleted successfully",
            success: true
        });

    } catch (error) {
        console.error("Error deleting application:", error);
        return res.status(500).json({
            message: "Server error while deleting application",
            success: false
        });
    }
};
