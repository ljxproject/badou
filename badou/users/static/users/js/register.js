import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from 'badou/templates/registration/login.html'

const login = {template: Login}

const routes = [{path: '/', component: login}]

Vue.use(VueRouter);
const router = new VueRouter(routes);
var vm = new Vue({
 	el: '#register',
	router,
    data: { 
        RegisterData: { 
             username: '', 
             password1: '',
             password2: ''
        },

    }, 
 	methods: { 
     	register: function () { 
         	var url = generateUrl('/users/register');
         	this.$http.post(url, this.RegisterData);
       },
       	cancel: function(){
       	var url = generateUrl('/login');
       	this.$http.get(url);
       }
 	}, 
 	ready: function () { 
 	} 
}); 
