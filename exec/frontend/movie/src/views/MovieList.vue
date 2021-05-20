<template>
  <div class="movielist"></div>
</template>

<script>
import { movieApi } from '@/utils/movie.js';
export default {
  data() {
    return {
      nowPlaying: {},
      popular: {},
      upComming: {},
    };
  },
  async mounted() {
    try {
      const { data } = await movieApi.nowPlaying();
      console.log(data.results);
      this.movieList = data.results;
      const { nowPlaying, popular, upComing } = movieApi;
      const requestArr = [nowPlaying, popular, upComing];
      const [now, pop, up] = await Promise.all(requestArr.map((li) => li().then((res) => res.data.results)));
      console.log('pop');
      console.log(pop);
      this.SET_LOADING(false);
      this.nowPlaying = now;
      this.popular = pop;
      this.upComming = up;
    } catch (error) {
      this.movieList = '해당 자료가 존재하지 않습니다.';
    }
  },
};
</script>
<style scoped></style>
