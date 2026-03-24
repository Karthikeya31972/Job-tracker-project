import express from 'express';
import { applyJob, getAppliedJobs, getApplicants, updateApplicationStatus, deleteApplication } from '../controllers/application.controller.js';
import authenticateToken from '../middleware/isAuthenticated.js';

const router = express.Router();

router.route("/apply/:id").post(authenticateToken, applyJob);
router.route("/get").get(authenticateToken, getAppliedJobs);
router.route("/applicants/:id").get(authenticateToken, getApplicants);
router.route("/status/:applicationId").put(authenticateToken, updateApplicationStatus);
router.route("/delete/:applicationId").delete(authenticateToken, deleteApplication);

export default router;
