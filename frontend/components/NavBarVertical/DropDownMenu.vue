<template>
    <li v-click-outside="closeEvent" class="nav-item">
        <a @click="colapsar()" :class="{'activate':active, 'collapsed': collapsed, 'exact-active': exact_computed}"  :data-bs-target="'#'+item_id" :aria-expanded="showDropDown" data-bs-toggle="collapse" class="nav-link text-white"  role="button">
            <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
                <i :class="icon" class="fa opacity-10 fs-20"></i>
            </div>
            <span class="nav-link-text ms-1">{{label}}</span>
        </a>
        <div :class="{ 'show': showDropDown }" class="collapse" :id="item_id">
            <ul class="nav ">
                <li v-for="(item, index) in links" v-bind:key="index" class="nav-item">
                    <DropDownItemMenu v-model="item.active" :labelitem='item.label' :link='item.link' :icon='item.icon' />
                </li>
            </ul>
        </div>
    </li>
</template>

<style scoped>

li.nav-item:hover a.activate, .nav-link.exact-active{
    background-color: hsla(0,0%,78%,.2);    
    box-shadow: 0 4px 6px -1px rgb(0 0 0 / 10%), 0 2px 4px -1px rgb(0 0 0 / 6%);
    border-radius: 0.375rem;
    
}

.navbar-vertical .navbar-nav .nav-link[data-bs-toggle=collapse][aria-expanded=true]:after {    
    transform: rotate(180deg);
}
.collapse.show{
    animation: fadeIn 0.50s ease-in both;
}
@keyframes fadeIn {
	from {
		opacity: 0;
		/*transform: translate3d(0, -20%, 0);*/
	}
	to {
		opacity: 1;
		/*transform: translate3d(0, 0, 0);*/
	}
}
</style>

<script>
import DropDownItemMenu from './DropDownItemMenu.vue'
import vClickOutside from 'v-click-outside'
export default {
    name:'DropDownMenu',
    directives: {
      clickOutside: vClickOutside.directive
    },
    components: { DropDownItemMenu }, 
    props:{    
        label: {
            type: String,
            required: true,
        },
        icon: {
            type: String,
            required: true,
        },
        enlaces:{
            type: Array,
            required: true,
            //{ label : { link:'enlace', icon:'icon'}}
        }
    },
    
    methods: {        
        trim_id(label){
            let text = label;
            let result = text.toLowerCase().split(" ").join("")            
            return result;
        },
        colapsar(){
            this.collapsed = !this.collapsed;
            if(!this.active){
                this.active = !this.active;
            }
        },
        closeEvent(event) {
            if(!this.exact_computed){
                this.active = false;
                this.collapsed = true;
            }
        }
    },
    data(){
        return {
            active:false,
            collapsed: true,            
            links: this.enlaces
        }
    },
    computed:{
        showDropDown() {
            if(this.active && this.collapsed){
                return false;
            }
            if(this.active && !this.collapsed){
                return true;
            }
            if(!this.active && this.collapsed && this.exact_computed)
            {
                return true;
            }
            return false;
            
                        
        },
        exact_computed(){            
            var found = false;
            this.links.forEach(element => {
                if(element.active){
                    found = true;
                }
            });
            return found;
        },
        item_id(){
            let text = this.label;
            let result = text.toLowerCase().split(" ").join("")            
            return result;
        }
    }
}
</script>