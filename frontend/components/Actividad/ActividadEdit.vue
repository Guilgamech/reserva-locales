<template>
    <div :class="{'show':show}" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class="vertical-center">
          <div class="col-lg-3 col-md-4 col-10 mx-auto" @click.stop>
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Editar Actividad</h4>                  
                </div>
              </div>
              <div class="card-body">
                <h6 class="mb-2 text-center">
                  Complete los siguientes Campos
                </h6>
                <form ref="create_actividad" role="form" class="text-start" @submit.prevent="submit">
                    <div class="row">
                        <div class="col-12">
                            <inputoutline
                                @error-solved="solved('nombre')"
                                :error="err_nombre"
                                label="Nombre"
                                type="text"
                                v-model="actividad.nombre"
                            />
                        </div>
                        <div class="col-12">
                            <fieldset class="mt-2 custom">
                                <legend>
                                    <div class="row">
                                        <div class="col-6">
                                            Tipo de Actividad
                                        </div>
                                    </div>
                                </legend>
                                <div class="row">
                                    <div class="col-12">
                                        <div class="form-control">
                                            <v-select
                                            v-model="actividad.tipo_actividad"
                                            @input="solved('tipo_actividad')"
                                            :class="{'hgl':tipo_actividad_hlg}"
                                            class="style-chooser"
                                            placeholder="Seleccionar"
                                            label="nombre"
                                            :options="tipo_actividad" />
                                            <div v-if="err_tipo_actividad.length>0" class="error">{{err_tipo_actividad}}</div>
                                        </div>
                                    </div>
                                </div>
                            </fieldset>
                        </div>
                        <div class="col-12">
                            <textareaoutline
                            label=""
                            @error-solved="solved('motivo')"
                            placeholder="Motivo"
                            v-model="actividad.motivo"
                            :error="err_motivo"/>
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
    components: {Textareaoutline, Inputoutline, },
    name:'ActividadEdit',
    props:{
        show:{
            type: Boolean,
            required:true,
        },
        objId:{
            type:String,
            required:true
        }
    },
    computed:{
        tipo_actividad_detail_id(){
            if(this.actividad.tipo_actividad === null){
                return '';
            }
            return ''+this.actividad.tipo_actividad.id;
        },
        tipo_actividad_hlg(){
            if(this.$store.state.actividad.error.tipo_actividad.length > 0){
                return true;
            }
            else if(this.actividad.tipo_actividad === null)
            {
                return false;
            }
            else{
                return true;
            }
        },
        edit(){
            return this.$store.state.actividad.edit;
        },
        existe(){
            return this.$store.state.actividad.existe
        },        
        editando(){            
            return this.$store.state.actividad.editando
        },
        editado(){
            return this.$store.state.actividad.editado
        },
        err_nombre(){
            if(this.$store.state.actividad.error.nombre.length == 0){
                return '';
            }
            return this.$store.state.actividad.error.nombre.join(", ");
        },
        err_motivo(){
            if(this.$store.state.actividad.error.motivo.length == 0){
                return '';
            }
            return this.$store.state.actividad.error.motivo.join(", ");
        },
        err_tipo_actividad(){
            if(this.$store.state.actividad.error.tipo_actividad.length == 0){
                return '';
            }
            return this.$store.state.actividad.error.tipo_actividad.join(", ");
        },
        error(){
            if( this.err_nombre.length>0 
                || this.err_motivo.length>0
                || this.err_tipo_actividad.length>0
            ){
                return true;
            }
            return false;
        },
        tipo_actividad(){           
            return this.$store.state.tipo_actividad.listado;            
        },
    },
    watch:{
        edit(newValue){
            var obj = new Object();
            for(const property in this.edit){
                var save = true;
                if(save){
                    obj[property] = this.edit[property]    
                }
            }
            this.actividad = obj;
        },
        show(newValue){
            if(newValue){
                this.$store.dispatch('actividad/unset_error');
                this.$store.dispatch('tipo_actividad/listado');
                this.$store.dispatch('actividad/edit', this.objId);
            }
        },
        editando(newValue){
            if(!newValue){
                if(this.editado){
                    this.$store.dispatch('actividad/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Editado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then( () => {
                        this.$emit('editado')
                    })
                }
                else{
                    if(this.tad_error){
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
            this.$store.dispatch('actividad/unset_error'); 
            this.$emit('ocultar')
            this.actividad = {
                nombre: '',
                motivo: '',
                tipo_actividad:null
            };
        },
        submit(){
            var vobj = {};
            var has_somting_wrong = false;
            for (const property in this.actividad) {
                if(property == "tipo_actividad")
                {
                    if(this.actividad[property] === null)
                    {
                        has_somting_wrong = true;
                        this.$store.dispatch('actividad/newError', {"tipo_actividad":["Seleccione un Tipo de Actividad"]});
                    }
                    else{
                        vobj[property] = this.actividad[property]['id'];
                    }
                }
                else{
                    vobj[property] = this.actividad[property]
                }
            }            
            if(!has_somting_wrong){
                var objEdit = new Object();
                for(const property in this.edit){
                    var save = true;
                    if(property === "nombre")
                        save=false;
                    if(property === "motivo")
                        save=false;
                    if(save){
                        objEdit[property] = this.edit[property]    
                    }
                }
                var data = {};
                for(const property in this.actividad){
                    if(objEdit[property] != this.actividad[property]){
                        if(property === "tipo_actividad"){
                            data[property] = this.actividad[property]["id"];
                        }
                        else{
                            data[property] = this.actividad[property];
                        }
                    }
                }
                var cont = 0;
                for(const property in data){
                    cont++;
                }
                if(cont>0)
                {
                    this.$store.dispatch('actividad/patch', { data:data, id:this.objId });
                }
                else{
                    swal({
                        title: "Alerta",
                        text: "No ha hecho ningún cambio",
                        icon: "warning",
                        button: "Continuar",
                    });
                }
            }
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
            this.$store.dispatch('actividad/solved', property);
        },
        tac_creado(){
            this.modal_tac = false;
            this.actividad.tipo_actividad = (this.tipo_actividad.filter((item) => {
                return item.id == this.$store.state.tipo_actividad.creado_id;
            }))[0];
        },
        tad_editado(){
            this.modal_tad = false;
            this.actividad.tipo_actividad = (this.tipo_actividad.filter((item) => {
                return item.id == this.$store.state.tipo_actividad.editado_id;
            }))[0];
        },
        tad_eliminado(){
            this.modal_tad = false;
            this.actividad.tipo_actividad = null;
        },
    },
    data(){
        return {
            actividad: {
                nombre: '',
                motivo: '',
                tipo_actividad:null
            },
            modal_tac:false,
            modal_tad:false
        }
    }
}
</script>