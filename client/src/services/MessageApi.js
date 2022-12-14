import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000";

export default {
    getMessage() {
        return axios.get("/api/message/").then((response) => {
            return response.data;
        });
    },
    postMessage(data) {
        return axios.post("/api/message/", data).then((response) => {
            return response.data;
        });
    },
};
