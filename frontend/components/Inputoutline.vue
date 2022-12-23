<template>
    <div>
        <div class="input-group input-group-outline my-3 mb-0"
             v-bind:class="{ 'focused': focus, 'is-focused':focus, 'is-filled':filled || haserror, 'has-danger':haserror}">
            <label class="form-label">{{ label }}</label>
            <input v-if="type==='number'"
                   :value="Number(value)"
                   @keyup="fillme($event.target.value)"
                   @focus="focusme()"
                   @blur="defocusme()"
                   :type="type" class="form-control"
                   :name="name"
                   step="any"
                   @input="updateValue($event.target.value)">
            <input v-else
                   :value="value"
                   @keyup="fillme($event.target.value)"
                   @focus="focusme()"
                   @blur="defocusme()"
                   :type="type" class="form-control"
                   :name="name"
                   @input="updateValue($event.target.value)">

        </div>
        <div class="icon-container">
            <span v-if="haserror" class="form-control-feedback text-primary"><i
                class="fa-solid fa-delete-left"></i></span>
        </div>
        <div class="error">{{ error }}</div>
    </div>
</template>
<style>
.input-group.input-group-outline.is-focused .form-label + .form-control, .input-group.input-group-outline.is-filled .form-label + .form-control {
    box-shadow: inset 1px -1px #1A73E8, inset -1px -1px #1A73E8, inset 0 -1px #1A73E8 !important;
}

.icon-container span {
    position: absolute;
    right: 5px;
}

.icon-container {
    position: relative;
    z-index: 3000;
    top: -32px;
    width: 100%;
    justify-content: flex-end;
}

input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
    transition: background-color 500000s;
}

.error {
    font-size: 12px;
    color: #1A73E8;
    padding-left: 13px;
}
</style>

<script>
export default {
    props: {
        value: {
            type: String,
            required: true,
        },
        label: {
            type: String,
            required: true,
        },
        type: {
            type: String,
            required: true,
        },
        error: {
            type: String,
            required: true,
        },
    },
    computed: {
        name() {
            return this.label.toLowerCase();
        },
        haserror() {
            return this.error !== '';

        },
        value_atr() {
            return this.value;
        }
    },
    created() {
        if (this.value.length > 0) {
            this.filled = true;
        }
        if (this.type === 'number') {
            if (this.value > 0 || this.value < 0) {
                this.filled = true;
            }
        }
    },
    data() {
        return {
            focus: false,
            filled: false,
            default_seting: false,
        }
    },
    watch: {
        value_atr(newValue, oldValue) {
            if (newValue !== oldValue) {
                this.filled = newValue !== '';
            }
        }
    },
    methods: {
        focusme: function () {
            this.focus = true;
        },
        defocusme: function () {
            this.focus = false;
        },
        fillme: function (value) {
            this.filled = value !== "";
            this.$emit("error-solved")
        },
        updateValue(value) {
            this.$emit("input", value)
            this.$emit("error-solved")
        }
    },
}
</script>
