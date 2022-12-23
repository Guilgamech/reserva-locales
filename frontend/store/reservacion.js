const inital_error = {
    estado: [],
    cantidad_participantes: [],
    fecha_inicio: [],
    fecha_fin: [],
    motivo: [],
    actividad: [],
    local: [],
    solicitante: [],
    others: []
};
const initialItem = {
    id: NaN,
    solicitante: {
        id: NaN,
        first_name: '',
        last_name: '',
        username: '',
        email: ''
    },
    local: {
        id: NaN,
        nombre: '',
        capacidad: NaN,
        telefono: '',
        responsable_email: '',
        area: NaN,
        medios: []
    },
    aseguramientos: [],
    actividad: {
        id: NaN,
        solicitante: {
            id: NaN,
            first_name: '',
            last_name: '',
            username: '',
            email: ''
        },
        tipo_actividad: {
            id: NaN,
            nombre: '',
            descripcion: ''
        },
        nombre: '',
        motivo: ''
    },
    estado: '',
    cantidad_participantes: NaN,
    fecha_inicio: '',
    fecha_fin: '',
    motivo: ''
};
export const state = () => ({
    listado: [],
    item: {...initialItem},
    loading: false,
    error: {...inital_error},
    actividadModal: false,
    aseguramientoModal: false,
    creado: false,
    editado: false,
    eliminado: false,
    aseguramientoAgregado: false,
    loadingNewAseguramiento: false,
})

export const actions = {
    async listado({commit},) {
        commit("setLoading", true)
        await this.$axios.$get('/reservacion/aprobadas/')
            .then((response) => {
                commit('setItem', response);
                commit("setLoading", false)
            })
            .catch((error) => {
                if (error?.response?.status < 500) {
                    commit('setError', error.response.data);
                } else {
                    if (error?.message)
                        commit('setError', {others: ["No hay conexión con la API"]});
                    else
                        console.log(error)
                }
            })
    },
    async getItem({commit}, id) {
        commit("setLoading", true)
        await this.$axios.$get(`/reservacion/${id}/`)
            .then((response) => {
                commit('setItem', response);
                commit("setLoading", false)
            })
            .catch((error) => {
                if (error?.response?.status < 500) {
                    commit('setError', error.response.data);
                } else {
                    if (error?.message)
                        commit('setError', {others: ["No hay conexión con la API"]});
                    else
                        console.log(error)
                }
            })
    },
    async addAseguramiento({commit}, data) {
        commit("setLoadingNewAseguramiento", true)
        await this.$axios.$post(`/reservacion-aseguramiento/`, data)
            .then(async (response) => {
                await this.$axios.$get(`/reservacion/${response.reservacion}/`)
                    .then((response) => {
                        commit('setItem', response);
                        commit('setAseguramientoAgregado', true)
                        commit("setLoadingNewAseguramiento", false)
                    })
                    .catch((error) => {
                        if (error?.response?.status < 500) {
                            commit('setError', error.response.data);
                        } else {
                            if (error?.message)
                                commit('setError', {others: ["No hay conexión con la API"]});
                            else
                                console.log(error)
                        }
                    })
            })
            .catch((error) => {
                if (error?.response?.status < 500) {
                    commit('setError', error.response.data);
                } else {
                    if (error?.message)
                        commit('setError', {others: ["No hay conexión con la API"]});
                    else
                        console.log(error)
                }
                commit('setAseguramientoAgregado', false)
                commit('setLoadingNewAseguramiento', false)
            })
    },
    async updateItem({commit}, {data, id}) {
        console.log({data, id})
    },
    async deleteItem({commit}, id) {
        await this.$axios.$delete(`/reservacion/${id}/`)
            .then(() => {
                commit('setEliminado', true);
            })
            .catch(error => {
                if (error?.response?.status < 500) {
                    commit('setError', error.response.data);
                } else {
                    if (error?.message)
                        commit('setError', {others: ["No hay conexión con la API"]});
                    else
                        console.log(error)
                }
            })
    },
    async newItem({commit}, data) {
        await this.$axios.$post(`/reservacion/`, data)
            .then((response) => {
                commit('setCreado', true)
            })
            .catch(error => {
                if (error?.response?.status < 500) {
                    commit('setError', error.response.data);
                } else {
                    if (error?.message)
                        commit('setError', {others: ["No hay conexión con la API"]});
                    else
                        console.log(error)
                }
            })
    },
    solved({commit}, property) {
        commit('solveError', property);
    },
    unset_error({commit}) {
        commit('resetError', inital_error)
    },
    setActividadModal({commit}, value) {
        commit('setActividadModal', value)
    },
    setAseguramientoModal({commit}, value) {
        commit('setAseguramientoModal', value)
    },
    setCreado({commit}, value) {
        commit('setCreado', value)
    },
    setEditado({commit}, value) {
        commit('setEditado', value)
    },
    setEliminado({commit}, value) {
        commit('setEliminado', value)
    },
    setAseguramientoAgregado({commit}, value) {
        commit('setAseguramientoAgregado', value)
    },
    setLoadingNewAseguramiento({commit}, value) {
        commit('setLoadingNewAseguramiento', value)
    },
    getListado({commit}, value) {
        commit('LISTADO', value)
    }
}
export const mutations = {
    setCreado(state, value) {
        state.creado = value
    },
    setLoadingNewAseguramiento(state, value) {
        state.loadingNewAseguramiento = value
    },
    setAseguramientoAgregado(state, value) {
        state.aseguramientoAgregado = value
    },
    LISTADO(state, value) {
        state.listado = value;
    },
    setEliminado(state, value) {
        state.eliminado = value
    },
    setEditado(state, value) {
        state.editado = value
    },
    setLoading(state, value) {
        state.loading = value;
    },
    setError(state, objError) {
        for (const property in objError) {
            if (property in state.error) {
                state.error[property] = objError[property]
            } else {
                state.error.others = [...state.error.others, ...objError[property]];
            }
        }
    },
    resetError(state, initial) {
        state.error = initial
    },
    solveError(state, property) {
        if (property in state.error) {
            state.error[property] = []
        }
    },
    setItem(state, value) {
        state.item = value
    },
    addAseguramiento(state, data) {

    },
    setActividadModal(state, value) {
        state.actividadModal = value;
    },
    setAseguramientoModal(state, value) {
        state.aseguramientoModal = value;
    }
}
// your root getters
export const getters = {}
