<template>
    <div>
        <v-data-table :items="messages" :headers="headers"> </v-data-table>
    </div>
</template>

<script>
import messageApi from "@/services/MessageApi";

export default {
    name: "MessageView",
    data() {
        return {
            messages: [],
            headers: [
                { text: "ID", value: "id" },
                { text: "Message", value: "text" },
            ],
        };
    },
    mounted() {
        messageApi
            .getMessage()
            .then((response) => {
                this.messages = response;
            })
            .catch((error) => {
                console.log(error);
            });
    },
};
</script>
