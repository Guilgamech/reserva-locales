<template>
    <div v-if="this.$store.state.auth.loggedIn" class="row">
        <div class="col-6 ">
            <div class="row">
                <div class="col-12">
                    <div class="card my-4 mt-5">
                        <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                            <div class="bg-gradient-dark shadow-dark border-radius-lg pt-4 pb-3 row">
                                <div class="col-12 d-flex align-items-center">
                                    <h6 class="text-white text-capitalize ps-3">Seleccione el local</h6>
                                </div>
                            </div>
                        </div>
                        <div class="card-body px-0 pb-2">
                            <div class="row">
                                <div class="col-10 mx-auto mb-2">
                                    <div class="form-control">
                                        <v-select v-model="localSelected" class="style-chooser"
                                                  placeholder="Seleccionar" label="nombre" :options="locales"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12">
                    <div class="card my-4 mt-5">
                        <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                            <div class="bg-gradient-dark shadow-dark border-radius-lg pt-4 pb-4 row">
                                <div class="col-6 d-flex align-items-center">
                                    <h6 class="text-white text-capitalize ps-3">Reservaciones</h6>
                                </div>
                            </div>
                        </div>
                        <div class="card-body px-0 pt-1 pb-2">
                            <div class="form-control d-flex justify-content-end pe-3 btn-filter pb-4">
                                <div class="form-control me-2 py-0 w-40">
                                    <v-select v-model="selecion" class="style-chooser" label="label"
                                              placeholder="Mostrar Todas" :options="selections"/>
                                </div>
                                <input type="text" v-model="filter" placeholder="Filtro:"/>
                            </div>
                            <h6 v-if="events.length === 0" class="text-center">No tiene actividades</h6>

                            <perfect-scrollbar key="table-reservation" v-else class="table-responsive py-0 px-2 mh-350">
                                <table class="table align-items-center mb-0">
                                    <thead>
                                    <tr>
                                        <th class="text-secondary font-weight-bolder opacity-8 ps-4">Tipo</th>
                                        <th class="text-secondary font-weight-bolder opacity-8 ps-2">Actividad</th>
                                        <th class="text-secondary font-weight-bolder opacity-8 ps-2">Fecha</th>
                                        <th class="text-secondary font-weight-bolder opacity-8 ps-2">Horario</th>
                                        <th class="text-end text-secondary font-weight-bolder opacity-8">Acciones
                                        </th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="(item, index) in tableContent" v-bind:key="index"
                                        :class="item.estado.toLowerCase()">
                                        <td class="text-justify text-sm ps-4">
                                            <h6 class="mb-0 text-sm">{{ item.tipo }}</h6>
                                        </td>
                                        <td class="text-justify text-sm">
                                            <h6 class="mb-0 text-sm">{{ item.actividad }}</h6>
                                        </td>
                                        <td class="text-justify text-sm">
                                            <h6 class="mb-0 text-sm">{{ item.fecha }}</h6>
                                        </td>
                                        <td class="text-justify text-sm">
                                            <h6 class="mb-0 text-sm">{{ item.horario }}</h6>
                                        </td>
                                        <td class="text-end pe-4">
                                            <a @click="changeSelectDate(item.fecha)"
                                               class="text-dark text-sm font-weight-bolder cursor-pointer"><i
                                                class="fa fa-search text-dark"></i> Buscar</a>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                            </perfect-scrollbar>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-6">
            <div class="card mt-3 mh-784">
                <div class="card-body">
                    <vue-cal ref="vuecal" :selected-date="selectDay" :disable-views="['years', 'year']" :events="events"
                             :locale="es" :hide-weekdays="[7]" :time="true" :time-cell-height="60" :time-from="8 * 60"
                             :time-step="90" :time-to="23 * 60" cell-contextmenu @cell-contextmenu="newEvent"
                             :on-event-click="enventClick">
                        <template v-tooltip="event.title_tooltip" #event="{ event, view }">
                            <div class="vuecal__event-title cursor-pointer" v-html="event.title"/>
                        </template>
                    </vue-cal>
                </div>
            </div>
        </div>
        <Modal modal-id="cliente-reservacion-create" size="sm" title="Nueva Reservación">
            <reservacion-form v-if="modalOpen === 'cliente-reservacion-create'" :reservaciones="reservaciones"
                              :local="localSelected" :start="selectedEvent" :newActividad="setActividadCreada"
                              @reservacion_cancelada="hideNewEvent" @reservacion_creada="refreshReservations"/>
        </Modal>
        <Modal modal-id="cliente-reservacion-detail" size="sm" title="Detalle Reservación">
            <Detalles @ocultar_detalles="hideNewEvent" @reservacion_eliminada="refreshReservations"/>
        </Modal>
        <ActividadCreate :show="showActividadModal" @creado="actividadCreada"
                         @ocultar="$store.dispatch('reservacion/setActividadModal', false)"/>
        <AseguramientoReservacionCreate
            :show="showAseguramientoModal"
            @creado="$store.dispatch('reservacion/setAseguramientoModal', false)"
            @ocultar="$store.dispatch('reservacion/setAseguramientoModal', false)"/>
    </div>
</template>
<script>
import {PerfectScrollbar} from "vue2-perfect-scrollbar";
import Modal from "@/components/Modal/Modal";
import MenuPosition from "@/components/Menu/MenuPosition";
import {VClosePopover, VPopover, VTooltip} from "v-tooltip";
import Vue from "vue";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import {utcToZonedTime} from 'date-fns-tz'
import {format as formatDate, parse as parseDate} from 'date-fns'
import Detalles from "@/components/Reservacion/Detalles";
import ActividadCreate from "@/components/Actividad/ActividadCreate";
import AseguramientoReservacionCreate
    from '../../components/AseguramientoReservacion/AseguramientoReservacionCreate.vue';

const es = {
    "weekDays": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    "weekDaysShort": ["L", "M", "MI", "J", "V", "S", "D"],
    "months": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    "years": "Años",
    "year": "Año",
    "month": "Meses",
    "week": "Semanas",
    "day": "Dia",
    "today": "Hoy",
    "noEvent": "No hay Eventos",
    "allDay": "Todo el Dia",
    "deleteEvent": "Eliminar Evento",
    "createEvent": "Crear Evento",
    "dateFormat": "YYYY MMMM D dddd"
}

const getIcon = (tipoActividad) => {
    switch (tipoActividad) {
        case "Clase":
            return "fa-person-chalkboard"
        case "Conferencia":
            return "fa-comments"
        case "Reunión":
            return "fa-handshake"
        default:
            return "fa fa-plus"
    }
}
Vue.directive("tooltip", VTooltip);
Vue.directive("close-popover", VClosePopover);
Vue.component("v-popover", VPopover);
export default {
    components: {
        MenuPosition,
        VueCal,
        Modal,
        PerfectScrollbar,
        Detalles,
        ActividadCreate,
        AseguramientoReservacionCreate
    },
    name: "Reservacion",
    middleware: ["login"],
    computed: {
        modalOpen() {
            return this.$store.state.ui.showModalId;
        },
        actividades() {
            return this.$store.state.actividad.listado;
        },
        showActividadModal() {
            return this.$store.state.reservacion.actividadModal;
        },
        showAseguramientoModal() {
            return this.$store.state.reservacion.aseguramientoModal;
        },
        locales() {
            return this.$store.state.local.listado;
        },
        localesReservaciones() {
            if (this.localSelected !== null) {
                const storeLocals = this.$store.state.local.listado;
                return storeLocals.filter(el => el.id === this.localSelected.id)[0].reservaciones;
            }
            return []


        },
        userId() {
            return this.$auth.user.id;
        },
        reservaciones() {
            if (this.localSelected !== null && !!this.locales.length > 0 && !!this.userId) {
                const allReservations = this.localesReservaciones;
                const aprovedReservations = allReservations.filter(element =>
                    (element.estado === "Aprobada" && element.solicitante !== this.userId))
                const currentUserReservations = allReservations.filter(element => element.solicitante === this.userId)
                const showReservations = aprovedReservations.concat(currentUserReservations)
                let newReservations = showReservations.map(el => {
                    let newEl = {}
                    const content = {...el}
                    const start = utcToZonedTime(content.fecha_inicio, 'Cuba')
                    const end = utcToZonedTime(content.fecha_fin, 'Cuba')
                    newEl.start = formatDate(start, "yyyy-MM-dd HH:mm")
                    newEl.end = formatDate(end, "yyyy-MM-dd HH:mm")
                    let tipoActividad = content.actividad?.tipo_actividad?.nombre;
                    let iconType = "undefined";
                    let title = `<i class="fa ${getIcon(iconType)}"></i> Undefined`
                    if (!!tipoActividad) {
                        iconType = tipoActividad
                        title = `<i class="fa ${getIcon(iconType)}"></i> ${tipoActividad}`
                    }
                    let clase = "pendiente"
                    if (content.solicitante !== this.userId && content.estado === "Aprobada") {
                        clase = "aprobada_other_owner";
                    } else {
                        clase = content.estado.toLowerCase()
                    }
                    newEl.id = content.id
                    newEl.title = title
                    newEl.content = content
                    newEl.class = clase
                    newEl.title_tooltip = content.actividad?.nombre
                    return newEl;
                });
                newReservations.sort((a, b) => {
                    let x = a.start
                    let y = b.start
                    return x < y ? -1 : x > y ? 1 : 0;
                })
                return newReservations;
            }
            return []
        },
        tableContent() {
            let newTableContent = this.reservaciones.map(el => {
                let tableItem = {};
                tableItem.tipo = el.content.actividad?.tipo_actividad?.nombre
                tableItem.actividad = el.content.actividad?.nombre
                const dtime = el.start.split(' ')
                tableItem.fecha = dtime[0];
                const hstart = dtime[1];
                const hend = el.end.split(' ')[1];
                tableItem.horario = `${hstart}-${hend}`;
                tableItem.estado = el.content.estado;
                return tableItem;
            })
            newTableContent.sort((a, b) => {
                let x = new Date(a.fecha)
                let y = new Date(b.fecha)
                return x < y ? -1 : x > y ? 1 : 0;
            })
            if (!!this.selecion) {
                newTableContent = newTableContent
                    .filter(element => element.estado.toLowerCase() === this.selecion.value)
            }
            if (this.filter !== '') {
                newTableContent = newTableContent
                    .filter(element => (element.fecha.toLowerCase().includes(this.filter.toLowerCase()) ||
                        element.tipo.toLowerCase().includes(this.filter.toLowerCase()) ||
                        element.actividad.toLowerCase().includes(this.filter.toLowerCase()) ||
                        element.horario.toLowerCase().includes(this.filter.toLowerCase())
                    ))
            }
            return newTableContent;
        }
    },
    watch: {
        reservaciones(newEl) {
            this.events = newEl
            // if (this.events.length > 0) {
            //     this.selectDay = this.events[0].start.split(' ')[0]
            // }
        }
    },
    data: () => ({
        modal_agregar_aseguramiento: false,
        es,
        localSelected: null,
        events: [],
        filter: '',
        selecion: null,
        selections: [
            {label: "Aprobadas", value: 'aprobada'},
            {label: "Pendientes", value: 'pendiente'},
            {label: "Canceladas", value: 'cancelada'}
        ],
        selectDay: formatDate(new Date(), "yyyy-MM-dd"),
        selectedEvent: null,
        setActividadCreada: {},
    }),
    methods: {
        async actividadCreada() {
            const newId = this.$store.state.actividad.creado_id;
            await this.$store.dispatch("actividad/listado");
            const foundActivity = this.actividades.filter(el => el.id === newId)
            if (foundActivity.length > 0) {
                this.setActividadCreada = foundActivity[0]
            } else {
                this.setActividadCreada = {}
            }
            await this.$store.dispatch('reservacion/setActividadModal', false)
        },
        newEvent($event) {
            console.log($event)
            if (!!this.localSelected) {
                if ($event.date < new Date()) {
                    swal({
                        title: "Información",
                        text: "Seleccione una fecha mayor a la de hoy",
                        icon: "info",
                        button: "Continuar",
                    })
                } else {
                    this.selectedEvent = $event.date;
                    this.$store.dispatch("ui/setShowModalId", "cliente-reservacion-create")
                }
            } else {
                swal({
                    title: "Información",
                    text: "Seleccione un local para crear una reservación",
                    icon: "info",
                    button: "Continuar",
                })
            }
        },
        hideNewEvent() {
            this.$store.dispatch("ui/setShowModalId", "")
        },
        refreshReservations() {
            const seleccionado = {...this.localSelected};
            this.localSelected = null;
            setTimeout(() => {
                this.localSelected = seleccionado;
            }, 50)
            this.hideNewEvent()
        },
        enventClick(event, e) {
            this.$store.dispatch("reservacion/getItem", event.id)
            this.$store.dispatch("ui/setShowModalId", "cliente-reservacion-detail")
            e.stopPropagation()
        },
        editShow() {
            this.$store.dispatch("reservacion/getItem",)
            this.$store.dispatch("ui/setShowModalId", "cliente-reservacion-edit")
        },
        changeSelectDate(fecha) {
            console.log(fecha);
            this.$refs.vuecal.switchView('day', parseDate(fecha, "yyyy-MM-dd", new Date()));
        },
    },
    mounted() {
        this.$store.dispatch('local/listado');
        this.$store.dispatch('actividad/listado');
        this.modal_agregar_aseguramiento = false;
    }
};
</script>
<style>
.vuecal__title button {
    color: white;
}

.vuecal__title-bar {
    background: linear-gradient(195deg, #42424a 0%, #191919 100%);
    color: white !important;;
}

.vuecal--view-with-time .vuecal__weekdays-headings,
.vuecal--view-with-time .vuecal__all-day {
    padding-right: 0 !important;
}

.vuecal__flex.weekday-label {
    font-size: 12px;
}

.vuecal__event {
    padding: 10px;
    border: 1px solid;
    overflow-y: scroll;
    cursor: pointer;
}

.vuecal__event::-webkit-scrollbar {
    display: none;
}

.vuecal__event {
    -ms-overflow-style: none;
    scrollbar-width: none;
}

.vuecal__event.aprobada {
    background-color: #c3fdb4;
    color: #333;
}

.vuecal__event.aprobada_other_owner {
    background-color: #344767;
    color: white;
}

.vuecal__event.pendiente {
    background-color: #49a3f1;
    color: #333;
}

.vuecal__event.cancelada {
    background-color: #fdb4b4;
    color: #333;
}

.vuecal__event-time {
    display: none;
}

tr.aprobada {
    background-color: #c3fdb4;
    border-radius: 5px;
}

tr.aprobada td:first-child {
    border-top-left-radius: 5px;
}

tr.aprobada td:last-child {
    border-top-right-radius: 5px;
}

tr.aprobada td:first-child {
    border-bottom-left-radius: 5px;
}

tr.aprobada td:last-child {
    border-bottom-right-radius: 5px;
}

tr.pendiente {
    background-color: #49a3f1;
    border-radius: 5px;
}

tr.pendiente td:first-child {
    border-top-left-radius: 5px;
}

tr.pendiente td:last-child {
    border-top-right-radius: 5px;
}

tr.pendiente td:first-child {
    border-bottom-left-radius: 5px;
}

tr.pendiente td:last-child {
    border-bottom-right-radius: 5px;
}

tr.cancelada {
    background-color: #fdb4b4;
    border-radius: 5px;
}

tr.cancelada td:first-child {
    border-top-left-radius: 5px;
}

tr.cancelada td:last-child {
    border-top-right-radius: 5px;
}

tr.cancelada td:first-child {
    border-bottom-left-radius: 5px;
}

tr.cancelada td:last-child {
    border-bottom-right-radius: 5px;
}

.table-responsive.ps.mh-350 {
    max-height: 389px !important;
    height: 100%;
}

.mh-784 {
    min-height: 779px;
    max-height: 779px;
    height: 100%;
}

.vuecal__cell-events-count {
    background-color: #5eb762;
}
.vuecal__title-bar button {

    color: white;

}
</style>
