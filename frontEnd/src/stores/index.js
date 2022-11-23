import {createStore} from 'vuex'

import authUser from './modules/auth.store'
import userData from './modules/user.store'

export default createStore ({
    modules: {
        authUser,
        userData
    }
})