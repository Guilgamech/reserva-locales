<template>
    <div class="txtarea-container custom-error-select">
        <label v-if="has_label" class="form-label">{{label}}</label>
        <select
            v-model="value"
            @change="fillme($event.target.value)" 
            @focus="focusme()" 
            @blur="defocusme()" 
            @input="updateValue($event.target.value)" 
            :class="{'filled': filled, 'focused': focus, 'is-filled':filled || haserror, 'has-danger':haserror }" 
            class="custom-select">
            <option v-if="has_default" value="">{{default_option}}</option>
            <option v-for="(item, index) in options" v-bind:key="index" :value="item.value">{{capitalize(item.label)}}</option>
        </select>
        <div class="icon-container">
            <span v-if="haserror" class="form-control-feedback text-primary"><i class="fa-solid fa-delete-left"></i></span>
        </div>
        <div class="error">{{error}}</div>
    </div>
    

</template>
<style>
    .custom-select.filled {
        border-color: #1A73E8;
        outline: none;
    }

    .custom-select.focused {
        border-color: #1A73E8;  
        outline: none;
    }
    .custom-select.has-danger{
        border-color: #1A73E8;  
        outline: none;
    }

    .input-group.input-group-outline.is-focused .form-label + .form-control, .input-group.input-group-outline.is-filled .form-label + .form-control{        
        box-shadow: inset 1px -1px #1A73E8, inset -1px -1px #1A73E8, inset 0 -1px #1A73E8!important;
    }
    .custom-error-select .icon-container span{
        position: absolute;
        right: 20px;
    }
    .icon-container{
        position: relative;    
        z-index: 3000;
        top: -32px;
        width: 100%;
        justify-content: flex-end;
    }
    input:-webkit-autofill,
    input:-webkit-autofill:hover, 
    input:-webkit-autofill:focus, 
    input:-webkit-autofill:active{
        transition: background-color 500000s;  
    }
    .error{    
        font-size: 12px;
        color: #e53371;
        padding-left: 13px;
    }
</style>

<script>
export default {
    name:'Selectoutline',
    props:{
        set_value:{
            type:Object,
            required:false
            //{value:(valor, porque puede ser int double or string or object)}
        },
        label:{
            type: String,
            required: false,
        },
        default_option:{
            type: String,
            required: false,
        },
        options: {
            type: Array,
            required: true,
        },
        error:{
            type:String,
            required:true,
        }       
    },    
    computed: {
        name() {
            return this.label.toLowerCase();
        },
        haserror(){            
            if(this.error !=''){
                return true;                
            }
            return false;
        },
        has_default(){
            if(typeof(this.default_option) !== "undefined"){
                return true;
            }
            return false;
        },
        has_label(){
            if(typeof(this.label) !== "undefined"){
                return true;
            }
            return false;
        }
    },
    created() {
        if(typeof(this.set_value) !== "undefined"){
            if(typeof this.set_value === 'object' && this.set_value !== null  && !this.default_seting){
                this.value = this.set_value.value;
                this.$emit("input",this.value)
                this.default_seting = true;
                this.filled = true;
            }
        }
    },
    data(){
        return{
            focus:false,
            filled:false,
            default_seting:false,
            value:""
        }
    },    
    methods:{
        focusme: function () {
            this.focus=true;
        },
        defocusme: function () {
            this.focus=false;
        },
        fillme: function(value) {
            if(value != "")
                this.filled = true;
            else
                this.filled = false;     
            this.$emit("error-solved")
        },
        updateValue(value){
            this.$emit("input",value)
            this.$emit("error-solved")
        },
        capitalize(value){
            if(typeof(value) === "undefined")
            {
                return value;
            }
            
            return value.replace(/(?:^|\s|-)\S/g, x => x.toUpperCase());
        },
    }, 
}
</script>