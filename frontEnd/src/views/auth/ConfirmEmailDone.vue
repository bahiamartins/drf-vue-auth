<template>
    <div class="row text-center" style="margin-top: 40px;">
        <div class="col-md-4 offset-md-4">

            <div class="progresses">

                <div class="stepDone">
                    <font-awesome-icon style="font-size: 1.5em" icon="fa-solid fa-check" />
                </div>

                <span class="line"></span>

                <div class="stepDone">
                    <font-awesome-icon style="font-size: 1.5em" icon="fa-solid fa-check" />
                </div>

                <span class="line"></span>

                <div class="stepDone">
                    <font-awesome-icon style="font-size: 1.5em" icon="fa-solid fa-check" />
                </div>

            </div>

            <h1>Parabéns!</h1>
            <p class="lead">
                Sua conta foi ativada.
                <br>
                Agora basta fazer login.
            </p>
            <div class="d-grid mx-auto col-4">
                <router-link class="btn btn-outline-success btn-rounded" :to="{ name: 'LogIn' }">Entrar</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ConfirmEmailDone',
    data() {
        return {
            uidb64: '',
            token: '',
        }
    },
    mounted() {

        this.uidb64 = this.$route.params.uidb64;
        this.token = this.$route.params.token;


        this.$axios.get('user/activate/' + this.uidb64 + '/' + this.token + '/' ).then((response)=>{
            console.log(response.data)
        })
    }
}
</script>