<template>
  <div id="nav">
    <header>
      <a class="logo" href="/"><img src="@/assets/logo.png" alt="logo" class="img" /></a>
      <nav>
        <ul class="nav__links">
          <li><a href="/main">영화목록</a></li>
          <li><a href="/recommended">추천영화</a></li>
          <li>
            <a href="/profile">{{ this.$store.state.nickname }}님의 마이페이지</a>
          </li>
        </ul>
      </nav>
      <div type="button" class="a-tag mr-8" @click="logout">로그아웃</div>
    </header>
  </div>
</template>

<script>
export default {
  components: {},
  methods: {
    logout() {
      this.$store.commit('clearEmail');
      this.$store.commit('clearPassword');
      this.$store.commit('clearNickname');
      this.$store.commit('clearUuid');
      this.$store.commit('clearPreferGenre');
      localStorage.clear();
      sessionStorage.clear();
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

#nav {
  z-index: 99;
}
header {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 14px 5% 14px 5%;
  background-color: rgba(0, 0, 0, 0.9);
  position: fixed;
}

.logo {
  margin-top: 3px;
  cursor: pointer;
}
.img {
  width: 25%;
  height: 12%;
}

.nav__links a,
.cta,
.overlay__content a {
  font-family: 'Montserrat', sans-serif;
  font-weight: 500;
  color: #edf0f1;
  text-decoration: none;
}

.nav__links {
  list-style: none;
  display: flex;
}

.nav__links li {
  padding: 0px 20px;
}

.nav__links li a {
  transition: color 0.3s ease 0s;
}

.nav__links li a:hover {
  color: #0088a9;
}

.cta {
  padding: 9px 25px;
  background-color: rgba(0, 136, 169, 1);
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: background-color 0.3s ease 0s;
}

.cta:hover {
  background-color: rgba(0, 136, 169, 0.8);
}

/* Mobile Nav */

.menu {
  display: none;
}

.overlay {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  background-color: #24252a;
  overflow-x: hidden;
  transition: width 0.5s ease 0s;
}

.overlay--active {
  width: 100%;
}

.overlay__content {
  display: flex;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.overlay a {
  padding: 15px;
  font-size: 36px;
  display: block;
  transition: color 0.3s ease 0s;
}

.overlay a:hover,
.overlay a:focus {
  color: #0088a9;
}
.overlay .close {
  position: absolute;
  top: 20px;
  right: 45px;
  font-size: 60px;
  color: #edf0f1;
}

@media screen and (max-height: 450px) {
  .overlay a {
    font-size: 20px;
  }
  .overlay .close {
    font-size: 40px;
    top: 15px;
    right: 35px;
  }
}

@media only screen and (max-width: 800px) {
  .nav__links,
  .cta {
    display: none;
  }
  .menu {
    display: initial;
  }
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
</style>
