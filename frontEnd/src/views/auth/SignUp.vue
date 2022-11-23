<template>
    <div class="row" style="margin-top: 40px;">
        <div class="col-md-4 offset-md-4">
            <p class="text-end" style="font-size:0.95em">Já possui cadastro? <router-link class="text-green" :to="{ name: 'LogIn' }">Entrar</router-link></p>
            <FormCreateUserVue></FormCreateUserVue>
        </div>
    </div>
</template>

<script>
import FormCreateUserVue from '@/components/forms/FormCreateUser.vue';

export default {
    name: 'SignUp',
    components: {
        FormCreateUserVue
    },
    mounted() {
        if(this.$store.state.authUser.accessToken) (
            this.$router.push({name: 'HomeApp'})
        )
    }
}
</script>