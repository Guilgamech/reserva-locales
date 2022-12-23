<template>    
    <nuxt-link :to="link" :id="'link'+item_id" class="nav-link text-white">
        <div class="text-white text-center me-2 d-flex align-items-center justify-content-center">
            <i :class="icon" class="fa opacity-10 fs-20"></i>
        </div>
        <span class="nav-link-text ms-1">{{labelitem}}</span>
    </nuxt-link>
</template>

<script>

export default {
    name:'DropDownItemMenu',
    props:{
        labelitem: {
            type: String,
            required: true,
        },
        icon: {
            type: String,
            required: true,
        },
        link:{
            type: String,
            required: true,
        }
    },
    computed:{
        item_id(){
            let text = this.link;
            let result = text.toLowerCase().split("/").join("")
            return result;
        }
    },    
    methods: {
        onClassChange(classAttrValue) {
            const classList = classAttrValue.split(' ');
            if (classList.includes('nuxt-link-exact-active')) {
                this.$emit('input', true);
            }
            else{
                this.$emit('input', false);
            }            
        }
    },
    mounted() {
        this.observer = new MutationObserver(mutations => {
            for (const m of mutations) {
                const newValue = m.target.getAttribute(m.attributeName);
                this.$nextTick(() => {
                    this.onClassChange(newValue, m.oldValue);
                });
            }
        });
        const elemento = document.querySelectorAll("#link"+this.item_id)[0];
        this.observer.observe(elemento, {
            attributes: true,
            attributeOldValue : true,
            attributeFilter: ['class'],
        });
        this.onClassChange(elemento.getAttribute('class'));
    }
}
</script>