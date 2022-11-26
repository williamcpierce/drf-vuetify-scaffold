<template>
    <p>{{ message }}</p>
</template>

<script>
import messageApi from "@/services/MessageApi";

export default {
    name: "MessageView",
    data() {
        return {
            message: "",
        };
    },
    mounted() {
        messageApi
            .getMessage()
            .then((response) => {
                this.message = response;
            })
            .catch((error) => {
                console.log(error);
            });
    },
};
</script>
