import React from "react";
import { Route, Routes, BrowserRouter } from "react-router-dom";

import Login from "./Login";


const RoutesT = () => {

    return (
        <BrowserRouter>
            <Routes>
                <Route path="" element={<Login />} />
            </Routes>
        </BrowserRouter>
    );
}

export default RoutesT;