<template>
  <div class="home">
    <div class="main-back">
      <div class="back">
        <div class="main-nav">
          <img type="button" class="logo" src="@/assets/logo.png" alt="" @click="logo" />
          <div type="button" class="a-tag" @click="login">로그인</div>
        </div>
        <div class="main-content">
          <h1 class="content1">
            영화, TV 프로그램을 무제한으로.
          </h1>
          <h2 class="content2">
            다양한 디바이스에서 시청하세요. 언제든 해지하실 수 있습니다.
          </h2>
          <div class="search">
            <input class="search-input" type="text" placeholder="입력하세요" />
            <button class="search-btn">검색하기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  components: {},
  methods: {
    login() {
      this.$router.push('/login');
    },
    logo() {
      this.$router.push('/home');
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
