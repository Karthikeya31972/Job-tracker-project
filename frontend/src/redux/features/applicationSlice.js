import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  applications: [],
  applicants: [],
  isLoading: false,
  error: null,
}

const applicationSlice = createSlice({
  name: 'applications',
  initialState,
  reducers: {
    setApplications: (state, action) => {
      state.applications = action.payload
    },
    setApplicants: (state, action) => {
      state.applicants = action.payload
    },
    setLoading: (state, action) => {
      state.isLoading = action.payload
    },
    setError: (state, action) => {
      state.error = action.payload
    },
    addApplication: (state, action) => {
      state.applications.unshift(action.payload)
    },
    updateApplicationStatus: (state, action) => {
      const { applicationId, status } = action.payload
      const index = state.applications.findIndex(app => app._id === applicationId)
      if (index !== -1) {
        state.applications[index].status = status
      }
    },
    deleteApplication: (state, action) => {
      state.applications = state.applications.filter(app => app._id !== action.payload)
    },
  },
})

export const { setApplications, setApplicants, setLoading, setError, addApplication, updateApplicationStatus, deleteApplication } = applicationSlice.actions
export default applicationSlice.reducer
