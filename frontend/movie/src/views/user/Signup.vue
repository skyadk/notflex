<template>
  <div class="main-back">
    <div class="back">
      <div class="main-nav">
        <img type="button" class="logo" src="@/assets/logo.png" alt="" @click="logo" />
        <div type="button" class="a-tag">로그인</div>
      </div>
      <div class="main-content">
        <div class="login-content">
          <h1 class="login-page-title">회원가입</h1>
          <div>
            <v-text-field class="login-input" v-model="name" label="이름을 입력하세요" hint="이름을 확인하세요" :rules="[rules_name.required]"></v-text-field>
          </div>
          <div>
            <v-text-field
              class="login-input"
              v-model="email"
              :rules="[rules_email.required, rules_email.check]"
              :type="show1 ? 'text' : 'email'"
              name="input-10-1"
              label="이메일을 입력하세요"
              hint="이메일 형식을 확인하세요"
              @click:append="show1 = !show1"
            ></v-text-field>
          </div>
          <div>
            <v-text-field
              class="login-input"
              v-model="password"
              :rules="[rules_password.required, rules_password.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="비밀번호를 입력하세요"
              hint="비밀번호를 확인하세요"
              @click:append="show1 = !show1"
            ></v-text-field>
          </div>
          <div>
            <v-text-field
              class="login-input"
              v-model="passwordconfirm"
              :rules="[rules_password.required, rules_password.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="비밀번호를 확인"
              hint="비밀번호를 확인하세요"
              @click:append="show1 = !show1"
            ></v-text-field>
          </div>
          <div>
            <v-select :items="items" label="선호 장르" class="login-input" v-model="genre"></v-select>
          </div>
          <button class="login-button">회원가입</button>
          <div class="login-other">
            <div class="login-other-content1">
              Notflex 회원이 이신가요?
            </div>
            <div type="button" class="login-other-content2" @click="login">
              지금 로그인하세요
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      passwordconfirm: '',
      nickname: '',
      genre: '',
      show1: false,
      rules_name: { required: (value) => !!value || '잘못된 입력입니다.' },
      rules_nickname: { required: (value) => !!value || '잘못된 입력입니다.' },
      rules_email: {
        required: (value) => !!value || '잘못된 입력입니다.',
        emailMatch: () => `The email and password you entered don't match`,
        check: (p) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(p) || 'Invalid e-mail.';
        },
      },
      rules_password: {
        required: (value) => !!value || '잘못된 입력입니다.',
        min: (v) => v.length >= 8 || 'Min 8 characters',
        emailMatch: () => `The email and password you entered don't match`,
      },
      items: ['공포', '액션', '로맨스', '...'],
    };
  },
  methods: {
    logo() {
      this.$router.push('/');
    },
    login() {
      this.$router.push('/login');
    },
    async signup() {
      if (this.email == null) {
        this.$swal({
          icon: 'error',
          title: '이메일을 입력해주세요!',
        });
      } else if (this.password == null) {
        this.$swal({
          icon: 'error',
          title: '비밀번호를 입력해주세요!',
        });
      } else if (this.passwordconfirm == null) {
        this.$swal({
          icon: 'error',
          title: '비밀번호 확인란을 입력해주세요!',
        });
      } else if (this.passwordconfirm != this.password) {
        this.$swal({
          icon: 'error',
          title: '비밀번호가 일지하지 않습니다.',
        });
      } else {
        const userData = {
          email: this.email,
          password: this.password,
          nickname: this.nickname,
          genre: this.genre,
        };

        console.log(userData);

        // const { data } = await register(userData);

        // if (data == 'SUCCESS') {
        //   this.$swal({
        //     position: 'top-end',
        //     icon: 'success',
        //     title: '회원가입성공!!',
        //     showConfirmButton: false,
        //     timer: 1500,
        //   });
        //   this.$router.push('/');
        // } else {
        //   this.$swal({
        //     icon: 'error',
        //     title: '회원가입 실패 관리자에게 문의해주세요',
        //   });
        // }
      }
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
  min-height: 500px;
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
  margin-bottom: 1.3rem;
}
.login-button {
  border-radius: 4px;
  font-size: 16px;
  font-weight: 700;
  margin: 30px 0 12px;
  width: 100%;
  max-width: 100%;
  background: #e50914;
  min-width: 98px;
  min-height: 50px;
  color: #fff;
}
.v-text-field {
  padding-top: 20px !important ;
}
#input-7,
#input-10,
#input-13,
#input-16 {
  color: #fff;
}
.v-label {
  color: #8c8c8c !important;
}
.login-other {
  margin-top: 1rem;
  color: #8c8c8c;
  font-size: 1rem;
  display: flex;
  justify-content: space-around;
}
.login-other-content2 {
  color: #fff;
  font-weight: 300;
}
.v-select__selection--comma {
  color: #fff;
}
</style>
