<template>
    <Form class="row g-2 divBorder formMarginBottom" @submit="recover">
        <h1 class="text-center">Recuperar Senha</h1>

        <div class="alert alert-warning" v-if="alertOn">
            {{ message }}
        </div>

        <div class="col-12">
            <label class="form-label">Insira Nova Senha</label>
            <Field name="password" type="password" class="form-control" required v-model="password" :rules="validatePassword" />
            <ErrorMessage name="password" class="text-vermelho" />
        </div>
        <div class="col-12">
            <label class="form-label">Confirmar Nova Senha</label>
            <Field name="password_confirm" type="password" class="form-control" required v-model="password_confirm" :rules="passwordMatch" />
            <ErrorMessage name="password_confirm" class="text-vermelho" />
        </div>
        <div class="d-grid mx-auto btnMargin">
            <button class="btn btn-success btn-rounded" type="submit">Confirmar</button>
        </div>

        <div class="noLogin text-center">
            <p>Já possui cadastro?</p>
            <div class="d-grid mx-auto col-4">
                <router-link class="btn btn-outline-success btn-rounded" :to="{ name: 'LogIn' }">Login</router-link>
            </div>
        </div>
    </Form>
</template>

<script>
import { Form, Field, ErrorMessage } from 'vee-validate';

export default {
    name: 'FormPasswordChange',
    components: {
        Form,
        Field,
        ErrorMessage
    },
    data() {
        return {
            password: null,
            password_confirm: null,
            alertOn: false,
            uidb64: '',
            token: '',
        }
    },
    methods: {
        passwordMatch(value) {
            if(value != this.password) {
                return 'Senhas digitadas não conferem'
            }
            return true
        },
        validatePassword(value) {
            const paswd =  /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,16}$/;
            var passValid = paswd.test(value)
            if (!passValid) {
                return 'Sua senha precisa ter 8 caracteres no mínimo, além de caracteres especiais, letras e números'
            }

            return true

        },
        recover() {

            var data = {
                password: this.password,
                password_confirm: this.password_confirm
            }

            this.uidb64 = this.$route.params.uidb64;
            this.token = this.$route.params.token;

            this.$axios.post('password/change/' + this.uidb64 + '/' + this.token + '/', data).then((response) => {

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