<template>
    <div :class="{ 'show': show }" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div v-if="data.reservacion_id!==''" class="vertical-center">
            <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
                <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                            <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Editar aseguramientos de mi reservacion</h4>
                        </div>
                    </div>
                    <div class="card-body">
                        <h6 class="mb-2 text-center">
                            Complete los siguientes Campos
                        </h6>
                        <form ref="create_reservacion" role="form" class="text-start" @submit.prevent="submit">
                            <div class="row">
                                <div class="col-12">
                                    <fieldset class="mt-2 custom">
                                        <legend>
                                            <div class="row">
                                                <div class="col-6">
                                                    <h4>reservacion: {{editreservacion.nombre}}</h4>
                                                </div>
                                            </div>
                                        </legend>                                
                                    </fieldset>
                                </div>
                                <div class="col-12">
                                    <fieldset class="mt-2 custom">
                                        <legend>
                                            <div class="row">
                                                <div class="col-6">
                                                    <h4>
                                                        aseguramiento: {{aseguramientoreservacion.aseguramiento.nombre}}
                                                    </h4>
                                                </div>
                                            </div>
                                        </legend>
                                    </fieldset>
                                </div>
                                <div class="col-12">
                                    <number-inputoutline :set_value="'' + edit.cantidad" @error-solved="solved('cantidad')"
                                        :error="err_cantidad" label="cantidad" type="number" v-model="aseguramientoreservacion.cantidad" />
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
export default {
    components: { Inputoutline, },
    name: 'AseguramientoReservacionEdit',
    props: {
        show: {
            type: Boolean,
            required: true,
        },
        data: {
            type: Object,
            required: true
        }
    },
    computed: {
        aseguramiento_detail_id(){
            if(this.aseguramientoreservacion.aseguramiento === null){
                return '';
            }
            return ''+this.aseguramientoreservacion.aseguramiento.id;
        },
        aseguramiento_hlg(){
            if(this.$store.state.aseguramientoreservacion.error.aseguramiento.length > 0){
                return true;
            }
            else if(this.aseguramientoreservacion.aseguramiento === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        reservacion_detail_id(){
            if(this.aseguramientoreservacion.reservacion === null){
                return '';
            }
            return ''+this.aseguramientoreservacion.reservacion.id;
        },
        reservacion_hlg(){
            if(this.$store.state.aseguramientoreservacion.error.reservacion.length > 0){
                return true;
            }
            else if(this.aseguramientoreservacion.reservacion === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        editreservacion() {
            return this.$store.state.reservacionresponsable.listado.filter(el=> Number(el.id) === Number(this.data.reservacion_id))[0]
        },
        edit() {
            return this.$store.state.aseguramientoreservacion.edit;
        },
        existe() {
            return this.$store.state.aseguramientoreservacion.existe
        },
        editando() {
            return this.$store.state.aseguramientoreservacion.editando
        },
        editado() {
            return this.$store.state.aseguramientoreservacion.editado
        },
        err_cantidad() {
            if (this.$store.state.aseguramientoreservacion.error.cantidad.length == 0) {
                return '';
            }
            return this.$store.state.aseguramientoreservacion.error.cantidad.join(", ");
        },
        err_reservacion() {
            if (this.$store.state.aseguramientoreservacion.error.reservacion.length == 0) {
                return '';
            }
            return this.$store.state.aseguramientoreservacion.error.reservacion.join(", ");
        },
        err_aseguramiento(){
            if (this.$store.state.aseguramientoreservacion.error.aseguramiento.length == 0) {
                return '';
            }
            return this.$store.state.aseguramientoreservacion.error.aseguramiento.join(", ");
        },
        error() {
            if (this.err_cantidad.length > 0
                || this.err_aseguramiento.length > 0
                || this.err_reservacion.length > 0
            ) {
                return true;
            }
            return false;
        },
        reservacion() {
            return this.$store.state.reservacionresponsable.listado;
        },
        aseguramiento() {
            return this.$store.state.aseguramiento.listado;
        },
    },
    watch: {
        edit(newValue) {
            var obj = new Object();
            for (const property in this.edit) {
                var save = true;
                if (save) {
                    obj[property] = this.edit[property]
                }
            }
            this.reservacionresponsable = obj;
            this.aseguramiento = obj;
        },
        show(newValue) {
            if (newValue) {
                this.$store.dispatch('aseguramientoreservacion/unset_error');                
                const aseguramientoreservacionFromreservacion = this.editreservacion.aseguramientos.filter(el => el.aseguramiento.id === Number(this.data.aseguramiento_id))[0]
                this.aseguramientoreservacion.reservacion = this.data.reservacion_id
                this.aseguramientoreservacion.aseguramiento = aseguramientoreservacionFromreservacion.aseguramiento
                this.aseguramientoreservacion.cantidad = aseguramientoreservacionFromreservacion.cantidad
            }
        },
        editando(newValue) {
            if (!newValue) {
                if (this.editado) {
                    this.$store.dispatch('reservacionresponsable/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Editado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$emit('editado')
                    })
                }
                else {
                    if (this.tad_error) {
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
            this.$store.dispatch('aseguramientoreservacion/unset_error');
            this.$emit('ocultar')
        },
        submit() {
            var vobj = {};
            var has_somting_wrong = false;
            for (const property in this.aseguramientoreservacion) {
                if (property== "aseguramiento") {
                    if (this.aseguramientoreservacion[property] === null) {
                        has_somting_wrong = true;
                        this.$store.dispatch('aseguramientoreservacion/newError', { "aseguramiento": ["Seleccione un aseguramiento"] });
                    }
                    else {
                        vobj[property] = this.aseguramientoreservacion[property]['id'];
                    }
                }
                else {
                    vobj[property] = this.aseguramientoreservacion[property]
                }
            }
            if (!has_somting_wrong) {
                var objEdit = new Object();
                for (const property in this.edit) {
                    var save = true;
                    if (property === "cantidad")
                        save = false;
                    if (property === "reservacion")
                        save = false;
                    if (property === "aseguramiento")
                        save = false;
                    if (save) {
                        objEdit[property] = this.edit[property]
                    }
                }
                var data = {};
                for (const property in this.aseguramientoreservacion) {
                    if (objEdit[property] != this.aseguramientoreservacion[property]) {                        
                        if (property === "aseguramiento" ) {
                            data[property] = this.aseguramientoreservacion[property]["id"];
                        }
                        else {
                            data[property] = this.aseguramientoreservacion[property];
                        }
                    }
                }
                var cont = 0;
                for (const property in data) {
                    cont++;
                }
                if (cont > 0) {
                    this.$store.dispatch('aseguramientoreservacion/patch', { data: data});
                }
                else {
                    swal({
                        title: "Alerta",
                        text: "No ha hecho ningún cambio",
                        icon: "warning",
                        button: "Continuar",
                    });
                }
            }
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
            this.$store.dispatch('aseguramientoreservacion/solved', property);
        },
    },
    data() {
        return {
            aseguramientoreservacion: {
                cantidad: NaN,
                reservacion: null,
                aseguramiento: null,
            },
        }
    },
    mounted() {
        this.$store.dispatch('aseguramiento/listado');
    },
}
</script>