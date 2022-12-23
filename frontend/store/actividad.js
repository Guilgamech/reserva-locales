export const state = () => ({
    listado: [],
    edit: {
        id: '',
        nombre: '',
        motivo: '',
        solicitante: {},
        tipo_actividad: {},
    },
    existe: true,
    creado: false,
    creando: false,
    creado_id: null,
    editado_id: null,
    editado: false,
    editando: false,
    deleting: false,
    deleted: false,
    error: {
        nombre: [],
        motivo: [],
        solicitante: [],
        tipo_actividad: []

    },
    response_status: 0
})

export const actions = {
    async listado({ commit }) {
        var has_error = false;
        const response = await this.$axios.$get('/actividad/').
            catch(({ response }) => {
                has_error = true;
                commit('RESPONSE_STATUS', response.status);
            })
        if (!has_error) {
            commit('RESPONSE_STATUS', 200);
            commit('LISTADO', response)
        }
    },
    async edit({ commit }, id) {
        let has_error = false;
        const response = await this.$axios.$get(`/actividad/${id}/`).
            catch(({ response }) => {
                has_error = true;
                commit('RESPONSE_STATUS', response.status);
                commit('EXISTE', false);
                commit('EDIT', {
                    id: 0,
                    nombre: '',
                    motivo: '',
                    solicitante: {},
                    tipo_actividad: {},
                });
            })
        if (!has_error) {
            commit('EDIT', response);
            commit('RESPONSE_STATUS', 200);
            commit('EXISTE', true);
        }
    },
    async save({ commit }, rol) {
        commit('CREANDO', true);
        let has_error = false;
        const res = await this.$axios.$post('/actividad/', rol).
            catch(({ response }) => {
                has_error = true;
                commit('CREADO', false);
                commit('CREADO_ID', null);
                commit('RESPONSE_STATUS', response.status);
                if (response.status === 400) {
                    commit('ERROR', response.data);
                }
            });
        if (!has_error) {
            commit('CREADO', true);
            commit('CREADO_ID', res.id);
            commit('RESPONSE_STATUS', 200);
        }
        commit('CREANDO', false);
    },
    solved({ commit }, property) {
        commit('SOLVED', property);
    },
    unset_error({ commit }) {
        commit('SOLVED', "nombre");
        commit('SOLVED', "motivo");
        commit('SOLVED', "soicitante");
        commit('SOLVED', "tipo_actividad");

    },
    async patch({ commit }, { data, id }) {
        commit('EDITANDO', true);
        var has_error = false;
        const response = await this.$axios.$patch(`/actividad/${id}/`, data).
            catch(({ response }) => {
                has_error = true;
                commit('RESPONSE_STATUS', response.status);
                if (response.status === 400) {
                    commit('ERROR', response.data);
                    commit('EDITADO', false);
                    commit('EDITADO_ID', null);
                }
            });
        if (!has_error) {
            commit('RESPONSE_STATUS', 200);
            commit('EDITADO', true);
            commit('EDITADO_ID', id);
            commit('PATCH', { data: data, id: id });
        }
        commit('EDITANDO', false);
    },
    async delete({ commit }, id) {
        commit('DELETING', true);
        var has_error = false;
        const response = await this.$axios.$delete(`/actividad/${id}/`).
            catch(({ response }) => {
                has_error = true;
                commit('RESPONSE_STATUS', response.status);
                if (response.status === 400) {
                    commit('ERROR', response.data);
                    commit('DELETED', false);
                }
            });
        if (!has_error) {
            commit('RESPONSE_STATUS', 200);
            commit('DELETED', true);
            commit('DELETE', id);
        }
        commit('DELETING', false);
    },

}
export const mutations = {
    RESPONSE_STATUS(state, status) {
        state.response_status = status;
    },
    EXISTE(state, value) {
        state.existe = value;
    },
    LISTADO(state, response) {
        state.listado = response;
    },
    EDIT(state, response) {
        state.edit = response;
    },
    PATCH(state, { data, id }) {
        state.listado.forEach((element, index) => {
            if (element.id == id) {
                for (const property in data) {
                    state.listado[index][property] = data[property];
                }
            }
        });
    },
    CREADO(state, success) {
        state.creado = success;
    },
    CREANDO(state, status) {
        state.creando = status;
    },
    EDITADO(state, success) {
        state.editado = success;
    },
    EDITANDO(state, status) {
        state.editando = status;
    },
    ERROR(state, err) {
        for (const property in err) {
            switch (property) {
                case "nombre":
                    state.error.nombre = err[property];
                    break;
                case "motivo":
                    state.error.motivo = err[property];
                    break;
                case "tipo_actividad":
                    state.error.tipo_actividad = err[property];
                    break;
                case "solicitante":
                    state.error.solicitante = err[property];
                    break;

                default:
                    break;
            }
        }
    },
    SOLVED(state, property) {
        switch (property) {
            case "nombre":
                state.error.nombre = [];
                break;
            case "motivo":
                state.error.motivo = [];
                break;
            case "tipo_actividad":
                state.error.tipo_actividad = [];
                break;
            case "solicitante":
                state.error.solicitante = [];
                break;
            default:
                break;
        }
    },
    DELETE(state, id) {
        state.listado = state.listado.filter((item) => item.id !== id);
    },
    DELETED(state, value) {
        state.deleted = value;
    },
    DELETING(state, value) {
        state.deleting = value;
    },
    CREADO_ID(state, value) {
        state.creado_id = value;
    },
    EDITADO_ID(state, value) {
        state.creado_id = value;
    }
}
// your root getters
export const getters = {
    total(state) { return state.listado.length }
}