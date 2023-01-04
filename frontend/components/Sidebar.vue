<template>
    <aside
        class="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 fixed-start ms-3   bg-gradient-dark"
        id="sidenav-main">
        <div class="sidenav-header">
            <i @click="toggleSidenav()"
                class="fas fa-times p-3 cursor-pointer text-white opacity-5 position-absolute end-0 top-0 d-none d-xl-none"
                aria-hidden="true" id="iconSidenav"></i>
            <a class="navbar-brand m-0" href="#" target="_blank">
                <i class="fas fa-university brand-logo" alt="main_logo"></i>
                <span class="ms-1 font-weight-bold text-white">SGRL</span>
            </a>
        </div>
        <hr class="horizontal light mt-0 mb-2">
        <perfect-scrollbar :options=ps_options class="collapse navbar-collapse  w-auto  max-height-vh-100"
            id="sidenav-collapse-main">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <nuxt-link to="/sistema" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-tachometer-alt opacity-10 fs-20"></i>
                        </div>
                        <span class="nav-link-text ms-1 fs-20">Area De Trabajo</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/reservacion" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-building"></i>
                        </div>
                        <span class="nav-link-text ms-1 fs-20">Reservacion</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/responsable-reservaciones" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-building"></i>
                        </div>
                        <span class="nav-link-text ms-1 fs-20">Reservacion</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/local" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-building"></i>
                        </div>
                        <span class="nav-link-text ms-1 fs-20">Locales</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/solicitantelocales" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-building"></i>
                        </div>
                        <span class="nav-link-text ms-1 fs-20">Locales</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/responsablelocales" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-city"></i>
                        </div>
                        <span class="nav-link-text ms-1 fs-20">Mis Locales</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/area" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-city"></i>
                        </div>
                        <span class="nav-link-text ms-1 fs-20">Areas</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/aseguramiento" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-box-archive"></i>

                        </div>
                        <span class="nav-link-text ms-1 fs-20">Aseguramientos</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/medio" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-screwdriver-wrench"></i>

                        </div>
                        <span class="nav-link-text ms-1 fs-20">Medio</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/actividad" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-list-check"></i>

                        </div>
                        <span class="nav-link-text ms-1 fs-20">Actividades</span>
                    </nuxt-link>
                </li>
                <li v-if="isAdmin" class="nav-item">
                    <nuxt-link to="/sistema/tipoactividad" class="nav-link text-white">
                        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                            <i class="fa fa-chart-line"></i>

                        </div>
                        <span class="nav-link-text ms-1 fs-20">Tipos De Actividades</span>
                    </nuxt-link>
                </li>
            </ul>
        </perfect-scrollbar>
    </aside>
</template>

<style>
.navbar-vertical.navbar-expand-xs .navbar-collapse {
    height: calc(100vh - 160px) !important;
}

.navbar-vertical .navbar-nav>.nav-item .nav-link.nuxt-link-exact-active.nuxt-link-active {
    font-weight: 400;
    color: #fff;
    border-right-width: 0;
    border-bottom-width: 0;
    background-color: rgba(199, 199, 199, 0.2);
    background-image: linear-gradient(195deg, #49a3f1 0%, #1A73E8 100%);
    ;
}

.navbar-vertical .navbar-nav>.nav-item .nav-link.nuxt-link-active>.nav-link.nuxt-link-exact-active.nuxt-link-active {
    font-weight: 400;
    color: #fff;
    border-right-width: 0;
    border-bottom-width: 0;
    background-color: rgba(199, 199, 199, 0.2);
}

.brand-logo {
    color: white;
    font-size: 1.5rem;
    margin-right: 5px;
}
</style>

<script>

import { PerfectScrollbar } from 'vue2-perfect-scrollbar'
import DropDownItemMenu from './NavBarVertical/DropDownItemMenu.vue'
import DropDownMenu from './NavBarVertical/DropDownMenu.vue'
export default {
    name: 'Sidebar',
    components: { PerfectScrollbar, DropDownItemMenu, DropDownMenu },

    data() {
        return {
            ps_options: {
                wheelSpeed: 0.3
            },
            active: false,


            drpoDownLocales: [
                //    {
                //        label: 'Locales',
                //        link:'/sistema/local',
                //        icon:'fa-list-check',
                //       active:false,
                //    },
                //     {
                //         label: 'Mis Locales',
                //         link:'/sistema/local',
                //         icon:'fa-list-check',
                //         active:false,
                //     },
                //     {
                //         label: 'Tipo de Medios',
                //         link:'/sistema/tipomedio',
                //         icon:'fa-chart-line',
                //         active:false,
                //     }
            ]

        }
    },
    methods: {
        toggleSidenav: () => {
            const iconSidenav = document.getElementById('iconSidenav');
            const sidenav = document.getElementById('sidenav-main');
            let body = document.getElementsByTagName('body')[0];
            let className = 'g-sidenav-pinned';
            if (body.classList.contains(className)) {
                body.classList.remove(className);
                setTimeout(function () {
                    sidenav.classList.remove('bg-white');
                }, 100);
                sidenav.classList.remove('bg-transparent');

            } else {
                body.classList.add(className);
                sidenav.classList.add('bg-white');
                sidenav.classList.remove('bg-transparent');
                iconSidenav.classList.remove('d-none');
            }
        }
    },
    computed: {
        isAdmin() {
            if (this.$auth.loggedIn) {
                if (this.$auth.user.is_superuser) {
                    return true;
                }
            }
            return false;
        },
        isResponsable() {
            if (this.$auth.loggedIn) {
                if (this.$auth.user.rol === "Responsable") {
                    return true;
                }
            }
            return false;
        }
    }
}
</script>
