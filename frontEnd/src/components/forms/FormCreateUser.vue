<template>
    <Form class="row g-2 divBorder formMarginBottom" @submit="createUser">
        <h1 class="text-center">Cadastrar</h1>

        <div class="alert alert-warning" v-if="message">
            {{ message }}
        </div>

        <div class="col">
            <label class="form-label">Seu Nome</label>
            <input type="text" class="form-control" required v-model="user.first_name">
        </div>
        <div class="col">
            <label class="form-label">Sobrenome</label>
            <input type="text" class="form-control" required v-model="user.last_name">
        </div>

        <div class="col-12">
            <label class="form-label noMarginBottom">Email</label>
            <div class="text-grey">Não são permitidos emails @gmail, @hotmail, @yahoo e similares</div>
            <Field name="email" type="email" class="form-control" required v-model="user.email" :rules="validateEmail" />
            <ErrorMessage name="email" class="text-vermelho" />
        </div>
        <div class="col-12">
            <label class="form-label">Confirmar Email</label>
            <Field name="email_confirm" type="email" class="form-control" required v-model="user.email_confirm" :rules="emailMatch" />
            <ErrorMessage name="email_confirm" class="text-vermelho" />
        </div>
        <div class="col-12">
            <label class="form-label">Senha</label>
            <Field name="password" type="password" class="form-control" required v-model="user.password" :rules="validatePassword" />
            <ErrorMessage name="password" class="text-vermelho" />
        </div>

        <div class="" style="margin-top:20px">
            <input class="form-check-input" type="checkbox" required v-model="user.agreeTerms">
            <label class="form-check-label">
                Eu concordo com <a href="/terms" class="text-green"> Termos</a> e <a href="/policy" class="text-green">Política</a>
            </label>
        </div>

        <div class="d-grid mx-auto btnMargin">
            <button class="btn btn-success btn-rounded" type="submit">Cadastrar</button>
        </div>
    </Form>
</template>

<script>
import { Form, Field, ErrorMessage } from 'vee-validate';
export default {
    name: 'FormCreateUser',
    components: {
        Form,
        Field,
        ErrorMessage
    },
    data() {
        return {
            user: {
                first_name: null,
                last_name: null,
                email: null,
                email_confirm: null,
                password: null,
                agreeTerms: null
            },
            message: null
        }
    },

    methods: {
        emailMatch(value) {
            if(value != this.user.email) {
                return 'Emails digitados não conferem'
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
        validateEmail(value) {

            // if the field is not a valid email
            const regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            var isValid = regex.test(value)
            
            if (!isValid) {
                return 'Favor inserir um email válido'
            }

            return true
        },
        createUser() {
            var data = {
                first_name: this.user.first_name,
                last_name: this.user.last_name,
                email: this.user.email,
                email_confirm: this.user.email_confirm,
                password: this.user.password,
                agreeTerms: this.user.agreeTerms
            }

            this.$axios.post('user/create/', data).then((response) => {
                this.$router.push(
                    {
                        name: 'ConfirmEmail', 
                        params: { email: response.data.email }
                    }
                )
                
            }).catch((error) => {
                console.log('error ', error.response.data )
                if (error.response.data['non_field_errors']) {
                    this.message = error.response.data['non_field_errors'][0]
                } else {
                    this.message = error.response.data[0]
                }
            })
            
        }

    }
}
</script>