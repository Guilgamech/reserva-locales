import swal from 'sweetalert';
export default function ({ store, redirect }) {
    
    if(store.state.auth.loggedIn){
        if (store.state.auth.user.rol === "Solicitante" ) {
            store.commit('AUTORIZADO', true);
        }
        else {
            store.commit('AUTORIZADO', false);
            return redirect('/sistema/401')
        }
    }
    else {
        store.commit('AUTORIZADO', false);
        return redirect('/')
    }
    
}