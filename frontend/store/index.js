export const state = () => ({
  extensionOptions: {'mi-base': 'MI - base','k8s': 'MI K8s','gh': 'MI Github','sq': 'MI Soanrqube','mi-k8s': 'MI with K8s', 'mi-gh': 'MI with Github','mi-sq': 'MI with Sonarqube'},
  hostOptions: ['demo-eu','demo-eu-1'],
  isLoading: false,
  apiErrorCode: false,
  apiError: "",
  apiSuccess: false,
  apiSuccessMessage: "",
  showSubmit: true

})


export const mutations = {
  toggleDropdownOn(state) {
    state.isDropdownVisible = true
    const body = document.getElementsByTagName('body')[0];
    body.classList.add("overflow-hidden")
  },

  changeApiError(state, error) {
    state.apiError = error
    state.apiErrorCode = true

  },
  changeApiSuccess(state) {
    state.apiSuccess = true
    state.apiSuccessMessage = "Extension sucessfully applied. Enjoy!"
    state.showSubmit = false
  },

  setLoading(val) {
    state.isLoading = val
  }

}

export const actions = {
  updateList: ({ commit }, payload) => {
    commit('updateList', payload);
  },

  // API Calls //
  
  async sendConfig({ commit }, payload) {
    const finalPayload = {
      extension:[payload.extension],
      host: payload.host,
      apiToken:payload.apiToken,
      addBaseModel:payload.addBaseModel
    }

    // let configJson = JSON.stringify(payload)
    console.log(payload)
    var config = {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },

    };
    commit('setLoading', true)
    const send = await this.$axios.$post('/createws', finalPayload, config)
      .then((res) => {

        if (res.status == 200) {

          commit('changeApiSuccess');
          commit('setLoading', false)
        }

        else if (res.status == 400) {
          let stringErr = "400 error"
          commit('changeApiError', stringErr);
        }
      })
      .catch((res) => {

        let stringErr = String(err)

        commit('changeApiError', stringErr);
        commit('setLoading', false)
      })

  }



}