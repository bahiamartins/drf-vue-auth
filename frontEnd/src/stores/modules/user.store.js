export default {
    namespaced: true,
    state: {
        user: {
            first_name: null,
            last_name: null,
            email: null,
        }
    },
    mutations: {
        storeUser(state, { first_name, last_name, email }) {
            state.first_name = first_name
            state.last_name = last_name
            state.email = email
        }
    },
    actions: {
        storeUser({commit}, { first_name, last_name, email }) {
            commit('storeUser', { first_name, last_name, email })
        },
    },
    getters: {
        fullName(state) {
            return state.user.first_name + ' ' + state.user.last_name
        }
    }
}