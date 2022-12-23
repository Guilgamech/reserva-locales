<template>
  <div v-if="this.$store.state.autorizado" class="row">
        <div class="col-md-10 col-lg-12 col-12">
            <div class="card my-4 mt-5">
                <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                    <div class="bg-gradient-dark shadow-dark border-radius-lg pt-4 pb-3 row">            
                        <div class="col-6 d-flex align-items-center">
                            <h6 class="text-white text-capitalize ps-3">Areas del Sistema</h6>
                        </div>
                        <div class="col-6 text-end">
                            <a role="button" @click="modal_agregar=true" class="btn bg-gradient-success mb-0 cursor-pointer"><i class="fa-solid fa-plus me-2"></i>Agregar</a>
                        </div>
                    </div>
                </div>
                <div class="card-body px-0 pb-2">
                    <h6 v-if="listado.length == 0" class="text-center">No hay Areas en el sistema</h6>     
                    <perfect-scrollbar v-else class="table-responsive p-0">
                        <table class="table align-items-center mb-0">
                            <thead>
                            <tr>                    
                                <th class="text-secondary font-weight-bolder opacity-8 ps-4">Nombre</th>
                                <th class="text-secondary font-weight-bolder opacity-8 ps-2">Descripción</th>
                                <th class="text-end text-secondary font-weight-bolder opacity-8">Acciones</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="(item, index) in listado" v-bind:key="index">
                                <td class="ps-4">
                                    <h6 class="mb-0 text-sm">{{item.nombre}}</h6>
                                </td>
                                <td class="text-justify text-sm">
                                    <h6 class="mb-0 text-sm">{{item.descripcion}}</h6>
                                </td>
                                <td class="text-end pe-4">
                                    <a @click="showModalDetail(item.id)" class="text-secondary cursor-pointer text-sm"><i class="fa fa-file-invoice text-dark"></i> Detalles</a>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </perfect-scrollbar>
                </div>
            </div>
        </div>
    <area-create :show="modal_agregar" @creado="modal_agregar=false" @ocultar="modal_agregar=false" />
    <area-details :objId="detail_id" :show="modal_detail" @editado="modal_detail = false" @eliminado="modal_detail=false" @ocultar="modal_detail=false" />
  </div>
</template>

<script>
import { PerfectScrollbar } from 'vue2-perfect-scrollbar'
import AreaCreate from '../../components/Area/AreaCreate.vue'
import AreaDetails from '../../components/Area/AreaDetails.vue'
export default {
    components:{ PerfectScrollbar, AreaCreate, AreaDetails },
    middleware: ['admin'],
    name:'Area',
    mounted() {
        this.modal_agregar=false,
        this.modal_detail=false,
        this.detail_id='';
        this.$store.dispatch('area/listado');
    },
    computed:{
      listado(){
        return this.$store.state.area.listado
      }
    },
    data(){
        return {
            modal_agregar:false,
            modal_detail:false,
            detail_id:'',
        }
    },
    methods:{
        showModalDetail(id){
            if(id>0){
                this.detail_id = ''+id
                this.modal_detail = true;
            }
        }
    },
}
</script>
