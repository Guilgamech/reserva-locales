<template>
    <div v-if="this.$store.state.autorizado" class="card my-4 mt-5">
        <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
            <div class="bg-gradient-dark shadow-dark border-radius-lg pt-4 pb-3 row">
                <div class="col-6 d-flex align-items-center">
                    <h6 class="text-white text-capitalize ps-3">Mis Locales del Sistema</h6>
                </div>
            </div>
        </div>
        <div class="card-body px-0 pb-2">
            <h6 v-if="listado.length == 0" class="text-center">No hay localresponsable en el sistema</h6>
            <perfect-scrollbar v-else class="table-responsive p-0">
                <table class="table align-items-center mb-0">
                    <thead>
                        <tr>
                            <th class="text-secondary font-weight-bolder opacity-8 ps-4">Nombre</th>
                            <th class="text-secondary font-weight-bolder opacity-8 ps-2">Capacidad</th>
                            <th class="text-secondary font-weight-bolder opacity-8 ps-2">Teléfono</th>
                            <th class="text-secondary font-weight-bolder opacity-8 ps-2">Correo del Responsable</th>
                            <th class="text-secondary font-weight-bolder opacity-8 ps-2">Area</th>
                            <th class="text-end text-secondary font-weight-bolder opacity-8">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(item, index) in listado" v-bind:key="index">
                            <td>
                                <h6 class="mb-0 text-sm ps-3">{{ item.nombre }}</h6>
                            </td>
                            <td>
                                <h6 class="mb-0 text-sm">{{ item.capacidad }}</h6>
                            </td>
                            <td>
                                <h6 class="mb-0 text-sm text-capitalize">{{ item.telefono }}</h6>
                            </td>
                            <td>
                                <h6 class="mb-0 text-sm ">{{ item.responsable_email }}</h6>
                            </td>
                            <td>
                                <h6 class="mb-0 text-sm text-capitalize">{{ item.area.nombre }}</h6>
                            </td>
                            <td class="text-end pe-4">

                                <a @click="showModalDetail(item.id)" class="text-secondary cursor-pointer text-sm"><i class="fa fa-file-invoice text-dark"></i> Detalles</a>

                            </td>
                            
                        </tr>
                    </tbody>
                </table>
            </perfect-scrollbar>
        </div>
        <MedioLocalesCreate :show="modal_agregar_medio" @creado="modal_agregar_medio = false" @ocultar="modal_agregar_medio = false" />
        <LocalResponsableDetails :objId="detail_id" :show="modal_detail"  @ocultar="modal_detail=false" />
    </div>


</template>
    
<script>
import MedioLocalesCreate from '../../components/MedioLocales/MedioLocalesCreate.vue';
import LocalResponsableDetails from '../../components/Local/LocalResponsableDetails.vue';

import { PerfectScrollbar } from 'vue2-perfect-scrollbar'

export default {
    components: { PerfectScrollbar, LocalResponsableDetails, MedioLocalesCreate},
    name: 'LocalResponsable',
    middleware: ['admin'],
    mounted() {
        this.modal_agregar = false,
        this.modal_agregar_medio = false,
        this.modal_detail = false,
        this.modal_edit = false,
        this.detail_id = '';
        this.$store.dispatch('localresponsable/listado');
        
    },
    computed: {
        listado() {
            return this.$store.state.localresponsable.listado
        },
    },
    data() {
        return {
            modal_agregar: false,
            modal_agregar_medio: false,
            modal_detail: false,
            modal_edit: false,
            detail_id: '',
        }
    },
    methods: {
        showModalDetail(id) {
            if (id > 0) {
                this.detail_id = '' + id
                this.modal_detail = true;
            }
        },
        showModalEdit(id) {
            if (id > 0) {
                this.detail_id = '' + id
                this.modal_edit = true;
            }
        },
    },
}
</script>