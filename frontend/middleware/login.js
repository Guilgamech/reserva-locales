import swal from 'sweetalert';
export default function ({ store, redirect }) {
   
    if (!store.state.auth.loggedIn) {
        
        store.commit('AUTORIZADO', false);
        return redirect('/')
    }
}