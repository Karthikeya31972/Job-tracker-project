import { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useForm } from 'react-hook-form'
import { updateUser } from '../redux/features/authSlice'
import { FiUser, FiMail, FiPhone, FiBriefcase, FiEdit2 } from 'react-icons/fi'
import toast from 'react-hot-toast'
import api from '../utils/api'

const Profile = () => {
  const { user } = useSelector((store) => store.auth)
  const dispatch = useDispatch()
  const [isEditing, setIsEditing] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const { register, handleSubmit, formState: { errors }, reset } = useForm()

  useEffect(() => {
    if (user) {
      reset({
        fullname: user.fullname || '',
        email: user.email || '',
        phoneNumber: user.phoneNumber || '',
        bio: user.profile?.bio || '',
        skills: user.profile?.skills?.join(', ') || ''
      })
    }
  }, [user, reset])

  const onSubmit = async (data) => {
    setIsLoading(true)
    
    try {
      const response = await api.post('/user/profile/update', data, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      
      dispatch(updateUser(response.data.user))
      toast.success('Profile updated successfully!')
      setIsEditing(false)
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to update profile')
    } finally {
      setIsLoading(false)
    }
  }

  if (!user) {
    return <div className="flex justify-center items-center min-h-screen">Loading...</div>
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="card">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold text-gray-900">Profile</h1>
          {!isEditing && (
            <button
              onClick={() => setIsEditing(true)}
              className="btn-primary flex items-center"
            >
              <FiEdit2 className="mr-2" />
              Edit Profile
            </button>
          )}
        </div>

        {!isEditing ? (
          <div className="space-y-6">
            {/* Profile Header */}
            <div className="flex items-center space-x-4">
              <div className="bg-primary-100 p-4 rounded-full">
                <FiUser className="text-primary-600 text-2xl" />
              </div>
              <div>
                <h2 className="text-xl font-semibold text-gray-900">{user.fullname}</h2>
                <p className="text-gray-600 capitalize">{user.role}</p>
              </div>
            </div>

            {/* Profile Information */}
            <div className="grid md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <div>
                  <label className="flex items-center text-sm font-medium text-gray-700 mb-1">
                    <FiUser className="mr-2" />
                    Full Name
                  </label>
                  <p className="text-gray-900">{user.fullname}</p>
                </div>

                <div>
                  <label className="flex items-center text-sm font-medium text-gray-700 mb-1">
                    <FiMail className="mr-2" />
                    Email
                  </label>
                  <p className="text-gray-900">{user.email}</p>
                </div>

                <div>
                  <label className="flex items-center text-sm font-medium text-gray-700 mb-1">
                    <FiPhone className="mr-2" />
                    Phone Number
                  </label>
                  <p className="text-gray-900">{user.phoneNumber}</p>
                </div>
              </div>

              <div className="space-y-4">
                <div>
                  <label className="flex items-center text-sm font-medium text-gray-700 mb-1">
                    <FiBriefcase className="mr-2" />
                    Bio
                  </label>
                  <p className="text-gray-900">
                    {user.profile?.bio || 'No bio added yet'}
                  </p>
                </div>

                <div>
                  <label className="flex items-center text-sm font-medium text-gray-700 mb-1">
                    <FiBriefcase className="mr-2" />
                    Skills
                  </label>
                  <div className="flex flex-wrap gap-2">
                    {user.profile?.skills?.length > 0 ? (
                      user.profile.skills.map((skill, index) => (
                        <span
                          key={index}
                          className="px-2 py-1 bg-primary-100 text-primary-700 rounded-full text-sm"
                        >
                          {skill}
                        </span>
                      ))
                    ) : (
                      <p className="text-gray-500">No skills added yet</p>
                    )}
                  </div>
                </div>

                {user.profile?.resume && (
                  <div>
                    <label className="text-sm font-medium text-gray-700 mb-1 block">
                      Resume
                    </label>
                    <a
                      href={user.profile.resume}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-primary-600 hover:text-primary-700 underline"
                    >
                      View Resume
                    </a>
                  </div>
                )}
              </div>
            </div>
          </div>
        ) : (
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <label htmlFor="fullname" className="block text-sm font-medium text-gray-700 mb-1">
                  Full Name
                </label>
                <input
                  {...register('fullname', { required: 'Full name is required' })}
                  type="text"
                  className="input-field"
                  placeholder="Enter your full name"
                />
                {errors.fullname && (
                  <p className="mt-1 text-sm text-red-600">{errors.fullname.message}</p>
                )}
              </div>

              <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                  Email
                </label>
                <input
                  {...register('email', { required: 'Email is required' })}
                  type="email"
                  className="input-field"
                  placeholder="Enter your email"
                />
                {errors.email && (
                  <p className="mt-1 text-sm text-red-600">{errors.email.message}</p>
                )}
              </div>

              <div>
                <label htmlFor="phoneNumber" className="block text-sm font-medium text-gray-700 mb-1">
                  Phone Number
                </label>
                <input
                  {...register('phoneNumber', { required: 'Phone number is required' })}
                  type="tel"
                  className="input-field"
                  placeholder="Enter your phone number"
                />
                {errors.phoneNumber && (
                  <p className="mt-1 text-sm text-red-600">{errors.phoneNumber.message}</p>
                )}
              </div>

              <div>
                <label htmlFor="resume" className="block text-sm font-medium text-gray-700 mb-1">
                  Resume
                </label>
                <input
                  type="file"
                  accept=".pdf,.doc,.docx"
                  className="input-field"
                />
              </div>
            </div>

            <div>
              <label htmlFor="bio" className="block text-sm font-medium text-gray-700 mb-1">
                Bio
              </label>
              <textarea
                {...register('bio')}
                rows={4}
                className="input-field"
                placeholder="Tell us about yourself..."
              />
            </div>

            <div>
              <label htmlFor="skills" className="block text-sm font-medium text-gray-700 mb-1">
                Skills
              </label>
              <input
                {...register('skills')}
                type="text"
                className="input-field"
                placeholder="Enter your skills separated by commas (e.g., JavaScript, React, Node.js)"
              />
              <p className="mt-1 text-sm text-gray-500">
                Separate multiple skills with commas
              </p>
            </div>

            <div className="flex space-x-4">
              <button
                type="submit"
                disabled={isLoading}
                className="btn-primary disabled:opacity-50"
              >
                {isLoading ? 'Saving...' : 'Save Changes'}
              </button>
              <button
                type="button"
                onClick={() => setIsEditing(false)}
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

export default Profile
