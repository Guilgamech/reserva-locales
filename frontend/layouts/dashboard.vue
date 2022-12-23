<template>
    <perfect-scrollbar v-if="this.$auth.loggedIn" id="data-app" ref="globalscroll" data-app :options=ps_options>
        <Sidebar/>
        <perfect-scrollbar ref="scroll" :options=ps_options
                           class="main-content position-relative vh-100 border-radius-lg">
            <!-- Navbar -->
            <Navbar/>
            <div class="container-fluid pt-4">
                <Nuxt/>
            </div>
        </perfect-scrollbar>
    </perfect-scrollbar>
</template>
<style>
@import 'vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css';
@import 'vue-select/dist/vue-select.css';

.tooltip {
    display: block !important;
    z-index: 10000;
}

.tooltip .tooltip-inner {
    background: rgb(29, 29, 29);
    color: white;
    border-radius: 16px;
    padding: 5px 10px 4px;
}

.tooltip .tooltip-arrow {
    width: 0;
    height: 0;
    border-style: solid;
    position: absolute;
    margin: 5px;
    border-color: rgb(29, 29, 29);
    z-index: 1;
}

.tooltip[x-placement^="top"] {
    margin-bottom: 5px;
}

.tooltip[x-placement^="top"] .tooltip-arrow {
    border-width: 5px 5px 0 5px;
    border-left-color: transparent !important;
    border-right-color: transparent !important;
    border-bottom-color: transparent !important;
    bottom: -5px;
    left: calc(50% - 5px);
    margin-top: 0;
    margin-bottom: 0;
}

.tooltip[x-placement^="bottom"] {
    margin-top: 5px;
}

.tooltip[x-placement^="bottom"] .tooltip-arrow {
    border-width: 0 5px 5px 5px;
    border-left-color: transparent !important;
    border-right-color: transparent !important;
    border-top-color: transparent !important;
    top: -5px;
    left: calc(50% - 5px);
    margin-top: 0;
    margin-bottom: 0;
}

.tooltip[x-placement^="right"] {
    margin-left: 5px;
}

.tooltip[x-placement^="right"] .tooltip-arrow {
    border-width: 5px 5px 5px 0;
    border-left-color: transparent !important;
    border-top-color: transparent !important;
    border-bottom-color: transparent !important;
    left: -5px;
    top: calc(50% - 5px);
    margin-left: 0;
    margin-right: 0;
}

.tooltip[x-placement^="left"] {
    margin-right: 5px;
}

.tooltip[x-placement^="left"] .tooltip-arrow {
    border-width: 5px 0 5px 5px;
    border-top-color: transparent !important;
    border-right-color: transparent !important;
    border-bottom-color: transparent !important;
    right: -5px;
    top: calc(50% - 5px);
    margin-left: 0;
    margin-right: 0;
}

.tooltip.popover .popover-inner {
    background: #f9f9f9;
    color: rgb(29, 29, 29);
    padding: 24px;
    border-radius: 5px;
    box-shadow: 0 5px 30px rgba(rgb(29, 29, 29), .1);
}

.tooltip.popover .popover-arrow {
    border-color: #f9f9f9;
}

.tooltip[aria-hidden='true'] {
    visibility: hidden;
    opacity: 0;
    transition: opacity .15s, visibility .15s;
}

.tooltip[aria-hidden='false'] {
    visibility: visible;
    opacity: 1;
    transition: opacity .15s;
}

.md-button.md-edit {
    background-color: rgb(61, 81, 148);
    color: #fff;
    -webkit-box-shadow: 0 2px 2px 0 rgb(85 172 238 / 14%), 0 3px 1px -2px rgb(85 172 238 / 20%), 0 1px 5px 0 rgb(85 172 238 / 12%);
    box-shadow: 0 2px 2px 0 rgb(85 172 238 / 14%), 0 3px 1px -2px rgb(85 172 238 / 20%), 0 1px 5px 0 rgb(85 172 238 / 12%);
}

.md-button.md-danger:hover {
    background-color: rgb(189, 82, 127);
    border-color: rgb(189, 82, 127);
    box-shadow: 0 14px 26px -12px rgba(189, 82, 166, 0.4), 0 4px 23px 0 rgba(189, 82, 189, 0.25), 0 8px 10px -5px rgba(189, 82, 189, 0.25);
}

.md-button.md-danger {
    background-color: rgb(148, 61, 73);
    color: #fff;
    -webkit-box-shadow: 0 2px 2px 0 rgb(85 172 238 / 14%), 0 3px 1px -2px rgb(85 172 238 / 20%), 0 1px 5px 0 rgb(85 172 238 / 12%);
    box-shadow: 0 2px 2px 0 rgb(85 172 238 / 14%), 0 3px 1px -2px rgb(85 172 238 / 20%), 0 1px 5px 0 rgb(85 172 238 / 12%);
}

.md-button.md-edit:hover {
    background-color: rgb(82, 107, 189);
    border-color: rgb(82, 107, 189);
    box-shadow: 0 14px 26px -12px rgb(82, 107, 189, 0.4), 0 4px 23px 0 rgba(82, 107, 189, 0.25), 0 8px 10px -5px rgba(82, 107, 189, 0.25);
}

.md-button.md-create {
    background-color: rgb(61, 148, 64);
    color: #fff;
    -webkit-box-shadow: 0 2px 2px 0 rgb(85 172 238 / 14%), 0 3px 1px -2px rgb(85 172 238 / 20%), 0 1px 5px 0 rgb(85 172 238 / 12%);
    box-shadow: 0 2px 2px 0 rgb(85 172 238 / 14%), 0 3px 1px -2px rgb(85 172 238 / 20%), 0 1px 5px 0 rgb(85 172 238 / 12%);
}

.md-button.md-create:hover {
    background-color: #4CAF50;
    border-color: #4CAF50;
    box-shadow: 0 14px 26px -12px rgba(76, 175, 80, 0.4), 0 4px 23px 0 rgba(76, 175, 80, 0.15), 0 8px 10px -5px rgba(76, 175, 80, 0.2);
}

.md-button {
    border: none;
    border-radius: 3px !important;
    position: relative;
    margin: 0.3125rem 1px;
    height: auto;
    line-height: 1.42857;
    font-size: 12px;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0;
    will-change: box-shadow, transform;
    -webkit-transition: background-color .2s cubic-bezier(.4, 0, .2, 1), -webkit-box-shadow .2s cubic-bezier(.4, 0, 1, 1);
    transition: background-color .2s cubic-bezier(.4, 0, .2, 1), -webkit-box-shadow .2s cubic-bezier(.4, 0, 1, 1);
    transition: box-shadow .2s cubic-bezier(.4, 0, 1, 1), background-color .2s cubic-bezier(.4, 0, .2, 1);
    transition: box-shadow .2s cubic-bezier(.4, 0, 1, 1), background-color .2s cubic-bezier(.4, 0, .2, 1), -webkit-box-shadow .2s cubic-bezier(.4, 0, 1, 1);
}

.md-button {
    min-width: 88px;
    height: 36px;
    margin: 6px 8px;
    -webkit-user-select: none;
    user-select: none;
    border-radius: 2px;
    font-size: 14px;
    font-weight: 500;
    text-transform: uppercase;
}

.md-button, .md-button-clean {
    margin: 0;
    padding: 0;
    display: inline-block;
    position: relative;
    overflow: hidden;
    outline: none;
    background: transparent;
    border: 0;
    border-radius: 0;
    transition: .4s cubic-bezier(.4, 0, .2, 1);
    font-family: inherit;
    line-height: normal;
    text-decoration: none;
    vertical-align: top;
    white-space: nowrap;
}

.md-button.md-fab, .md-button.md-just-icon {
    font-size: 16px;
    height: 30px;
    min-width: 30px;
    width: 30px;
    padding: 0;
    overflow: hidden;
    position: relative;
    line-height: 30px;
}

.md-button .md-ripple {
    padding: 0 8px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.md-ripple {
    width: 100%;
    height: 100%;
    position: relative;
    z-index: 5;
    overflow: visible;
}

.md-button .md-button-content {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
}

.md-button-content {
    position: relative;
    z-index: 2;
}

.md-button .md-button-content i {
    font-size: 16px !important;
}

.table-responsive.ps {
    max-height: 450px !important;
}

.example {
    overflow-y: hidden; /* Add the ability to scroll */
}

/* Hide scrollbar for Chrome, Safari and Opera */
.example::-webkit-scrollbar {
    display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.example {
    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
}

#data-app {
    height: 100vh !important;
}

.nav-link {
    cursor: pointer;
}

.fs-20 {
    font-size: 16px;

}

.fs-25 {
    font-size: 25px;
}

span.psr-2 {
    position: relative;
    top: -2px;
}

span.psr-3 {
    position: relative;
    top: -3px;
}

span.psr-4 {
    position: relative;
    top: -4px;
}

.btn-close.btn-icon-close {
    color: #494949;
    height: auto !important;
}

.btn-close.btn-icon-close:hover {
    color: #0b0b0b;
}

.btn-icon-close i {
    font-size: 25px !important;
    font-weight: 800 !important;
    transform: rotate(45deg) !important;
}

.modal.show {
    display: block !important;
}

.modal-overlay {
    background-color: rgb(0 0 0 / 40%);
}


.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.vertical-center {
    display: inline-block;
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
}

.outline-textarea {
    height: 114px;
    border: 2px solid #e8ebec;
    margin-top: 5px;
    padding: 5px 10px;
    margin-top: 10px;
}

.txtarea-container {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    width: 100%;
    transition: 0.2s ease;
}

.txtarea-control {
    display: block;
    width: 100%;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1.5rem;
    color: #495057;
    background-color: transparent;
    background-clip: padding-box;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border-radius: 0.375rem;
    transition: 0.2s ease;
}

.outline-textarea:focus {
    border: 2px solid #1A73E8 !important;
    outline: none !important;
}

.custom-select {
    box-sizing: border-box;
    -moz-appearance: none;
    -webkit-appearance: none;
    appearance: none;

    background-color: transparent;
    border: none;
    padding: 0;
    margin: 0;
    width: 100%;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1.3;
    cursor: default;
}

.custom-select::-ms-expand {
    display: none;
}

.custom-select {
    padding: 10px 12px;
    border: 2px solid #e8ebec;
    border-radius: 5px;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='292.4' height='292.4'%3E%3Cpath fill='%23333' d='M287 69.4a17.6 17.6 0 0 0-13-5.4H18.4c-5 0-9.3 1.8-12.9 5.4A17.6 17.6 0 0 0 0 82.2c0 5 1.8 9.3 5.4 12.9l128 127.9c3.6 3.6 7.8 5.4 12.8 5.4s9.2-1.8 12.8-5.4L287 95c3.5-3.5 5.4-7.8 5.4-12.8 0-5-1.9-9.2-5.5-12.8z'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 8px center;
    background-size: 9px;
    color: #7b809a;
}

.custom-select:hover {
    border-color: #1A73E8;
}

.custom-select:focus {
    border-color: #1A73E8;
    outline: none;
}

.custom-select.filled {
    border-color: #1A73E8 !important;
}

.custom-select:disabled,
.custom-select[aria-disabled="true"] {
    cursor: not-allowed;
    background-color: rgba(211, 211, 211, 0.75);
}

.custom-select:disabled:hover,
.custom-select[aria-disabled="true"]:hover {
    border-color: #999;
}

.vertical-center {
    display: inline-block;
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
}

.fade-enter-active, .fade-leave-active {
    transition: opacity .5s
}

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
{
    opacity: 0
}

fieldset.custom legend {
    font-size: 1rem;
}

.style-chooser .vs__search::placeholder,
.style-chooser .vs__dropdown-toggle,
.style-chooser .vs__dropdown-menu {


    color: #7b809a !important;

}

.style-chooser.hgl .vs__dropdown-toggle[aria-expanded="false"] {
    border: 2px solid #1A73E8 !important;
}

.style-chooser.hgl .vs__dropdown-toggle[aria-expanded="true"] {
    border-top: 2px solid #1A73E8 !important;
    border-left: 2px solid #1A73E8 !important;
    border-right: 2px solid #1A73E8 !important;
}

ul .vs__dropdown-option--highlight[aria-selected="true"] {
    background-color: #1A73E8 !important;
    color: white !important;
}

.style-chooser .vs__dropdown-toggle[aria-expanded="true"] {
    border-top: 2px solid #1A73E8 !important;
    border-left: 2px solid #1A73E8 !important;
    border-right: 2px solid #1A73E8 !important;
}

.style-chooser ul {
    border-bottom: 2px solid #1A73E8 !important;
    border-left: 2px solid #1A73E8 !important;
    border-right: 2px solid #1A73E8 !important;
}

.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
    fill: #7b809a !important;
}
</style>
<script>
import Vue from 'vue'
import {VTooltip, VPopover, VClosePopover} from 'v-tooltip'

Vue.directive('tooltip', VTooltip)
Vue.directive('close-popover', VClosePopover)
Vue.component('v-popover', VPopover)
import vSelect from 'vue-select'

Vue.component('v-select', vSelect)
import Sidebar from '../components/Sidebar.vue'
import {PerfectScrollbar} from 'vue2-perfect-scrollbar'
import Navbar from '../components/Navbar.vue'

export default {
    name: 'Dashboard',
    components: {Sidebar, PerfectScrollbar, Navbar},
    data() {
        return {
            ps_options: {
                wheelSpeed: 0.3,

            }
        }
    },
    watch: {
        $route() {
            this.$refs.scroll.update();
        }
    },
    head: {
        link: [
            {rel: 'apple-touch-icon', sizes: '76x76', href: '/assets/img/apple-icon.png'},
            {rel: 'icon', type: 'image/png', href: '/assets/img/favicon.png'},
            {
                rel: 'stylesheet',
                type: 'text/css',
                href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900|Roboto+Slab:400,700'
            },

            {rel: 'stylesheet', href: '/assets/css/nucleo-icons.css'},
            {rel: 'stylesheet', href: '/assets/css/nucleo-svg.css'},
            {rel: 'stylesheet', href: '/assets/fontawesome/css/all.css'},
            {rel: 'stylesheet', id: 'pagestyle', href: '/assets/css/material-dashboard.css?v=3.0.0'},
        ],
        script: [
            // { src: 'https://kit.fontawesome.com/42d5adcbca.js', crossorigin:'anonymous' },
            {src: '/assets/js/core/popper.min.js', body: true},
            {src: '/assets/js/core/bootstrap.min.js', body: true},
            //{ src: '/assets/js/plugins/perfect-scrollbar.min.js', body: true },
            //{ src: '/assets/js/plugins/smooth-scrollbar.min.js', body: true },
            {src: '/assets/js/material-dashboard.js', body: true},
            //{ src: '/assets/js/charts.js', body: true },
            //{ src: '/assets/js/custom.js', body: true },
        ],
        bodyAttrs: {
            class: 'g-sidenav-show  bg-gray-200 example'
        }
    }
}
</script>
