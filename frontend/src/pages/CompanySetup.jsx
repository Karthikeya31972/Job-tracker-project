import { useState, useEffect } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { useForm } from 'react-hook-form'
import { addCompany } from '../redux/features/companySlice'
import { FiBriefcase, FiUpload } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const CompanySetup = () => {
  const [searchParams] = useSearchParams()
  const [isLoading, setIsLoading] = useState(false)
  const [logoPreview, setLogoPreview] = useState(null)
  const { user } = useSelector((store) => store.auth)
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { register, handleSubmit, formState: { errors }, setValue } = useForm()

  const companyId = searchParams.get('id')
  const isEditing = !!companyId

  useEffect(() => {
    if (isEditing) {
      // Fetch company data for editing
      fetchCompanyData()
    }
  }, [isEditing, companyId])

  const fetchCompanyData = async () => {
    try {
      const response = await api.get(`/company/get/${companyId}`)
      const company = response.data.company
      
      // Set form values
      setValue('name', company.name)
      setValue('description', company.description)
      setValue('website', company.website)
      setValue('location', company.location)
      
      if (company.logo) {
        setLogoPreview(company.logo)
      }
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to fetch company data')
      navigate('/companies')
    }
  }

  const handleLogoChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      // Check file size (max 5MB)
      if (file.size > 5 * 1024 * 1024) {
        toast.error('Logo file size should be less than 5MB')
        return
      }

      // Check file type
      if (!file.type.startsWith('image/')) {
        toast.error('Please upload an image file')
        return
      }

      // Create preview
      const reader = new FileReader()
      reader.onload = (e) => {
        setLogoPreview(e.target.result)
      }
      reader.readAsDataURL(file)
    }
  }

  const onSubmit = async (data) => {
    setIsLoading(true)
    
    try {
      const formData = new FormData()
      formData.append('name', data.name)
      formData.append('description', data.description)
      formData.append('website', data.website)
      formData.append('location', data.location)
      
      // Add logo file if selected
      const logoInput = document.querySelector('input[type="file"]')
      if (logoInput && logoInput.files[0]) {
        formData.append('logo', logoInput.files[0])
      }

      let response
      if (isEditing) {
        response = await api.put(`/company/update/${companyId}`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        toast.success('Company updated successfully!')
      } else {
        response = await api.post('/company/register', {
          companyName: data.name
        })
        
        // If registration successful, update with additional details
        if (response.data.company) {
          await api.put(`/company/update/${response.data.company._id}`, formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
        }
        
        dispatch(addCompany(response.data.company))
        toast.success('Company created successfully!')
      }
      
      navigate('/companies')
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to save company')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="card">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-900 mb-2">
            {isEditing ? 'Edit Company' : 'Create New Company'}
          </h1>
          <p className="text-gray-600">
            {isEditing 
              ? 'Update your company information' 
              : 'Add your company to start posting jobs'
            }
          </p>
        </div>

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
          {/* Company Logo */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Company Logo
            </label>
            <div className="flex items-center space-x-6">
              <div className="flex-shrink-0">
                <div className="w-24 h-24 bg-gray-100 rounded-lg flex items-center justify-center overflow-hidden">
                  {logoPreview ? (
                    <img
                      src={logoPreview}
                      alt="Company logo preview"
                      className="w-full h-full object-cover"
                    />
                  ) : (
                    <FiBriefcase className="text-gray-400 text-2xl" />
                  )}
                </div>
              </div>
              <div className="flex-1">
                <label className="btn-secondary cursor-pointer inline-flex items-center">
                  <FiUpload className="mr-2" />
                  Upload Logo
                  <input
                    type="file"
                    accept="image/*"
                    onChange={handleLogoChange}
                    className="hidden"
                  />
                </label>
                <p className="mt-2 text-sm text-gray-500">
                  PNG, JPG, GIF up to 5MB
                </p>
              </div>
            </div>
          </div>

          {/* Company Name */}
          <div>
            <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
              Company Name *
            </label>
            <input
              {...register('name', { required: 'Company name is required' })}
              type="text"
              className="input-field"
              placeholder="Enter company name"
            />
            {errors.name && (
              <p className="mt-1 text-sm text-red-600">{errors.name.message}</p>
            )}
          </div>

          {/* Description */}
          <div>
            <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
              Description *
            </label>
            <textarea
              {...register('description', { required: 'Description is required' })}
              rows={4}
              className="input-field"
              placeholder="Describe your company culture, mission, and what makes it a great place to work"
            />
            {errors.description && (
              <p className="mt-1 text-sm text-red-600">{errors.description.message}</p>
            )}
          </div>

          {/* Website */}
          <div>
            <label htmlFor="website" className="block text-sm font-medium text-gray-700 mb-1">
              Website
            </label>
            <input
              {...register('website', {
                pattern: {
                  value: /^https?:\/\/.+/,
                  message: 'Please enter a valid URL (e.g., https://example.com)'
                }
              })}
              type="url"
              className="input-field"
              placeholder="https://example.com"
            />
            {errors.website && (
              <p className="mt-1 text-sm text-red-600">{errors.website.message}</p>
            )}
          </div>

          {/* Location */}
          <div>
            <label htmlFor="location" className="block text-sm font-medium text-gray-700 mb-1">
              Location *
            </label>
            <input
              {...register('location', { required: 'Location is required' })}
              type="text"
              className="input-field"
              placeholder="City, State or Remote"
            />
            {errors.location && (
              <p className="mt-1 text-sm text-red-600">{errors.location.message}</p>
            )}
          </div>

          {/* Submit Buttons */}
          <div className="flex space-x-4">
            <button
              type="submit"
              disabled={isLoading}
              className="btn-primary flex-1 disabled:opacity-50"
            >
              {isLoading 
                ? (isEditing ? 'Updating...' : 'Creating...') 
                : (isEditing ? 'Update Company' : 'Create Company')
              }
            </button>
            <button
              type="button"
              onClick={() => navigate('/companies')}
              className="btn-secondary"
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CompanySetup
