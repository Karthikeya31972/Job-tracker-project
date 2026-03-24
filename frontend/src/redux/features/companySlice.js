import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  companies: [],
  singleCompany: null,
  isLoading: false,
  error: null,
}

const companySlice = createSlice({
  name: 'companies',
  initialState,
  reducers: {
    setCompanies: (state, action) => {
      state.companies = action.payload
    },
    setSingleCompany: (state, action) => {
      state.singleCompany = action.payload
    },
    setLoading: (state, action) => {
      state.isLoading = action.payload
    },
    setError: (state, action) => {
      state.error = action.payload
    },
    addCompany: (state, action) => {
      state.companies.unshift(action.payload)
    },
    updateCompany: (state, action) => {
      const index = state.companies.findIndex(company => company._id === action.payload._id)
      if (index !== -1) {
        state.companies[index] = action.payload
      }
    },
  },
})

export const { setCompanies, setSingleCompany, setLoading, setError, addCompany, updateCompany } = companySlice.actions
export default companySlice.reducer
