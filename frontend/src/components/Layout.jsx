import { Outlet, Link, useNavigate } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { logout } from '../redux/features/authSlice'
import { FiUser, FiBriefcase, FiLogOut, FiMenu, FiX } from 'react-icons/fi'
import { useState } from 'react'
import api from '../utils/api'

const Layout = () => {
  const { isAuthenticated, user } = useSelector((store) => store.auth)
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const handleLogout = async () => {
    try {
      await api.post('/user/logout')
      dispatch(logout())
      navigate('/')
    } catch (error) {
      console.error('Logout failed:', error)
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <Link to="/" className="text-2xl font-bold text-primary-600">
              JobPortal
            </Link>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex items-center space-x-8">
              <Link to="/jobs" className="text-gray-700 hover:text-primary-600 transition-colors">
                Browse Jobs
              </Link>
              {isAuthenticated ? (
                <>
                  <Link to="/dashboard" className="text-gray-700 hover:text-primary-600 transition-colors">
                    Dashboard
                  </Link>
                  <Link to="/companies" className="text-gray-700 hover:text-primary-600 transition-colors">
                    Companies
                  </Link>
                  <div className="flex items-center space-x-4">
                    <span className="text-sm text-gray-600">
                      Welcome, {user?.fullname}
                    </span>
                    <button
                      onClick={handleLogout}
                      className="flex items-center space-x-2 text-gray-700 hover:text-primary-600 transition-colors"
                    >
                      <FiLogOut />
                      <span>Logout</span>
                    </button>
                  </div>
                </>
              ) : (
                <div className="flex items-center space-x-4">
                  <Link
                    to="/login"
                    className="text-gray-700 hover:text-primary-600 transition-colors"
                  >
                    Login
                  </Link>
                  <Link
                    to="/register"
                    className="btn-primary"
                  >
                    Sign Up
                  </Link>
                </div>
              )}
            </nav>

            {/* Mobile menu button */}
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="md:hidden p-2 rounded-md text-gray-700 hover:bg-gray-100"
            >
              {isMenuOpen ? <FiX size={24} /> : <FiMenu size={24} />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden border-t bg-white">
            <div className="px-4 pt-2 pb-3 space-y-1">
              <Link
                to="/jobs"
                className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md"
                onClick={() => setIsMenuOpen(false)}
              >
                Browse Jobs
              </Link>
              {isAuthenticated ? (
                <>
                  <Link
                    to="/dashboard"
                    className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    Dashboard
                  </Link>
                  <Link
                    to="/companies"
                    className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    Companies
                  </Link>
                  <div className="px-3 py-2 text-sm text-gray-600">
                    Welcome, {user?.fullname}
                  </div>
                  <button
                    onClick={() => {
                      handleLogout()
                      setIsMenuOpen(false)
                    }}
                    className="flex items-center space-x-2 px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md w-full"
                  >
                    <FiLogOut />
                    <span>Logout</span>
                  </button>
                </>
              ) : (
                <>
                  <Link
                    to="/login"
                    className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    Login
                  </Link>
                  <Link
                    to="/register"
                    className="block px-3 py-2 text-primary-600 hover:bg-gray-50 rounded-md"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    Sign Up
                  </Link>
                </>
              )}
            </div>
          </div>
        )}
      </header>

      {/* Main Content */}
      <main className="flex-1">
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-8 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <p className="text-sm">
              © 2024 JobPortal. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default Layout
