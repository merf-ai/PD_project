import { createApp } from 'vue'
import App from './App.vue'
// import components from "@/components/UI";
import router from './router'
import store from './store'
import axios from "axios"
import bootstrap from 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'

createApp(App).use(store).use(router).mount('#app')

axios.defaults.baseURL = 'http://192.168.0.103:8000/';

const app = createApp(App);

directives.forEach(directive => {
    app.directive(directive.name, directive)
});

// components.forEach(component => {
//     app.component(component.name, component)
// });

app
    .use(store)
    .use(router, axios, bootstrap)
    .mount("#app");
