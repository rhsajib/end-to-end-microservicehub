from .config import config

SERVICE_API = {
    'file_convert' : f'{config.FILE_CONVERT_SERVICE_BASE_URL}/api/v1/file/convert/',
    'chat'         : f'{config.CHAT_SERVICE_BASE_URL}/api/v1/chat/'
}

