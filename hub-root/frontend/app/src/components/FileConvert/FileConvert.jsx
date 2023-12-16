import React, { useEffect, useState } from "react";
import { handleFileConvertUpload } from "../../services/api/handlers";
import SelectType from "./SelectType";
import Choosefile from "./Choosefile";
import UploadFile from "./UploadFile";
import { getFileConvertWebSocketURL } from "../../services/webSockerEndPoints";
import { v4 as uuidv4 } from "uuid";

// https://www.filestack.com/fileschool/react/react-file-upload/
// https://uploadcare.com/blog/how-to-upload-file-in-react/

const FileConvert = () => {
    // when user will click upload button a `channelId` will be generated
    // when the `channelId` will be generated, it will connecte to a websocket
    // with this file id as unique `channelId` or `roomId`

    const [selectedFile, setSelectedFile] = useState(null);
    const [fileType, setFileType] = useState("");
    const [channelId, setChannelId] = useState("");
    const [status, setStatus] = useState(null);
    const [socket, setSocket] = useState(null);
    const [download, setDownload] = useState(false);

    useEffect(() => {
        if (channelId) {
            // Create a WebSocket connection using the generated ID
            const newSocket = new WebSocket(
                getFileConvertWebSocketURL(channelId)
            );

            newSocket.onopen = () => {
                console
                    .log
                    // `WebSocket connection established for ${channelId}`
                    ();
            };

            newSocket.onmessage = (e) => {
                const data = JSON.parse(e.data);
                console.log("Received Status:", data.status);
                setStatus(data.status);
                if (data.status === "Completed") {
                    setDownload(true);
                }
            };

            // Store the socket in state to manage its lifecycle
            setSocket(newSocket);

            return () => {
                // Close the socket when the component unmounts or when the file ID changes
                console.log("WebSocket cleaned up.");
                if (socket) {
                    socket.close();
                }
            };
        }
    }, [channelId]);

    const handleFileChange = (e) => {
        e.preventDefault();
        const file = e.target.files[0];
        // console.log(e.target.files)
        // console.log('handleFileChange', file);
        setDownload(false);
        setStatus("Click upload button...");
        setSelectedFile(file);
    };

    const handleUploadButtonClick = () => {
        // Check if a file is selected

        if (!selectedFile) {
            alert("Please select a file before uploading.");
            return;
        }

        // if (selectedFile.type !== "text/plain") {
        //     alert("Please select a valid text file (.txt).")
        // }

        // Generate a unique ID when the upload button is clicked
        // generating uuid causes some delay.
        // const generatedID = 4;
        let generatedID;
        try {
            generatedID = uuidv4();
        } catch (error) {
            console.error("Error generating UUID:", error);
            alert("Error generating unique ID. Please try again.");
            return;
        }

        setChannelId(generatedID);

        // Create FormData to send the file
        const formData = new FormData();
        formData.append("file", selectedFile);
        formData.append("channelId", generatedID);

        // for debug

        // Accessing the value of the "file" key
        const fileValue = formData.get("file");
        console.log(fileValue);
        console.log(formData.get("channelId"));

        // for (const entry of formData.entries()) {
        //     const [key, value] = entry;
        //     console.log(`${key}: ${value}`);
        // }

        // Make a POST request using Axios
        setStatus("Uploading...");
        handleFileConvertUpload(formData);
    };

    return (
        <div className="flex h-screen">
            <div className="flex flex-col w-1/2 border px-8 border-r-orange-400">
                <div className="flex items-center mt-6">
                    <div className="text-cyan-700">Select File Type</div>
                    <div className="flex-grow">
                        <SelectType fileType={fileType} />
                    </div>
                </div>
                <Choosefile handleFileChange={handleFileChange} />
            </div>
            <UploadFile
                selectedFile={selectedFile}
                status={status}
                download={download}
                handleUploadButtonClick={handleUploadButtonClick}
            />
        </div>
    );
};

export default FileConvert;
