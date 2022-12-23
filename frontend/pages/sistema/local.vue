<template>
    <div v-if="this.$store.state.autorizado" class="card my-4 mt-5">
        <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
            <div class="bg-gradient-dark shadow-dark border-radius-lg pt-4 pb-3 row">
                <div class="col-6 d-flex align-items-center">
                    <h6 class="text-white text-capitalize ps-3">Locales del Sistema</h6>
                </div>
                <div class="col-6 text-end">
                    <a role="button" @click="modal_agregar = true" class="btn bg-gradient-success mb-0 cursor-pointer"><i
                            class="fa-solid fa-plus me-2"></i>Agregar</a>
                </div>
            </div>
        </div>
        <div class="card-body px-0 pb-2">
            <h6 v-if="listado.length == 0" class="text-center">No hay Local en el sistema</h6>
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

                                <div class="d-flex justify-content-end">
                                    <button v-tooltip="'Detalles Local'" type="button" @click="showModalDetail(item.id)"
                                        class="md-button md-secondary md-just-icon">
                                        <div class="md-ripple">
                                            <div class="md-button-content">
                                                <i class="fa fa-file-invoice text-dark"></i>
                                            </div>
                                        </div>
                                    </button>
                                    <button v-if="isAdmin" v-tooltip="'Editar Local'" type="button" @click="showModalEdit(item.id)"
                                        class="md-button md-edit md-just-icon">
                                        <div class="md-ripple">
                                            <div class="md-button-content">
                                                <i class="fa-solid fa-wand-magic-sparkles"></i>
                                            </div>
                                        </div>
                                    </button>
                                    <button v-if="isAdmin" v-tooltip="'Eliminar Local'" type="button" @click="local_delete(item.id)"
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
        <LocalCreate :show="modal_agregar" @creado="modal_agregar = false" @ocultar="modal_agregar = false" />
        <LocalDetails :objId="detail_id" :show="modal_detail"  @ocultar="modal_detail=false" />
        <LocalEdit :objId="detail_id" :show="modal_edit" @editado="modal_edit = false" @ocultar="modal_edit=false" />

    </div>


</template>
    
<script>
import LocalCreate from '../../components/Local/LocalCreate.vue'
import LocalEdit from '../../components/Local/LocalEdit.vue';
import LocalDetails from '../../components/Local/LocalDetails.vue';

import { PerfectScrollbar } from 'vue2-perfect-scrollbar'

export default {
    components: { PerfectScrollbar, LocalCreate, LocalEdit, LocalDetails},
    name: 'Local',
    middleware: ['admin'],
    mounted() {
        this.modal_agregar = false,
        this.modal_detail = false,
        this.modal_edit = false,
        this.detail_id = '';
        this.$store.dispatch('local/listado');
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
        },
        listado() {
            return this.$store.state.local.listado
        },
        deleting() {
            return this.$store.state.local.deleting
        },
        deleted() {
            return this.$store.state.local.deleted
        },
    },
    watch: {
        deleting(newValue) {
            if (!newValue) {
                if (this.deleted) {
                    this.$store.dispatch('local/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Eliminado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    })
                }
                else {
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
        local_delete(id) {
            swal({
                title: "Estas seguro de Eliminar",
                text: "Una vez eliminado no hay vuelta atrás",
                icon: "warning",
                buttons: ["Cancelar", "Sí, Eliminar"],
                dangerMode: true
            }).then((willDelete) => {
                if (willDelete) {
                    this.$store.dispatch('local/delete', id);
                } else {
                    swal("Se ha cancelado la Acción de Eliminar")
                }
            });
        }
    },
}
</script>