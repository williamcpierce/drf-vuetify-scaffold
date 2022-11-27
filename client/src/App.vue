<template>
    <v-app id="inspire">
        <v-app-bar app>
            <v-container fluid class="py-0 fill-height">
                <v-toolbar-title>Bird App</v-toolbar-title>
                <!-- <v-btn
                    v-for="(link, index) in links"
                    :key="index"
                    :to="link.name"
                    depressed
                >
                    {{ link.text }}
                </v-btn> -->
                <v-spacer></v-spacer>
                <v-btn icon @click="toggle_dark_mode">
                    <v-icon>mdi-theme-light-dark</v-icon>
                </v-btn>
            </v-container>
        </v-app-bar>
        <v-main>
            <v-container>
                <router-view :key="$route.path" />
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: "App",
    // data: () => ({
    //     links: [
    //         {
    //             text: "Messages",
    //             name: "/",
    //         },
    //     ],
    // }),
    methods: {
        toggle_dark_mode: function () {
            this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
            localStorage.setItem(
                "dark_theme",
                this.$vuetify.theme.dark.toString()
            );
        },
    },
    mounted() {
        const theme = localStorage.getItem("dark_theme");
        if (theme) {
            if (theme === "true") {
                this.$vuetify.theme.dark = true;
            } else {
                this.$vuetify.theme.dark = false;
            }
        } else if (
            window.matchMedia &&
            window.matchMedia("(prefers-color-scheme: dark)").matches
        ) {
            this.$vuetify.theme.dark = true;
            localStorage.setItem(
                "dark_theme",
                this.$vuetify.theme.dark.toString()
            );
        }
    },
};
</script>
