import React from "react";

const UploadFile = ({
    selectedFile,
    status,
    download,
    handleUploadButtonClick,
}) => {
    return (
        <div className="flex w-1/2 flex-col items-center">
            {selectedFile && (
                <>
                    <div className="mt-24 mb-6">
                        <h3>
                            File Status: {status}
                            {download ? <a href="#">  (Download)</a> : null}
                        </h3>
                    </div>
                    <div>
                        <div className="text-center mt-10 mb-12">
                            <h1 className="text-xl pb-2">File Details</h1>
                            <hr />
                            <p className="flex">Name: {selectedFile.name}</p>
                            <hr />
                            {/* Add your logic for processing the uploaded file here */}

                            <p className="flex">
                                Size: {(selectedFile.size / 1024).toFixed(1)} KB
                            </p>
                            <hr />
                        </div>
                    </div>
                    <div className="flex justify-center mx-16 my-2 w-full">
                        <button
                            className="border p-1 bg-cyan-700 hover:bg-cyan-400 hover:text-black w-2/5 text-white rounded-lg"
                            onClick={handleUploadButtonClick}
                        >
                            Upload File
                        </button>
                    </div>
                </>
            )}
        </div>
    );
};

export default UploadFile;
