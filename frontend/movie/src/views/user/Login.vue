<template>
  <div class="main-back">
    <div class="back">
      <div class="main-nav">
        <img type="button" class="logo" src="@/assets/logo.png" alt="" @click="logo" />
        <div type="button" class="a-tag">로그인</div>
      </div>
      <div class="main-content">
        <div class="login-content">
          <h1 class="login-page-title">로그인</h1>
          <div>
            <input class="login-input" type="text" placeholder="이메일 주소" />
            <label for="">이메일 주소</label>
          </div>
          <div>
            <input class="login-input" type="text" placeholder="비밀번호" />
            <label for="">비밀번호</label>
          </div>
          <button class="login-button">로그인</button>
        </div>
      </div>
    </div>
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
  </div>
</template>

<script>
export default {
  methods: {
    logo() {
      this.$router.push('/');
    },
  },
};
</script>

<style>
.home {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}
.main-back {
  background: url(../../assets/back.png) no-repeat;
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
  margin: 0 auto -236px;
  min-height: 100vh;
  background-color: transparent;
  max-width: 450px;
}
.login-content {
  min-height: 660px;
  padding: 60px 68px 40px;
  margin-bottom: 90px;
  background-color: rgba(0, 0, 0, 0.75);
  border-radius: 4px;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  flex-direction: column;
  margin: 0;
  width: 100%;
}
.login-page-title {
  color: #fff;
  margin-bottom: 28px;
}
.login-input {
  background: #333;
  border-radius: 4px;
  border: 0;
  color: #fff;
  height: 50px;
  /* line-height: 50px; */
  padding: 16px 20px 0;
  width: 100%;
}
.login-button {
  border-radius: 4px;
  font-size: 16px;
  font-weight: 700;
  margin: 24px 0 12px;
  width: 100%;
  max-width: 100%;
  background: #e50914;
  min-width: 98px;
  min-height: 50px;
  color: #fff;
}
</style>
