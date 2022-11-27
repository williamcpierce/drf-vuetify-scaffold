<template>
    <v-app id="inspire">
        <v-app-bar app>
            <v-container>
                <v-btn
                    v-for="(link, index) in links"
                    :key="index"
                    :to="link.name"
                    depressed
                    class="mx-1"
                >
                    {{ link.text }}
                </v-btn>
            </v-container>
        </v-app-bar>
        <v-main>
            <v-container>
                <v-card>
                    <router-view :key="$route.path" />
                </v-card>
            </v-container>
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: "App",
    data: () => ({
        links: [
            {
                text: "Messages",
                name: "/",
            },
        ],
    }),
};
</script>
