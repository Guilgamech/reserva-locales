<template>
    <div :class="{ 'show': show }" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div v-if="data.local_id!==''" class="vertical-center">
            <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
                <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                            <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Editar Medios de mi Local</h4>
                        </div>
                    </div>
                    <div class="card-body">
                        <h6 class="mb-2 text-center">
                            Complete los siguientes Campos
                        </h6>
                        <form ref="create_local" role="form" class="text-start" @submit.prevent="submit">
                            <div class="row">
                                <div class="col-12">
                                    <fieldset class="mt-2 custom">
                                        <legend>
                                            <div class="row">
                                                <div class="col-6">
                                                    <h4>Local: {{editlocal.nombre}}</h4>
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
                                                        Medio: {{mediolocal.medio.nombre}}
                                                    </h4>
                                                </div>
                                            </div>
                                        </legend>
                                    </fieldset>
                                </div>
                                <div class="col-12">
                                    <number-inputoutline :set_value="'' + edit.cantidad" @error-solved="solved('cantidad')"
                                        :error="err_cantidad" label="cantidad" type="number" v-model="mediolocal.cantidad" />
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
    name: 'LocalMedioEdit',
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
        medio_detail_id(){
            if(this.mediolocal.medio === null){
                return '';
            }
            return ''+this.mediolocal.medio.id;
        },
        medio_hlg(){
            if(this.$store.state.mediolocal.error.medio.length > 0){
                return true;
            }
            else if(this.mediolocal.medio === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        local_detail_id(){
            if(this.mediolocal.local === null){
                return '';
            }
            return ''+this.mediolocal.local.id;
        },
        local_hlg(){
            if(this.$store.state.mediolocal.error.local.length > 0){
                return true;
            }
            else if(this.mediolocal.local === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        editlocal() {
            return this.$store.state.localresponsable.listado.filter(el=> Number(el.id) === Number(this.data.local_id))[0]
        },
        edit() {
            return this.$store.state.mediolocal.edit;
        },
        existe() {
            return this.$store.state.mediolocal.existe
        },
        editando() {
            return this.$store.state.mediolocal.editando
        },
        editado() {
            return this.$store.state.mediolocal.editado
        },
        err_cantidad() {
            if (this.$store.state.mediolocal.error.cantidad.length == 0) {
                return '';
            }
            return this.$store.state.mediolocal.error.cantidad.join(", ");
        },
        err_local() {
            if (this.$store.state.mediolocal.error.local.length == 0) {
                return '';
            }
            return this.$store.state.mediolocal.error.local.join(", ");
        },
        err_medio(){
            if (this.$store.state.mediolocal.error.medio.length == 0) {
                return '';
            }
            return this.$store.state.mediolocal.error.medio.join(", ");
        },
        error() {
            if (this.err_cantidad.length > 0
                || this.err_medio.length > 0
                || this.err_local.length > 0
            ) {
                return true;
            }
            return false;
        },
        local() {
            return this.$store.state.localresponsable.listado;
        },
        medio() {
            return this.$store.state.medio.listado;
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
            this.localresponsable = obj;
            this.medio = obj;
        },
        show(newValue) {
            if (newValue) {
                this.$store.dispatch('mediolocal/unset_error');                
                const medioLocalFromLocal = this.editlocal.medios.filter(el => el.medio.id === Number(this.data.medio_id))[0]
                this.mediolocal.local = this.data.local_id
                this.mediolocal.medio = medioLocalFromLocal.medio
                this.mediolocal.cantidad = medioLocalFromLocal.cantidad
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
            this.$store.dispatch('mediolocal/unset_error');
            this.$emit('ocultar')
        },
        submit() {
            var vobj = {};
            var has_somting_wrong = false;
            for (const property in this.mediolocal) {
                if (property== "medio") {
                    if (this.mediolocal[property] === null) {
                        has_somting_wrong = true;
                        this.$store.dispatch('mediolocal/newError', { "medio": ["Seleccione un medio"] });
                    }
                    else {
                        vobj[property] = this.mediolocal[property]['id'];
                    }
                }
                else {
                    vobj[property] = this.mediolocal[property]
                }
            }
            if (!has_somting_wrong) {
                var objEdit = new Object();
                for (const property in this.edit) {
                    var save = true;
                    if (property === "cantidad")
                        save = false;
                    if (property === "local")
                        save = false;
                    if (property === "medio")
                        save = false;
                    if (save) {
                        objEdit[property] = this.edit[property]
                    }
                }
                var data = {};
                for (const property in this.mediolocal) {
                    if (objEdit[property] != this.mediolocal[property]) {                        
                        if (property === "medio" ) {
                            data[property] = this.mediolocal[property]["id"];
                        }
                        else {
                            data[property] = this.mediolocal[property];
                        }
                    }
                }
                var cont = 0;
                for (const property in data) {
                    cont++;
                }
                if (cont > 0) {
                    this.$store.dispatch('mediolocal/patch', { data: data});
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
            this.$store.dispatch('mediolocal/solved', property);
        },
    },
    data() {
        return {
            mediolocal: {
                cantidad: NaN,
                local: null,
                medio: null,
            },
        }
    },
    mounted() {
        this.$store.dispatch('medio/listado');
    },
}
</script>