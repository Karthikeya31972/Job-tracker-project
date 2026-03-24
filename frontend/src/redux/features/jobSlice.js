import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  jobs: [],
  singleJob: null,
  myJobs: [],
  isLoading: false,
  error: null,
}

const jobSlice = createSlice({
  name: 'jobs',
  initialState,
  reducers: {
    setJobs: (state, action) => {
      state.jobs = action.payload
    },
    setSingleJob: (state, action) => {
      state.singleJob = action.payload
    },
    setMyJobs: (state, action) => {
      state.myJobs = action.payload
    },
    setLoading: (state, action) => {
      state.isLoading = action.payload
    },
    setError: (state, action) => {
      state.error = action.payload
    },
    addJob: (state, action) => {
      state.jobs.unshift(action.payload)
    },
    updateJob: (state, action) => {
      const index = state.jobs.findIndex(job => job._id === action.payload._id)
      if (index !== -1) {
        state.jobs[index] = action.payload
      }
    },
    deleteJob: (state, action) => {
      state.jobs = state.jobs.filter(job => job._id !== action.payload)
    },
  },
})

export const { setJobs, setSingleJob, setMyJobs, setLoading, setError, addJob, updateJob, deleteJob } = jobSlice.actions
export default jobSlice.reducer
