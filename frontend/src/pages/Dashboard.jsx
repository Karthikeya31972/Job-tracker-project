import { useSelector } from 'react-redux'
import { Link } from 'react-router-dom'
import { FiBriefcase, FiUsers, FiFileText, FiTrendingUp, FiArrowRight } from 'react-icons/fi'

const Dashboard = () => {
  const { user } = useSelector((store) => store.auth)

  const isRecruiter = user?.role === 'recruiter'

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Welcome Section */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          Welcome back, {user?.fullname}!
        </h1>
        <p className="text-gray-600">
          {isRecruiter 
            ? "Manage your job postings and track applications" 
            : "Find your dream job and track your applications"}
        </p>
      </div>

      {/* Quick Stats */}
      <div className="grid md:grid-cols-4 gap-6 mb-8">
        <div className="card">
          <div className="flex items-center">
            <div className="bg-primary-100 p-3 rounded-lg">
              <FiBriefcase className="text-primary-600 text-xl" />
            </div>
            <div className="ml-4">
              <p className="text-sm text-gray-600">
                {isRecruiter ? "Posted Jobs" : "Applied Jobs"}
              </p>
              <p className="text-2xl font-bold text-gray-900">
                {isRecruiter ? "12" : "8"}
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="bg-green-100 p-3 rounded-lg">
              <FiTrendingUp className="text-green-600 text-xl" />
            </div>
            <div className="ml-4">
              <p className="text-sm text-gray-600">
                {isRecruiter ? "Total Applicants" : "Profile Views"}
              </p>
              <p className="text-2xl font-bold text-gray-900">
                {isRecruiter ? "45" : "23"}
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="bg-blue-100 p-3 rounded-lg">
              <FiUsers className="text-blue-600 text-xl" />
            </div>
            <div className="ml-4">
              <p className="text-sm text-gray-600">
                {isRecruiter ? "Companies" : "Saved Jobs"}
              </p>
              <p className="text-2xl font-bold text-gray-900">
                {isRecruiter ? "3" : "15"}
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="bg-purple-100 p-3 rounded-lg">
              <FiFileText className="text-purple-600 text-xl" />
            </div>
            <div className="ml-4">
              <p className="text-sm text-gray-600">
                {isRecruiter ? "Pending Reviews" : "Interviews"}
              </p>
              <p className="text-2xl font-bold text-gray-900">
                {isRecruiter ? "7" : "2"}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="grid md:grid-cols-2 gap-6">
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Quick Actions</h2>
          <div className="space-y-3">
            {isRecruiter ? (
              <>
                <Link
                  to="/post-job"
                  className="flex items-center justify-between p-3 bg-primary-50 rounded-lg hover:bg-primary-100 transition-colors"
                >
                  <span className="text-primary-700">Post a New Job</span>
                  <FiArrowRight className="text-primary-600" />
                </Link>
                <Link
                  to="/my-jobs"
                  className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
                >
                  <span className="text-gray-700">Manage Job Postings</span>
                  <FiArrowRight className="text-gray-600" />
                </Link>
                <Link
                  to="/companies"
                  className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
                >
                  <span className="text-gray-700">Company Settings</span>
                  <FiArrowRight className="text-gray-600" />
                </Link>
              </>
            ) : (
              <>
                <Link
                  to="/jobs"
                  className="flex items-center justify-between p-3 bg-primary-50 rounded-lg hover:bg-primary-100 transition-colors"
                >
                  <span className="text-primary-700">Browse Jobs</span>
                  <FiArrowRight className="text-primary-600" />
                </Link>
                <Link
                  to="/applications"
                  className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
                >
                  <span className="text-gray-700">My Applications</span>
                  <FiArrowRight className="text-gray-600" />
                </Link>
                <Link
                  to="/profile"
                  className="flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
                >
                  <span className="text-gray-700">Update Profile</span>
                  <FiArrowRight className="text-gray-600" />
                </Link>
              </>
            )}
          </div>
        </div>

        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Recent Activity</h2>
          <div className="space-y-3">
            {isRecruiter ? (
              <>
                <div className="flex items-start space-x-3">
                  <div className="bg-green-100 p-2 rounded-full">
                    <FiUsers className="text-green-600 text-sm" />
                  </div>
                  <div>
                    <p className="text-sm text-gray-900">New application for Senior Developer</p>
                    <p className="text-xs text-gray-500">2 hours ago</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="bg-blue-100 p-2 rounded-full">
                    <FiBriefcase className="text-blue-600 text-sm" />
                  </div>
                  <div>
                    <p className="text-sm text-gray-900">Posted new job: UI/UX Designer</p>
                    <p className="text-xs text-gray-500">1 day ago</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="bg-purple-100 p-2 rounded-full">
                    <FiFileText className="text-purple-600 text-sm" />
                  </div>
                  <div>
                    <p className="text-sm text-gray-900">Reviewed 3 applications</p>
                    <p className="text-xs text-gray-500">2 days ago</p>
                  </div>
                </div>
              </>
            ) : (
              <>
                <div className="flex items-start space-x-3">
                  <div className="bg-green-100 p-2 rounded-full">
                    <FiFileText className="text-green-600 text-sm" />
                  </div>
                  <div>
                    <p className="text-sm text-gray-900">Applied to Frontend Developer position</p>
                    <p className="text-xs text-gray-500">1 day ago</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="bg-blue-100 p-2 rounded-full">
                    <FiBriefcase className="text-blue-600 text-sm" />
                  </div>
                  <div>
                    <p className="text-sm text-gray-900">Saved 5 new job listings</p>
                    <p className="text-xs text-gray-500">3 days ago</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="bg-purple-100 p-2 rounded-full">
                    <FiTrendingUp className="text-purple-600 text-sm" />
                  </div>
                  <div>
                    <p className="text-sm text-gray-900">Profile viewed by 3 recruiters</p>
                    <p className="text-xs text-gray-500">1 week ago</p>
                  </div>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
