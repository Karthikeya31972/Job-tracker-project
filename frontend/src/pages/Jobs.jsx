import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { setJobs, setLoading } from '../redux/features/jobSlice'
import { useSelector, useDispatch } from 'react-redux'
import { FiBriefcase, FiMapPin, FiDollarSign, FiClock, FiSearch } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const Jobs = () => {
  const { jobs, isLoading } = useSelector((store) => store.jobs)
  const dispatch = useDispatch()
  const [searchTerm, setSearchTerm] = useState('')
  const [filters, setFilters] = useState({
    jobType: '',
    salaryRange: ''
  })

  useEffect(() => {
    fetchJobs()
  }, [searchTerm])

  const fetchJobs = async () => {
    try {
      dispatch(setLoading(true))
      const response = await api.get(`/job/get${searchTerm ? `?keyword=${searchTerm}` : ''}`)
      dispatch(setJobs(response.data.jobs))
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch jobs')
    } finally {
      dispatch(setLoading(false))
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

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Browse Jobs</h1>
        <p className="text-gray-600">Find your next opportunity from thousands of job listings</p>
      </div>

      {/* Search and Filters */}
      <div className="card mb-8">
        <div className="grid md:grid-cols-4 gap-4">
          <div className="md:col-span-2">
            <div className="relative">
              <FiSearch className="absolute left-3 top-3 text-gray-400" />
              <input
                type="text"
                placeholder="Search jobs by title or keywords..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="input-field pl-10"
              />
            </div>
          </div>
          
          <select
            value={filters.jobType}
            onChange={(e) => setFilters({ ...filters, jobType: e.target.value })}
            className="input-field"
          >
            <option value="">All Job Types</option>
            <option value="Full-time">Full-time</option>
            <option value="Part-time">Part-time</option>
            <option value="Contract">Contract</option>
            <option value="Internship">Internship</option>
          </select>

          <select
            value={filters.salaryRange}
            onChange={(e) => setFilters({ ...filters, salaryRange: e.target.value })}
            className="input-field"
          >
            <option value="">All Salary Ranges</option>
            <option value="0-50000">$0 - $50,000</option>
            <option value="50000-100000">$50,000 - $100,000</option>
            <option value="100000-150000">$100,000 - $150,000</option>
            <option value="150000+">$150,000+</option>
          </select>
        </div>
      </div>

      {/* Job Listings */}
      {isLoading ? (
        <div className="flex justify-center items-center py-12">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
        </div>
      ) : jobs.length === 0 ? (
        <div className="text-center py-12">
          <FiBriefcase className="mx-auto text-gray-400 text-4xl mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No jobs found</h3>
          <p className="text-gray-600">Try adjusting your search or filters</p>
        </div>
      ) : (
        <div className="space-y-4">
          {jobs.map((job) => (
            <div key={job._id} className="card hover:shadow-lg transition-shadow">
              <div className="flex flex-col md:flex-row md:items-center md:justify-between">
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
                    <span className="px-2 py-1 bg-green-100 text-green-700 text-xs rounded-full">
                      {job.jobType}
                    </span>
                  </div>

                  <p className="text-gray-600 mb-3 line-clamp-2">
                    {job.description}
                  </p>

                  <div className="flex flex-wrap items-center gap-4 text-sm text-gray-500">
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
                  </div>
                </div>

                <div className="mt-4 md:mt-0 md:ml-6">
                  <Link
                    to={`/jobs/${job._id}`}
                    className="btn-primary inline-block"
                  >
                    View Details
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default Jobs
