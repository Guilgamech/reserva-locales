<template>
    <div class="txtarea-container">
        <textarea
            v-model="value"      
            :placeholder="placeholder"
            @keyup="fillme($event.target.value)"
            @focus="focusme()" @blur="defocusme()"
            @input="updateValue($event.target.value)"
            :class="{'filled': filled, 'focused': focus, 'is-filled':filled || haserror, 'has-danger':haserror }"
            class="txtarea-control outline-textarea" rows="4"></textarea>
        <div class="icon-container">
            <span v-if="haserror" class="form-control-feedback text-primary"><i class="fa-solid fa-delete-left"></i></span>
        </div>
        <div class="error">{{error}}</div>
    </div>
</template>
<style>
    .txtarea-container textarea.filled {
        border-color: #1A73E8;
        outline: none;
    }

    .txtarea-container textarea.focused {
        border-color: #1A73E8;  
        outline: none;
    }
    .txtarea-container textarea.has-danger{
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
    name:'Textareaoutline',
    props:{
        set_value:{
            type: String,
            required:false
        },
        label:{
            type: String,
            required: false,
        },
        placeholder:{
            type: String,
            required: true,
        },
        error:{
            type:String,
            required:true,
        }       
    },    
    computed: {
        haserror(){            
            if(this.error !=''){
                return true;                
            }
            return false;
        },
        value_atr(){
            return this.$attrs.value;
        }
    },
    created() {
        if(typeof(this.set_value) !== "undefined"){
            if(this.set_value != "" && !this.default_seting){
                this.value = this.set_value;
                this.$emit("input",this.value)
                this.default_seting = true;
                this.filled = true;
            }
        }
        if(this.value_atr.length>0){
            this.value = this.value_atr;
            this.filled = true;
        }
    },
    data(){
        return{
            focus:false,
            filled:false,
            default_seting:false,
            value:''
        }
    },
    watch:{
        value_atr(newValue){
            if(newValue != this.value)
            {
                this.value = newValue;
                if(newValue == ''){
                    this.filled = false;
                }
                else{
                    this.filled = true;
                }
            }
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
        }
    }, 
}
</script>