import React, { Children } from "react";
import { Link, NavLink } from "react-router-dom";

const ActiveLink = ({ to, children }) => {
    return <NavLink to={to}>{children}</NavLink>;
};

export default ActiveLink;
