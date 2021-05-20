import { instance } from './index';

function viewList(uuid) {
  return instance.get(`my_view_list/${uuid}/`);
}

function preferPerGenre(uuid) {
  return instance.post('my_preferGenre_list/', uuid);
}

function genreRecommend(genre) {
  return instance.post('genre_recommend/', genre);
}

function evaluate(data) {
  return instance.post(`add_my_view_list/`, data);
}
export { viewList, preferPerGenre, genreRecommend, evaluate };
