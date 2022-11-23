<template>
    <header class="d-flex flex-wrap justify-content-md-between py-3 mb-4 headerBorder" style="background-color:#fff">
        <div class="container">
            <div class="container-fluid d-grid gap-3" style="grid-template-columns: 11fr 1fr;">
                <router-link class="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-decoration-none" :to="{ name: 'LogIn' }">
                    <img class="" alt="Frontend" src="@/assets/images/logo.png" height="40" >
                </router-link>
                <ul class="nav">
                    <li class="nav-item" v-if="$store.state.authUser.accessToken">
                        <router-link class="nav-link text-default px-2" :to="{ name: 'LogIn'}" @click="logout()">Logout</router-link>
                    </li>
                </ul>
            </div>
            
        </div>
    </header>
    <router-view />
</template>

<script>
export default {
    name: 'HeaderSite',
    methods: {
        logout() {
            this.$store.dispatch('authUser/logoutUser')
        }
    }
}
</script>
