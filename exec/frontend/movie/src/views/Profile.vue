<template>
  <div class="main-back">
    <div class="back">
      <div class="container">
        <div class="main">
          <div class="row">
            <div class="col-md-4">
              <div class="card text-center sidebar">
                <div class="card-bady pt-10">
                  <img src="@/assets/profile.jpg" class="rounded-circle pt-5 mb-5" alt="" width="150" />
                  <h3 class="mb-10">{{ this.$store.state.nickname }}</h3>
                  <div class="mt-3 text">
                    <a href="/">홈</a>
                    <a href="/recommended">추천영화</a>
                    <a click="logout">로그아웃</a>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-8 mt-1">
              <div class="card mb-3 content">
                <h2 class="m-3 pt-3">기본정보</h2>
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-3">
                      <h5>Nickname</h5>
                    </div>
                    <div class="col-md-9 text-secondary">
                      {{ this.$store.state.nickname }}
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-3">
                      <h5>Email</h5>
                    </div>
                    <div class="col-md-9 text-secondary">
                      {{ this.$store.state.email }}
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-3">
                      <h5>PreferGenre</h5>
                    </div>
                    <div class="col-md-9 text-secondary">
                      {{ this.$store.state.preferGenre }}
                    </div>
                  </div>
                </div>
              </div>
              <div class="card mb-3 content">
                <h2 class="m-3">평가한 영화</h2>
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-12 text-secondary">
                      <ViewMovieLists :movieList="view_list"></ViewMovieLists>
                    </div>
                  </div>
                </div>
              </div>
              <div class="card mb-3 content">
                <h2 class="m-3">선호도 분석</h2>
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-12 text-secondary">
                      <Chart :user_id="this.$store.state.uuid"></Chart>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ViewMovieLists from '../components/ViewMovieLists';
import Chart from '@/components/Chart';
import { viewList } from '@/api/movie';
import { movieApi } from '../utils/movie';

export default {
  data() {
    return {
      view_list: [],
      genre_list: [],
    };
  },
  components: {
    ViewMovieLists,
    Chart,
  },
  async created() {
    const { data } = await viewList(this.$store.state.uuid);
    // console.log(data);
    for (let i = 0; i < data.length; i++) {
      if (data[i].mid > 10) {
        const res = await movieApi.movieDetail(data[i].mid);
        // console.log(res.data);
        this.view_list.push(res.data);
      }
    }
    // const uuid = {
    //   uid: this.$store.state.uuid,
    // };
    // const res = await preferPerGenre(uuid);
    // console.log(res.data.message);
    // this.genre_list = res.data.message;
  },
  methods: {
    logout() {
      this.$store.commit('clearEmail');
      this.$store.commit('clearPassword');
      this.$store.commit('clearNickname');
      this.$store.commit('clearPreferGenre');
      this.$store.commit('clearPreferGenre');
      localStorage.clear();
      sessionStorage.clear();
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
.main-back {
  background: url(../assets/back.png) no-repeat;
  background-size: cover;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-attachment: fixed;
}
.back {
  background: rgba(0, 0, 0, 0.8);
  width: 100%;
  height: 100%;
  margin-top: 5%;
}
.main {
  padding-top: 5%;
}
.sidebar {
  background: #333;
  color: #fff;
  height: 100%;
}
.sidebar a {
  margin-left: 10px;
  display: block;
  color: #fff;
  padding-bottom: 10px;
  font-size: 30px;
  text-decoration: none;
  margin-top: 10px;
}
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  /* border: none; */
}
.content {
  background-color: whitesmoke;
}
.rounded-circle {
  border-radius: 50% !important;
}
.text {
  margin: 15% 0px;
}
</style>
