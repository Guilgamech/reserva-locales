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
                                <h6 class="mb-2 text-end">Capacidad:</h6>
                                <h6 class="mb-2 text-end">Telefono:</h6>
                                <h6 class="mb-2 text-end">Responsable:</h6>
                                <h6 class="mb-2 text-end">Area:</h6>
                                <h6 class="mb-2 text-end">Medios:</h6>
                            </div>
                            <div class="col-7">
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{edit.nombre}}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{edit.capacidad}}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{edit.telefono}}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{edit.responsable_email}}</span></h6>
                                <h6 class="mb-2"><span class="text-sm text-secondary">{{edit.area.nombre}}</span></h6>
                                <div class="row mb-2" v-for=" (item, index) in edit.medios ">
                                    <h6  class="col-6"><span class="text-sm text-secondary">{{item.medio.nombre}}</span></h6>
                                    <h6  class="col-6"><span class="text-sm text-secondary">{{item.cantidad}}</span></h6>
                                </div>
                            </div>
                            <div class="row justify-content-center text-center mt-3">
                                <div class="col-lg-4 cl-md-6 col-sm-6 col-12">
                                    <button type="button" @click="ocultar()" class="btn bg-gradient-dark w-100 ">Salir</button>
                                </div>
                            </div>
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
export default{
    components: { Inputoutline },
    name:'LocalDetails',
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
            return this.$store.state.local.edit;
        },
        existe(){
            return this.$store.state.local.existe
        },        
        editando(){
            return this.$store.state.local.editando
        },
        editado(){
            return this.$store.state.local.editado
        },
        deleting(){            
            return this.$store.state.local.deleting
        },
        deleted(){            
            return this.$store.state.local.deleted
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
        err_medios(){
            if(this.$store.state.local.error.medios.length == 0){
                return '';
            }
            return this.$store.state.local.error.medios.join(", ");
        },
        error(){
            if( this.err_nombre.length>0 
            || this.err_capacidad.length>0 
            || this.err_telefono.length>0 
            || this.err_responsable_email.length>0
            || this.err_area.length>0
            || this.err_medios.length>0
            ){
                return true;
            }
            return false;
        },

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
                this.$store.dispatch('local/unset_error');
                this.$store.dispatch('local/edit', this.objId);
            }
        },
        editando(newValue){
            if(!newValue){
                if(this.editado){
                    this.$store.dispatch('local/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Editado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then( () => {
                        this.$emit('editado')
                        this.canedit=false;
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
        },
        deleting(newValue){
            if(!newValue){
                if(this.deleted){
                    this.$store.dispatch('local/listado');
                    swal({
                        title: "Correcto !!",
                        text: "Eliminado Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then( () => {
                        this.$emit('eliminado');
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
    },
    methods:{
        ocultar(){
            this.$store.dispatch('local/unset_error');
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
                this.$store.dispatch('local/patch', { data:data, id:this.objId });
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
            this.$store.dispatch('local/solved', property);
        },
        todelete(){
            swal({
                title: "Estas seguro de Eliminar",
                text: "Una vez eliminado no hay vuelta atrás",
                icon: "warning",
                buttons: ["Cancelar", "Sí, Eliminar"],
                dangerMode:true
            }).then((willDelete) => {
                if (willDelete) {
                    this.$store.dispatch('local/delete', this.objId);
                } else {
                    swal("Se ha cancelado la Acción de Eliminar")
                }
            });
        }
    },
    data(){
        return {
            canedit:false,            
            item:{
                nombre: '',
                capacidad: '',
                telefono: '',
                responsable_email: '',
                area:null,
                medios:null
            },            
        }
    },
}   
</script>