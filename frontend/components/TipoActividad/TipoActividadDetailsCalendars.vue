<template>
    <div :class="{'show':show}" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class=" vertical-center">
            <div class="col-lg-4 col-md-6 col-10 mx-auto" @click.stop>
                <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                            <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Detalles</h4>
                        </div>
                    </div>
                    <div v-if="!existe" class="card-body">
                        <h6  class="mb-2 text-center">
                            Revise la Conexión con la base de datos, o ha ingresado a una ruta inválida
                        </h6>
                        <div class="text-center mt-3">
                            <div class="row justify-content-center">                        
                                <div class="col-6">
                                    <button type="button" @click="ocultar()" class="btn bg-gradient-dark w-100 my-4 mb-2">Salir</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div v-else class="card-body">
                        <div v-if="!canedit" class="row">
                            <div class="col-5 justify-content-end">

                                <h6 class="mb-2 text-end">Nombre:</h6>
                                <h6 class="mb-2 text-end">Descripción:</h6>
                            </div>
                            <div class="col-7">
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{edit.nombre}}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{edit.descripcion}}</span></h6>
                            </div>
                            <div class="row justify-content-center text-center mt-3">
                                <div class="col-lg-4 cl-md-6 col-sm-6 col-12">
                                    <button type="button" @click="ocultar()" class="btn bg-gradient-dark w-100 ">Salir</button>
                                </div>
                            </div>
                        </div>
                        <div v-else class="row">
                            <h6 class="mb-2 text-center">
                                Edite los siguientes campos
                            </h6>
                            <form role="form" class="text-start" @submit.prevent="submit">
                                <div class="row">
                                    <div class="col-12">
                                        <inputoutline
                                            @error-solved="solved('nombre')"
                                            :error="err_nombre"
                                            label="Nombre"
                                            type="text"
                                            v-model="item.nombre"
                                        />
                                    </div>
                                    <div class="col-12">
                                        <textareaoutline
                                            label=""
                                            @error-solved="solved('descripcion')"
                                            placeholder="Descripción"
                                            v-model="item.descripcion"
                                            :error="err_descripcion" />
                                    </div>                        
                                </div>       
                                <div class="text-center mt-3">
                                    <div class="row">
                                        <div class="col-6">
                                            <button type="button" @click="canedit=false" class="btn bg-gradient-dark w-100 my-4 mb-2">Cancelar</button>
                                        </div>
                                        <div class="col-6">
                                            <button type="submit" class="btn bg-gradient-info w-100 my-4 mb-2">Guardar Cambios</button>
                                        </div>
                                    </div>
                                </div>                  
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
import swal from 'sweetalert';
import Inputoutline from '../Inputoutline.vue'
import Textareaoutline from '../Textareaoutline.vue';
export default{
    components: { Textareaoutline, Inputoutline },
    name:'TipoActividadDetails',
    props:{
        show:{
            type: Boolean,
            required:true
        },
        objId:{
            type:String,
            required:true
        }
    },
    computed:{
        edit(){
            return this.$store.state.tipo_actividad.edit;
        },
        existe(){
            return this.$store.state.tipo_actividad.existe
        },        
        err_nombre(){
            if(this.$store.state.tipo_actividad.error.nombre.length == 0){
                return '';
            }
            return this.$store.state.tipo_actividad.error.nombre.join(", ");
        },
        err_descripcion(){
            if(this.$store.state.tipo_actividad.error.descripcion.length == 0){
                return '';
            }
            return this.$store.state.tipo_actividad.error.descripcion.join(", ");
        },
        error(){
            if( this.err_nombre.length>0 || this.err_descripcion.length>0){
                return true;
            }
            return false;
        }
    },
    watch:{
        edit(newValue){
            for(const property in this.edit){
                if(property !== "id"){
                    this.item[property] = this.edit[property];
                }
            }
        },
        show(newValue){
            if(newValue){
                this.$store.dispatch('tipo_actividad/unset_error');
                this.$store.dispatch('tipo_actividad/edit', this.objId);
            }
        },
    },
    methods:{
        ocultar(){
            this.$store.dispatch('tipo_actividad/unset_error');
            this.$emit('ocultar')
            this.canedit=false;
        },
        submit(){
            var data = new Object();
            for(const property in this.item){
                if(this.edit[property] != this.item[property]){
                    data[property] = this.item[property];
                }
            }
            var cont = 0;
            for(const property in data){
                cont++;
            }
            if(cont>0)
            {
                this.$store.dispatch('tipo_actividad/patch', { data:data, id:this.objId });
            }
            else{
                swal({
                    title: "Alerta",
                    text: "No ha hecho ningún cambio",
                    icon: "warning",
                    button: "Continuar",
                });
            }
        },
        solved(property){
            this.$store.dispatch('tipo_actividad/solved', property);
        },
        
    },
    data(){
        return {
            canedit:false,            
            item:{
                nombre: '',
                descripcion:''
            },            
        }
    }
}
</script>