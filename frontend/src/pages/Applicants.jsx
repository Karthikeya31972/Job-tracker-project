import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { setApplicants } from '../redux/features/applicationSlice'
import { FiUser, FiMail, FiPhone, FiBriefcase, FiFileText, FiCheck, FiX, FiClock } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const Applicants = () => {
  const { id: jobId } = useParams()
  const { applicants, isLoading } = useSelector((store) => store.applications)
  const dispatch = useDispatch()
  const [updatingStatus, setUpdatingStatus] = useState(null)

  useEffect(() => {
    if (jobId) {
      fetchApplicants()
    }
  }, [jobId])

  const fetchApplicants = async () => {
    try {
      const response = await api.get(`/application/applicants/${jobId}`)
      dispatch(setApplicants(response.data.applications))
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch applicants')
    }
  }

  const handleStatusUpdate = async (applicationId, newStatus) => {
    setUpdatingStatus(applicationId)
    try {
      await api.put(`/application/status/${applicationId}`, { status: newStatus })
      
      // Update local state
      const updatedApplicants = applicants.map(app => 
        app._id === applicationId ? { ...app, status: newStatus } : app
      )
      dispatch(setApplicants(updatedApplicants))
      
      toast.success(`Application status updated to ${newStatus}`)
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to update status')
    } finally {
      setUpdatingStatus(null)
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
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Job Applicants</h1>
        <p className="text-gray-600">
          Review and manage applications for this position
        </p>
      </div>

      {/* Applicants List */}
      {applicants.length === 0 ? (
        <div className="text-center py-12">
          <FiUser className="mx-auto text-gray-400 text-4xl mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No applicants yet</h3>
          <p className="text-gray-600">
            Applications will appear here once candidates start applying
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {applicants.map((application) => (
            <div key={application._id} className="card hover:shadow-lg transition-shadow">
              <div className="flex flex-col lg:flex-row lg:items-start lg:justify-between">
                {/* Applicant Info */}
                <div className="flex-1">
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex items-center space-x-4">
                      <div className="bg-primary-100 p-3 rounded-full">
                        <FiUser className="text-primary-600 text-xl" />
                      </div>
                      <div>
                        <h3 className="text-lg font-semibold text-gray-900">
                          {application.applicant.fullname}
                        </h3>
                        <p className="text-gray-600">{application.applicant.email}</p>
                      </div>
                    </div>
                    <div className="flex items-center space-x-2">
                      <span className={`px-3 py-1 rounded-full text-sm flex items-center ${getStatusColor(application.status)}`}>
                        {getStatusIcon(application.status)}
                        <span className="ml-1 capitalize">{application.status}</span>
                      </span>
                    </div>
                  </div>

                  {/* Contact Info */}
                  <div className="grid md:grid-cols-2 gap-4 mb-4">
                    <div className="flex items-center text-sm text-gray-600">
                      <FiMail className="mr-2" />
                      {application.applicant.email}
                    </div>
                    <div className="flex items-center text-sm text-gray-600">
                      <FiPhone className="mr-2" />
                      {application.applicant.phoneNumber}
                    </div>
                  </div>

                  {/* Bio */}
                  {application.applicant.profile?.bio && (
                    <div className="mb-4">
                      <h4 className="text-sm font-medium text-gray-900 mb-2">Bio</h4>
                      <p className="text-gray-600 text-sm">
                        {application.applicant.profile.bio}
                      </p>
                    </div>
                  )}

                  {/* Skills */}
                  {application.applicant.profile?.skills?.length > 0 && (
                    <div className="mb-4">
                      <h4 className="text-sm font-medium text-gray-900 mb-2">Skills</h4>
                      <div className="flex flex-wrap gap-2">
                        {application.applicant.profile.skills.map((skill, index) => (
                          <span
                            key={index}
                            className="px-2 py-1 bg-primary-100 text-primary-700 rounded-full text-sm"
                          >
                            {skill}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Resume */}
                  {application.applicant.profile?.resume && (
                    <div className="mb-4">
                      <a
                        href={application.applicant.profile.resume}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center text-primary-600 hover:text-primary-700 text-sm font-medium"
                      >
                        <FiFileText className="mr-2" />
                        View Resume
                      </a>
                    </div>
                  )}
                </div>

                {/* Actions */}
                <div className="flex lg:flex-col space-x-2 lg:space-x-0 lg:space-y-2 mt-4 lg:mt-0 lg:ml-6">
                  {application.status === 'pending' && (
                    <>
                      <button
                        onClick={() => handleStatusUpdate(application._id, 'accepted')}
                        disabled={updatingStatus === application._id}
                        className="btn-primary bg-green-600 hover:bg-green-700 disabled:opacity-50 flex items-center justify-center lg:justify-start"
                      >
                        <FiCheck className="mr-2" />
                        {updatingStatus === application._id ? 'Updating...' : 'Accept'}
                      </button>
                      <button
                        onClick={() => handleStatusUpdate(application._id, 'rejected')}
                        disabled={updatingStatus === application._id}
                        className="btn-secondary bg-red-50 text-red-600 hover:bg-red-100 flex items-center justify-center lg:justify-start"
                      >
                        <FiX className="mr-2" />
                        {updatingStatus === application._id ? 'Updating...' : 'Reject'}
                      </button>
                    </>
                  )}
                  
                  {application.status === 'accepted' && (
                    <button
                      onClick={() => handleStatusUpdate(application._id, 'pending')}
                      disabled={updatingStatus === application._id}
                      className="btn-secondary flex items-center justify-center lg:justify-start"
                    >
                      <FiClock className="mr-2" />
                      {updatingStatus === application._id ? 'Updating...' : 'Move to Pending'}
                    </button>
                  )}
                  
                  {application.status === 'rejected' && (
                    <button
                      onClick={() => handleStatusUpdate(application._id, 'pending')}
                      disabled={updatingStatus === application._id}
                      className="btn-secondary flex items-center justify-center lg:justify-start"
                    >
                      <FiClock className="mr-2" />
                      {updatingStatus === application._id ? 'Updating...' : 'Reconsider'}
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default Applicants
