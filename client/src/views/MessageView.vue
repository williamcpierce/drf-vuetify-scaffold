<template>
    <v-card rounded="lg" class="elevation-5">
        <v-card-title>
            Posts
            <v-dialog v-model="dialog" max-width="700px">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn class="ml-3" icon v-bind="attrs" v-on="on">
                        <v-icon>mdi-plus</v-icon>
                    </v-btn>
                </template>
                <v-card rounded="lg">
                    <v-card-title>
                        <span class="text-h5">New Post</span>
                    </v-card-title>
                    <v-card-text>
                        <v-textarea
                            v-model="message"
                            label="Message"
                            auto-grow
                        />
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer />
                        <v-btn text @click="close"> Cancel </v-btn>
                        <v-btn color="blue" text @click="save"> Post </v-btn>
                        <v-spacer />
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-spacer></v-spacer>
            <v-responsive max-width="260">
                <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    hide-details
                    dense
                    rounded
                    filled
                ></v-text-field>
            </v-responsive>
        </v-card-title>
        <v-data-table
            :items="messages"
            :headers="headers"
            :search="search"
        ></v-data-table>
    </v-card>
</template>

<script>
import messageApi from "@/services/MessageApi";

export default {
    name: "MessageView",
    data() {
        return {
            messages: [],
            dialog: false,
            search: "",
            message: "",
            headers: [{ text: "Message", value: "text" }],
        };
    },
    mounted() {
        this.read();
    },
    methods: {
        read() {
            messageApi
                .getMessage()
                .then((response) => {
                    this.messages = response;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        close() {
            this.dialog = false;
            this.$nextTick(() => {
                this.message = "";
            });
        },
        save() {
            messageApi
                .postMessage({ text: this.message })
                .then((response) => {
                    this.read();
                })
                .catch((error) => {
                    console.log(error);
                });
            this.close();
        },
    },
};
</script>
