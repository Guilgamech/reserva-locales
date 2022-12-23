<template>
<perfect-scrollbar id="data-app" ref="globalscroll" data-app :options=ps_options>
    <Menuhome/>
    <main class="main-content  mt-0">
        <div class="page-header align-items-start min-vh-100" style="background-image: url('/assets/img/bg-home.jpg');">
            <span class="mask bg-gradient-dark opacity-6"></span>
            <div class="container my-auto">
                <div class="row">
                    <Nuxt />
                </div>
            </div>      
        </div>
    </main>
</perfect-scrollbar>
</template>
<style>
@import 'vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css';
.example {  
  overflow-y: hidden; /* Add the ability to scroll */
}

/* Hide scrollbar for Chrome, Safari and Opera */
.example::-webkit-scrollbar {
    display: none;
}

.example {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>

<script>
import { PerfectScrollbar } from 'vue2-perfect-scrollbar'
import Menuhome from '../components/Menuhome.vue'
export default {
   
    components: { PerfectScrollbar, Menuhome },
    name:'Default',
    data(){
        return{            
            ps_options:{
                wheelSpeed: 0.3,
            }
        }
    },
    watch: {
        $route() {
            this.$refs.globalscroll.update();
        }
    },
    head:{
        link: [
            { rel: 'apple-touch-icon', sizes: '76x76', href: '/assets/img/apple-icon.png' },
            { rel: 'icon', type:'image/png', href: '/assets/img/favicon.png' },
            { rel: 'stylesheet', type:'text/css', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900|Roboto+Slab:400,700' },
            // { rel: 'stylesheet', href: 'https://fonts.googleapis.com/icon?family=Material+Icons+Round' },
            { rel: 'stylesheet', href: '/assets/css/nucleo-icons.css' },
            { rel: 'stylesheet', href: '/assets/fontawesome/css/all.css' },
            { rel: 'stylesheet', href: '/assets/css/nucleo-svg.css' },            
            { rel: 'stylesheet', id:'pagestyle', href: '/assets/css/material-dashboard.css?v=3.0.0' },
        ],
        script: [ 
            // { src: 'https://kit.fontawesome.com/42d5adcbca.js', crossorigin:'anonymous' },
            { src: '/assets/js/core/popper.min.js', body: true }, 
            { src: '/assets/js/core/bootstrap.min.js', body: true },       
            { src: '/assets/js/plugins/perfect-scrollbar.min.js', body: true },       
            { src: '/assets/js/plugins/smooth-scrollbar.min.js', body: true },
            { src: '/assets/js/material-dashboard.js', body: true },
            { src: '/assets/js/custom.js', body: true },            
        ],
        bodyAttrs: {
          class: 'bg-gray-200 example' 
        }
    }
}
</script>