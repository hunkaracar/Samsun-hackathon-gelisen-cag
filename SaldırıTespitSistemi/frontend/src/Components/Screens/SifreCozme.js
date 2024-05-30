import React, { useState } from 'react';

export default function SifreCozme() {
  const [encryptedText, setEncryptedText] = useState('');
  const [key, setKey] = useState('');
  const [decryptedText, setDecryptedText] = useState('');
  const [loading, setLoading] = useState(false);

  const handleEncryptedTextChange = (e) => {
    setEncryptedText(e.target.value);
  };

  const handleKeyChange = (e) => {
    setKey(e.target.value);
  };

  const handleDecryptClick = () => {
    console.log(`Encrypted Text: ${encryptedText}, Key: ${key}`);
    setLoading(true);
  
    fetch("http://127.0.0.1:5000/api/sifre-cozme", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ encrypted_text: encryptedText, key: key })
    })
    .then(response => response.json())
    .then(data => {
      setDecryptedText(data.decrypted_text);
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
        <h1 style={styles.logo}>Şifre Çözme</h1>
      </div>
      <div style={styles.inputContainer}>
        <input
          type="text"
          value={encryptedText}
          onChange={handleEncryptedTextChange}
          placeholder="Şifreli metin giriniz"
          style={styles.input}
        />
        <input
          type="text"
          value={key}
          onChange={handleKeyChange}
          placeholder="Anahtar giriniz"
          style={styles.input}
        />
        <button onClick={handleDecryptClick} style={styles.button}>
          Çöz
        </button>
      </div>
      <div style={styles.resultContainer}>
        <div style={styles.resultItem}>
          <label style={styles.label}>Çözülen Metin:</label>
          <span>{decryptedText}</span>
        </div>
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
    marginTop: '15%',
  },
  logoContainer: {
    marginBottom: '40px',
  },
  logo: {
    fontSize: '64px',
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
    width: '50%',
    padding: '15px',
    margin: '10px 0',
    fontSize: '18px',
    border: '1px solid #dfe1e5',
    borderRadius: '24px',
    outline: 'none',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
  },
  button: {
    padding: '15px 20px',
    fontSize: '18px',
    border: 'none',
    borderRadius: '24px',
    backgroundColor: 'black',
    color: 'white',
    cursor: 'pointer',
    outline: 'none',
  },
  resultContainer: {
    marginTop: '20px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  resultItem: {
    margin: '10px 0',
  },
  label: {
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
