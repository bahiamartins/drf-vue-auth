import {getCookie, setCookie, removeCookie} from '@/shared/cookies/cookie'

export default {
    namespaced: true,
    state: {
        accessToken: getCookie('access'),
        refreshToken: getCookie('refresh')
    },
    mutations: {
        storeToken(state, { access, refresh }) {
            setCookie('access', access, { secure: true })
            setCookie('refresh', refresh, { secure: true })
            state.accessToken = access
            state.refreshToken = refresh
        },
        deleteToken (state) {
            state.accessToken = null
            state.refreshToken = null
        },
        updateToken(state, { access }) {
            setCookie('access', access, { secure: true })
            state.accessToken = access
        },
    },
    actions: {
        storeToken({commit}, { access, refresh }) {
            commit('storeToken', { access, refresh })
        },

        logoutUser(context) {
            removeCookie('access')
            removeCookie('refresh')
            context.commit('deleteToken')
        },

        refreshToken({commit}, { access }) {
            commit('updateToken', { access })
        }
    }
}