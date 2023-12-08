import axios from "axios";
import { DocToPdfApi } from "./apiEndPoints";

const handleDocToPdfUpload = (formData) => {
    console.log(formData);
    axios
        .post(DocToPdfApi, formData)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.error("Error uploading file:", error);
        });
};

export { handleDocToPdfUpload };
