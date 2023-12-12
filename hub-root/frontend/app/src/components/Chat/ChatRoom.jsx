import React from "react";
import { Outlet } from "react-router-dom";
import ActiveLink from "../ActiveLink/ActiveLink";

const ChatRoom = () => {
    const chatId = "chat-a4sfdkj490";
    return (
        <div className="h-screen">
            <div className="flex justify-center border py-4 border-b-amber-400">
                <h1 className="text-3xl">Welcome to chat room</h1>
            </div>
            <div className="flex">
                <div className="flex w-1/3 border border-t-0 border-r-amber-400 h-screen pt-4">
                    <button
                        type="submit"
                        className="border rounded-md w-full h-10  mx-6 bg-cyan-400"
                    >
                        <ActiveLink to={`/chat/${chatId}`}>
                            Chat Id: {chatId}
                        </ActiveLink>
                    </button>
                </div>
                <div className="flex-grow">
                    <h1>Chat</h1>
                    <Outlet />
                </div>
            </div>
        </div>
    );
};

export default ChatRoom;
