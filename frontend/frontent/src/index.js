import React from 'react';
import ReactDOM from 'react-dom/client';
import { AuthProvider } from './context/auth'
import RoutesT from './Routes';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(

  <AuthProvider>
    <React.StrictMode>
      <RoutesT />
    </React.StrictMode>
  </AuthProvider>

);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
