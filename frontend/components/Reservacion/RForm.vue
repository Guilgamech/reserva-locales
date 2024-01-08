<template>
    <div class="container-fluid">
        <form @submit.prevent="submit">
            <div class="row">
                <div class="col-12">
                    <fieldset class="mt-2 custom">
                        <div class="row">
                            <div class="col-6">
                                Actividad
                            </div>
                            <div class="col-6">
                                <div class="d-flex justify-content-end">
                                    <button v-tooltip="'Nueva Actividad'" type="button"
                                            @click="$store.dispatch('reservacion/setActividadModal', true)"
                                            class="md-button md-create md-just-icon">
                                    <span class="md-ripple">
                                        <span class="md-button-content">
                                            <i class="fa fa-plus"></i>
                                        </span>
                                    </span>
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12">
                                <div class="form-control">
                                    <v-select
                                        v-model="evento.actividad"
                                        @input="solved('actividad')"
                                        :class="{'hgl':error.actividad.length>0}"
                                        class="style-chooser"
                                        placeholder="Seleccionar"
                                        label="nombre"
                                        :options="actividadOptions"/>
                                    <div v-if="error.actividad.length>0" class="error">{{
                                            error.actividad.join(', ')
                                        }}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </fieldset>
                </div>
                <div class="col-6">
                    <date-inputoutline v-model="evento.fecha" label="Fecha" :error="fechaErr"
                                       :placeholder="evento.fecha"/>
                </div>
                <div class="col-6">
                    <number-inputoutline v-model="evento.cantidad_participantes" label="Participantes"
                                         :error="cantidad_participantesErr"
                                         @error-solved="solved('cantidad_participantes')"/>
                </div>
                <div class="col-6">
                    <div class="form-control">
                        <v-select
                            v-model="evento.hora_inicio"
                            :class="{'hgl':horaInicioErr.length>0}"
                            class="style-chooser"
                            placeholder="Seleccionar"
                            label="label"
                            :options="horarioInicioOptions"/>
                        <div v-if="horaInicioErr.length>0" class="error">{{ horaInicioErr }}</div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="form-control">
                        <v-select
                            v-model="evento.hora_fin"
                            :class="{'hgl':horaFinErr.length>0}"
                            class="style-chooser"
                            placeholder="Seleccionar"
                            label="label"
                            :options="horaFinOptions"/>
                        <div v-if="horaFinErr.length>0" class="error">{{ horaFinErr }}</div>
                    </div>
                </div>
                <div class="col-12 mt-2">
                    <div class="row">
                        <div class="col-6">
                            <button type="button" @click="$emit('reservacion_cancelada')"
                                    class="btn bg-gradient-dark w-100 my-4 mb-2">Cancelar
                            </button>
                        </div>
                        <div class="col-6">
                            <button type="submit" class="btn bg-gradient-info w-100 my-4 mb-2">Guardar
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import {format as dateFormat, addDays, parse as parseDate, endOfDay, formatISO, addSeconds, subSeconds} from 'date-fns'
import {zonedTimeToUtc} from 'date-fns-tz'

const horario_inicio = [
    {label: '08:00', value: 8 * 60},
    {label: '09:30', value: 9 * 60 + 30},
    {label: '11:00', value: 11 * 60},
    {label: '12:30', value: 12 * 60 + 30},
    {label: '14:00', value: 14 * 60},
    {label: '15:30', value: 15 * 60 + 30},
    {label: '17:00', value: 17 * 60},
    {label: '18:30', value: 18 * 60 + 30},
    {label: '20:00', value: 20 * 60},
    {label: '21:30', value: 21 * 60 + 30},
];
const horario_fin = [
    {label: '09:30', value: 9 * 60 + 30},
    {label: '11:00', value: 11 * 60},
    {label: '12:30', value: 12 * 60 + 30},
    {label: '14:00', value: 14 * 60},
    {label: '15:30', value: 15 * 60 + 30},
    {label: '17:00', value: 17 * 60},
    {label: '18:30', value: 18 * 60 + 30},
    {label: '20:00', value: 20 * 60},
    {label: '21:30', value: 21 * 60 + 30},
    {label: '23:00', value: 23 * 60},

];
const getHoraInicio = (horaValue) => {
    const foundHour = horario_inicio.filter(el => el.value < horaValue)
    if (foundHour.length > 0) {
        return foundHour.at(-1)
    }
    return horario_inicio[0]
}
const containDates = (
    list = [
        {
            id: NaN,
            start: new Date(),
            end: new Date(),
        },
    ],
    start = new Date(),
    end = new Date()
) => {
    const newStart = addSeconds(start, 1);
    const newEnd = subSeconds(end, 1);
    return list.filter((element) => {
        const elStart = parseDate(element.start, 'yyyy-MM-dd HH:mm', new Date())
        const elEnd = parseDate(element.end, 'yyyy-MM-dd HH:mm', new Date())
        return (
            (newStart < elStart && elStart < newEnd) ||
            (newStart < elEnd && elEnd < newEnd) ||
            (elStart < newStart && newStart < elEnd) ||
            (elStart < newEnd && newEnd < elEnd)
        );
    });
};
const dateInRange = (check, start, end) => {
    return start < check && check < end
}
export default {
    name: "From",
    props: {
        start: {
            type: Date,
            required: false,
            default: () => addDays(new Date(), 1)
        },
        local: {
            type: Object,
            required: true
        },
        reservaciones: {
            type: Array,
            required: true
        },
        newActividad: {
            type: Object,
            required: true,
            default: () => ({})
        }
    },
    computed: {
        actividadOptions() {
            return this.$store.state.actividad.listado;
        },
        error() {
            return this.$store.state.reservacion.error;
        },
        horarioInicioOptions() {
            return horario_inicio
        },
        horaFinOptions() {
            if (!!this.evento.hora_inicio) {
                return horario_fin.filter(el => el.value > this.evento.hora_inicio.value)
            }
            return horario_fin
        },
        horaInicioErr() {
            if (!(!!this.evento.hora_inicio)) {
                return "Este campo es requerido"
            }
            if (this.evento.hora_fin?.value <= this.evento.hora_inicio?.value) {
                return "Horario no concuerda"
            }
            return ""
        },
        horaFinErr() {
            if (!(!!this.evento.hora_fin)) {
                return "Este campo es requerido"
            }
            if (this.horaInicioErr === "Horario no concuerda") {
                return "Horario no concuerda"
            }
            return ""
        },
        fechaErr() {
            let inicio = this.evento.fecha + " " + this.evento.hora_inicio?.label
            let fin = this.evento.fecha + " " + this.evento.hora_fin?.label
            const inicioDate = parseDate(inicio, 'yyyy-MM-dd HH:mm', new Date())
            const finDate = parseDate(fin, 'yyyy-MM-dd HH:mm', new Date())
            const foundReservation = containDates(this.reservaciones, inicioDate, finDate)
            if (inicioDate < new Date()) {
                return "La fecha no puede ser menor a la actual"
            }
            if (foundReservation.length > 0) {
                console.log(foundReservation[0])
                return "Ya existe una reservacion en esta fecha con ese horario"
            }
            return ""
        },
        cantidad_participantesErr() {
            if (this.error.cantidad_participantes.length > 0) {
                return this.error.cantidad_participantes.join(', ')
            }
            if (!(!!this.evento.cantidad_participantes)) {
                return "Complete este campo"
            }
            if (this.evento.cantidad_participantes <= 0) {
                return "tiene que ser mayor que 0"
            }
            return ""
        },
        hasError() {
            for (const property in this.error) {
                if (this.error[property].length > 0) {
                    return true
                }
            }
            if (this.horaInicioErr.length > 0)
                return true
            if (this.horaFinErr.length > 0)
                return true
            if (this.fechaErr.length > 0)
                return true
            return this.cantidad_participantesErr.length > 0;
        },
        propActivity() {
            return this.newActividad
        },
        creado() {
            return this.$store.state.reservacion.creado
        }
    },
    watch: {
        propActivity(newValue) {
            if (!!newValue)
                this.evento.actividad = newValue
            else
                this.evento.actividad = null
        },
        creado(newValue) {
            if (newValue) {
                this.$store.dispatch('reservacion/setCreado', false);
                swal({
                    title: "Correcto!!",
                    text: "Creada Satisfactoriamente",
                    icon: "success",
                    button: "Continuar",
                }).then(() => {
                    this.$store.dispatch('local/listado');
                    this.$emit('reservacion_creada')
                })

            }
        }
    },
    data: () => ({
        evento: {
            actividad: null,
            fecha: '',
            hora_inicio: null,
            hora_fin: null,
            cantidad_participantes: NaN
        },
    }),
    methods: {
        solved(property) {
            this.$store.dispatch("reservacion/solved", property)
        },
        submit() {
            if (this.hasError) {
                console.log(this.error)
                swal({
                    title: "ERROR !!",
                    text: "Revise los campos con error",
                    icon: "error",
                    button: "Continuar",
                })
            } else {
                let sendData = {}
                sendData.actividad = this.evento.actividad?.id
                const fecha_inicio = `${this.evento.fecha} ${this.evento.hora_inicio.label}`
                const fecha_fin = `${this.evento.fecha} ${this.evento.hora_fin.label}`
                console.log({fecha_inicio, fecha_fin})
                sendData.fecha_inicio = parseDate(fecha_inicio, 'yyyy-MM-dd HH:mm', new Date())
                sendData.fecha_fin = parseDate(fecha_fin, 'yyyy-MM-dd HH:mm', new Date())
                sendData.fecha_inicio = formatISO(sendData.fecha_inicio)
                sendData.fecha_fin = formatISO(sendData.fecha_fin)
                sendData.solicitante = this.$auth.user.id
                sendData.cantidad_participantes = this.evento.cantidad_participantes
                sendData.local = this.local.id
                console.log({sendData})
                this.$store.dispatch('reservacion/newItem', sendData)
            }
        }
    },
    mounted() {
        const fecha = this.start
        this.evento.fecha = dateFormat(fecha, "yyyy-MM-dd")
        const hour = dateFormat(fecha, "HH:mm");
        const splitHour = hour.split(':')
        const hValue = Number(splitHour[0]) * 60 + Number(splitHour[1])
        console.log({fecha, start: this.start, hour, hValue, fechaf: dateFormat(fecha, "yyyy-MM-dd")})
        this.evento.hora_inicio = getHoraInicio(hValue)
        this.evento.hora_fin = this.horaFinOptions[0]
    }
}
</script>

<style scoped>

</style>
