<template>
    <form class="row g-2 divBorder formMarginBottom" @submit.prevent="recover">
        <h1 class="text-center">Recuperar Senha</h1>

        <div class="alert alert-warning" v-if="alertOn">
            Enviamos uma messagem no email para recuperar a senha
        </div>

        <div class="col-12">
            <label class="form-label">Insira seu Email</label>
            <input type="email" class="form-control" required v-model="email">
        </div>
        <div class="d-grid mx-auto btnMargin">
            <button class="btn btn-success btn-rounded" type="submit">Recuperar Senha</button>
        </div>

        <div class="noLogin text-center">
            <p>Já possui cadastro?</p>
            <div class="d-grid mx-auto col-4">
                <router-link class="btn btn-outline-success btn-rounded" :to="{ name: 'LogIn' }">Login</router-link>
            </div>
        </div>
    </form>
</template>

<script>


export default {
    name: 'FormPasswordRecover',
    data() {
        return {
            email: null,
            alertOn: false,
            message: null,
        }
    },
    methods: {
        recover() {

            var data = {
                email: this.email
            }

            this.$axios.post('password/reset/', data).then((response) => {

                this.message = response.data.message
                this.alertOn = true
                
            })
        }
    }
}
</script>

<style scoped>
.noLogin {
    border-top:#CBD6E2 solid 1px;
    padding-top: 20px;
    margin-top:60px;
}
</style>