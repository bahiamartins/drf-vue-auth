<template>
    <div class="row text-center" style="margin-top: 40px;">
        <div class="col-md-4 offset-md-4">

            <div class="progresses">

                <div class="stepDone">
                    <font-awesome-icon style="font-size: 1.5em" icon="fa-solid fa-check" />
                </div>

                <span class="line"></span>

                <div class="stepActive">
                    <span>2</span>
                </div>

                <span class="lineNext"></span>

                <div class="stepPending">
                    <span>3</span>
                </div>

            </div>

            <h1>Por favor confirme seu cadastro</h1>
            <p class="lead">
                Uma mensagem foi enviada para <strong class="text-green">{{ email }}</strong>
                <br>
                Você tem 1 dia para ativar a sua conta
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ConfirmEmail',
    data() {
        return {
            email: '',
        }
    },
    mounted() {

        this.email = this.$route.params.email;
        /*if(this.$route.query.debug) {
            this.debug = this.$route.query.debug;
        }*/
    }
}
</script>