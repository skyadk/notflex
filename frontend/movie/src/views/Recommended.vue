<template>
  <div class="main-back">
    <div class="back">
      <MovieText :text="'시청 선호도 추천'"></MovieText>
      <MovieLists :movieList="view_record"></MovieLists>
      <MovieText :text="'사용자가 좋아하는 장르'"></MovieText>
      <MovieLists :movieList="prefer_genre"></MovieLists>
    </div>
  </div>
</template>

<script>
import { preferPerGenre, genreRecommend } from '@/api/movie';

import MovieLists from '../components/MovieLists';
import MovieText from '../components/MovieText';
export default {
  data() {
    return {
      view_record: [],
      prefer_genre: [],
    };
  },
  components: {
    MovieText,
    MovieLists,
  },
  async created() {
    const preferGenre1 = {
      genre_name: this.$store.state.preferGenre,
    };
    const response = await genreRecommend(preferGenre1);
    // console.log(response.data.message);
    this.prefer_genre = response.data.message;

    const uuid = {
      uid: this.$store.state.uuid,
    };
    const { data } = await preferPerGenre(uuid);
    // console.log('평가한 영화 장르', data.message);

    var first_key = Object.keys(data.message)[0];
    // console.log(first_key);
    const preferGenre2 = {
      genre_name: first_key,
    };
    const res = await genreRecommend(preferGenre2);
    // console.log(res.data.message);
    this.view_record = res.data.message;
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
  padding-top: 5%;
}
</style>
