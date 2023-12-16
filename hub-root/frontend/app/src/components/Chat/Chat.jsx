import React, { useEffect, useState } from "react";
import { getChatWebSocketURL } from "../../services/webSockerEndPoints";
import { useLoaderData, useParams } from "react-router-dom";
// import { messagesLoader } from "../../services/api/apiLoaders";

const Chat = () => {
    const loadedMessages = useLoaderData();

    // Access chatId from route parameters
    const { chatId } = useParams();

    const [messages, setMessages] = useState(loadedMessages);
    const [messageText, setMessageText] = useState("");

    // State to store the WebSocket instance
    const [socket, setSocket] = useState(null);

    useEffect(() => {
        console.log(messages, chatId);

        // Create a WebSocket instance
        const newSocket = new WebSocket(getChatWebSocketURL(chatId));

        newSocket.onopen = () => {
            console.log(`WebSocket connection established for ${chatId}.`);
        };

        newSocket.onmessage = (e) => {
            // console.log(e.data)
            const message = JSON.parse(e.data);
            // console.log("Received Message:", message);
            setMessages([...messages, message]);
        };

        newSocket.onclose = () => {
            console.log("WebSocket connection closed.");
        };

        setSocket(newSocket);

        return () => {
            // Clean up WebSocket when component unmounts
            console.log("WebSocket cleaned up.");
            if (socket) {
                socket.close();
            }
        };
    }, [messages, chatId]);

    const handleSendMessageClick = () => {
        if (socket) {
            const data = JSON.stringify({
                // Trim leading and trailing whitespace
                message: messageText.trim(),
            });
            socket.send(data);
            setMessageText("");
        }
        // Clear the input field by resetting messageText to an empty string
        setMessageText("");
    };

    const handleFormSubmit = (e) => {
        e.preventDefault(); // Prevent the default form submission behavior
        if (messageText.trim() !== "") {
            handleSendMessageClick(); // Trigger the send click when the form is submitted
        }
    };

    // return (
    //     <div className="">
    //         <div className="flex flex-col mt-4 mx-4 h-screen">
    //             <div className="flex flex-col h-screen overflow-y-auto">
    //                 {messages.map((msg, index) => (
    //                     <p className="" key={index}>{msg.message}</p>
    //                 ))}
    //             </div>
    //             <div className="w-1/2 flex justify-center h-full">
    //                 <form onSubmit={handleFormSubmit}>
    //                     <input
    //                         className="border border-blue-300 w-full h-12 mb-4 px-4 py-2 rounded-md"
    //                         type="text"
    //                         placeholder="write here..."
    //                         id="message"
    //                         value={messageText}
    //                         onChange={(e) => setMessageText(e.target.value)}
    //                     />

    //                     <button
    //                         type="submit"
    //                         className="w-1/3 bg-cyan-500 rounded-md py-1 px-2"
    //                     >
    //                         Send
    //                     </button>
    //                 </form>
    //             </div>
    //         </div>
    //     </div>
    // );

    return (
        <div className="flex  h-screen flex-col mt-4">
            <div className="flex flex-grow flex-col border overflow-y-auto">
                {messages.map((msg, index) => (
                    <p className="" key={index}>
                        {msg.message}
                    </p>
                ))}
            </div>
            <div className="flex flex-shrink-0 justify-center mb-12">
                <form onSubmit={handleFormSubmit}>
                    <input
                        className="border border-blue-300 w-full h-12 mb-4 px-4 py-2 rounded-md"
                        type="text"
                        placeholder="write here..."
                        id="message"
                        value={messageText}
                        onChange={(e) => setMessageText(e.target.value)}
                    />

                    <button
                        type="submit"
                        className="w-full bg-cyan-500 rounded-md py-1 px-2"
                    >
                        Send
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Chat;
