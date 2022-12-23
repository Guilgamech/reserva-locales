<template>
    <div class="container-fluid py-4">
        <div class="row mt-4 mb-4">
            <div class="col-xl-3 col-sm-6 mb-xl-0 mb-4">
                <div class="card">
                    <div class="card-header p-3 pt-2">
                        <div
                            class="icon icon-lg icon-shape bg-gradient-primary shadow-primary text-center border-radius-xl mt-n4 position-absolute">
                            <i class="fa fa-user"></i>
                        </div>
                        <div class="text-end pt-1">
                            <p class="text-sm mb-0 text-capitalize">Usuarios Activos</p>
                            <h4 class="mb-0"> {{abbreviateNumber(total_users)}} </h4>
                        </div>
                    </div>
                    <hr class="dark horizontal my-0">
                    <div class="card-footer p-3">
                        <!-- <p class="mb-0"><span class="text-success text-sm font-weight-bolder">+3% </span>than last month
                        </p> -->
                    </div>
                </div>
            </div>
            <div class="col-xl-3 col-sm-6 mb-xl-0 mb-4">
                <div class="card">
                    <div class="card-header p-3 pt-2">
                        <div
                            class="icon icon-lg icon-shape bg-gradient-info shadow-info text-center border-radius-xl mt-n4 position-absolute">
                            <i class="fa fa-building"></i>
                        </div>
                        <div class="text-end pt-1">
                            <p class="text-sm mb-0 text-capitalize">Locales</p>
                            <h4 class="mb-0"> {{abbreviateNumber(total_local)}} </h4>
                        </div>
                    </div>
                    <hr class="dark horizontal my-0">
                    <div class="card-footer p-3">
                        <!-- <p class="mb-0"><span class="text-success text-sm font-weight-bolder">+3% </span>than last month
                        </p> -->
                    </div>
                </div>
            </div>
            <div class="col-xl-3 col-sm-6 mb-xl-0 mb-4">
                <div class="card">
                    <div class="card-header p-3 pt-2">
                        <div
                            class="icon icon-lg icon-shape bg-gradient-success shadow-success text-center border-radius-xl mt-n4 position-absolute">
                            <i class="fa fa-box-archive"></i>
                        </div>
                        <div class="text-end pt-1">
                            <p class="text-sm mb-0 text-capitalize">Aseguramientos</p>
                            <h4 class="mb-0"> {{abbreviateNumber(total_aseguramiento)}} </h4>
                        </div>
                    </div>
                    <hr class="dark horizontal my-0">
                    <div class="card-footer p-3">
                        <!-- <p class="mb-0"><span class="text-success text-sm font-weight-bolder">+3% </span>than last month
                        </p> -->
                    </div>
                </div>
            </div>
            <div class="col-xl-3 col-sm-6 mb-xl-0 mb-4">
                <div class="card">
                    <div class="card-header p-3 pt-2">
                        <div
                            class="icon icon-lg icon-shape bg-gradient-warning shadow-warning text-center border-radius-xl mt-n4 position-absolute">
                            <i class="fa fa-screwdriver-wrench"></i>
                        </div>
                        <div class="text-end pt-1">
                            <p class="text-sm mb-0 text-capitalize">Medios</p>
                            <h4 class="mb-0"> {{abbreviateNumber(total_medio)}} </h4>
                        </div>
                    </div>
                    <hr class="dark horizontal my-0">
                    <div class="card-footer p-3">
                        <!-- <p class="mb-0"><span class="text-success text-sm font-weight-bolder">+3% </span>than last month
                        </p> -->
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col-lg-12 mt-4 mb-3">
                <div class="card z-index-2 ">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                        <div class="bg-gradient-dark shadow-dark border-radius-lg py-3 pe-1">
                            <div class="chart">
                                <canvas id="chart-line-tasks" class="chart-canvas" height="212" width="450"
                                    style="display: block; box-sizing: border-box; height: 170px; width: 360.7px;"></canvas>
                            </div>
                        </div>
                    </div>
                    <div class="card-body">
                        <h6 class="mb-0 ">Reservaciones</h6>
                        <p class="text-sm ">Por Meses</p>
                        <hr class="dark horizontal">
                        <div class="d-flex ">
                            <i class="fa fa-clock text-sm my-auto me-1"></i>
                            <p class="mb-0 text-sm">Actualizado</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.chart {
    width: 100% !important;
}

.icon-lg.custom i {
    top: 12px !important
}
</style>

<script>
import AreaChart from "~/components/Charts/AreaChart.vue";
export default {
    name: 'Sistema',
    middleware: 'login',
    components: { AreaChart },
    computed: {
        total_users(){
            return this.$store.getters['users/total'];
        },
        total_local(){
            return this.$store.getters['local/total'];
        },
        total_medio(){
            return this.$store.getters['medio/total'];
        },
        total_aseguramiento(){
            return this.$store.getters['aseguramiento/total'];
        },
    },
    mounted() {
        this.$store.dispatch('local/listado')
        this.$store.dispatch('aseguramiento/listado')
        this.$store.dispatch('medio/listado')
        this.$store.dispatch('users/listado')
    },
    methods: {
        abbreviateNumber(number) {
            var SI_SYMBOL = ["", "k", "M", "G", "T", "P", "E"];
            // what tier? (determines SI symbol)
            var tier = Math.log10(Math.abs(number)) / 3 | 0;

            // if zero, we don't need a suffix
            if (tier == 0) return number;

            // get suffix and determine scale
            var suffix = SI_SYMBOL[tier];
            var scale = Math.pow(10, tier * 3);

            // scale the number
            var scaled = number / scale;

            // format number and add suffix
            return scaled.toFixed(1) + suffix;
        },

    },
}
</script>
