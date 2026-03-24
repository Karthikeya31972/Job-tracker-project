import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  user: null,
  isAuthenticated: false,
  isLoading: false,
}

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    loginStart: (state) => {
      state.isLoading = true
    },
    loginSuccess: (state, action) => {
      state.user = action.payload.user
      state.isAuthenticated = true
      state.isLoading = false
    },
    loginFailure: (state) => {
      state.user = null
      state.isAuthenticated = false
      state.isLoading = false
    },
    logout: (state) => {
      state.user = null
      state.isAuthenticated = false
      state.isLoading = false
    },
    updateUser: (state, action) => {
      state.user = { ...state.user, ...action.payload }
    },
  },
})

export const { loginStart, loginSuccess, loginFailure, logout, updateUser } = authSlice.actions
export default authSlice.reducer
