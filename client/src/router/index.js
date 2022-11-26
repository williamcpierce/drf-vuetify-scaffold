import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

export default new VueRouter({
    routes: [
        {
            path: "/home",
            name: "home",
            component: () =>
                import(/* webpackChunkName: "home" */ "@/views/HomeView.vue"),
        },
        {
            path: "/message",
            name: "message",
            component: () =>
                import(
                    /* webpackChunkName: "message" */ "@/views/MessageView.vue"
                ),
        },
    ],
});
