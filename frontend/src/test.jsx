import React from 'react'

const Test = () => {
  return (
    <div style={{ 
      padding: '40px', 
      fontSize: '32px', 
      color: '#3b82f6',
      textAlign: 'center',
      backgroundColor: '#f0f9ff',
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column'
    }}>
      <div style={{ marginBottom: '20px' }}>🎉</div>
      <div>Job Portal Frontend is Working!</div>
      <div style={{ fontSize: '16px', color: '#6b7280', marginTop: '10px' }}>
        If you can see this, React is rendering correctly
      </div>
    </div>
  )
}

export default Test
