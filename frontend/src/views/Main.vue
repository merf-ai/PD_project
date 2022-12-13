<template>
    <div class="main">
        <div class="alert alert-info" role="alert">
            Ниже будут ссылки на предполагаемые страницы
        </div>
        <ul class="nav flex-column">
        <li class="nav-item">
            <router-link to="/account" class="nav-link">
                Аккаунт
            </router-link>
        </li>
        <li class="nav-item">
            <router-link to="/signin" class="nav-link">
                Войти
            </router-link>
        </li>
        <li class="nav-item">
            <router-link to="/register" class="nav-link">
                Регистрация
            </router-link>
        </li>
        <li class="nav-item">
            <router-link to="/create" class="nav-link disabled">
                Создание нового варианта
            </router-link>
        </li>
        <li class="nav-item">
            <router-link to="/info" class="nav-link">
                Информация о сайте
            </router-link>
        </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Main'
}
</script>

<style scoped>

</style>