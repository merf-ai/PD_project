<template>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">

            <router-link to="/" class="navbar-item">
                <img :src="require('@/assets/logo-novacproject.svg')" class="mx-auto d-block" alt="NovacProject"
                    width="100" height="21">
            </router-link>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link to="/info" class="nav-link active">
                            О сайте
                        </router-link>
                    </li>
                </ul>

                <template v-if="$store.state.isAuthenticated">
                    <router-link to="/account" class="nav-link active">My account</router-link>
                    <button @click="logout()" class="btn btn-outline-success mx-2">Выйти</button>
                </template>

                <template v-else>
                    <router-link to="/register" class="btn btn-outline-success mx-2">Регистрация</router-link>
                    <router-link to="/login" class="btn btn-outline-success">Войти</router-link>
                </template>
            </div>
        </div>
    </nav>

</template>

<script>
import axios from "axios";

export default {
    methods: {
        async logout() {
                await axios
                    .post('/api/v1/token/logout/')
                    .then(response => {
                        console.log('Logged out')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                localStorage.removeItem('username')
                localStorage.removeItem('userid')
                localStorage.removeItem('team_name')
                localStorage.removeItem('team_id')
                this.$store.commit('removeToken')
                this.$router.push('/')
            }
    }
}
</script>

<style scoped>

</style>