<template>
    <div :class="{ 'show': show }" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div v-if="objId !== ''" class=" vertical-center">
            <div class="col-lg-4 col-md-6 col-10 mx-auto" @click.stop>
                <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                            <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Detalles</h4>
                        </div>
                    </div>
                    <div v-if="!existe" class="card-body">
                        <h6 class="mb-2 text-center">
                            Revise la Conexión con la base de datos, o ha ingresado a una ruta inválida
                        </h6>
                        <div class="text-center mt-3">
                            <div class="row justify-content-center">
                                <div class="col-6">
                                    <button type="button" @click="ocultar()"
                                        class="btn bg-gradient-dark w-100 my-4 mb-2">Salir</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-else class="card-body">
                        <div v-if="!canedit" class="row">
                            <div class="col-5 justify-content-end">

                                <h6 class="mb-2 text-end">Nombre:</h6>
                                <h6 class="mb-2 text-end">Capacidad:</h6>
                                <h6 class="mb-2 text-end">Telefono:</h6>
                                <h6 class="mb-2 text-end">Responsable:</h6>
                                <h6 class="mb-2 text-end">Area:</h6>
                                <h6 class="mb-2 text-end">Medios:</h6>
                            </div>
                            <div class="col-7">
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{ edit.nombre }}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{ edit.capacidad }}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{ edit.telefono }}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{ edit.responsable_email
                                }}</span>
                                </h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{ edit.area.nombre }}</span></h6>
                                <div class="row">
                                    <div class="row col-12 mb-2" v-for=" (item, index) in edit.medios ">
                                        <h6 class="col-6"><span class="text-sm text-secondary">{{ item.medio.nombre
                                        }}</span>
                                        </h6>
                                        <h6 class="col-2"><span class="text-sm text-secondary">{{ item.cantidad
                                        }}</span>
                                        </h6>
                                        <button v-tooltip="'Editar medios de mi local'" type="button"
                                            @click="showModalEdit({ local_id: '' + edit.id, medio_id: '' + item.medio.id })"
                                            class="md-button md-edit md-just-icon col-2">
                                            <div class="md-ripple">
                                                <div class="md-button-content">
                                                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                                                </div>
                                            </div>
                                        </button>
                                        <button v-tooltip="'Eliminar Medio de mi Local'" type="button"
                                            @click="todelete({ local_id: '' + edit.id, medio_id: '' + item.medio.id })"
                                            class="md-button md-danger md-just-icon col-2 ms-2">
                                            <div class="md-ripple">
                                                <div class="md-button-content">
                                                    <i class="fas fa-trash-alt"></i>
                                                </div>
                                            </div>
                                        </button>
                                    </div>
                                </div>
                                <div class="col-2">
                                    <button
                                    @click="modal_agregar_medio = true"
                                    type="button" class="btn btn-success">
                                        <i class="fa fa-plus"></i>
                                    </button>
                                </div>
                            </div>
                            <div class="row justify-content-center text-center mt-3">
                                <div class="col-lg-4 cl-md-6 col-sm-6 col-12">
                                    <button type="button" @click="ocultar()"
                                        class="btn bg-gradient-dark w-100 ">Salir</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <MedioLocalesCreate :currentlocal="edit" :show="modal_agregar_medio" @creado="modal_agregar_medio = false" @ocultar="modal_agregar_medio = false" />

        <MedioLocalesEdit :data="data" :show="modal_edit" @editado="modal_edit = false" @ocultar="modal_edit = false" />
    </div>

</template>

<script>
import swal from 'sweetalert';
import Inputoutline from '../Inputoutline.vue'
import MedioLocalesEdit from '../../components/MedioLocales/MedioLocalesEdit.vue';
import MedioLocalesCreate from '../MedioLocales/MedioLocalesCreate';
export default {
    components: { Inputoutline, MedioLocalesEdit, MedioLocalesCreate },
    name: 'LocalResponsableDetails',
    props: {
        show: {
            type: Boolean,
            required: true
        },
        objId: {
            type: String,
            required: true
        }
    },
    mounted() {
        this.modal_agregar_medio = false,
        this.modal_edit = false,
            this.detail_id = '';


    },
    computed: {
        edit() {
            return this.$store.state.localresponsable.listado.filter(el => Number(el.id) === Number(this.objId))[0]
        },
        existe() {
            return this.$store.state.local.existe
        },
        editando() {
            return this.$store.state.local.editando
        },
        editado() {
            return this.$store.state.local.editado
        },
        err_nombre() {
            if (this.$store.state.local.error.nombre.length == 0) {
                return '';
            }
            return this.$store.state.local.error.nombre.join(", ");
        },
        err_capacidad() {
            if (this.$store.state.local.error.capacidad.length == 0) {
                return '';
            }
            return this.$store.state.local.error.capacidad.join(", ");
        },
        err_telefono() {
            if (this.$store.state.local.error.telefono.length == 0) {
                return '';
            }
            return this.$store.state.local.error.telefono.join(", ");
        },
        err_responsable_email() {
            if (this.$store.state.local.error.responsable_email.length == 0) {
                return '';
            }
            return this.$store.state.local.error.responsable_email.join(", ");
        },
        err_area() {
            if (this.$store.state.local.error.area.length == 0) {
                return '';
            }
            return this.$store.state.local.error.area.join(", ");
        },
        err_medios() {
            if (this.$store.state.local.error.medios.length == 0) {
                return '';
            }
            return this.$store.state.local.error.medios.join(", ");
        },
        error() {
            if (this.err_nombre.length > 0
                || this.err_capacidad.length > 0
                || this.err_telefono.length > 0
                || this.err_responsable_email.length > 0
                || this.err_area.length > 0
                || this.err_medios.length > 0
            ) {
                return true;
            }
            return false;
        },
        deleting() {
            return this.$store.state.mediolocal.deleting
        },
        deleted() {
            return this.$store.state.mediolocal.deleted
        }
    },
    watch: {
        edit(newValue) {
            for (const property in this.edit) {
                if (property !== "id") {
                    this.item[property] = this.edit[property];
                }
            }
        },
        show(newValue) {
            if (newValue) {
                this.$store.dispatch('local/unset_error');
            }
        },
        editando(newValue) {
            if (!newValue) {
                if (this.editado) {
                    this.$store.dispatch('localresponsable/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Editado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$emit('editado')
                        this.canedit = false;
                    })
                }
                else {
                    if (this.error) {
                        swal({
                            title: "ERROR !!",
                            text: "Revise los campos con error",
                            icon: "error",
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
        deleting(newValue) {
            if (!newValue) {
                if (this.deleted) {
                    this.$store.dispatch('localresponsable/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Eliminado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$emit('eliminado');
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
    methods: {
        ocultar() {
            this.$store.dispatch('local/unset_error');
            this.$emit('ocultar')
            this.canedit = false;
        },

        todelete(data) {

            swal({
                title: "Estas seguro de Eliminar",
                text: "Una vez eliminado no hay vuelta atrás",
                icon: "warning",
                buttons: ["Cancelar", "Sí, Eliminar"],
                dangerMode: true
            }).then((willDelete) => {
                if (willDelete) {
                    this.$store.dispatch('mediolocal/delete', data);
                } else {
                    swal("Se ha cancelado la Acción de Eliminar")
                }
            });

        },
        showModalEdit(data) {
            if (data.local_id !== '') {
                this.data = data
                this.modal_edit = true;
            }
        },
    },
    data() {
        return {
            modal_agregar_medio: false,
            canedit: false,
            modal_edit: false,
            data: { local_id: '', medio_id: '' },
            item: {
                nombre: '',
                capacidad: '',
                telefono: '',
                responsable_email: '',
                area: null,
                medios: null
            },
        }
    },


}
</script>
