<template>
    <div :class="{'show':show}" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div class="vertical-center">
            <div :class="sizeClass" @click.stop>
                <div class="card z-index-0 fadeIn3 fadeInBottom">
                    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                        <div class="bg-gradient-info shadow-info border-radius-lg py-3 pe-1">
                            <h4 class="text-white font-weight-bolder text-center mt-2 mb-0">{{ title }}</h4>
                            <p v-if="description!==''">{{description}}</p>
                        </div>
                    </div>
                    <div class="card-body">
                        <slot></slot>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Modal.vue",
    props: {
        size: {
            type: String,
            required: false,
            default: 'sm'
        },
        modalId: {
            type: String,
            required: true,
            default: ''
        },
        title: {
            type: String,
            required: true,
            default: 'Title Modal'
        },
        description: {
            type: String,
            required: false,
            default: ''
        },
        parentModalId:{
            type: String,
            required: false,
            default: ''
        }
    },
    computed: {
        show() {
            const stateID = this.$store.state.ui.showModalId;
            return (this.modalId !== '' && this.modalId === stateID);
        },
        sizeClass() {
            switch (this.size) {
                case "sm":
                    return "col-lg-3 col-md-4 col-10 mx-auto"
                case "md":
                    return "col-lg-5 col-md-6 col-10 mx-auto"
                case "lg":
                    return "col-lg-8 col-md-8 col-10 mx-auto"
                default:
                    throw new Error("Size can be only (sm, md, lg)")
            }
        }
    },
    data() {
        return{
            datos:''
        }
    },
    methods: {
        ocultar() {
            this.$store.dispatch("ui/setShowModalId", this.parentModalId)
        }
    }
}
</script>

<style scoped>

</style>
