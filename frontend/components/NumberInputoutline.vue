<template>
    <div>
        <div class="input-group input-group-outline my-3 mb-0"
             v-bind:class="{ 'focused': focus, 'is-focused':focus, 'is-filled':!!value || haserror, 'has-danger':haserror}">
            <label class="form-label">{{ label }}</label>
            <input type="number"
                   :value="Number(value)"
                   @focus="focusme()"
                   @blur="defocusme()"
                   class="form-control"
                   step="any"
                   @input="updateValue($event.target.value)">

        </div>
        <div class="error">{{ error }}</div>
    </div>
</template>
<script>
export default {
    props: {
        value: {
            type: Number,
            required: true,
        },
        label: {
            type: String,
            required: true,
        },
        error: {
            type: String,
            required: true,
        },
    },
    computed: {
        haserror() {
            return this.error !== '';

        },
    },
    data() {
        return {
            focus: false,
            filled: false,
            default_seting: false,
        }
    },
    methods: {
        focusme: function () {
            this.focus = true;
        },
        defocusme: function () {
            this.focus = false;
        },
        updateValue(value) {
            this.$emit("input", Number(value))
            this.$emit("error-solved")
        }
    },
}
</script>
