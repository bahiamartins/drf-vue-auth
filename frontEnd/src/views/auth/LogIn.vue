<template>
    <div class="row" style="margin-top: 40px;">
        <div class="col-md-4 offset-md-4">
            <FormLogIn></FormLogIn>
        </div>
    </div>
</template>

<script>

import FormLogIn from '@/components/forms/FormLogIn.vue';

export default {
    name: 'LogIn',
    components: {
        FormLogIn
    },
    mounted() {
        if(this.$store.state.authUser.accessToken) (
            this.$router.push({name: 'HomeApp'})
        )
    }
}
</script>