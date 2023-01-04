<template>
    <div class="container-fluid">
        <div v-if="!!item" class="row">
            <div class="col-12">
                <h6>Tipo de Actividad: <span class="text-sm text-secondary">{{
                    item.actividad.tipo_actividad.nombre
                }}</span></h6>
                <h6>Actividad: <span class="text-sm text-secondary">{{ item.actividad.nombre }}</span></h6>
                <h6>Cantidad de Participantes: <span class="text-sm text-secondary">{{
                    item.cantidad_participantes
                }}</span></h6>
                <h6>Fecha: <span class="text-sm text-secondary">{{ fmDate(item.fecha_inicio) }}</span></h6>
                <h6>Horario: <span class="text-sm text-secondary">{{ hDate(item.fecha_inicio) }} - {{
                    hDate(item.fecha_fin)
                }}</span></h6>
                <h6>Estado: <span class="text-sm text-secondary">{{ item.estado }}</span></h6>
                <h6>Solicitante: <span class="text-sm text-secondary">{{ item.solicitante.email }}</span></h6>
                <h6 v-if="item.estado === 'Cancelada'">Motivo Cancelación: <span class="text-sm text-secondary">{{
                    item.motivo
                }}</span></h6>
                <div class="row " v-if="item.estado === 'Aprobada'">
                    <div class="row col-12 mb-3 ">
                        <h6 class="col-12">Aseguramientos:
                        </h6>
                    </div>
                    <div class="row col-12 mb-3" v-for=" (itemAseguramiento, index) in item.aseguramientos "
                        :key="`ia-${index}`">
                        <h6 class="col-6"><span class="text-sm text-secondary">{{
                            itemAseguramiento.aseguramiento.nombre
                        }}</span>
                        </h6>
                        <h6 class="col-3"><span class="text-sm text-secondary">{{ itemAseguramiento.cantidad }}</span>
                        </h6>
                    </div>
                </div>
            </div>
            <div class="col-12 mt-2">
                <div class="row">
                    <div v-if="item.estado == 'Pendiente' && canChangeState" class="col-4">
                        <button type="button" @click="sendCancel" class="btn bg-gradient-danger w-100 my-4 mb-2">
                            <i class="fa-solid fa-cancel"></i>
                        </button>
                    </div>
                    <div v-if="item.estado === 'Aprobada' && canChangeState" class="col-6">
                        <button type="button" @click="sendCancel" class="btn bg-gradient-danger w-100 my-4 mb-2">
                            <i class="fa-solid fa-cancel"></i>
                        </button>
                    </div>
                    <div class="col-4" v-if="item.estado == 'Pendiente'">
                        <button type="button" @click="$emit('ocultar_detalles')"
                            class="btn bg-gradient-dark w-100 my-4 mb-2 ">
                            <i class="fa-solid fa-close"></i>
                        </button>
                    </div>
                    <div class="col-6" v-else>
                        <button type="button" @click="$emit('ocultar_detalles')"
                            class="btn bg-gradient-dark w-100 my-4 mb-2 ">
                            <i class="fa-solid fa-close"></i>
                        </button>
                    </div>
                    <div class="col-4" v-if="item.estado == 'Pendiente' && canChangeState">
                        <button type="button" @click="sendAproved"
                            class="btn bg-gradient-success w-100 my-4 mb-2">
                            <i class="fa-solid fa-check"></i>
                        </button>
                    </div>
                    <div class="col-6" v-if="item.estado == 'Cancelada' && canChangeState">
                        <button type="button" @click="sendAproved"
                            class="btn bg-gradient-success w-100 my-4 mb-2">
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
import { format as formatDate, addDays, parse as parseDate, endOfDay, formatISO, addSeconds, subSeconds } from 'date-fns'
import { utcToZonedTime } from "date-fns-tz";

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
        canChangeState() {
            const fecha = utcToZonedTime(this.item?.fecha_inicio, 'Cuba') > new Date()
            const aprobada = this.item?.estado === "Aprobada"
            if (aprobada) {
                if (!fecha) {
                    return false
                }
            }
            return true

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
        async sendCancel() {
            await swal({
                title: "Estas Seguro de Cancelarla",
                icon: "error",
                content: {
                    element: "textarea",
                    attributes: {
                        placeholder: "Motivo por el cual se cancela",
                        name: 'motivo'
                    },
                },
                buttons: ["Salir", "Sí, Cancelala"],
                dangerMode: true
            }).then(async (willCancel) => {
                if (willCancel) {
                    const tarea = document.querySelector('textarea[name="motivo"]')
                    const motivo = tarea ? tarea.value : ''
                    const data = {
                        estado: 'Cancelada',
                        cantidad_participantes: this.item.cantidad_participantes,
                        fecha_inicio: this.item.fecha_inicio,
                        fecha_fin: this.item.fecha_fin,
                        motivo,
                        actividad: this.item.actividad.id,
                        local: this.item.local.id,
                        solicitante: this.item.solicitante.id
                    }
                    await this.$axios.$put(`/reservacion/${this.item.id}/`, data)
                        .then(() => {
                            swal({
                                title: "Correcto!!",
                                text: "Cancelada Satisfactoriamente",
                                icon: "success",
                                button: "Continuar",
                            }).then(() => {
                                this.$emit('reservacion-cancelada')
                            })
                        })
                        .catch((error) => {
                            console.log(error)
                            swal({
                                title: "ERROR !!",
                                text: "Revise la conexión con la Api",
                                icon: "error",
                                button: "Continuar",
                            })
                        })
                } else {
                    swal("Se ha Salido de la Acción de Cancelar")
                }
            });
        },
        async sendAproved() {
            const data = {
                estado: 'Aprobada',
                cantidad_participantes: this.item.cantidad_participantes,
                fecha_inicio: this.item.fecha_inicio,
                fecha_fin: this.item.fecha_fin,
                motivo: this.item.motivo,
                actividad: this.item.actividad.id,
                local: this.item.local.id,
                solicitante: this.item.solicitante.id
            }
            await this.$axios.$put(`/reservacion/${this.item.id}/`, data)
                .then(() => {
                    swal({
                        title: "Correcto!!",
                        text: "Aprobada Satisfactoriamente",
                        icon: "success",
                        button: "Continuar",
                    }).then(() => {
                        this.$emit('reservacion-aprobada')
                    })
                })
                .catch((error) => {
                    if (error.status === 500) {
                        swal({
                            title: "ERROR !!",
                            text: "Revise la conexión con la Api",
                            icon: "error",
                            button: "Continuar",
                        })
                    }
                    else {
                        swal({
                            title: "ERROR !!",
                            text: "Ya existe una reservación en este horario",
                            icon: "error",
                            button: "Continuar",
                        })
                    }
                })
        },
    }
}
</script>

<style scoped>

</style>
