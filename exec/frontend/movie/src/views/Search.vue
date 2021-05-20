<template>
  <div class="search">
    <div class="main-search">
      <div class="back">
        <div class="search-main">
          <input class="search-input" type="text" placeholder="영화 제목을 입력하세요" v-model="keyword" />
          <button class="search-btn" @click="onSearch">검색하기</button>
        </div>
        <MovieText v-if="movieList" class="mt-10" :text="'검색결과'" :keyword="keyword"></MovieText>
        <MovieLists class="mt-5" :movieList="movieList"></MovieLists>
      </div>
    </div>
  </div>
</template>

<script>
import MovieLists from '../components/MovieLists';
import MovieText from '../components/MovieText';
import { movieApi } from '../utils/movie';
import { mapMutations } from 'vuex';
export default {
  data() {
    return {
      keyword: '',
      movieList: '',
    };
  },
  components: {
    MovieText,
    MovieLists,
  },
  async created() {
    this.SET_LOADING(true);
    console.log(this.$route.query.keyword);
    this.keyword = this.$route.query.keyword;
    if (!this.keyword) {
      alert('영화 제목을 입력하세요!');
      this.keyword = '';
      return;
    }
    const { data } = await movieApi.search(this.keyword);
    console.log(data);
    this.movieList = data.results;
    this.SET_LOADING(false);
  },
  methods: {
    ...mapMutations(['SET_LOADING']),
    async onSearch() {
      this.SET_LOADING(true);
      console.log(this.keyword);
      if (!this.keyword) {
        alert('영화 제목을 입력하세요!');
        this.keyword = '';
        return;
      }
      const { data } = await movieApi.search(this.keyword);
      console.log(data);
      this.movieList = data.results;
      this.SET_LOADING(false);
    },
  },
};
</script>

<style scoped>
.search {
  width: 100%;
  height: 100%;
  /* margin-top: 5%;
  padding-top: 5%; */
}
.main-search {
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
}
.search-main {
  min-height: 50px !important;
  max-width: 980px;
  margin: 5rem auto 1rem;
  padding-top: 5rem;
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
