export const state = () => ({
    showModalId:'',
    showMenuPositionId:'',
})

export const actions = {
    setShowModalId({ commit }, value) {
        commit('SETMODALID', value);
    },
    setShowMenuPositionId({ commit }, value) {
        commit('SETMENUPOSITIONID', value);
    },
}
export const mutations = {
    SETMODALID(state, value){
        state.showModalId = value
    },
    SETMENUPOSITIONID(state, value){
        state.showMenuPositionId = value
    }
}
// your root getters
export const getters = {}
