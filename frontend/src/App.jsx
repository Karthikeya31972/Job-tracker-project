import { Routes, Route } from 'react-router-dom'
import { useSelector } from 'react-redux'
import Layout from './components/Layout'
import Login from './pages/auth/Login'
import Register from './pages/auth/Register'
import Home from './pages/Home'
import Jobs from './pages/Jobs'
import JobDetails from './pages/JobDetails'
import Dashboard from './pages/Dashboard'
import Profile from './pages/Profile'
import Companies from './pages/Companies'
import CompanySetup from './pages/CompanySetup'
import PostJob from './pages/PostJob'
import MyJobs from './pages/MyJobs'
import Applications from './pages/Applications'
import Applicants from './pages/Applicants'
import ProtectedRoute from './components/ProtectedRoute'

function App() {
  const { isAuthenticated } = useSelector((store) => store.auth)

  return (
    <div className="min-h-screen bg-gray-50">
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
          <Route path="jobs" element={<Jobs />} />
          <Route path="jobs/:id" element={<JobDetails />} />

          <Route element={<ProtectedRoute />}>
            <Route path="dashboard" element={<Dashboard />} />
            <Route path="profile" element={<Profile />} />
            <Route path="companies" element={<Companies />} />
            <Route path="companies/setup" element={<CompanySetup />} />
            <Route path="post-job" element={<PostJob />} />
            <Route path="my-jobs" element={<MyJobs />} />
            <Route path="applications" element={<Applications />} />
            <Route path="applicants/:id" element={<Applicants />} />
          </Route>
        </Route>
      </Routes>
    </div>
  )
}

export default App
