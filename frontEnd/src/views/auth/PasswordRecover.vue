<template>
    <div class="row" style="margin-top: 40px;">
        <div class="col-md-4 offset-md-4">
            <FormPasswordRecover></FormPasswordRecover>
        </div>
    </div>
</template>

<script>

import FormPasswordRecover from '@/components/forms/FormPasswordRecover.vue'

export default {
    name: 'PasswordRecover',
    components: {
        FormPasswordRecover
    },
    mounted() {
        if(this.$store.state.authUser.accessToken) (
            this.$router.push({name: 'HomeApp'})
        )
    }
}
</script>