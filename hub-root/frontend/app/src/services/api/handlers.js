import axios from "axios";
import { API } from "./apiEndPoints";

const handleFileConvertUpload = (formData) => {
    // console.log(formData.get("channelId"));
    axios
        .post(API.fileConvert, formData)
        .then((response) => {
            console.log(response.data);
        })
        .catch((error) => {
            console.error("Error uploading file:", error);
        });
};

export { handleFileConvertUpload };
