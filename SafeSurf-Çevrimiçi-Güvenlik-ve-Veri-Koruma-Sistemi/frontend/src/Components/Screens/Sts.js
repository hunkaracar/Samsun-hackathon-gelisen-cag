import React, { useState } from 'react';

export default function Sts() {
  const [inputValue, setInputValue] = useState('');
  const [attackType, setAttackType] = useState('');
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleAnalyzeClick = () => {
    console.log(`URL/IP: ${inputValue}`);
    setLoading(true);
  
    fetch("http://127.0.0.1:5000/api/sts", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url_or_ip: inputValue })
    })
    .then(response => response.json())
    .then(data => {
      setAttackType(data.attack_type);
      setLoading(false);
    })
    .catch(error => {
      console.error('Error:', error);
      setLoading(false);
    });
  };
  

  return (
    <div style={styles.container}>
      <div style={styles.logoContainer}>
        <h1 style={styles.logo}>Saldırı Tespit Sistemi</h1>
      </div>
      <div style={styles.inputContainer}>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="URL veya IP adresi giriniz"
          style={styles.input}
        />
        <button onClick={handleAnalyzeClick} style={styles.button}>
          Analiz Et
        </button>
      </div>
      <div style={styles.resultContainer}>
        <label style={styles.label}>Saldırı Türü:</label>
        <span>{attackType}</span>
      </div>
      {loading && (
        <div style={styles.loadingOverlay}>
          <div style={styles.loader}></div>
          <p style={styles.loadingText}>Yükleniyor...</p>
        </div>
      )}
      <style jsx>{`
        .loader {
          border: 16px solid #f3f3f3; /* Light grey */
          border-top: 16px solid #3498db; /* Blue */
          border-radius: 50%;
          width: 80px;
          height: 80px;
          animation: spin 2s linear infinite;
        }

        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}

const styles = {
  container: {
    textAlign: 'center',
    marginTop: '10%',
    padding: '20px',
    backgroundColor: '#f0f0f0',
    borderRadius: '8px',
    boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
    position: 'relative',
  },
  logoContainer: {
    marginBottom: '30px',
  },
  logo: {
    fontSize: '48px',
    fontFamily: 'Arial, sans-serif',
    color: 'black',
  },
  inputContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginBottom: '20px',
  },
  input: {
    width: '80%',
    padding: '15px',
    fontSize: '18px',
    border: '1px solid #dfe1e5',
    borderRadius: '24px',
    outline: 'none',
    marginBottom: '10px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
  },
  button: {
    padding: '15px 30px',
    fontSize: '18px',
    border: 'none',
    borderRadius: '24px',
    backgroundColor: '#3498db',
    color: 'white',
    cursor: 'pointer',
    outline: 'none',
  },
  resultContainer: {
    marginTop: '20px',
    textAlign: 'center',
  },
  label: {
    fontSize: '20px',
    fontWeight: 'bold',
    marginRight: '10px',
  },
  loadingOverlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000,
  },
  loader: {
    border: '16px solid #f3f3f3',
    borderTop: '16px solid #3498db',
    borderRadius: '50%',
    width: '80px',
    height: '80px',
    animation: 'spin 2s linear infinite',
  },
  loadingText: {
    marginTop: '20px',
    fontSize: '20px',
    color: '#000',
  },
};
