import { WS_BASE_URL } from "./configCore";

export const getChatWebSocketURL = (chatId) => {
    return `${WS_BASE_URL}/ws/chat/${chatId}/`;
};

export const getFileConvertWebSocketURL = (channelId) => {
    return `${WS_BASE_URL}/ws/file/convert/${channelId}/`;
    // return `${WS_BASE_URL}/ws/file/convert/${channelId}/`;
};
