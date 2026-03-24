import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { setCompanies, setLoading } from '../redux/features/companySlice'
import { FiBriefcase, FiPlus, FiEdit, FiMapPin, FiGlobe } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const Companies = () => {
  const { companies, isLoading } = useSelector((store) => store.companies)
  const dispatch = useDispatch()

  useEffect(() => {
    fetchCompanies()
  }, [])

  const fetchCompanies = async () => {
    try {
      dispatch(setLoading(true))
      const response = await api.get('/company/get')
      dispatch(setCompanies(response.data.companies))
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch companies')
    } finally {
      dispatch(setLoading(false))
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
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Companies</h1>
          <p className="text-gray-600">Manage your company profiles and information</p>
        </div>
        <Link
          to="/companies/setup"
          className="btn-primary flex items-center"
        >
          <FiPlus className="mr-2" />
          Add Company
        </Link>
      </div>

      {/* Companies List */}
      {companies.length === 0 ? (
        <div className="text-center py-12">
          <FiBriefcase className="mx-auto text-gray-400 text-4xl mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">No companies yet</h3>
          <p className="text-gray-600 mb-4">Create your first company to start posting jobs</p>
          <Link
            to="/companies/setup"
            className="btn-primary"
          >
            Create Company
          </Link>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {companies.map((company) => (
            <div key={company._id} className="card hover:shadow-lg transition-shadow">
              {/* Company Logo */}
              <div className="flex items-center justify-center h-32 bg-gray-50 rounded-lg mb-4">
                {company.logo ? (
                  <img
                    src={company.logo}
                    alt={company.name}
                    className="h-full w-full object-contain rounded-lg"
                  />
                ) : (
                  <FiBriefcase className="text-gray-400 text-4xl" />
                )}
              </div>

              {/* Company Info */}
              <div className="space-y-3">
                <div>
                  <h3 className="text-lg font-semibold text-gray-900">{company.name}</h3>
                  <p className="text-gray-600 text-sm line-clamp-2">
                    {company.description || 'No description available'}
                  </p>
                </div>

                <div className="space-y-2">
                  {company.location && (
                    <div className="flex items-center text-sm text-gray-500">
                      <FiMapPin className="mr-2" />
                      {company.location}
                    </div>
                  )}
                  
                  {company.website && (
                    <div className="flex items-center text-sm text-gray-500">
                      <FiGlobe className="mr-2" />
                      <a
                        href={company.website}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-primary-600 hover:text-primary-700 truncate"
                      >
                        {company.website}
                      </a>
                    </div>
                  )}
                </div>

                {/* Actions */}
                <div className="flex space-x-2 pt-3 border-t">
                  <Link
                    to={`/companies/edit/${company._id}`}
                    className="btn-secondary flex-1 text-center flex items-center justify-center"
                  >
                    <FiEdit className="mr-1" />
                    Edit
                  </Link>
                  <Link
                    to={`/post-job?company=${company._id}`}
                    className="btn-primary flex-1 text-center"
                  >
                    Post Job
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

export default Companies
