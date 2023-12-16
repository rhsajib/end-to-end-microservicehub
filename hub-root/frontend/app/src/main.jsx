import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from "./components/Home/Home.jsx";
import Layout from "./components/Layout/Layout.jsx";
import FileConvert from "./components/FileConvert/FileConvert.jsx";
import ChatRoom from "./components/Chat/ChatRoom.jsx";
import Chat from "./components/Chat/Chat.jsx";
import { messagesLoader } from "./services/api/apiLoaders.js";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Layout />,
        children: [
            {
                path: "/home",
                element: <Home />,
            },
            {
                path: "/file-convert",
                element: <FileConvert />,
            },
            {
                path: "/chat",
                element: <ChatRoom />,
                children: [
                    {
                        path: "/chat/:chatId",
                        element: <Chat />,
                        loader: ({ params }) => messagesLoader(params.chatId),
                    },
                ],
            },
        ],
    },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <RouterProvider router={router} />
        {/* <App /> */}
    </React.StrictMode>
);
