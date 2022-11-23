<template>
    <div class="row" style="margin-top: 40px;">
        <div class="col-md-4 offset-md-4">
            <FormPasswordChange></FormPasswordChange>
        </div>
    </div>
</template>

<script>

import FormPasswordChange from '@/components/forms/FormPasswordChange.vue'

export default {
    name: 'PasswordChange',
    components: {
        FormPasswordChange
    },
    mounted() {
        if(this.$store.state.authUser.accessToken) (
            this.$router.push({name: 'HomeApp'})
        )
    }
}
</script>