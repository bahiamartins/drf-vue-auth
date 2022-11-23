import store from '@/stores/index'

export default function authHeader() {

    let token = store.state.authUser.accessToken
  
    if (token) {
      return { Authorization: 'Bearer ' + token };
    } else {
      return {};
    }
  }