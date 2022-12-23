<template>
    <div :class="{'show':show}" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class="vertical-center">
          <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Nuevo Tipo de Actividads </h4>                  
                </div>
              </div>
              <div class="card-body">
                <h6 class="mb-2 text-center">
                  Complete los siguientes Campos
                </h6>
                <form ref="create_tipo_actividad" role="form" class="text-start" @submit.prevent="submit">
                    <div class="row">
                        <div class="col-12">
                            <inputoutline
                                @error-solved="solved('nombre')"
                                :error="err_nombre"
                                label="Nombre"
                                type="text"
                                v-model="tipo_actividad.nombre"
                            />
                        </div>
                        <div class="col-12">
                            <textareaoutline
                                label=""
                                @error-solved="solved('descripcion')"
                                placeholder="Descripción"
                                v-model="tipo_actividad.descripcion"
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
    name:'TipoActividadCreate',
    props:{
        show:{
            type: Boolean,
            required:true,
        }
    },
    computed:{
        creando_tipo_actividad(){            
            return this.$store.state.tipo_actividad.creando
        },
        creado_tipo_actividad(){            
            return this.$store.state.tipo_actividad.creado
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
        show(newValue){
            if(newValue){
                this.$store.dispatch('tipo_actividad/unset_error');
            }
        },
        creando_tipo_actividad(newValue){
            if(!newValue){
                if(this.creado_tipo_actividad){
                    this.$store.dispatch('tipo_actividad/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Creado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then( () => {
                        this.$emit('creado')
                        this.tipo_actividad.nombre = '';
                        this.tipo_actividad.descripcion = '';
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
            this.$store.dispatch('tipo_actividad/unset_error'); 
            this.$emit('ocultar')
            this.tipo_actividad.nombre = '';
            this.tipo_actividad.descripcion = '';
        },
        submit(){
            this.$store.dispatch('tipo_actividad/save', this.tipo_actividad);
        },
        solved(property){
            this.$store.dispatch('tipo_actividad/solved', property);
        }
    },
    data(){
        return {
            tipo_actividad: {
                nombre: '',
                descripcion: '',
            },
        }
    }
}
</script>