<template>
  <div class="d-flex  movielist" v-if="movieList">
    <div class="movie-card" style="width:125px;" v-for="li in movieList" :key="li.id">
      <div @click="goDetail(li.id)" v-if="li">
        <img style="width:125px; height:180px;" v-if="li.poster_path" fluid :src="image(li.poster_path)" alt="Image 2" />
        <img style="width:125px; height:180px;" v-else fluid :src="noImage" alt="Image 2" />
        <div class="movie-information">
          <div class="movie-title">{{ li.title }}</div>
          <div class="movie-date" v-if="li.release_date">{{ li.release_date.split('-')[0] }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['movieList'],
  data() {
    return {
      noImage: require('../assets/noimg.png'),
    };
  },
  methods: {
    image(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`;
    },
    goDetail(id) {
      // console.log(id);
      this.$router.push(`detail/${id}`);
    },
  },
};
</script>

<style scoped>
.movielist {
  /* justify-content: space-between; */
  margin: 5%;
  overflow-x: auto;
}

.movie-card {
  margin: 12px;
  min-width: 125px;
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
  margin-top: 7px;
}
.movie-title {
  font-weight: 1000;
  color: #333;
}
.movie-date {
  font-size: 10px;
  margin-top: 5px;
  /* color: #cccccc; */
  font-weight: 1000;
  color: #333;
}
::-webkit-scrollbar {
  width: 12px;
}
::-webkit-scrollbar-thumb {
  background: linear-gradient(transparent, #333);
  border-radius: 6px;
}
::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(transparent, #fff);
  border-radius: 6px;
}
</style>
