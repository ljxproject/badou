import Vue from 'vue'
import VueRouter from 'vue-router'
import Register from 'badou/templates/register.html'

const register = {template: Register}

const routes = [{path: '/register', component: register}]

Vue.use(VueRouter);
const router = new VueRouter(routes);
new Vue({
    el: '#login',
    router,
    data: {
        LoginData: {
            mobile: '',
            password: ''
        },

    },
    methods: {
        login: function () {
            var url = generateUrl('/');
            this.$http.post(url, this.LoginData);
        },
        // register: function () {
        //     // var url = generateUrl('/users/register');
        //
        //     // this.$router.push('/users/register')
        //     // this.$http.get(url);
        // }
    },
    ready: function () {
    }
}); 
