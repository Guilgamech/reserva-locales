<template>
  <div v-if="this.$auth.loggedIn" class="row">
    <div class="col-12">
      <NuxtChild  />
    </div>
  </div> 
</template>

<script>
export default {
    name: 'SistemaTemplate',
    layout: 'dashboard',
    middleware: 'login',
}
</script>

