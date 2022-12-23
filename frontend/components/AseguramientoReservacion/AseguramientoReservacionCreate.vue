<template>
    <div :class="{ 'show': show }" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class="vertical-center">
            <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
                <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                            <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Nuevo aseguramiento para un
                                reservacion
                            </h4>
                        </div>
                    </div>
                    <div class="card-body">
                        <h6 class="mb-2 text-center">
                            Complete los siguientes Campos
                        </h6>
                        <form ref="create_aseguramientoreservacion" role="form" class="text-start"
                              @submit.prevent="submit">
                            <div class="row">
                                <div class="col-12">
                                    <fieldset class="mt-2 custom">
                                        <legend>
                                            <div class="row">
                                                <div class="col-6">
                                                    aseguramiento
                                                </div>
                                            </div>
                                        </legend>
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="form-control">
                                                    <v-select v-model="aseguramientoreservacion.aseguramiento"
                                                              @input="solved('aseguramiento')"
                                                              :class="{ 'hgl': aseguramiento_hlg }"
                                                              class="style-chooser"
                                                              placeholder="Seleccionar" label="nombre"
                                                              :options="aseguramiento"/>
                                                    <div v-if="err_aseguramiento.length > 0" class="error">{{
                                                            err_aseguramiento
                                                        }}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </fieldset>
                                </div>
                                <div class="col-12 mt-2">
                                    <number-inputoutline @error-solved="solved('cantidad')" :error="err_cantidad"
                                                         label="Cantidad" type="text"
                                                         v-model="aseguramientoreservacion.cantidad"/>

                                </div>
                            </div>
                            <div class="text-center mt-3">
                                <div class="row">
                                    <div class="col-6">
                                        <button type="button" @click="ocultar()"
                                                class="btn bg-gradient-dark w-100 my-4 mb-2">Cancelar
                                        </button>
                                    </div>
                                    <div class="col-6">
                                        <button type="submit"
                                                class="btn bg-gradient-info w-100 my-4 mb-2">Guardar
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import Inputoutline from '../Inputoutline.vue';
import Textareaoutline from '../Textareaoutline.vue';

export default {
    components: {Textareaoutline, Inputoutline,},
    name: 'AseguramientoReservacionCreate',
    props: {
        show: {
            type: Boolean,
            required: true,
        }
    },
    computed: {
        aseguramiento_detail_id() {
            if (this.aseguramientoreservacion.aseguramiento === null) {
                return '';
            }
            return '' + this.aseguramientoreservacion.aseguramiento.id;
        },
        aseguramiento_hlg() {
            if (this.$store.state.aseguramientoreservacion.error.aseguramiento.length > 0) {
                return true;
            }
            return this.aseguramientoreservacion.aseguramiento !== null;
        },
        item() {
            const itemValue = this.$store.state.reservacion.item;
            if (itemValue?.id) {
                return itemValue;
            }
            return null;
        },
        reservacionActividad() {
            return this.item ? this.item.actividad.nombre : ''
        },
        reservacion_hlg() {
            if (this.$store.state.aseguramientoreservacion.error.reservacion.length > 0) {
                return true;
            } else return this.aseguramientoreservacion.reservacion !== null;
        },
        creando_aseguramientoreservacion() {
            return this.$store.state.aseguramientoreservacion.creando
        },
        creado_aseguramientoreservacion() {
            return this.$store.state.aseguramientoreservacion.creado
        },
        err_cantidad() {
            if (this.$store.state.aseguramientoreservacion.error.cantidad.length === 0) {
                return '';
            }
            return this.$store.state.aseguramientoreservacion.error.cantidad.join(", ");
        },
        err_aseguramiento() {
            if (this.$store.state.aseguramientoreservacion.error.aseguramiento.length === 0) {
                return '';
            }
            return this.$store.state.aseguramientoreservacion.error.aseguramiento.join(", ");
        },
        err_reservacion() {
            if (this.$store.state.aseguramientoreservacion.error.reservacion.length === 0) {
                return '';
            }
            return this.$store.state.aseguramientoreservacion.error.reservacion.join(", ");
        },
        err_non_field_errors() {
            if (this.$store.state.aseguramientoreservacion.error.non_field_errors.length === 0) {
                return '';
            }
            return this.$store.state.aseguramientoreservacion.error.non_field_errors.join(", ");
        },
        error() {
            return this.err_cantidad.length > 0
                || this.err_aseguramiento.length > 0
                || this.err_reservacion.length > 0
                || this.err_non_field_errors.length > 0;

        },
        aseguramiento() {
            return this.$store.state.aseguramiento.listado;
        },
        reservacion() {
            return this.$store.state.reservacion.getItem;
        },
        loading() {
            return this.$store.state.reservacion.loadingNewAseguramiento;
        },
        aseguramientoAgregado() {
            return this.$store.state.reservacion.aseguramientoAgregado;
        }
    },
    watch: {
        show(newValue) {
            if (newValue) {
                this.$store.dispatch('aseguramientoreservacion/unset_error');

                this.$store.dispatch('aseguramiento/listado');

            }
        },
        creando_aseguramientoreservacion(newValue) {
            if (!newValue) {
                if (this.creado_aseguramientoreservacion) {
                    swal({
                        title: "Correcto !!",
                        text: "Creado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$emit('creado');
                        this.aseguramientoreservacion = {
                            cantidad: NaN,
                            reservacion: null,
                            aseguramiento: null
                        };
                    })
                } else {
                    if (this.error) {
                        swal({
                            title: "ERROR !!",
                            text: "Revise los campos con error",
                            icon: "error",
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
        loading(newValue) {
            if (!newValue && this.aseguramientoAgregado) {
                swal({
                    title: "Correcto !!",
                    text: "Creado Satisfactoriamente",
                    icon: "success",
                    button: "Continuar",
                }).then(() => {
                    this.$store.dispatch('reservacion/setAseguramientoAgregado', false)
                    this.$emit('creado');
                    this.aseguramientoreservacion = {
                        cantidad: NaN,
                        reservacion: null,
                        aseguramiento: null
                    };
                })
            }
            if (!newValue && !this.aseguramientoAgregado) {
                swal({
                    title: "ERROR !!",
                    text: "Revise los campos con error",
                    icon: "error",
                    button: "Continuar",
                })
            }
        }
    },
    methods: {
        ocultar() {
            this.$store.dispatch('aseguramientoreservacion/unset_error');
            this.$emit('ocultar')
            this.aseguramientoreservacion = {
                cantidad: NaN,
                reservacion: null,
                aseguramiento: null
            };
        },
        submit() {
            if (this.err_cantidad.length > 0 || this.err_aseguramiento.length > 0 || this.err_reservacion.length > 0 ||
                this.err_non_field_errors.length > 0) {
                swal({
                    title: "ERROR !!",
                    text: "Revise los campos con error",
                    icon: "error",
                    button: "Continuar",
                })
            } else {
                console.log({item: this.item, aseguramiento: this.aseguramientoreservacion.aseguramiento})
                this.$store.dispatch('reservacion/addAseguramiento', {
                    cantidad: this.aseguramientoreservacion.cantidad,
                    reservacion: this.item.id,
                    aseguramiento: this.aseguramientoreservacion.aseguramiento.id
                });
            }

        },
        solved(property) {
            this.$store.dispatch('aseguramientoreservacion/solved', property);
        },
    },
    data() {
        return {
            aseguramientoreservacion: {
                cantidad: NaN,
                aseguramiento: null
            },
        }
    },
}
</script>
