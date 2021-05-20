<template>
  <div class="home">
    <div class="main-back">
      <div class="back">
        <div class="main-nav">
          <img class="logo" src="@/assets/logo.png" alt="" />
          <div class="d-flex">
            <div type="button" class="a-tag mr-8" @click="movemain">영화 목록</div>
            <div v-if="this.$store.state.email" type="button" class="a-tag" @click="logout">로그아웃</div>
            <div v-else type="button" class="a-tag" @click="login">로그인</div>
          </div>
        </div>
        <div class="main-content">
          <h1 class="content1">
            영화, TV 프로그램을 무제한으로.
          </h1>
          <h2 class="content2">
            다양한 디바이스에서 시청하세요. 언제든 해지하실 수 있습니다.
          </h2>
          <div class="search">
            <input class="search-input" type="text" placeholder="영화 제목을 입력하세요" v-model="keyword" />
            <button class="search-btn" @click="onSearch">검색하기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  name: 'Home',
  components: {},
  data() {
    return {
      keyword: '',
    };
  },
  methods: {
    ...mapMutations(['SET_LOADING']),
    login() {
      this.$router.push('/login');
    },
    logout() {
      this.$store.commit('clearEmail');
      this.$store.commit('clearPassword');
      this.$store.commit('clearNickname');
      this.$store.commit('clearPreferGenre');
      this.$store.commit('clearPreferGenre');
      localStorage.clear();
      sessionStorage.clear();
    },
    movemain() {
      this.$router.push('/main');
    },
    async onSearch() {
      if (!this.keyword) {
        alert('영화 제목을 입력하세요!');
        this.keyword = '';
        return;
      } else {
        this.$router.push({ name: 'Search', query: { keyword: this.keyword } });
        this.keyword = '';
      }
    },
  },
};
</script>

<style scoped>
.home {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
.main-back {
  background: url(../assets/back.png) no-repeat;
  background-size: cover;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-attachment: fixed;
}
.back {
  background: rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 100%;
}
.main-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 3rem 0 3rem;
}
.logo {
  width: 8%;
  height: 10%;
}
.a-tag {
  background-color: #e50914;
  line-height: normal;
  padding: 7px 17px;
  font-weight: 400;
  font-size: 1rem;
  color: #fff;
  border-radius: 0.3rem;
}

.main-content {
  position: relative;
  width: 100%;
  padding: 75px 0;
  max-width: 950px;
  margin: 0 auto;
  text-align: center;
  top: 15%;
}
.content1 {
  color: #fff;
  font-weight: 1000;
  font-size: 3.125rem;
  max-width: 500px;
  text-align: center;
  margin: auto;
}
.content2 {
  color: #fff;
  font-weight: 1000;
  font-size: 1.625rem;
}
.search {
  min-height: 60px !important;
  max-width: 980px;
  margin: 1rem;
}
.search-input {
  color: #000;
  background-color: #fff;
  height: 60px;
  width: 70%;
  vertical-align: middle;
}
.search-btn {
  color: #fff;
  background-color: #e50914;
  vertical-align: middle;
  cursor: pointer;
  font-weight: 400;
  font-size: 1.5rem;
  height: 60px;
  width: 20%;
}
</style>
