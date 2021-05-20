import axios from 'axios';
import { setInterceptors } from './common/interceptors';

function createInstance() {
  return axios.create({
    // baseURL: 'http://127.0.0.1:8000/',
    baseURL: 'http://k4d108.p.ssafy.io:8000/',
    headers: { 'Content-Type': 'application/json' },
  });
}

function createInstanceWithAuth() {
  const instance = axios.create({
    // baseURL: 'http://127.0.0.1:8000/',
    baseURL: 'http://k4d108.p.ssafy.io:8000/',
    headers: { 'Content-Type': 'application/json' },
  });
  return setInterceptors(instance);
}

export const instance = createInstance();
export const posts = createInstanceWithAuth();
