import React from "react";
import { Route, Routes, BrowserRouter } from "react-router-dom";

import Login from "./pages/Login";
import Home from "./pages/Home";
import LerContent from "./pages/LerContent"


const RoutesT = () => {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<Home />} />
                <Route path="/ler/:id" element={<LerContent />}/> 
            </Routes>
        </BrowserRouter>
    );
}

export default RoutesT;