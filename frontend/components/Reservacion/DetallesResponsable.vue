<template>
    <div class="container-fluid">
        <div v-if="!!item" class="row">
            <div class="col-12">
                <h6>Tipo de Actividad: <span class="text-sm text-secondary">{{ item.actividad.tipo_actividad.nombre }}</span></h6>
                <h6>Actividad: <span class="text-sm text-secondary">{{ item.actividad.nombre }}</span></h6>
                <h6>Cantidad de Participantes: <span class="text-sm text-secondary">{{ item.cantidad_participantes }}</span></h6>
                <h6>Fecha: <span class="text-sm text-secondary">{{ fmDate(item.fecha_inicio) }}</span></h6>
                <h6>Horario: <span class="text-sm text-secondary">{{ hDate(item.fecha_inicio) }} - {{ hDate(item.fecha_fin) }}</span></h6>
                <h6>Estado: <span class="text-sm text-secondary">{{ item.estado }}</span></h6>
                <h6>Solicitante: <span class="text-sm text-secondary">{{ item.solicitante.email }}</span></h6>
                <h6 v-if="item.estado === 'Cancelada'">Motivo Cancelación: <span class="text-sm text-secondary">{{ item.motivo }}</span></h6>
                <h6 v-if="item.estado === 'Aprobada'">Aseguramientos: <span class="text-sm text-secondary">{{ item.aseguramientos }}</span></h6>
            </div>
            <div class="col-12 mt-2">
                <div class="row">
                    <div class="col-4">
                        <button type="button" @click="sendCancel" class="btn bg-gradient-danger w-100 my-4 mb-2">
                            <i class="fa-solid fa-cancel"></i>
                        </button>
                    </div>
                    <div class="col-4">
                        <button type="button" @click="$emit('ocultar_detalles')"
                            class="btn bg-gradient-dark w-100 my-4 mb-2">
                            <i class="fa-solid fa-close"></i>
                        </button>
                    </div>
                    <div class="col-4">
                        <button type="button" @click="sendAproved" class="btn bg-gradient-success w-100 my-4 mb-2">
                            <i class="fa-solid fa-check"></i>
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
import { title } from "process";

export default {
    name: "ReservacionDetallesResponsable",
    computed: {
        item() {
            const itemValue = this.$store.state.reservacion.item;
            if (!!itemValue?.id) {
                return itemValue;
            }
            return null;
        },
        editado() {
            return this.$store.state.reservacion.editado;
        },
    },
    watch: {
        cancelado(newValue) {
            if (newValue) {
                if (!newValue) {
                    this.$store.dispatch('reservacion/setEditado', false);
                    swal({
                        title: "Correcto!!",
                        text: "Cancelacion Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$store.dispatch('local/listado');
                        this.$emit('reservacion_cancelada')
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
        },
        aprobado(newValue) {
            if (newValue) {
                this.$store.dispatch('reservacion/setEditado', false);
                swal({
                    title: "Correcto!!",
                    text: "Aprobación Satisfactoriamente",
                    icon: "success",
                    button: "Continuar",
                }).then(() => {
                    this.$store.dispatch('local/listado');
                    this.$emit('reservacion_aprobada')
                })
            }
        },
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
        sendCancel(id) {
            swal({
                title: "Estas Seguro de Cancelarla",
                icon: "error",
                content: {
                    element: "textarea",
                    attributes: {
                        placeholder: "Motivo por el cual se cancela",
                    },
                },
                buttons: ["Salir", "Sí, Cancelala"],
                dangerMode: true
            }).then((willCancel) => {
                if (willCancel) {
                    this.$store.dispatch('reservacion/update9852Item', this.item?.id);
                } else {
                    swal("Se ha Salido de la Acción de Cancelar")
                }
            });
        },
        sendAproved(id) {
            this.$store.dispatch('reservacion/aprovedItem', this.item?.id)
            console.log('send Aproved')
        },
    }
}
</script>

<style scoped>

</style>
