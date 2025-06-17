import React from 'react';
import { FaGithub, FaLinkedin, FaEnvelope, FaPhone } from 'react-icons/fa';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="icon-row">
        <a href="https://github.com/maneesxh" target="_blank" rel="noopener noreferrer">
          <FaGithub size={24} /> <span>GitHub</span>
        </a>
        <a href="https://linkedin.com/in/maneeshthota" target="_blank" rel="noopener noreferrer">
          <FaLinkedin size={24} /> <span>LinkedIn</span>
        </a>
        <a href="mailto:your.thotamaneesh@gmail.com">
          <FaEnvelope size={24} /> <span>Email</span>
        </a>
        <a href="tel:+917013938953">
          <FaPhone size={24} /> <span>Phone</span>
        </a>
      </div>
      <div className="signature">
        Coded by Maneesh Thota
      </div>
    </footer>
  );
}

export default Footer;
