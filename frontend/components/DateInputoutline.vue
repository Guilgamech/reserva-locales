<template>
    <div>
        <div class="input-group input-group-outline my-3 mb-0"
             v-bind:class="{ 'focused': focus, 'is-focused':focus, 'is-filled':value.length>0 || haserror, 'has-danger':haserror}">
            <label class="form-label">{{ label }}</label>
            <input
                ref="idate"
                :value="value"
                @focus="focusme()"
                @blur="defocusme()"
                type="date" class="form-control"
                @input="updateValue($event.target.value)">
        </div>
        <div class="error">{{ error }}</div>
    </div>
</template>
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
        error: {
            type: String,
            required: true,
        },
        placeholder: {
            type: String,
            required: false
        }
    },
    computed: {
        haserror() {
            return this.error !== '';

        }
    },
    data() {
        return {
            focus: false,
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
            this.$emit("input", value)
            this.$emit("error-solved")
        }
    }
}
</script>
