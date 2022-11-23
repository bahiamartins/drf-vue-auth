<template>
    <form class="row g-2 divBorder formMarginBottom" @submit.prevent="login">
        <h1 class="text-center">Login</h1>
        <div class="col-12">
            <label class="form-label">Email</label>
            <input type="email" class="form-control" required v-model="username">
        </div>
        <div class="col-12">
            <label class="form-label">Senha</label>
            <input type="password" class="form-control" required v-model="password">
        </div>
        <div class="d-grid mx-auto btnMargin">
            <button class="btn btn-success btn-rounded" type="submit">Login</button>
        </div>
        <p class="text-end btnMargin" style="font-size:0.95em">
            Esqueceu a senha? <router-link class="text-green" :to="{ name: 'PasswordRecover' }">Clique Aqui</router-link>
        </p>
        <div class="noLogin text-center">
            <p>Não possui cadastro?</p>
            <div class="d-grid mx-auto col-4">
                <router-link class="btn btn-outline-success btn-rounded" :to="{ name: 'SignUp' }">Cadastrar</router-link>
            </div>
        </div>
    </form>
</template>

<script>


export default {
    name: 'FormLogIn',
    data() {
        return {
            username: null,
            password: null
        }
    },
    methods: {
        login() {

            var data = {
                username: this.username,
                password: this.password
            }

            this.$axios.post('login/token/', data).then((response) => {

                this.$store.dispatch(
                    'authUser/storeToken',
                    { access: response.data.access, refresh: response.data.refresh },
                    { root: true }
                )

                this.$router.push({name: 'HomeApp'})
                
            })
        }
    }
}
</script>

<style scoped>
.noLogin {
    border-top:#CBD6E2 solid 1px;
    padding-top: 20px;
}
</style>