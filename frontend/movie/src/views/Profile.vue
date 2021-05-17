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
                    <a href="#">추천영화</a>
                    <a href="#">로그아웃</a>
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
                <h2 class="m-3">영화</h2>
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-3">
                      <h5>평가한 영화</h5>
                    </div>
                    <div class="col-md-12 text-secondary">
                      <br />
                      <br />
                      <br />
                      <br />
                      <br />
                      <br />
                      <br />
                      <br />
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
export default {};
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
