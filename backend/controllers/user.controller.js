import { User } from "../models/user.model.js";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";

// REGISTER
export const register = async (req, res) => {
    try {
        const { fullname, email, phoneNumber, password, role } = req.body;

        if (!fullname || !email || !phoneNumber || !password || !role) {
            return res.status(400).json({
                message: "Missing required fields",
                success: false,
            });
        }

        let user = await User.findOne({ email });

        if (user) {
            return res.status(400).json({
                message: "Email already exists",
                success: false,
            });
        }

        const hashedPassword = await bcrypt.hash(password, 10);

        const newUser = new User({
            fullname,
            email,
            phoneNumber,
            password: hashedPassword,
            role,
        });

        await newUser.save();

        return res.status(200).json({
            message: `Account Created Successfully ${fullname}`,
            success: true,
        });

    } catch (error) {
        console.log(error);
        res.status(500).json({
            message: "Server Error Register user",
            success: false,
        });
    }
};
//login
export const login = async (req, res) => {
    try {
        const { email, password, role } = req.body;

        if (!email || !password || !role) {
            return res.status(400).json({
                message: "All fields are required",
                success: false,
            });
        }

        const user = await User.findOne({ email });

        if (!user) {
            return res.status(400).json({
                message: "Invalid email or password",
                success: false,
            });
        }

        const isMatch = await bcrypt.compare(password, user.password);

        if (!isMatch) {
            return res.status(400).json({
                message: "Invalid email or password",
                success: false,
            });
        }

        if (user.role !== role) {
            return res.status(400).json({
                message: "Invalid credentials",
                success: false,
            });
        }

        const token = jwt.sign(
            { userId: user._id },
            process.env.JWT_SECRET,
            { expiresIn: "1d" }
        );

        return res
            .status(200)
            .cookie("token", token, {
                httpOnly: true,
                maxAge: 24 * 60 * 60 * 1000,
                sameSite: "Strict",
                secure: process.env.NODE_ENV === "production",
            })
            .json({
                message: `Welcome Back ${user.fullname}`,
                success: true,
                user: {
                    id: user._id,
                    fullname: user.fullname,
                    email: user.email,
                    role: user.role,
                },
            });

    } catch (error) {
        console.error("Login Error:", error.message);
        return res.status(500).json({
            message: "Server Error",
            success: false,
        });
    }
};
// LOGOUT
export const logout = (req, res) => {
    try {
        return res
            .status(200)
            .cookie("token", "", {
                httpOnly: true,
                expires: new Date(0),
                sameSite: "Strict",
                secure: process.env.NODE_ENV === "production",
            })
            .json({
                message: "Logged out Successfully",
                success: true,
            });

    } catch (error) {
        console.log(error);
        return res.status(500).json({
            message: "Server Error",
            success: false,
        });
    }
};
// UPDATE PROFILE
export const updateProfile = async (req, res) => {
    try {
        const { fullname, email, phoneNumber, bio, skills } = req.body;
        const file = req.file;

        let skillsArray;

        if (skills) {
            skillsArray = skills.split(",");
        }

        const userId = req.id;

        let user = await User.findById(userId);

        if (!user) {
            return res.status(404).json({
                message: "User Not Found",
                success: false,
            });
        }

        // update fields safely
        if (fullname) user.fullname = fullname;
        if (email) user.email = email;
        if (phoneNumber) user.phoneNumber = phoneNumber;

        if (bio) user.profile.bio = bio;
        if (skills) user.profile.skills = skillsArray;

        await user.save();

        return res.status(200).json({
            message: "Profile updated successfully",
            success: true,
            user
        });

    } catch (error) {
        console.log(error);
        return res.status(500).json({
            message: "Server Error updating profile",
            success: false,
        });
    }
};
