export const state = () => ({
    autorizado: false,
    
})

export const actions = {
    autorizado({ commit }, value) {
        commit('AUTORIZADO', value);
    },
    
}

export const mutations = {
    AUTORIZADO(state, value) { 
        state.autorizado = value;
    },
    
}

export const getters = {
    
}