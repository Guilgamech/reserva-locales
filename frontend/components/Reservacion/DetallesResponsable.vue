<template>
    <div class="container-fluid">
        <div v-if="!!item" class="row">
            <div class="col-12">
                <h5>Tipo de Actividad: {{ item.actividad.tipo_actividad.nombre }}</h5>
                <h5>Actividad: {{ item.actividad.nombre }}</h5>
                <h5>Cantidad de Participantes: {{ item.cantidad_participantes }}</h5>
                <h5>Fecha: {{ fmDate(item.fecha_inicio) }}</h5>
                <h5>Horario: {{ hDate(item.fecha_inicio) }} - {{ hDate(item.fecha_fin) }}</h5>
                <h5>Estado: {{ item.estado }}</h5>
                <h5 v-if="item.estado === 'Cancelada'">Motivo Cancelación: {{ item.motivo }}</h5>
                <h5 v-if="item.estado === 'Aprobada'">Aseguramientos: {{ item.aseguramientos }}</h5>
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
