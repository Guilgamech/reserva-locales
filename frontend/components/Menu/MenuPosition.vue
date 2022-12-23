<template>
    <div :class="{'show':show}" class="modal modal-overlay" tabindex="-1" @click="ocultar()" @click.stop>
        <div :style="position">
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: "MenuPosition",
    props: {
        menuId: {
            type: String,
            required: true,
            default: ''
        },
        x: {
            type: String,
            required: true
        },
        y: {
            type: String,
            required: true
        }
    },
    computed: {
        position() {
            return `position:absolute; top:${this.y}px; left:${this.x}px;`
        },
        show() {
            const stateID = this.$store.state.ui.showMenuPositionId;
            return (this.menuId !== '' && this.menuId === stateID);
        },
    },
    methods: {
        ocultar() {
            this.$store.dispatch("ui/setShowMenuPositionId", '')
        }
    }
}
</script>

<style scoped>
.MenuPosition {

}
</style>
