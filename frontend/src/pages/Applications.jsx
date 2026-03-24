import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { setApplications, deleteApplication } from '../redux/features/applicationSlice'
import { FiBriefcase, FiMapPin, FiClock, FiTrash2, FiEye, FiCheck, FiX } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const Applications = () => {
  const { applications, isLoading } = useSelector((store) => store.applications)
  const dispatch = useDispatch()
  const [confirmDelete, setConfirmDelete] = useState(null)

  useEffect(() => {
    fetchApplications()
  }, [])

  const fetchApplications = async () => {
    try {
      const response = await api.get('/application/get')
      dispatch(setApplications(response.data.applications))
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch applications')
    }
  }

  const handleDelete = async (applicationId) => {
    try {
      await api.delete(`/application/delete/${applicationId}`)
      dispatch(deleteApplication(applicationId))
      toast.success('Application withdrawn successfully!')
      setConfirmDelete(null)
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to withdraw application')
    }
  }

  const getStatusColor = (status) => {
    switch (status) {
      case 'pending':
        return 'bg-yellow-100 text-yellow-700'
      case 'accepted':
        return 'bg-green-100 text-green-700'
      case 'rejected':
        return 'bg-red-100 text-red-700'
      default:
        return 'bg-gray-100 text-gray-700'
    }
  }

  const getStatusIcon = (status) => {
    switch (status) {
      case 'pending':
        return <FiClock className="text-yellow-600" />
      case 'accepted':
        return <FiCheck className="text-green-600" />
      case 'rejected':
        return <FiX className="text-red-600" />
      default:
        return <FiClock className="text-gray-600" />
    }
  }

  const getTimeAgo = (date) => {
    const now = new Date()
    const appDate = new Date(date)
    const diffTime = Math.abs(now - appDate)
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    
    if (diffDays === 1) return '1 day ago'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
    return `${Math.floor(diffDays / 30)} months ago`
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
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">My Applications</h1>
        <p className="text-gray-600">Track the status of your job applications</p>
      </div>

      {/* Applications List */}
      {applications.length === 0 ? (
        <div className="text-center py-12">
          <FiBriefcase className="mx-auto text-gray-400 text-4xl mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No applications yet</h3>
          <p className="text-gray-600 mb-4">Start applying to jobs to track your applications here</p>
          <Link
            to="/jobs"
            className="btn-primary"
          >
            Browse Jobs
          </Link>
        </div>
      ) : (
        <div className="space-y-4">
          {applications.map((application) => (
            <div key={application._id} className="card hover:shadow-lg transition-shadow">
              <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between">
                <div className="flex-1">
                  <div className="flex items-start justify-between mb-2">
                    <div>
                      <h3 className="text-lg font-semibold text-gray-900 mb-1">
                        <Link 
                          to={`/jobs/${application.job._id}`}
                          className="hover:text-primary-600 transition-colors"
                        >
                          {application.job.title}
                        </Link>
                      </h3>
                      <p className="text-primary-600 font-medium mb-2">
                        {application.job.company?.name}
                      </p>
                    </div>
                    <div className="flex items-center space-x-2">
                      <span className={`px-3 py-1 rounded-full text-sm flex items-center ${getStatusColor(application.status)}`}>
                        {getStatusIcon(application.status)}
                        <span className="ml-1 capitalize">{application.status}</span>
                      </span>
                    </div>
                  </div>

                  <p className="text-gray-600 mb-3 line-clamp-2">
                    {application.job.description}
                  </p>

                  <div className="flex flex-wrap items-center gap-4 text-sm text-gray-500 mb-3">
                    <div className="flex items-center">
                      <FiMapPin className="mr-1" />
                      {application.job.company?.location || 'Remote'}
                    </div>
                    <div className="flex items-center">
                      <FiClock className="mr-1" />
                      Applied {getTimeAgo(application.createdAt)}
                    </div>
                  </div>
                </div>

                {/* Actions */}
                <div className="flex lg:flex-col space-x-2 lg:space-x-0 lg:space-y-2 mt-4 lg:mt-0 lg:ml-6">
                  <Link
                    to={`/jobs/${application.job._id}`}
                    className="btn-secondary flex items-center justify-center lg:justify-start"
                  >
                    <FiEye className="mr-2" />
                    View Job
                  </Link>
                  {application.status === 'pending' && (
                    <button
                      onClick={() => setConfirmDelete(application._id)}
                      className="btn-secondary bg-red-50 text-red-600 hover:bg-red-100 flex items-center justify-center lg:justify-start"
                    >
                      <FiTrash2 className="mr-2" />
                      Withdraw
                    </button>
                  )}
                </div>
              </div>

              {/* Delete Confirmation */}
              {confirmDelete === application._id && (
                <div className="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
                  <p className="text-red-800 mb-3">
                    Are you sure you want to withdraw this application? This action cannot be undone.
                  </p>
                  <div className="flex space-x-3">
                    <button
                      onClick={() => handleDelete(application._id)}
                      className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition-colors"
                    >
                      Yes, Withdraw
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

export default Applications
