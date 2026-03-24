import { useState, useEffect } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { useForm } from 'react-hook-form'
import { addJob } from '../redux/features/jobSlice'
import { setCompanies } from '../redux/features/companySlice'
import { FiBriefcase, FiDollarSign } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const PostJob = () => {
  const [searchParams] = useSearchParams()
  const [isLoading, setIsLoading] = useState(false)
  const { companies } = useSelector((store) => store.companies)
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { register, handleSubmit, formState: { errors }, setValue } = useForm()

  const preselectedCompanyId = searchParams.get('company')

  useEffect(() => {
    fetchCompanies()
    if (preselectedCompanyId) {
      setValue('companyId', preselectedCompanyId)
    }
  }, [preselectedCompanyId, setValue])

  const fetchCompanies = async () => {
    try {
      const response = await api.get('/company/get')
      dispatch(setCompanies(response.data.companies))
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch companies')
    }
  }

  const onSubmit = async (data) => {
    setIsLoading(true)
    
    try {
      const response = await api.post('/job/post', data)
      dispatch(addJob(response.data.job))
      toast.success('Job posted successfully!')
      navigate('/my-jobs')
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to post job')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="card">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 mb-2">Post a New Job</h1>
          <p className="text-gray-600">
            Create a job listing to find the perfect candidate
          </p>
        </div>

        {companies.length === 0 ? (
          <div className="text-center py-8">
            <FiBriefcase className="mx-auto text-gray-400 text-4xl mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">No Companies Found</h3>
            <p className="text-gray-600 mb-4">
              You need to create a company profile before posting jobs
            </p>
            <button
              onClick={() => navigate('/companies/setup')}
              className="btn-primary"
            >
              Create Company
            </button>
          </div>
        ) : (
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
            {/* Company Selection */}
            <div>
              <label htmlFor="companyId" className="block text-sm font-medium text-gray-700 mb-1">
                Company *
              </label>
              <select
                {...register('companyId', { required: 'Please select a company' })}
                className="input-field"
              >
                <option value="">Select a company</option>
                {companies.map((company) => (
                  <option key={company._id} value={company._id}>
                    {company.name}
                  </option>
                ))}
              </select>
              {errors.companyId && (
                <p className="mt-1 text-sm text-red-600">{errors.companyId.message}</p>
              )}
            </div>

            {/* Job Title */}
            <div>
              <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-1">
                Job Title *
              </label>
              <input
                {...register('title', { required: 'Job title is required' })}
                type="text"
                className="input-field"
                placeholder="e.g., Senior Frontend Developer"
              />
              {errors.title && (
                <p className="mt-1 text-sm text-red-600">{errors.title.message}</p>
              )}
            </div>

            {/* Position */}
            <div>
              <label htmlFor="position" className="block text-sm font-medium text-gray-700 mb-1">
                Position Level *
              </label>
              <select
                {...register('position', { required: 'Position level is required' })}
                className="input-field"
              >
                <option value="">Select position level</option>
                <option value="Entry Level">Entry Level</option>
                <option value="Mid Level">Mid Level</option>
                <option value="Senior Level">Senior Level</option>
                <option value="Lead">Lead</option>
                <option value="Manager">Manager</option>
                <option value="Director">Director</option>
                <option value="VP">VP</option>
                <option value="C-Level">C-Level</option>
              </select>
              {errors.position && (
                <p className="mt-1 text-sm text-red-600">{errors.position.message}</p>
              )}
            </div>

            {/* Job Type */}
            <div>
              <label htmlFor="jobType" className="block text-sm font-medium text-gray-700 mb-1">
                Job Type *
              </label>
              <select
                {...register('jobType', { required: 'Job type is required' })}
                className="input-field"
              >
                <option value="">Select job type</option>
                <option value="Full-time">Full-time</option>
                <option value="Part-time">Part-time</option>
                <option value="Contract">Contract</option>
                <option value="Internship">Internship</option>
                <option value="Temporary">Temporary</option>
              </select>
              {errors.jobType && (
                <p className="mt-1 text-sm text-red-600">{errors.jobType.message}</p>
              )}
            </div>

            {/* Salary */}
            <div>
              <label htmlFor="salary" className="block text-sm font-medium text-gray-700 mb-1">
                Annual Salary (USD) *
              </label>
              <div className="relative">
                <FiDollarSign className="absolute left-3 top-3 text-gray-400" />
                <input
                  {...register('salary', { 
                    required: 'Salary is required',
                    min: {
                      value: 0,
                      message: 'Salary must be a positive number'
                    }
                  })}
                  type="number"
                  className="input-field pl-10"
                  placeholder="75000"
                />
              </div>
              {errors.salary && (
                <p className="mt-1 text-sm text-red-600">{errors.salary.message}</p>
              )}
            </div>

            {/* Description */}
            <div>
              <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
                Job Description *
              </label>
              <textarea
                {...register('description', { required: 'Job description is required' })}
                rows={6}
                className="input-field"
                placeholder="Describe the role, responsibilities, and what the candidate will be doing..."
              />
              {errors.description && (
                <p className="mt-1 text-sm text-red-600">{errors.description.message}</p>
              )}
            </div>

            {/* Requirements */}
            <div>
              <label htmlFor="requirements" className="block text-sm font-medium text-gray-700 mb-1">
                Requirements *
              </label>
              <textarea
                {...register('requirements', { required: 'Requirements are required' })}
                rows={6}
                className="input-field"
                placeholder="List the required skills, experience, and qualifications for this role..."
              />
              {errors.requirements && (
                <p className="mt-1 text-sm text-red-600">{errors.requirements.message}</p>
              )}
            </div>

            {/* Submit Buttons */}
            <div className="flex space-x-4">
              <button
                type="submit"
                disabled={isLoading}
                className="btn-primary flex-1 disabled:opacity-50"
              >
                {isLoading ? 'Posting...' : 'Post Job'}
              </button>
              <button
                type="button"
                onClick={() => navigate('/dashboard')}
                className="btn-secondary"
              >
                Cancel
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  )
}

export default PostJob
