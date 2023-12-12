import React from "react";
import Header from "../Header/Header";
import { Outlet } from "react-router-dom";

const Layout = () => {
    return (
        <div className="h-screen">
        {/* <div className="h-screen bg-gray-100"> */}
            <div>
                <Header />
            </div>
            <div>
                <Outlet />
            </div>
        </div>
    );
};

export default Layout;
