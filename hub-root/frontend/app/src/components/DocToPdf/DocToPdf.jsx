import React, { useState } from "react";
import { handleDocToPdfUpload } from "../../services/api/handlers";

// https://www.filestack.com/fileschool/react/react-file-upload/
// https://uploadcare.com/blog/how-to-upload-file-in-react/

const DocToPdf = () => {
    // const [selectedFile, setSelectedFile] = useState<File>(null);
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (e) => {
        e.preventDefault();
        const file = e.target.files[0];
        // console.log(e.target.files)
        // console.log('handleFileChange', file);

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

        // Create FormData to send the file
        const formData = new FormData();
        formData.append("file", selectedFile);

        // for debug

        // Accessing the value of the "file" key
        const fileValue = formData.get("file");
        console.log(fileValue);

        // for (const entry of formData.entries()) {
        //     const [key, value] = entry;
        //     console.log(`${key}: ${value}`);
        // }

        // Make a POST request using Axios
        handleDocToPdfUpload(formData);
    };

    return (
        <div className="">
            <div className="flex">
                <label htmlFor="fileInput">Upload Doc (.docx/.doc/.txt) File (max size: 20 MB): </label>
                <input
                    className="px-4"
                    type="file"
                    id="fileInput"
                    // Make sure to include the name attribute
                    name="file"
                    // Without the name attribute, the file input doesn't contribute to the FormData when it is appended.
                    accept=".txt, .doc, .docx"
                    onChange={handleFileChange}
                />
            </div>
            <div className="flex">
                <button
                    className="border p-1 bg-slate-200"
                    onClick={handleUploadButtonClick}
                >
                    Upload File
                </button>
            </div>
            <div className="flex justify-center">
                {selectedFile && (
                    <div>
                        <h1 className="flex">File Details</h1>
                        <p className="flex">
                            Selected File: {selectedFile.name}
                        </p>
                        {/* Add your logic for processing the uploaded file here */}

                        <p className="flex">
                            File Size: {(selectedFile.size / 1024).toFixed(1)}{" "}
                            KB
                        </p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default DocToPdf;
