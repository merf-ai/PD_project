<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title mb-3">Sign up</h1>

                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label class="form-label">Электронная почта</label>
                        <input required type="email" name="email" class="form-control" v-model="email">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Фамилия</label>
                        <input required type="text" name="last_name" class="form-control" v-model="last_name">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Имя</label>
                        <input required type="text" name="first_name" class="form-control" v-model="first_name">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Отчество</label>
                        <input required type="text" name="middle_name" class="form-control" v-model="middle_name">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Роль</label>
                        <select required class="form-select" name="groups" v-model="selectedGroup">
                            <option disabled selected>Выберите роль</option>
                            <option v-for="group in groups" :value="group">{{ group.name }}</option>
                        </select>
                    </div>
                    <div v-if="selectedGroup['id']===1" class="mb-3">
                        <label class="form-label">Группа</label>
                        <input required type="text" name="student_group" pattern="[0-9]{3}-[0-9]{3}" class="form-control" 
                        title="Группа должна быть в формате 111-111, проверьте лишние пробелы" v-model="student_group">
                        <div class="form-text">Группа в формате 111-111</div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Пароль</label>
                        <input required type="password" name="password1" class="form-control" v-model="password1">
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Повторите пароль</label>
                        <input required type="password" name="password2" class="form-control" v-model="password2">
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'SignUp',
    data() {
        return {
            first_name: '',
            last_name: '',
            middle_name: '',
            student_group: '',
            email: '',
            password1: '',
            password2: '',
            groups: [
                {name: 'Студент', id:1},
                {name: 'Преподаватель', id:2}
            ],
            selectedGroup: {
                id: 0
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []
            if (this.password1 === '') {
                this.errors.push('The password is too short')
            }
            if (this.email === '') {
                this.errors.push('The email is missing')
            }
            if (this.email.length > 254) {
                this.errors.push('Почта может не содержать более 254 символов')
            }
            if (this.first_name.length > 150) {
                this.errors.push('Имя может не содержать более 150 символов')
            }
            if (this.middle_name.length > 100) {
                this.errors.push('Отчество может не содержать более 100 символов')
            }
            if (this.student_group.length > 30) {
                this.errors.push('Группа может не содержать более 30 символов')
            }
            if ( /^\d\d\d-\d\d\d$/.test(this.student_group) === false) {
                this.errors.push('Группа должна быть в формате 111-111, пример 191-363')
            }
            if (this.password1 === '') {
                this.errors.push('The password is too short')
            }
            if (this.password1 !== this.password2) {
                this.errors.push('The password are not matching')
            }
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                const formData = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    middle_name: this.middle_name,
                    student_group: this.student_group,
                    email: this.email,
                    password: this.password1,
                    groups: this.selectedGroup['name']
                }
                await axios
                    .post('/users/reg/', formData)
                    .then(response => {
                        toast({
                            message: 'Аккаунт был создан, проверьте свою почту',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/login')
                    })
                    .catch(error => {
                        // if (error.response) {
                            
                        //     for (const property in error.response.data) {
                        //         this.errors.push(`${property}: ${error.response.data[property]}`)
                        //     }
                        // } else if (error.message) {
                        //     this.errors.push('Something went wrong. Please try again!')
                        // }
                        if (error.message) {
                            this.errors.push(error)
                            this.errors.push('Что-то пошло не так. Попробуйте еще раз!')
                        }
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>