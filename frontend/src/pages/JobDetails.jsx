import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { setSingleJob, setLoading } from '../redux/features/jobSlice'
import { FiBriefcase, FiMapPin, FiDollarSign, FiClock, FiArrowLeft, FiSend } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const JobDetails = () => {
  const { id } = useParams()
  const navigate = useNavigate()
  const { singleJob, isLoading } = useSelector((store) => store.jobs)
  const { user, isAuthenticated } = useSelector((store) => store.auth)
  const dispatch = useDispatch()
  const [isApplying, setIsApplying] = useState(false)

  useEffect(() => {
    if (id) {
      fetchJobDetails()
    }
  }, [id])

  const fetchJobDetails = async () => {
    try {
      dispatch(setLoading(true))
      const response = await api.get(`/job/get/${id}`)
      dispatch(setSingleJob(response.data.job))
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch job details')
      navigate('/jobs')
    } finally {
      dispatch(setLoading(false))
    }
  }

  const handleApply = async () => {
    if (!isAuthenticated) {
      toast.error('Please login to apply for this job')
      navigate('/login')
      return
    }

    if (user?.role === 'recruiter') {
      toast.error('Recruiters cannot apply for jobs')
      return
    }

    setIsApplying(true)
    try {
      const response = await api.post(`/application/apply/${id}`)
      toast.success('Application submitted successfully!')
      // Optionally refresh job details to show updated application count
      fetchJobDetails()
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to submit application')
    } finally {
      setIsApplying(false)
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

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  if (!singleJob) {
    return (
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Job not found</h2>
          <button
            onClick={() => navigate('/jobs')}
            className="btn-primary"
          >
            Back to Jobs
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Back Button */}
      <button
        onClick={() => navigate('/jobs')}
        className="flex items-center text-gray-600 hover:text-gray-900 mb-6"
      >
        <FiArrowLeft className="mr-2" />
        Back to Jobs
      </button>

      {/* Job Header */}
      <div className="card mb-6">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-4">
          <div>
            <h1 className="text-3xl font-bold text-gray-900 mb-2">{singleJob.title}</h1>
            <div className="flex items-center space-x-4 text-gray-600">
              <span className="text-primary-600 font-medium text-lg">
                {singleJob.company?.name}
              </span>
              <span className="px-3 py-1 bg-primary-100 text-primary-700 rounded-full text-sm">
                {singleJob.jobType}
              </span>
            </div>
          </div>
          
          {isAuthenticated && user?.role === 'Student' && (
            <button
              onClick={handleApply}
              disabled={isApplying}
              className="btn-primary mt-4 md:mt-0 disabled:opacity-50 flex items-center"
            >
              <FiSend className="mr-2" />
              {isApplying ? 'Applying...' : 'Apply Now'}
            </button>
          )}
        </div>

        {/* Job Meta */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4 border-t">
          <div className="flex items-center text-gray-600">
            <FiMapPin className="mr-2" />
            <span>{singleJob.company?.location || 'Remote'}</span>
          </div>
          <div className="flex items-center text-gray-600">
            <FiDollarSign className="mr-2" />
            <span>{formatSalary(singleJob.salary)}</span>
          </div>
          <div className="flex items-center text-gray-600">
            <FiBriefcase className="mr-2" />
            <span>{singleJob.position}</span>
          </div>
          <div className="flex items-center text-gray-600">
            <FiClock className="mr-2" />
            <span>{getTimeAgo(singleJob.createdAt)}</span>
          </div>
        </div>
      </div>

      {/* Job Details */}
      <div className="grid md:grid-cols-3 gap-6">
        <div className="md:col-span-2 space-y-6">
          {/* Description */}
          <div className="card">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Job Description</h2>
            <div className="prose max-w-none text-gray-600">
              {singleJob.description.split('\n').map((paragraph, index) => (
                <p key={index} className="mb-4">
                  {paragraph}
                </p>
              ))}
            </div>
          </div>

          {/* Requirements */}
          <div className="card">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Requirements</h2>
            <div className="prose max-w-none text-gray-600">
              {singleJob.requirements.split('\n').map((paragraph, index) => (
                <p key={index} className="mb-4">
                  {paragraph}
                </p>
              ))}
            </div>
          </div>
        </div>

        {/* Company Info */}
        <div className="space-y-6">
          <div className="card">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Company Information</h2>
            <div className="space-y-4">
              {singleJob.company?.logo && (
                <img
                  src={singleJob.company.logo}
                  alt={singleJob.company.name}
                  className="w-full h-32 object-contain rounded-lg"
                />
              )}
              <div>
                <h3 className="font-medium text-gray-900 mb-2">{singleJob.company?.name}</h3>
                <p className="text-gray-600 text-sm mb-2">{singleJob.company?.description}</p>
                {singleJob.company?.website && (
                  <a
                    href={singleJob.company.website}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary-600 hover:text-primary-700 text-sm underline"
                  >
                    Visit Website
                  </a>
                )}
              </div>
            </div>
          </div>

          {/* Quick Info */}
          <div className="card">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Info</h2>
            <div className="space-y-3">
              <div>
                <p className="text-sm text-gray-500">Position</p>
                <p className="font-medium text-gray-900">{singleJob.position}</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Job Type</p>
                <p className="font-medium text-gray-900">{singleJob.jobType}</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Salary</p>
                <p className="font-medium text-gray-900">{formatSalary(singleJob.salary)}</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Location</p>
                <p className="font-medium text-gray-900">{singleJob.company?.location || 'Remote'}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default JobDetails
