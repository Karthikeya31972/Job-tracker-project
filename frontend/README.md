# Job Portal Frontend

A modern React-based frontend for the Job Portal application built with Vite, Tailwind CSS, and Redux Toolkit.

## Features

- **Authentication**: User registration, login, and logout
- **Dashboard**: Role-based dashboards for job seekers and recruiters
- **Job Management**: Browse, search, and apply for jobs
- **Company Management**: Create and manage company profiles
- **Application Tracking**: Track job application status
- **Profile Management**: Update user profiles and skills
- **Responsive Design**: Mobile-first responsive UI

## Tech Stack

- **React 18** - UI framework
- **Vite** - Build tool and development server
- **React Router** - Client-side routing
- **Redux Toolkit** - State management
- **Tailwind CSS** - Utility-first CSS framework
- **React Hook Form** - Form handling
- **React Hot Toast** - Toast notifications
- **React Icons** - Icon library
- **Axios** - HTTP client

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd job-portal/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:5173`

### Environment Variables

Create a `.env` file in the root directory:

```env
VITE_API_URL=http://localhost:5011
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Project Structure

```
src/
├── components/          # Reusable components
│   ├── Layout.jsx      # Main layout component
│   └── ProtectedRoute.jsx # Route protection wrapper
├── pages/               # Page components
│   ├── auth/           # Authentication pages
│   ├── Home.jsx        # Landing page
│   ├── Jobs.jsx        # Job listings
│   ├── JobDetails.jsx  # Individual job details
│   ├── Dashboard.jsx   # User dashboard
│   ├── Profile.jsx     # User profile
│   ├── Companies.jsx   # Company management
│   ├── CompanySetup.jsx # Company creation/editing
│   ├── PostJob.jsx     # Job posting
│   ├── MyJobs.jsx      # User's job postings
│   ├── Applications.jsx # User's applications
│   └── Applicants.jsx  # Job applicants management
├── redux/              # Redux store and slices
│   ├── features/       # Feature slices
│   └── store.js        # Redux store configuration
├── utils/              # Utility functions
│   └── api.js         # API configuration
├── App.jsx             # Main App component
├── main.jsx           # Application entry point
└── index.css          # Global styles and Tailwind imports
```

## Features Overview

### For Job Seekers
- Browse and search job listings
- Apply for jobs with one click
- Track application status
- Update profile and skills
- Upload resume

### For Recruiters
- Create and manage company profiles
- Post job listings
- Review and manage applications
- Update application status (accept/reject)
- Track job performance

### Authentication
- Role-based access control (Job Seeker/Recruiter)
- Secure JWT-based authentication
- Protected routes
- Automatic logout on token expiration

## API Integration

The frontend communicates with the backend API through Axios with the following endpoints:

### Authentication
- `POST /api/user/register` - User registration
- `POST /api/user/login` - User login
- `POST /api/user/logout` - User logout
- `POST /api/user/profile/update` - Update profile

### Jobs
- `GET /api/job/get` - Get all jobs
- `GET /api/job/get/:id` - Get job by ID
- `POST /api/job/post` - Post new job
- `PUT /api/job/update/:id` - Update job
- `DELETE /api/job/delete/:id` - Delete job
- `GET /api/job/getadminjobs` - Get admin's jobs

### Companies
- `POST /api/company/register` - Register company
- `GET /api/company/get` - Get user's companies
- `GET /api/company/get/:id` - Get company by ID
- `PUT /api/company/update/:id` - Update company

### Applications
- `POST /api/application/apply/:id` - Apply for job
- `GET /api/application/get` - Get user's applications
- `GET /api/application/applicants/:id` - Get job applicants
- `PUT /api/application/status/:applicationId` - Update application status
- `DELETE /api/application/delete/:applicationId` - Delete application

## Styling

The application uses Tailwind CSS for styling with a custom color scheme:

- Primary: Blue shades (`primary-50` to `primary-700`)
- Custom components defined in `index.css`
- Responsive design with mobile-first approach

## State Management

Redux Toolkit is used for state management with the following slices:
- `authSlice` - Authentication state
- `jobSlice` - Job listings and details
- `applicationSlice` - Application management
- `companySlice` - Company management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the ISC License.
