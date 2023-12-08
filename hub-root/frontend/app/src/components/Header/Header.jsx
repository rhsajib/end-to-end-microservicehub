import React from "react";
import ActiveLink from "../ActiveLink/ActiveLink";
import { Link } from "react-router-dom";

const Header = () => {
    return (
        <nav>
            <div className="flex justify-around mb-10 border p-3">
                <ActiveLink to="/home">Home</ActiveLink>
                <ActiveLink to="/doc-to-pdf">Doc To Pdf</ActiveLink>
            </div>
        </nav>
    );
};

export default Header;
