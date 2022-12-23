<template>
    <div class="card">
        <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
            <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Nueva Reservación</h4>
            </div>
        </div>
        <div class="card-body">
            <h6 class="mb-2 text-center">
                Complete los siguientes Campos
            </h6>
            <form ref="create_reservacion" role="form" class="text-start">
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
                                        <v-select 
                                        v-model="reservacion.local" 
                                        @input="solved('local')"
                                        :class="{ 'hgl': local_hlg }" 
                                        class="style-chooser"
                                        placeholder="Seleccionar" 
                                        label="nombre" 
                                        :options="local" />
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
                                        Actividad
                                    </div>
                                    <div class="col-6">
                                        <div class="d-flex justify-content-end">
                                            <button v-tooltip="'Crear Tipo de Obra'" type="button"
                                                @click="modal_actc = true" class="md-button md-create md-just-icon">
                                                <div class="md-ripple">
                                                    <div class="md-button-content">
                                                        <i class="fa fa-plus"></i>
                                                    </div>
                                                </div>
                                            </button>
                                            <button v-if="!(reservacion.actividad === null)"
                                                v-tooltip="'Editar Tipo de Obra'" type="button"
                                                @click="modal_actd = true" class="ms-2 md-button md-edit md-just-icon">
                                                <div class="md-ripple">
                                                    <div class="md-button-content">
                                                        <i class="fa-solid fa-wand-magic-sparkles"></i>
                                                    </div>
                                                </div>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </legend>
                            <div class="row">
                                <div class="col-12">
                                    <div class="form-control">
                                        <v-select v-model="reservacion.actividad" @input="solved('actividad')"
                                            :class="{ 'hgl': actividad_hlg }" class="style-chooser"
                                            placeholder="Seleccionar" label="nombre" :options="actividad" />
                                        <div v-if="err_actividad.length > 0" class="error">{{ err_actividad }}</div>
                                    </div>
                                </div>
                            </div>
                        </fieldset>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <inputoutline @error-solved="solved('cantidad_participantes')"
                                :error="err_cantidad_participantes" label="Cantidad de Participantes" type="number"
                                v-model="reservacion.cantidad_participantes" />
                        </div>
                        <div class="col-12">
                            <inputoutline @error-solved="solved('fecha_inico')" :error="err_fecha_inico"
                                label="Fecha de Inicio De La Reservacion" type="text"
                                v-model="reservacion.fecha_inico" />
                        </div>
                        <div class="col-12">
                            <inputoutline @error-solved="solved('fecha_fin')" :error="err_fecha_fin"
                                label="Fecha de Fin De La Reservacion" type="text" v-model="reservacion.fecha_fin" />
                        </div>
                    </div>
                </div>
                <div class="text-center mt-3">
                    <div class="row">
                        <div class="col-12">
                            <button type="submit" class="btn bg-gradient-info w-100 my-4 mb-2">Guardar</button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
        <ActividadCreate :show="modal_actc" @creado="actc_creado" @ocultar="modal_actc = false" />
        <ActividadEdit :objId="actividad_detail_id" :show="modal_actd" @editado="actd_editado"
            @eliminado="actd_eliminado" @ocultar="modal_actd = false" />
    </div>
</template>


<script>

import Inputoutline from '../Inputoutline.vue';
import ActividadCreate from '../Actividad/ActividadCreate.vue';
import ActividadEdit from '../Actividad/ActividadEdit.vue';
export default {
    components: { Inputoutline, ActividadCreate, ActividadEdit },
    name: 'ReservacionForm',


    computed: {
        actividad_detail_id(){
            if(this.reservacion.actividad === null){
                return '';
            }
            return ''+this.reservacion.actividad.id;
        },
        actividad_hlg(){
            if(this.$store.state.reservacion.error.actividad.length > 0){
                return true;
            }
            else if(this.reservacion.actividad === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        local_detail_id(){
            if(this.reservacion.local === null){
                return '';
            }
            return ''+this.reservacion.local.id;
        },
        local_hlg(){
            if(this.$store.state.reservacion.error.local.length > 0){
                return true;
            }
            else if(this.reservacion.local === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        creando_reservacion() {
            return this.$store.state.reservacion.creando
        },
        creado_reservacion() {
            return this.$store.state.reservacion.creado
        },
        err_estado() {
            if (this.$store.state.reservacion.error.estado.length == 0) {
                return '';
            }
            return this.$store.state.reservacion.error.estado.join(", ");
        },
        err_cantidad_participantes() {
            if (this.$store.state.reservacion.error.cantidad_participantes.length == 0) {
                return '';
            }
            return this.$store.state.reservacion.error.cantidad_participantes.join(", ");
        },
        err_fecha_fin() {
            if (this.$store.state.reservacion.error.fecha_fin.length == 0) {
                return '';
            }
            return this.$store.state.reservacion.error.fecha_fin.join(", ");
        },
        err_fecha_inico() {
            if (this.$store.state.reservacion.error.fecha_inico.length == 0) {
                return '';
            }
            return this.$store.state.reservacion.error.fecha_inico.join(", ");
        },
        err_actividad(){
            if(this.$store.state.reservacion.error.actividad.length == 0){
                return '';
            }
            return this.$store.state.reservacion.error.actividad.join(", ");
        },
        err_local(){
            if(this.$store.state.reservacion.error.local.length == 0){
                return '';
            }
            return this.$store.state.reservacion.error.local.join(", ");
        },
        err_solicitante() {
            if (this.$store.state.reservacion.error.solicitante.length == 0) {
                return '';
            }
            return this.$store.state.reservacion.error.solicitante.join(", ");
        },

        error() {
            if (this.err_estado.length > 0
                || this.err_cantidad_participantes.length > 0
                || this.err_fecha_fin.length > 0
                || this.err_fecha_inico.length > 0
                || this.err_actividad.length > 0
                || this.err_local.length > 0
                || this.err_solicitante.length > 0
            ) {
                return true;
            }
            return false;
        },
        actividad() {
            return this.$store.state.actividad.listado;
        },
        local() {
            return this.$store.state.local.listado;
        }
    },
    watch: {
        show(newValue) {
            if (newValue) {
                this.$store.dispatch('reservacion/unset_error');
            }
        },
        creando_reservacion(newValue) {
            if (!newValue) {
                if (this.creado_reservacion) {
                    this.$store.dispatch('reservacion/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Creado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$emit('creando');
                        this.reservacion = {
                            estado: '',
                            cantidad_participantes: '',
                            fecha_fin: '',
                            fecha_inico: '',
                            actividad: null,
                            local: null,
                            solicitante: null,
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
            this.$store.dispatch('reservacion/unset_error');
            this.$emit('ocultar')
            this.reservacion = {
                estado: '',
                cantidad_participantes: '',
                fecha_fin: '',
                fecha_inico: '',
                actividad: null,
                local: null,
                solicitante: null,
            };
        },
        submit() {
            var vobj = {};
            var has_somting_wrong = false;
            for (const property in this.reservacion) {
                if (property == "actividad" || property == "local") {
                    if (this.reservacion[property] === null) {
                        has_somting_wrong = true;
                        this.$store.dispatch('reservacion/newError', { "actividad": ["Seleccione una Actividad"] });
                        this.$store.dispatch('reservacion/newError', { "local": ["Seleccione un Local"] });

                    }
                    else {
                        vobj[property] = this.reservacion[property]['id'];
                    }
                }
                else {
                    vobj[property] = this.reservacion[property]
                }
            }
            if (!has_somting_wrong)
                this.$store.dispatch('reservacion/save', vobj);
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
            this.$store.dispatch('reservacion/solved', property);
        },
        actc_creado() {
            this.modal_actc = false;
            this.reservacion.actividad = (this.actividad.filter((item) => {
                return item.id == this.$store.state.actividad.creado_id;
            }))[0];
        },
        actd_editado() {
            this.modal_actd = false;
            this.reservacion.actividad = (this.actividad.filter((item) => {
                return item.id == this.$store.state.actividad.editado_id;
            }))[0];
        },
        actd_eliminado() {
            this.modal_actd = false;
            this.reservacion.actividad = null;
        },
    },
    data() {
        return {
            reservacion: {
                estado: '',
                cantidad_participantes: '',
                fecha_fin: '',
                fecha_inico: '',
                actividad: null,
                local: null,
                solicitante: null,
            },
            modal_actc: false,
            modal_actd: false
        }
    },
    mounted() {
        this.reservacion.solicitante = this.$auth.user.id
        this.$store.dispatch('actividad/listado');
        this.$store.dispatch('local/listado');
    },
}
</script>