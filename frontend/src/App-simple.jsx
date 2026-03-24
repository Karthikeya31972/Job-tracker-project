import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Jobs from './pages/Jobs'
import JobDetails from './pages/JobDetails'
import Login from './pages/auth/Login'
import Register from './pages/auth/Register'

function App() {
  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f9fafb' }}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/jobs" element={<Jobs />} />
        <Route path="/jobs/:id" element={<JobDetails />} />
      </Routes>
    </div>
  )
}

export default App
