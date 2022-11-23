<template>
    <div class="row" style="margin-top: 40px;">
        <div class="col-md-4 offset-md-4">
            <h1 class="text-center">
                Bem vindo(a)
                <span class="text-green">{{ $store.state.userData.first_name }} {{ $store.state.userData.last_name }}</span>!
            </h1>
        </div>
    </div>
</template>

<script>

import authHeader from '@/stores/modules/auth.header';

export default {
    name: 'HomeApp',
    components: {
    },
    created() {

        this.$axios.get('get/user/', { headers: authHeader() }).then((response) => {

            this.$store.dispatch(
                'userData/storeUser',
                { 
                    first_name: response.data.first_name, 
                    last_name: response.data.last_name,
                    email: response.data.email
                }
            )
        
        })
        
    }
}
</script>