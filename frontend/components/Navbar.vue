<template>
<nav class="navbar navbar-main navbar-expand-lg px-0 mx-4 shadow-none border-radius-xl position-sticky blur shadow-blur left-auto top-3 z-index-sticky" id="navbarBlur" navbar-scroll="true">
    <div class="container-fluid py-1 px-3">
        <nav aria-label="breadcrumb">
            <li class="nav-item ps-3 d-block align-items-center me-2">
                    <p class="mb-0">Bienvenido</p>
                    <h6 class="font-weight-bolder mb-0 text-capitalize"><i class="fa fa-user-tie me-1 fs-20"></i>{{fullname}}</h6>
            </li>
        </nav>
        <div class="collapse navbar-collapse mt-sm-0 mt-2 me-md-0 me-sm-4" id="navbar">
            <div class="ms-md-auto pe-md-3 d-flex align-items-center">                
            </div>
            <ul class="navbar-nav  justify-content-end">
                
                
                <li class="nav-item d-xl-none pe-3 d-flex align-items-center">
                <a @click="toggleSidenav()" class="nav-link text-body p-0" id="iconNavbarSidenav">
                    <div class="sidenav-toggler-inner">
                    <i class="sidenav-toggler-line"></i>
                    <i class="sidenav-toggler-line"></i>
                    <i class="sidenav-toggler-line"></i>
                    </div>
                </a>
                </li>
                <li class="nav-item d-flex align-items-center">
                    <a @click="logout()" class="nav-link cursor-pointer">
                        <i class="fa-solid fa-power-off font-weight-bolder fs-30"></i>
                    </a>
                </li>
            </ul>
        </div>
    </div>
</nav>
        <!-- End Navbar -->
    
</template>

<style>
.fs-30{
    font-size: 30px!important;
}
.fs-40{
    font-size: 40px!important;
}
.fs-35{
    font-size: 35px!important;
}
.sidenav{
    z-index: 1040!important;
}
</style>

<script>
export default {
    computed: {        
        fullname(){
            if(this.$auth.loggedIn){
                const fullname = ''+this.$auth.user.first_name+' '+this.$auth.user.last_name;
                return fullname;
            }
            return '';
        }
    },
    methods:{
        toggleSidenav: ()=> {            
            const iconSidenav = document.getElementById('iconSidenav');
            const sidenav = document.getElementById('sidenav-main');
            let body = document.getElementsByTagName('body')[0];
            let className = 'g-sidenav-pinned';
            if (body.classList.contains(className)) {
                body.classList.remove(className);
                setTimeout(function() {
                sidenav.classList.remove('bg-white');
                }, 100);
                sidenav.classList.remove('bg-transparent');

            } else {
                body.classList.add(className);
                sidenav.classList.add('bg-white');
                sidenav.classList.remove('bg-transparent');
                iconSidenav.classList.remove('d-none');
            }
        },
        async logout(){
            const refresh = this.$auth.strategy.refreshToken.get();
            const data = { 'refresh': refresh }
            try {
                swal({
                    title: "Salir del Sistema",
                    text: "Gracias por Trabajar con nosotros",
                    icon: "success",
                    button: "Continuar",
                }).then( async () => {
                        const response = await this.$auth.logout({data:data})
                    })
            } catch (e) {
                console.log(e);
            }
        }
    }
}
</script>