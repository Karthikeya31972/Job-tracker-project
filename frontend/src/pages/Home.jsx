import { Link } from 'react-router-dom'
import { useSelector } from 'react-redux'
import { FiBriefcase, FiUsers, FiTrendingUp, FiArrowRight } from 'react-icons/fi'

const Home = () => {
  const { isAuthenticated } = useSelector((store) => store.auth)

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary-600 to-primary-700 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Find Your Dream Job
            </h1>
            <p className="text-xl md:text-2xl mb-8 text-primary-100">
              Connect with top companies and take your career to the next level
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              {isAuthenticated ? (
                <Link
                  to="/jobs"
                  className="btn-primary bg-white text-primary-600 hover:bg-gray-100 inline-flex items-center justify-center"
                >
                  Browse Jobs
                  <FiArrowRight className="ml-2" />
                </Link>
              ) : (
                <>
                  <Link
                    to="/register"
                    className="btn-primary bg-white text-primary-600 hover:bg-gray-100 inline-flex items-center justify-center"
                  >
                    Get Started
                    <FiArrowRight className="ml-2" />
                  </Link>
                  <Link
                    to="/jobs"
                    className="btn-secondary bg-transparent border-2 border-white text-white hover:bg-white hover:text-primary-600"
                  >
                    Browse Jobs
                  </Link>
                </>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Why Choose JobPortal?
            </h2>
            <p className="text-xl text-gray-600">
              We make job searching simple and effective
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <FiBriefcase className="text-primary-600 text-2xl" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Thousands of Jobs</h3>
              <p className="text-gray-600">
                Browse through thousands of job listings from top companies
              </p>
            </div>

            <div className="text-center">
              <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <FiUsers className="text-primary-600 text-2xl" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Direct Applications</h3>
              <p className="text-gray-600">
                Apply directly to companies and track your application status
              </p>
            </div>

            <div className="text-center">
              <div className="bg-primary-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <FiTrendingUp className="text-primary-600 text-2xl" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Career Growth</h3>
              <p className="text-gray-600">
                Find opportunities that match your skills and career goals
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Ready to Find Your Next Opportunity?
          </h2>
          <p className="text-xl text-gray-600 mb-8">
            Join thousands of job seekers who have found their dream jobs through JobPortal
          </p>
          {!isAuthenticated && (
            <Link
              to="/register"
              className="btn-primary inline-flex items-center"
            >
              Sign Up Now
              <FiArrowRight className="ml-2" />
            </Link>
          )}
        </div>
      </section>
    </div>
  )
}

export default Home
