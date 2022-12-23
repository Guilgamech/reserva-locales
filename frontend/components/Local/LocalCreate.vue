<template>
    <div :class="{'show':show}" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class="vertical-center">
          <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Nueva local</h4>                  
                </div>
              </div>
              <div class="card-body">
                <h6 class="mb-2 text-center">
                  Complete los siguientes Campos
                </h6>
                <form ref="create_local" role="form" class="text-start" @submit.prevent="submit">
                    <div class="col-12">
                        <fieldset class="mt-2 custom">
                            <legend>
                                <div class="row">
                                    <div class="col-6">
                                        Area
                                    </div>
                                    <div class="col-6">
                                        <div class="d-flex justify-content-end">                                                
                                            <button v-tooltip="'Crear Tipo de Obra'" type="button" @click="modal_ac=true" class="md-button md-create md-just-icon">
                                                <div class="md-ripple">
                                                    <div class="md-button-content">
                                                        <i class="fa fa-plus"></i>
                                                    </div>
                                                </div>
                                            </button>
                                            <button v-if="!(local.area===null)" v-tooltip="'Editar Tipo de Obra'" type="button" @click="modal_ad=true" class="ms-2 md-button md-edit md-just-icon">
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
                                        <v-select
                                        v-model="local.area"
                                        @input="solved('area')"
                                        :class="{'hgl':area_hlg}"
                                        class="style-chooser"
                                        placeholder="Seleccionar"
                                        label="nombre"
                                        :options="area" />
                                        <div v-if="err_area.length>0" class="error">{{err_area}}</div>
                                    </div>
                                </div>
                            </div>
                        </fieldset>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <inputoutline
                                @error-solved="solved('nombre')"
                                :error="err_nombre"
                                label="Nombre"
                                type="text"
                                v-model="local.nombre"
                            />
                        </div>
                        <div class="col-12">
                            <number-inputoutline
                                @error-solved="solved('capacidad')"
                                :error="err_capacidad"
                                label="Capacidad"
                                type="number"
                                v-model="local.capacidad"
                            />
                        </div>
                        <div class="col-12">
                            <inputoutline
                                @error-solved="solved('telefono')"
                                :error="err_telefono"
                                label="Teléfono Del Local"
                                type="text"
                                v-model="local.telefono"
                            />
                        </div>
                        <div class="col-12">
                            <inputoutline
                                @error-solved="solved('responsable_email')"
                                :error="err_responsable_email"
                                label="Correo del Responsable"
                                type="email"
                                v-model="local.responsable_email"
                            />
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
       <AreaCreate :show="modal_ac" @creado="ac_creado" @ocultar="modal_ac=false"/>
       <AreaDetails :objId="area_detail_id" :show="modal_ad" @editado="ad_editado" @eliminado="ad_eliminado" @ocultar="modal_ad = false" />
    </div>
</template>


<script>
import Inputoutline from '../Inputoutline.vue';
import Textareaoutline from '../Textareaoutline.vue';
import AreaCreate from '../Area/AreaCreate.vue';
import AreaDetails from '../Area/AreaDetails.vue';
export default {
    components: {Textareaoutline, Inputoutline, AreaCreate},
    name:'LocalCreate',
    props:{
        show:{
            type: Boolean,
            required:true,
        }
    },
    computed:{
        area_detail_id(){
            if(this.local.area === null){
                return '';
            }
            return ''+this.local.area.id;
        },
        area_hlg(){
            if(this.$store.state.local.error.area.length > 0){
                return true;
            }
            else if(this.local.area === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        creando_local(){            
            return this.$store.state.local.creando
        },
        creado_local(){            
            return this.$store.state.local.creado
        },
        err_nombre(){
            if(this.$store.state.local.error.nombre.length == 0){
                return '';
            }
            return this.$store.state.local.error.nombre.join(", ");
        },
        err_capacidad(){
            if(this.$store.state.local.error.capacidad.length == 0){
                return '';
            }
            return this.$store.state.local.error.capacidad.join(", ");
        },
        err_telefono(){
            if(this.$store.state.local.error.telefono.length == 0){
                return '';
            }
            return this.$store.state.local.error.telefono.join(", ");
        },
        err_responsable_email(){
            if(this.$store.state.local.error.responsable_email.length == 0){
                return '';
            }
            return this.$store.state.local.error.responsable_email.join(", ");
        },
        err_area(){
            if(this.$store.state.local.error.area.length == 0){
                return '';
            }
            return this.$store.state.local.error.area.join(", ");
        },
        error(){
            if( this.err_nombre.length>0 
                || this.err_capacidad.length>0
                || this.err_telefono.length>0
                || this.err_responsable_email.length>0
                || this.err_area.length>0
            ){
                return true;
            }
            return false;
        },
        area(){           
            return this.$store.state.area.listado;            
        },
    },
    watch:{
        show(newValue){
            if(newValue){
                this.$store.dispatch('local/unset_error');
                this.$store.dispatch('area/listado');
            }
        },
        creando_local(newValue){
            if(!newValue){
                if(this.creado_local){
                    this.$store.dispatch('local/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Creado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then( () => {
                        this.$emit('creando');
                        this.local = {
                            nombre: '',
                            capacidad: NaN,
                            telefono: '',
                            responsable_email: '',
                            area:null,
                        };
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
            this.$store.dispatch('local/unset_error'); 
            this.$emit('ocultar')
            this.local = {
                nombre: '',
                capacidad: NaN,
                telefono: '',
                responsable_email: '',
                area:null,
            };
        },
        submit(){
            var vobj = {};
            var has_somting_wrong = false;
            for (const property in this.local) {
                if(property == "area")
                {
                    if(this.local[property] === null)
                    {
                        has_somting_wrong = true;
                        this.$store.dispatch('local/newError', {"area":["Seleccione un Tipo de local"]});
                    }
                    else{
                        vobj[property] = this.local[property]['id'];
                    }
                }
                else{
                    vobj[property] = this.local[property]
                }
            }            
            if(!has_somting_wrong)
                this.$store.dispatch('local/save', vobj);
            else{
                swal({
                    title: "ERROR !!",
                    text: "Revise los campos con error",
                    icon: "error",
                    button: "Continuar",
                })
                var has_somting_wrong = false;
            }
        },
        solved(property){
            this.$store.dispatch('local/solved', property);
        },
        ac_creado(){
            this.modal_ac = false;
            this.local.area = (this.areae.filter((item) => {
                return item.id == this.$store.state.area.creado_id;
            }))[0];
        },
        ad_editado(){
            this.modal_ad = false;
            this.local.area = (this.area.filter((item) => {
                return item.id == this.$store.state.area.editado_id;
            }))[0];
        },
        ad_eliminado(){
            this.modal_ad = false;
            this.local.area = null;
        },
    },
    data(){
        return {
            local: {
                nombre: '',
                capacidad: NaN,
                telefono: '',
                responsable_email: '',
                area:null,
            },
            modal_ac:false,
            modal_ad:false
        }
    },
}
</script>