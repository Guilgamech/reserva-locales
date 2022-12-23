<template>
    <div :class="{ 'show': show }" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class="vertical-center">
            <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
                <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                            <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Nuevo Medio para un Local
                            </h4>
                        </div>
                    </div>
                    <div class="card-body">
                        <h6 class="mb-2 text-center">
                            Complete los siguientes Campos
                        </h6>
                        <form ref="create_mediolocal" role="form" class="text-start" @submit.prevent="submit">
                            <div class="row">
                                <div class="col-12">
                                    <fieldset class="mt-2 custom">
                                        <legend>
                                            <div class="row">
                                                <div class="col-6">
                                                    Local
                                                </div>
                                            </div>
                                        </legend>
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="form-control">
                                                    <v-select v-model="mediolocal.local" @input="solved('local')"
                                                        :class="{ 'hgl': local_hlg }" class="style-chooser"
                                                        placeholder="Seleccionar" label="nombre" :options="local" />
                                                    <div v-if="err_local.length > 0" class="error">{{ err_local }}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </fieldset>
                                </div>
                                <div class="col-12">
                                    <fieldset class="mt-2 custom">
                                        <legend>
                                            <div class="row">
                                                <div class="col-6">
                                                    Medios
                                                </div>
                                            </div>
                                        </legend>
                                        <div class="row">
                                            <div class="col-12">
                                                <div class="form-control">
                                                    <v-select v-model="mediolocal.medio" @input="solved('medio')"
                                                        :class="{ 'hgl': medio_hlg }" class="style-chooser"
                                                        placeholder="Seleccionar" label="nombre" :options="medio" />
                                                    <div v-if="err_medio.length > 0" class="error">{{ err_medio }}</div>
                                                </div>
                                            </div>
                                        </div>
                                    </fieldset>
                                </div>
                                <div class="col-12 mt-2">
                                    <number-inputoutline @error-solved="solved('cantidad')" :error="err_cantidad"
                                        label="Cantidad" type="text" v-model="mediolocal.cantidad" />
                                        
                                </div>
                            </div>
                            <div class="text-center mt-3">
                                <div class="row">
                                    <div class="col-6">
                                        <button type="button" @click="ocultar()"
                                            class="btn bg-gradient-dark w-100 my-4 mb-2">Cancelar</button>
                                    </div>
                                    <div class="col-6">
                                        <button type="submit"
                                            class="btn bg-gradient-info w-100 my-4 mb-2">Guardar</button>
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
    components: { Textareaoutline, Inputoutline, },
    name: 'MedioLocalCreate',

    props: {
        show: {
            type: Boolean,
            required: true,
        }
    },
    computed: {
        medio_detail_id() {
            if (this.mediolocal.medio === null) {
                return '';
            }
            return '' + this.mediolocal.medio.id;
        },
        medio_hlg() {
            if (this.$store.state.mediolocal.error.medio.length > 0) {
                return true;
            }
            else if (this.mediolocal.medio === null) {
                return false;
            }
            else {
                return true;
            }
        },
        local_detail_id() {
            if (this.mediolocal.local === null) {
                return '';
            }
            return '' + this.mediolocal.local.id;
        },
        local_hlg() {
            if (this.$store.state.mediolocal.error.local.length > 0) {
                return true;
            }
            else if (this.mediolocal.local === null) {
                return false;
            }
            else {
                return true;
            }
        },
        creando_mediolocal() {
            return this.$store.state.mediolocal.creando
        },
        creado_mediolocal() {
            return this.$store.state.mediolocal.creado
        },
        err_cantidad() {
            if (this.$store.state.mediolocal.error.cantidad.length == 0) {
                return '';
            }
            return this.$store.state.mediolocal.error.cantidad.join(", ");
        },
        err_medio() {
            if (this.$store.state.mediolocal.error.medio.length == 0) {
                return '';
            }
            return this.$store.state.mediolocal.error.medio.join(", ");
        },
        err_local() {
            if (this.$store.state.mediolocal.error.local.length == 0) {
                return '';
            }
            return this.$store.state.mediolocal.error.local.join(", ");
        },
        err_non_field_errors() {
            if (this.$store.state.mediolocal.error.non_field_errors.length == 0) {
                return '';
            }
            return this.$store.state.mediolocal.error.non_field_errors.join(", ");
        },
        error() {
            if (
                this.err_cantidad.length > 0
                || this.err_medio.length > 0
                || this.err_local.length > 0
                || this.err_non_field_errors.length > 0
            ) {
                return true;
            }
            return false;
        },
        medio() {
            return this.$store.state.medio.listado;
        },
        local() {
            return this.$store.state.localresponsable.listado;
        },
    },
    watch: {
        show(newValue) {
            if (newValue) {
                this.$store.dispatch('mediolocal/unset_error');
                this.$store.dispatch('medio/listado');
                this.$store.dispatch('localresponsable/listado');
            }
        },
        creando_mediolocal(newValue) {
            if (!newValue) {
                if (this.creado_mediolocal) {
                    swal({
                        title: "Correcto !!",
                        text: "Creado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$store.dispatch('localresponsable/listado');
                        this.$emit('creado');
                        this.mediolocal = {
                            cantidad: NaN,
                            local: null,
                            medio: null
                        };
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
        }
    },
    methods: {
        ocultar() {
            this.$store.dispatch('mediolocal/unset_error');
            this.$emit('ocultar')
            this.mediolocal = {
                cantidad: NaN,
                local: null,
                medio: null
            };
        },
        submit() {
            var vobj = {};
            var has_somting_wrong = false;
            for (const property in this.mediolocal) {
                if (property == "local" || property == "medio") {
                    if (this.mediolocal[property] === null) {
                        has_somting_wrong = true;
                        this.$store.dispatch('mediolocal/newError', { "local": ["Seleccione un Local"] });
                        this.$store.dispatch('mediolocal/newError', { "medio": ["Seleccione un Medio"] });

                    }
                    else {
                        vobj[property] = this.mediolocal[property]['id'];
                    }
                }
                else {
                    vobj[property] = this.mediolocal[property]
                }
            }
            if (!has_somting_wrong)
                this.$store.dispatch('mediolocal/save', vobj);
            else {
                swal({
                    title: "ERROR !!",
                    text: "Revise los campos con error",
                    icon: "error",
                    button: "Continuar",
                })
                var has_somting_wrong = false;
            }
        },
        solved(property) {
            this.$store.dispatch('mediolocal/solved', property);
        },
    },
    data() {
        return {
            mediolocal: {
                cantidad: NaN,
                local: null,
                medio: null
            },
            modal_tac: false,
            modal_tad: false
        }
    },
}
</script>