import React from 'react';
import { useNavigate } from 'react-router-dom'; 


const Navbar = () => {
  const navigate=useNavigate();

  const handleContact=()=>{
    navigate('/contact');
  }
  const handleAbout=()=>{
    navigate('/about');
  }
  const handleSifrele=()=>{
    navigate('/sifreleme');
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <a className="navbar-brand" href="/">
          STS
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
          <li className="nav-item">
              <a className="nav-link" href="/sifreleme" onClick={handleSifrele}>
              Veri Şifrele
              </a>
            </li>

            <li className="nav-item">
              <a className="nav-link" href="/sifrecoz" onClick={handleSifrele}>
              Şifre Çöz
              </a>
            </li>

            <li className="nav-item">
              <a className="nav-link" href="/sifregucu" onClick={handleSifrele}>
              Sifre Gücü
              </a>
            </li>

            <li className="nav-item">
              <a className="nav-link" href="/contact" onClick={handleContact}>
                İletişim
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
