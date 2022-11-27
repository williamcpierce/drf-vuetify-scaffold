<template>
    <v-app id="inspire">
        <v-app-bar app>
            <v-container fluid class="py-0 fill-height">
                <v-toolbar-title>Bird App</v-toolbar-title>
                <v-spacer></v-spacer>
                <ThemeToggle />
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
import ThemeToggle from "@/components/ThemeToggle";

export default {
    name: "App",
    components: { ThemeToggle },
};
</script>
