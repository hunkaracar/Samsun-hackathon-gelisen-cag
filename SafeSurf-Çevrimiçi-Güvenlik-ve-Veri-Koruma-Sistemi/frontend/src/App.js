import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sts from './Components/Screens/Sts';
import Navbar from '../src/Components/Navbar';
import Footer from '../src/Components/Footer';
import Contact from '../src/Components/Screens/Contact'
import VeriSifreleme from './Components/Screens/VeriSifreleme';
import SifreCozme from './Components/Screens/SifreCozme';
import SifreGucu from './Components/Screens/SifreGucu';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Sts />} />
          <Route path="/contact" element={<Contact/>} />
          <Route path="/sifreleme" element={<VeriSifreleme/>} />
          <Route path="/sifrecoz" element={<SifreCozme/>} />
          <Route path="sifregucu" element={<SifreGucu />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
