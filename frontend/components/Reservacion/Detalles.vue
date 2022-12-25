<template>
    <div class="container-fluid">
        <div v-if="!!item" class="row">
            <div class="col-12">
                <h5>Tipo de Actividad: <span class="text-sm text-secondary">{{ item.actividad.tipo_actividad.nombre }}</span></h5>
                <h5>Actividad: <span class="text-sm text-secondary">{{ item.actividad.nombre }}</span></h5>
                <h5>Cantidad de Participantes: <span class="text-sm text-secondary">{{ item.cantidad_participantes }}</span></h5>
                <h5>Fecha: <span class="text-sm text-secondary">{{ fmDate(item.fecha_inicio) }}</span></h5>
                <h5>Horario: <span class="text-sm text-secondary">{{ hDate(item.fecha_inicio) }} - {{ hDate(item.fecha_fin) }}</span></h5>
                <h5>Estado: <span class="text-sm text-secondary">{{ item.estado }}</span></h5>
                <h5>Solicitante: <span class="text-sm text-secondary">{{ item.solicitante.email }}</span></h5>
                <h5 v-if="item.estado === 'Cancelada'">Motivo Cancelación: <span class="text-sm text-secondary">{{ item.motivo }}</span></h5>
                <div class="row " v-if="item.estado === 'Aprobada'">
                    <div class="row col-12 mb-3 ">
                        <h5 class="col-12">Aseguramientos:
                        </h5>
                    </div>
                    <div class="row col-12 mb-3" v-for=" (itemAseguramiento, index) in item.aseguramientos ">
                        <h5 class="col-6"><span class="text-sm text-secondary">{{ itemAseguramiento.aseguramiento.nombre }}</span>
                        </h5>
                        <h5 class="col-3"><span class="text-sm text-secondary">{{ itemAseguramiento.cantidad }}</span>
                        </h5>
                        <button v-if="canDelete" v-tooltip="'Eliminar Aseguramiento'" type="button"
                            class="md-button md-danger md-just-icon col-1 ms-2">
                            <div class="md-ripple">
                                <div class="md-button-content">
                                    <i class="fas fa-trash-alt"></i>
                                </div>
                            </div>
                        </button>
                    </div>
                </div>
                <div class="col-2">
                    <button v-if="canDelete && item.estado === 'Aprobada'"
                    @click="$store.dispatch('reservacion/setAseguramientoModal', true)"
                    type="button" class="btn btn-success">
                        <i class="fa fa-plus"></i>
                    </button>
                </div>
            </div>
            <div class="col-12 mt-2">
                <div class="row">
                    <div class="col-6">
                        <button v-if="canDelete" type="button" @click="sendDelete"
                            class="btn bg-gradient-danger w-100 my-4 mb-2">Eliminar
                        </button>
                    </div>
                    <div class="col-6">
                        <button type="button" @click="$emit('ocultar_detalles')"
                            class="btn bg-gradient-dark w-100 my-4 mb-2">Cerrar
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <h1 v-else>Not Found</h1>
    </div>
</template>

<script>
import { format as formatDate } from "date-fns";
import { utcToZonedTime } from "date-fns-tz";

export default {
    name: "ReservacionDetalles",
    computed: {
        item() {
            const itemValue = this.$store.state.reservacion.item;
            if (!!itemValue?.id) {
                return itemValue;
            }
            return null;
        },
        eliminado() {
            return this.$store.state.reservacion.eliminado;
        },
        canDelete() {
            const isUser = this.item?.solicitante?.id === this.$auth.user.id;
            const fecha = utcToZonedTime(this.item?.fecha_inicio, 'Cuba') > new Date()
            const aprobada = this.item?.estado === "Aprobada"
            if (isUser) {
                if (aprobada) {
                    if (!fecha) {
                        return false
                    }
                }
                return true
            }
            return false
        },


    },
    watch: {
        eliminado(newValue) {
            if (newValue) {
                this.$store.dispatch('reservacion/setEliminado', false);
                swal({
                    title: "Correcto!!",
                    text: "Eliminada Satisfactoriamente",
                    icon: "success",
                    button: "Continuar",
                }).then(() => {
                    this.$store.dispatch('local/listado');
                    this.$emit('reservacion_eliminada')
                })
            }
        }
    },
    methods: {
        fmDate(date = new Date()) {
            const fecha = utcToZonedTime(date, 'Cuba')
            return formatDate(fecha, "yyyy-MM-dd");
        },
        hDate(date = new Date()) {
            const fecha = utcToZonedTime(date, 'Cuba')
            return formatDate(fecha, "HH:mm");
        },
        sendDelete() {
            this.$store.dispatch('reservacion/deleteItem', this.item?.id)
            console.log('send Delete')
        }
    },
    mounted() {
        this.reservacion = this.$auth.user.id
    },
}

</script>

<style scoped>

</style>
