<template>
  <div class="col-lg-4 col-md-8 col-12 mx-auto">
    <div class="card z-index-0 fadeIn3 fadeInBottom">
      <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
          <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">Autenticarse en el Sistema</h4>                  
        </div>
      </div>
      <div class="card-body">
        <h6 class="mb-4 text-center">
          Introduce las Credenciales de Acceso
        </h6>
        <form role="form" class="text-start" @submit.prevent="submit">
          <inputoutline :error="err_username" label="Usuario" type="text" v-model="username"/>
          <inputoutline :error="err_password" label="Contraseña" type="password" v-model="password"/>
          <div class="text-center mt-3">
            <button type="submit" class="btn bg-gradient-info w-100 my-4 mb-2">Autenticarse</button>
          </div>
          
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import swal from 'sweetalert';
import SingleSelect from './SingleSelect';
export default {
  name:'Login',
  components:{},
  data() {
    return {
      username:'',
      err_username:'',
      err_password:'',
      password:'',
    }
  },
  watch:{
    username(newValue, oldValue){
      if (newValue !== oldValue){
        this.err_username = ''
      }
    },
    password(newValue, oldValue){
      if (newValue !== oldValue){
        this.err_password = ''
      }
    }  
  },
  methods:{    
    async submit () {
      const req = {'username':this.username, 'password':this.password}
      if(this.username == '')
        this.err_username = 'Por favor complete este campo';
      else if(this.password == ''){
        this.err_password = 'Por favor complete este campo';
      }
      else{        
        try{
          const response = await this.$auth.loginWith('local', {data: req})
            .then( () => {
              const fullname = ''+this.$auth.user.first_name + ' '+ this.$auth.user.last_name;
              swal({
                title: fullname,
                text: "Bienvenido a SGRL",
                icon: "success",
                button: "Continuar",
              }).then( () => {
                this.$router.push("/sistema")
              })
            })
        } catch (e) {          
          swal({
            title: "Fallo de Autenticación!",
            text: "Rectifique las credenciales",
            icon: "error",
            button: "Continuar",
          });
        }          
      }            
    },    
  }
}
</script>
