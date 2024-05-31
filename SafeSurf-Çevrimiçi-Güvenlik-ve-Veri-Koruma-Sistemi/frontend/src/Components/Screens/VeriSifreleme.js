import React, { useState } from 'react';

export default function VeriSifreleme() {
  const [inputValue, setInputValue] = useState('');
  const [encryptedText, setEncryptedText] = useState('');
  const [key, setKey] = useState('');
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleKeyChange = (e) => {
    setKey(e.target.value);
  };

  const handleSearchClick = () => {
    console.log(inputValue);
    setLoading(true);

    fetch("http://127.0.0.1:5000/api/veri-sifreleme", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      mode: 'cors',
      body: JSON.stringify({ text: inputValue, key: key }) // Anahtarı isteğe ekle
    })
      .then(response => response.json())
      .then(data => {
        setEncryptedText(data.encrypted_data);
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
        <h1 style={styles.logo}>Metin Girişi: </h1>
      </div>
      <div style={styles.searchContainer}>
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Metin giriniz"
          style={styles.input}
        />
        <input
          type="text" // Anahtarın girişi için input alanı eklendi
          value={key}
          onChange={handleKeyChange}
          placeholder="Anahtar giriniz"
          style={styles.keyinput}
        />
        <button onClick={handleSearchClick} style={styles.button}>
          Şifrele
        </button>
      </div>
      <div style={styles.resultContainer}>
        <div style={styles.resultItem}>
          <label style={styles.label}>Şifreli Metin:</label>
          <span>{encryptedText}</span>
        </div>
      </div>
      {loading && (
        <div style={styles.loadingOverlay}>
          <div style={styles.loader}></div>
          <p style={styles.loadingText}>Metin Şifreleniyor...</p>
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
  searchContainer: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: '20px',
  },
  input: {
    width: '50%',
    padding: '15px',
    fontSize: '18px',
    border: '1px solid #dfe1e5',
    borderRadius: '24px',
    outline: 'none',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
  },
  keyinput: {
    width: '10%',
    padding: '15px',
    fontSize: '18px',
    border: '1px solid #dfe1e5',
    borderRadius: '24px',
    outline: 'none',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)',
  },
  button: {
    marginLeft: '10px',
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
