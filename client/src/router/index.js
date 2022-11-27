import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

export default new VueRouter({
    routes: [
        {
            path: "/",
            name: "message",
            component: () =>
                import(
                    /* webpackChunkName: "message" */ "@/views/MessageView.vue"
                ),
        },
    ],
});
