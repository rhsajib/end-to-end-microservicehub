import React from "react";
import ActiveLink from "../ActiveLink/ActiveLink";

const Header = () => {
    return (
        <nav>
            <div className="flex justify-around border border-b-cyan-500 bg-gray-200 p-3">
                <ActiveLink to="/home">Home</ActiveLink>
                <ActiveLink to="/file-convert">File Conversion</ActiveLink>
                <ActiveLink to="/chat">Chat</ActiveLink>
            </div>
        </nav>
    );
};

export default Header;
