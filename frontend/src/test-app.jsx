import React from 'react'

function TestApp() {
  return (
    <div style={{ 
      padding: '40px', 
      fontSize: '24px', 
      color: '#2563eb',
      textAlign: 'center',
      backgroundColor: '#f9fafb',
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }}>
      <div>
        <h1 style={{ marginBottom: '20px' }}>Job Portal Test</h1>
        <p style={{ color: '#6b7280' }}>If you can see this, React is working!</p>
      </div>
    </div>
  )
}

export default TestApp
