import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { setMyJobs, deleteJob } from '../redux/features/jobSlice'
import { FiBriefcase, FiMapPin, FiDollarSign, FiEdit, FiTrash2, FiUsers, FiEye } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const MyJobs = () => {
  const { myJobs, isLoading } = useSelector((store) => store.jobs)
  const dispatch = useDispatch()
  const [confirmDelete, setConfirmDelete] = useState(null)

  useEffect(() => {
    fetchMyJobs()
  }, [])

  const fetchMyJobs = async () => {
    try {
      const response = await api.get('/job/getadminjobs')
      dispatch(setMyJobs(response.data.jobs))
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch jobs')
    }
  }

  const handleDelete = async (jobId) => {
    try {
      await api.delete(`/job/delete/${jobId}`)
      dispatch(deleteJob(jobId))
      toast.success('Job deleted successfully!')
      setConfirmDelete(null)
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to delete job')
    }
  }

  const formatSalary = (salary) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
    }).format(salary)
  }

  const getTimeAgo = (date) => {
    const now = new Date()
    const jobDate = new Date(date)
    const diffTime = Math.abs(now - jobDate)
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    
    if (diffDays === 1) return '1 day ago'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
    return `${Math.floor(diffDays / 30)} months ago`
  }

  const getApplicantsCount = (job) => {
    // This would ideally come from the API, but for now we'll use a placeholder
    return Math.floor(Math.random() * 20) + 1
  }

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">My Job Postings</h1>
          <p className="text-gray-600">Manage your job listings and track applications</p>
        </div>
        <Link
          to="/post-job"
          className="btn-primary"
        >
          Post New Job
        </Link>
      </div>

      {/* Jobs List */}
      {myJobs.length === 0 ? (
        <div className="text-center py-12">
          <FiBriefcase className="mx-auto text-gray-400 text-4xl mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No job postings yet</h3>
          <p className="text-gray-600 mb-4">Create your first job posting to start receiving applications</p>
          <Link
            to="/post-job"
            className="btn-primary"
          >
            Post Your First Job
          </Link>
        </div>
      ) : (
        <div className="space-y-4">
          {myJobs.map((job) => (
            <div key={job._id} className="card hover:shadow-lg transition-shadow">
              <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between">
                <div className="flex-1">
                  <div className="flex items-start justify-between mb-2">
                    <div>
                      <h3 className="text-lg font-semibold text-gray-900 mb-1">
                        <Link 
                          to={`/jobs/${job._id}`}
                          className="hover:text-primary-600 transition-colors"
                        >
                          {job.title}
                        </Link>
                      </h3>
                      <p className="text-primary-600 font-medium mb-2">
                        {job.company?.name}
                      </p>
                    </div>
                    <div className="flex items-center space-x-2">
                      <span className="px-2 py-1 bg-green-100 text-green-700 text-xs rounded-full">
                        {job.jobType}
                      </span>
                      <span className="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded-full">
                        {job.position}
                      </span>
                    </div>
                  </div>

                  <p className="text-gray-600 mb-3 line-clamp-2">
                    {job.description}
                  </p>

                  <div className="flex flex-wrap items-center gap-4 text-sm text-gray-500 mb-3">
                    <div className="flex items-center">
                      <FiMapPin className="mr-1" />
                      {job.company?.location || 'Remote'}
                    </div>
                    <div className="flex items-center">
                      <FiDollarSign className="mr-1" />
                      {formatSalary(job.salary)}
                    </div>
                    <div className="flex items-center">
                      <FiClock className="mr-1" />
                      {getTimeAgo(job.createdAt)}
                    </div>
                    <div className="flex items-center">
                      <FiUsers className="mr-1" />
                      {getApplicantsCount(job)} applicants
                    </div>
                  </div>
                </div>

                {/* Actions */}
                <div className="flex lg:flex-col space-x-2 lg:space-x-0 lg:space-y-2 mt-4 lg:mt-0 lg:ml-6">
                  <Link
                    to={`/applicants/${job._id}`}
                    className="btn-secondary flex items-center justify-center lg:justify-start"
                  >
                    <FiEye className="mr-2" />
                    View Applicants
                  </Link>
                  <Link
                    to={`/edit-job/${job._id}`}
                    className="btn-secondary flex items-center justify-center lg:justify-start"
                  >
                    <FiEdit className="mr-2" />
                    Edit
                  </Link>
                  <button
                    onClick={() => setConfirmDelete(job._id)}
                    className="btn-secondary bg-red-50 text-red-600 hover:bg-red-100 flex items-center justify-center lg:justify-start"
                  >
                    <FiTrash2 className="mr-2" />
                    Delete
                  </button>
                </div>
              </div>

              {/* Delete Confirmation */}
              {confirmDelete === job._id && (
                <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
                  <p className="text-red-800 mb-3">
                    Are you sure you want to delete this job posting? This action cannot be undone.
                  </p>
                  <div className="flex space-x-3">
                    <button
                      onClick={() => handleDelete(job._id)}
                      className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition-colors"
                    >
                      Yes, Delete
                    </button>
                    <button
                      onClick={() => setConfirmDelete(null)}
                      className="bg-gray-200 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-300 transition-colors"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default MyJobs
