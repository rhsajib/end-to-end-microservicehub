import { API } from "./apiEndPoints";

const messagesLoader = (chatId) => {
    const url = API.messages(chatId);
    return fetch(url);
};

export {
    messagesLoader
}
