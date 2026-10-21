const { Document, Packer, Paragraph, TextRun, AlignmentType } = require("docx");
const fs = require("fs");

// Create document
const doc = new Document({
  sections: [
    {
      children: [

        // Title Page
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "MINI PROJECT REPORT", bold: true, size: 40 }),
          ],
        }),

        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "JOB TRACKING SYSTEM", bold: true, size: 36 }),
          ],
        }),

        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: " ", size: 24 }),
          ],
        }),

        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Submitted By", bold: true }),
          ],
        }),

        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "ARE KARTHIKEYA", bold: true }),
          ],
        }),

        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Your Roll Number", bold: true }),
          ],
        }),

        new Paragraph({
          children: [new TextRun("")],
        }),

        // Abstract
        new Paragraph({
          children: [
            new TextRun({ text: "ABSTRACT", bold: true, size: 32 }),
          ],
        }),

        new Paragraph({
          children: [
            new TextRun(
              "This project is a Job Tracking System designed to help users manage job applications efficiently. It allows users to track job status, manage resumes, and analyze skills."
            ),
          ],
        }),

        // Introduction
        new Paragraph({
          children: [
            new TextRun({ text: "INTRODUCTION", bold: true, size: 32 }),
          ],
        }),

        new Paragraph({
          children: [
            new TextRun(
              "The Job Tracking System helps job seekers manage multiple applications and track their progress."
            ),
          ],
        }),

        // Conclusion
        new Paragraph({
          children: [
            new TextRun({ text: "CONCLUSION", bold: true, size: 32 }),
          ],
        }),

        new Paragraph({
          children: [
            new TextRun(
              "This system improves efficiency and organization for job seekers."
            ),
          ],
        }),

      ],
    },
  ],
});

// Save file
Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("Job_Tracking_System_Report.docx", buffer);
  console.log("DOCX file created successfully!");
});