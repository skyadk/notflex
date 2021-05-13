import axios from 'axios';
import { setInterceptors } from './common/interceptors';

function createInstance() {
  return axios.create({
    baseURL: 'http://127.0.0.1:8000/',
  });
}

function createInstanceWithAuth() {
  const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
  });
  return setInterceptors(instance);
}

export const instance = createInstance();
export const posts = createInstanceWithAuth();
