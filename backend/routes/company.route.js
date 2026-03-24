import express from 'express';
import { registerCompany, getAllCompanies, getCompanyById, updateCompany } from '../controllers/company.controller.js';
import authenticateToken from '../middleware/isAuthenticated.js';
import upload from '../middleware/multer.js';

const router = express.Router();

router.route("/register").post(authenticateToken, registerCompany);
router.route("/get").get(authenticateToken, getAllCompanies);
router.route("/get/:id").get(authenticateToken, getCompanyById);
router.route("/update/:id").put(authenticateToken, upload.single('logo'), updateCompany);

export default router;
