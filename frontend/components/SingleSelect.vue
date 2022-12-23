<template>
    <div class="mb-1">
		<label v-if="label.length > 0" class="form-label">{{ label }}</label>
		<div
			ref="content"
            class="selectDropDown"
			:class="{ focusSelect: mostrar ,  invalidSelect: !valid}"
			
		>
			<button
				class="btnSelect"
				@click="mostrarContenido"
			>
				<span class="selectPlaceholder">{{ btnText }}</span>
				<span class="selectArrow">
					<i
						v-if="!valid && !mostrar"
						class="invalidSelect"
					></i>

					<i
                        class="fa-solid fa-caret-down"
						:class="{ rotateArrow: mostrar }"
					></i>
				</span>
			</button>
			<div
				v-if="options.length > 0"
                class="selectContent"
				:class="{show: mostrar}"
			>
				<div class="w-100 p-2">
					<input
						type="text"
						class="form-control"
						placeholder="Filtrar Opciones"
                        :value="filtro"
						@input="filterOptions($event.target.value)"
						autocomplete="off"
					/>
				</div>
				<div class="optionsContainer">
					<div
						v-for="(option, i) in options_data"
						class="selectOption"
						:data-label="option.label"
						@click="markSelected(option)"
					>
						<span class="spanSelectOption">{{ option.label }}</span>
						<span class="spanSelectIcon"
							><i class="fa fa-check"></i
						></span>
					</div>
				</div>
			</div>
			<div v-else :class="['selectContent', { show: mostrar }]">
				<div class="selectOption" data-label="">
					<span class="spanSelectOption">No hay opciones</span>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
export default {
    name:'SingleSelect',
    props:{
        label: {
			type: String,
			default: "",
			required: false,
		},
		placeholder: {
			type: String,
			default: "Seleccionar",
			required: false,
		},
		value: {
			type: Object,
			default: null,
			required: true,
		},
		options: {
			type: Array,
			default: [],
			required: true,
		},
        valid:{
            type:Boolean,
            default:true,
            required:false
        }
    },
    computed: {
        optionSelected(){
            return this.value
        },
        options_data(){
            if(this.filtro !== ""){
                return this.options.filter(element => element.label.toLowerCase().includes(this.filtro))
            }
            return this.options
        },
        btnText(){
            if(!!this.value.label){
                return this.value.label
            }
            return this.placeholder
        },
        mostrado(){
            return this.mostrar
        }
    },
    watch: {
        mostrado(newValue){
            if(!newValue){
                this.filtro = ""
            }
        }
    },
    data() {
        return {
            mostrar: false,
            filtro:"",
        }
    },
    methods:{
        outsideToggleSelect(){
            if(this.mostrar){
                this.mostrar = false;
            }
        },
        filterOptions(value){
            this.filtro = value
        },
        markSelected(element){
            this.$emit("input",element)
            this.mostrar = !this.mostrar
        },
        mostrarContenido(){
            this.mostrar = !this.mostrar
        }
    },
    mounted() {
        
    },
}
</script>
<style>
.btnSelect:hover:focus {
    border-color: #1b89f7;
}
i.validSelect {
    color: #66d432;
    margin-right: 5px;
}
i.invalidSelect {
    color: #fd5c70;
    margin-right: 5px;
}
.feedbackSelect {
    width: 100%;
    margin-top: 0.25rem;
    font-size: 0.875em;
    text-align: left;
}
.feedbackSelect.invalidSelect {
    color: #fd5c70;
}
.feedbackSelect.validSelect {
    color: #66d432;
}
.selectDropDown.validSelect .btnSelect {
    border-color: #66d432;
}
.selectDropDown.invalidSelect .btnSelect {
    border-color: #fd5c70;
}
.selectDropDown.focusSelect .btnSelect {
    border-radius: 0.375rem 0.375rem 0 0;
    border-color: #1b89f7;
}
.selectDropDown.focusSelect .selectContent {
    border-radius: 0 0 0.375rem 0.375rem;
    border-top: 0px;
    border-left: 2px solid #1b89f7;
    border-right: 2px solid #1b89f7;
    border-bottom: 2px solid #1b89f7;
    color: #495057;
}
.btnSelect {
    width: 100%;
    padding: 0.6875rem 0.75rem;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1rem;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 2px solid #dde0e5;
    border-top-color: rgb(221, 224, 229);
    border-right-color: rgb(221, 224, 229);
    border-bottom-color: rgb(221, 224, 229);
    border-left-color: rgb(221, 224, 229);
    border-left-width: 2px;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border-radius: 0.375rem;
    transition: box-shadow 0.15s ease,
        border-color 0.2s cubic-bezier(0.655, 0.055, 0.345, 1);
}

.selectDropDown {
    position: relative;
    display: inline-block;
    width: 100%;
}
.selectDropDown .btnSelect {
    text-align: left;
    -ms-box-orient: horizontal;
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -moz-flex;
    display: -webkit-flex;
    display: flex;

    -webkit-justify-content: space-between;
    justify-content: space-between;
    -webkit-flex-flow: row wrap;
    flex-flow: row wrap;
    -webkit-align-items: stretch;
    align-items: stretch;
}

.selectContent {
    max-height: 0;
    position: absolute;
    overflow: hidden;
    background-color: #fff;
    width: 100%;
    overflow: auto;
    box-shadow: 0 20px 27px 0 rgba(0, 0, 0, 0.05);
    z-index: 1;
    transition: max-height 0s cubic-bezier(0.655, 0.055, 0.345, 1);
}
.optionsContainer {
    width: 100%;
    max-height: 180px;
    overflow-y: auto;
}
.selectContent.show {
    max-height: 180px;
    overflow: hidden !important;
    transition: max-height 0.3s cubic-bezier(0.655, 0.055, 0.345, 1);
}
.selectContent .selectOption {
    color: #495057;
    padding: 9px 10px;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1rem;
    cursor: pointer;
    text-decoration: none;
    width: 100%;
    text-align: left;
    -ms-box-orient: horizontal;
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -moz-flex;
    display: -webkit-flex;
    display: flex;
    -webkit-justify-content: space-between;
    justify-content: space-between;
    -webkit-flex-flow: row wrap;
    flex-flow: row wrap;
    -webkit-align-items: stretch;
    align-items: stretch;
}
.selectContent .selectOption:hover {
    background-color: #1b89f7;
    color: white;
}
.selectContent .selectOption:hover .spanSelectIcon {
    display: inline-block !important;
}
.spanSelectIcon {
    display: none;
}
.selectPlaceholder {
    display: inline-block;
    overflow: hidden;
    text-overflow: ellipsis;
    width: calc(100% - 40px);
    height: 1.1rem;
}
.spanSelectOption {
    display: inline-block;
    overflow: hidden;
    text-overflow: ellipsis;
    width: calc(100% - 20px);
    height: 1.1rem;
}
.selectOption.hide {
    display: none;
}
.selectOption.selected {
    font-weight: bold;
}
.selectOption.selected .spanSelectIcon {
    display: inline-block !important;
    font-weight: bold;
}
.rotateArrow {
    transform: rotate(180deg);
}

.selectContent a:hover {
    background-color: #ddd;
}
input.form-control{
    border: 2px solid #d2d6da;
    padding: 5px;
}
input.form-control:focus{
    border: 2px solid #1b89f7;
}
input.form-control:hover{
    border: 2px solid #1b89f7;
}
</style>