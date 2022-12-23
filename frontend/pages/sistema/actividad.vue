<template>
    <div class="card my-4 mt-5">
        <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
            <div class="bg-gradient-dark shadow-dark border-radius-lg pt-4 pb-3 row">
                <div class="col-6 d-flex align-items-center">
                    <h6 class="text-white text-capitalize ps-3">Actividades del Sistema</h6>
                </div>
                <div class="col-6 text-end">
                    <a role="button" @click="modal_agregar=true" class="btn bg-gradient-success mb-0 cursor-pointer"><i
                        class="fa-solid fa-plus me-2"></i>Agregar</a>
                </div>
            </div>
        </div>
        <div class="card-body px-0 pb-2">
            <h6 v-if="listado.length == 0" class="text-center">No hay Actividad en el sistema</h6>
            <perfect-scrollbar v-else class="table-responsive p-0">
                <table class="table align-items-center mb-0">
                    <thead>
                    <tr>
                        <th class="text-secondary font-weight-bolder opacity-8 ps-4">Nombre</th>
                        <th class="text-secondary font-weight-bolder opacity-8 ps-2">Motivo</th>
                        <th class="text-secondary font-weight-bolder opacity-8 ps-2">Tipo de Actividad</th>
                        <th class="text-end text-secondary font-weight-bolder opacity-8">Acciones</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(item, index) in listado" v-bind:key="index">
                        <td>
                            <h6 class="mb-0 text-sm ps-3">{{ item.nombre }}</h6>
                        </td>
                        <td>
                            <h6 class="mb-0 text-sm">{{ item.motivo }}</h6>
                        </td>
                        <td>
                            <h6 class="mb-0 text-sm text-capitalize">{{ item.tipo_actividad.nombre }}</h6>
                        </td>
                        <td class="text-end pe-4">
                            <div class="d-flex justify-content-end">
                                <button v-tooltip="'Editar actividad'" type="button" @click="showModalDetail(item.id)"
                                        class="md-button md-edit md-just-icon">
                                    <div class="md-ripple">
                                        <div class="md-button-content">
                                            <i class="fa-solid fa-wand-magic-sparkles"></i>
                                        </div>
                                    </div>
                                </button>
                                <button v-tooltip="'Eliminar actividad'" type="button"
                                        @click="actividad_delete(item.id)"
                                        class="md-button md-danger ms-2 md-just-icon">
                                    <div class="md-ripple">
                                        <div class="md-button-content">
                                            <i class="fas fa-trash-alt"></i>
                                        </div>
                                    </div>
                                </button>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </perfect-scrollbar>
        </div>
        <ActividadCreate :show="modal_agregar" @creado="modal_agregar=false" @ocultar="modal_agregar=false"/>
        <ActividadEdit :objId="detail_id" :show="modal_detail" @editado="modal_detail = false"
                       @ocultar="modal_detail=false"/>

    </div>


</template>

<script>
import ActividadCreate from '../../components/Actividad/ActividadCreate.vue'
import ActividadEdit from '../../components/Actividad/ActividadEdit.vue'

import {PerfectScrollbar} from 'vue2-perfect-scrollbar'

export default {
    components: {PerfectScrollbar, ActividadCreate, ActividadEdit},
    name: 'Actividad',
    middleware: ['login'],
    mounted() {
        this.$store.dispatch('actividad/listado');
        this.modal_agregar = false;
        this.modal_detail = false;
        this.detail_id = '';
    },
    computed: {
        listado() {
            return this.$store.state.actividad.listado
        },
        deleting() {
            return this.$store.state.actividad.deleting
        },
        deleted() {
            return this.$store.state.actividad.deleted
        },
    },
    watch: {
        deleting(newValue) {
            if (!newValue) {
                if (this.deleted) {
                    this.$store.dispatch('actividad/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Eliminado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    })
                } else {
                    swal({
                        title: "ERROR !!",
                        text: "Revise su Conexión con la API",
                        icon: "error",
                        button: "Continuar",
                    })
                }
            }
        }
    },
    data() {
        return {
            modal_agregar: false,
            modal_detail: false,
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
        actividad_delete(id) {
            swal({
                title: "Estas seguro de Eliminar",
                text: "Una vez eliminado no hay vuelta atrás",
                icon: "warning",
                buttons: ["Cancelar", "Sí, Eliminar"],
                dangerMode: true
            }).then((willDelete) => {
                if (willDelete) {
                    this.$store.dispatch('actividad/delete', id);
                } else {
                    swal("Se ha cancelado la Acción de Eliminar")
                }
            });
        }
    },
}
</script>
