import { apiBaseUrl, apiVersion } from "../configCore";

const apiBase = apiBaseUrl + apiVersion;

export const DocToPdfApi = `${apiBase}/convert/doc-to-pdf`