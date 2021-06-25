export default {
    clearUserToken() {
        if (localStorage.userToken) {
            localStorage.removeItem('userToken')
        } else if (sessionStorage.userToken) {
            sessionStorage.removeItem('userToken')
        }
    },

    setUserToken(token) {
        localStorage.setItem('userToken', token)
        sessionStorage.setItem('userToken', token)
    },

    get userToken() {
        return localStorage.userToken || sessionStorage.userToken
    },

    get isAuthorized() {
        return Boolean(this.userToken)
    }
}
