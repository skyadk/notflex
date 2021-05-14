<template>
  <div class="search">
    <div class="main-search">
      <div class="back">
        <form @submit.prevent="onSearch">
          <input class="border-black" v-model="keyword" placeholder="영화 제목을 입력하세요." />
        </form>
        <MovieText v-if="movieList" :text="'검색결과'"></MovieText>
        <MovieLists :movieList="movieList"></MovieLists>
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
  margin: 0;
  padding: 0;
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
</style>
