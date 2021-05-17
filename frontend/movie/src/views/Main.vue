<template>
  <div class="main-back">
    <div class="back">
      <v-carousel class="top" hide-delimiters>
        <v-carousel-item v-for="(item, i) in topRating" :key="i" :src="image(item.backdrop_path)" reverse-transition="fade-transition" transition="fade-transition">
          <div>
            <span class="text1">최고 인기작</span>
            <span class="text2">{{ item.title }}</span>
          </div>
        </v-carousel-item>
      </v-carousel>
      <div v-if="nowPlaying">
        <MovieText :text="'NowPlaying'"></MovieText>
        <MovieLists :movieList="nowPlaying"></MovieLists>
        <MovieText :text="'Popular'"></MovieText>
        <MovieLists :movieList="popular"></MovieLists>
        <MovieText :text="'UpComming'"></MovieText>
        <MovieLists :movieList="upComming"></MovieLists>
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
      nowPlaying: {},
      popular: {},
      upComming: {},
      topRating: [],
    };
  },
  components: {
    // MovieCard,
    MovieText,
    MovieLists,
  },
  methods: {
    ...mapMutations(['SET_LOADING']),
    image(img) {
      return `https://image.tmdb.org/t/p/original/${img}`;
    },
  },

  created() {
    this.SET_LOADING(true);
  },
  async mounted() {
    try {
      // vuex를 통해서 로딩을 없애준다.

      const { data } = await movieApi.nowPlaying();
      console.log(data.results);
      this.movieList = data.results;
      const { nowPlaying, popular, upComing, topRating } = movieApi;
      const requestArr = [nowPlaying, popular, upComing, topRating];
      const [now, pop, up, top] = await Promise.all(requestArr.map((li) => li().then((res) => res.data.results)));
      console.log('pop');
      console.log(pop);
      console.log('up');
      console.log(up);
      console.log('top');
      console.log(top);
      this.SET_LOADING(false);
      this.nowPlaying = now;
      this.popular = pop;
      this.upComming = up;
      this.topRating = pop.slice(0, 4);
    } catch (error) {
      this.movieList = '해당 자료가 존재하지 않습니다.';
    }
  },
};
</script>

<style>
.text1 {
  position: absolute;
  text-align: center;
  color: #fff;
  font-size: 3rem;
  font-weight: 1000;
  width: 30%;
  top: 30%;
  left: 5%;
}
.text2 {
  position: absolute;
  text-align: center;
  color: #fff;
  font-size: 2.5rem;
  font-weight: 1000;
  width: 25%;
  top: 45%;
  left: 8%;
}
.v-image__image--cover {
  background-size: contain !important;
  margin-left: 15%;
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
  background: rgba(0, 0, 0, 0.8);
  width: 100%;
  height: 100%;
}
.top {
  margin-top: 5%;
  height: 100px;
}
.movie-card {
  margin: 12px;
  width: 125px;
  font-size: 12px;
  font-weight: 400;
}
.movie-card:hover {
  opacity: 0.5;
  cursor: pointer;
}
.movie-card > img {
  height: 180px;
  border-radius: 8px;
}
.movie-information {
  /* margin-top: 7px; */
}

.movie-date {
  font-size: 10px;
  margin-top: 5px;
  color: #cccccc;
}
</style>
