<template>
    <div :class="{'show':show}" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class="vertical-center">
          <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Nuevo Medios </h4>                  
                </div>
              </div>
              <div class="card-body">
                <h6 class="mb-2 text-center">
                  Complete los siguientes Campos
                </h6>
                <form ref="create_medio" role="form" class="text-start" @submit.prevent="submit">
                    <div class="row">
                        <div class="col-12">
                            <inputoutline
                                @error-solved="solved('codigo')"
                                :error="err_codigo"
                                label="Codigo"
                                type="text"
                                v-model="medio.codigo"
                            />
                        </div>
                        <div class="col-12">
                            <inputoutline
                                @error-solved="solved('nombre')"
                                :error="err_nombre"
                                label="Nombre"
                                type="text"
                                v-model="medio.nombre"
                            />
                        </div>
                        <div class="col-12">
                            <textareaoutline
                                label=""
                                @error-solved="solved('descripcion')"
                                placeholder="Descripción"
                                v-model="medio.descripcion"
                                :error="err_descripcion"/>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <div class="row">
                            <div class="col-6">
                                <button type="button" @click="ocultar()" class="btn bg-gradient-dark w-100 my-4 mb-2">Cancelar</button>
                            </div>
                            <div class="col-6">
                                <button type="submit" class="btn bg-gradient-info w-100 my-4 mb-2">Guardar</button>
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
    components: {Textareaoutline, Inputoutline },
    name:'MedioCreate',
    props:{
        show:{
            type: Boolean,
            required:true,
        }
    },
    computed:{
        creando_medio(){            
            return this.$store.state.medio.creando
        },
        creado_medio(){            
            return this.$store.state.medio.creado
        },

        err_nombre(){
            if(this.$store.state.medio.error.nombre.length == 0){
                return '';
            }
            return this.$store.state.medio.error.nombre.join(", ");
        },
        err_descripcion(){
            if(this.$store.state.medio.error.descripcion.length == 0){
                return '';
            }
            return this.$store.state.medio.error.descripcion.join(", ");
        },
        err_codigo(){
            if(this.$store.state.medio.error.codigo.length == 0){
                return '';
            }
            return this.$store.state.medio.error.codigo.join(", ");
        },
        error(){
            if( this.err_nombre.length>0 || this.err_descripcion.length>0 || this.err_codigo.length>0){
                return true;
            }
            return false;
        }
    },
    watch:{
        show(newValue){
            if(newValue){
                this.$store.dispatch('medio/unset_error');
            }
        },
        creando_medio(newValue){
            if(!newValue){
                if(this.creado_medio){
                    this.$store.dispatch('medio/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Creado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then( () => {
                        this.$emit('creado')
                        this.medio.codigo = '';
                        this.medio.nombre = '';
                        this.medio.descripcion = '';
                    })
                }
                else{
                    if(this.error){
                        swal({
                            title: "ERROR !!",
                            text: "Revise los campos con error",
                            icon: "error",
                            button: "Continuar",
                        })
                    }
                    else{
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
    methods:{
        ocultar(){
            this.$store.dispatch('medio/unset_error'); 
            this.$emit('ocultar')
            this.medio.codigo = '';
            this.medio.nombre = '';
            this.medio.descripcion = '';
        },
        submit(){
            this.$store.dispatch('medio/save', this.medio);
        },
        solved(property){
            this.$store.dispatch('medio/solved', property);
        }
    },
    data(){
        return {
            medio: {
                codigo: '',
                nombre: '',
                descripcion: '',
            },
        }
    }
}
</script>