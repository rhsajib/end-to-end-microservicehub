import React from 'react';
import Header from '../Header/Header';
import { Outlet } from 'react-router-dom';

const Layout = () => {
    return (
        <div>
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