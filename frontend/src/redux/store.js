import { configureStore } from '@reduxjs/toolkit'
import authReducer from './features/authSlice'
import jobReducer from './features/jobSlice'
import applicationReducer from './features/applicationSlice'
import companyReducer from './features/companySlice'

export const store = configureStore({
  reducer: {
    auth: authReducer,
    jobs: jobReducer,
    applications: applicationReducer,
    companies: companyReducer,
  },
})
