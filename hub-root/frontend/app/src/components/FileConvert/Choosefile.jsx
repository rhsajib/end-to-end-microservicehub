import React from "react";

const Choosefile = ({handleFileChange}) => {
    return (
        <div className="flex justify-center">
            <div className="my-4">
                <label htmlFor="fileInput"></label>
                <input
                    type="file"
                    className="block w-full text-sm text-slate-500
                            file:mr-4 file:py-2 file:px-4
                            file:rounded-full file:border-0
                            file:text-sm file:font-semibold
                            file:bg-violet-50 file:text-violet-700
                            hover:file:bg-violet-100
                            "
                    id="fileInput"
                    // Make sure to include the name attribute
                    name="file"
                    // Without the name attribute, the file input doesn't contribute to the FormData when it is appended.
                    accept=".txt, .doc, .docx"
                    onChange={handleFileChange}
                />
            </div>
        </div>
    );
};

export default Choosefile;
