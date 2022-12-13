<template>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-avatar@latest/dist/avatar.min.css" rel="stylesheet">
    <div class="Account">
        <!-- <div class="card" style="width: 18rem;"></div> -->
        <div v-for="profile in user" :key="profile.id">
            <div class="card">
                <div class="card-body">
                    <div class="d-flex justify-content-between mb-3">
                        <div>
                            <h4 class="card-title">{{ profile.type }}</h4>
                            <h5 class="card-subtitle mb-2 text-muted">{{ profile.surname }} {{ profile.name }}</h5>
                        </div>
                        <div class="image">
                            <img :src="require('@/assets/student.svg')" class="rounded-circle" style="width: 150px;" />
                        </div>
                    </div>

                    <div class="mb-3">
                        <h5 class="card-title">
                            Контактная информация:
                        </h5>
                        <dl class="row">
                            <dt class="col-sm-3">Никнейм: </dt>
                            <dd class="col-sm-9">{{ profile.username }}</dd>
                            <dt class="col-sm-3">Почта: </dt>
                            <dd class="col-sm-9">{{ profile.email }}</dd>
                        </dl>

                        <button type="button" class="btn btn-outline-primary">Редактировать информацию</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Main',
    data() {
        return {
            user: [{
                id: 1,
                username: 'novackirr',
                surname: 'Мясников',
                name: 'Кирилл',
                type: 'Студент',
                email: 'std1@mail.ru'
            }],
        }
    },
}
</script>

<style scoped>

</style>