export const state = () => ({
    listado: [],
    edit: {
        id: '',
        cantidad: '',
        local: {},
        medio: {}
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
        cantidad: [],
        local: [],
        medio: [],
        non_field_errors: []

    },
    response_status: 0
})

export const actions = {
    async save({ commit }, rol) {
        commit('CREANDO', true);
        let has_error = false;
        const res = await this.$axios.$post('/local-medio/', rol).
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
        commit('SOLVED', "cantidad");
        commit('SOLVED', "local");
        commit('SOLVED', "medio");
        commit('SOLVED', "non_field_errors");


    },
    async patch({ commit }, { data }) {
        commit('EDITANDO', true);
        var has_error = false;
        let editdata = {
            medio_id: data.medio,
            cantidad: data.cantidad,
        }
        const response = await this.$axios.$put(`/local/${data.local}/modificar-medio/`, editdata).
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
        }
        commit('EDITANDO', false);
    },
    async delete({ commit }, data) {
        commit('DELETING', true);
        var has_error = false;
        let deletedata = {
            medio_id: data.medio_id,
        }
        const response = await this.$axios.$post(`/local/${data.local_id}/eliminar-medio/`, deletedata).
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
                case "cantidad":
                    state.error.cantidad = err[property];
                    break;
                case "local":
                    state.error.local = err[property];
                    break;
                case "medio":
                    state.error.medio = err[property];
                    break;
                case "non_field_errors":
                    state.error.medio = ["el medio ya existe en este local"];
                    break;

                default:
                    break;
            }
        }
    },
    SOLVED(state, property) {
        switch (property) {
            case "cantidad":
                state.error.cantidad = [];
                break;
            case "local":
                state.error.local = [];
                break;
            case "medio":
                state.error.medio = [];
                break;
            case "non_field_errors":
                state.error.non_field_errors = [];
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