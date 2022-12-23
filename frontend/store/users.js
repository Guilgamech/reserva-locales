
export const state = () => ({
    listado: [],
    error:""

})

// contains your actions
export const actions = {
    async listado({ commit }) {
        await this.$axios.$get('/users/')
            .then((response) => {
                commit('setListado', response)
            })
            .catch(error =>{
                if(!!error.response){
                    commit('setError', 'No estás Autorizado');
                }else{
                    commit('setError', 'No hay conexión con la API');
                }
            })
    },
    setError({ commit }, value) {
        commit('setError', value);
    }
}
// contains your mutations
export const mutations = {
    setListado(state, response){
        state.listado = response;
    }, 
    setError(state, value){
        state.error = value;
    }
}
// your root getters
export const getters = {
    total(state){ return state.listado.length}
}