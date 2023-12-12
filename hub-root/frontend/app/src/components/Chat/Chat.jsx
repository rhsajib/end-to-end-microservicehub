import React, { useEffect, useState } from "react";
import { getChatWebSocketURL } from "../../services/webSockerEndPoints";
import { useParams } from "react-router-dom";

const Chat = () => {
    // Access chatId from route parameters
    const { chatId } = useParams();

    const [messages, setMessages] = useState([]);
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
            const data = JSON.parse(e.data);
            console.log("Received Message:", data.message);
            setMessages([...messages, data.message]);
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

    const handleFormSubmit = (e) => {
        e.preventDefault(); // Prevent the default form submission behavior

        if (socket) {
            const data = JSON.stringify({
                message: messageText,
                service: "chat",
            });
            socket.send(data);
            setMessageText("");
        }
    };

    return (
        <div className="flex flex-col">
            <div className="flex mt-4 mx-4">
                <div className="w-1/2 flex flex-col justify-center">
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
                            className="w-1/3 bg-cyan-500 rounded-md py-1 px-2"
                        >
                            Send
                        </button>
                    </form>
                </div>

                <div>
                    {messages.map((msg, idx) => (
                        <p key={idx}>{msg}</p>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Chat;
