export const state = () => ({
  wsOptions: { 'mi-k8s': 'MI with K8s', 'mi-base': 'MI - base' },
  hostOptions: ['demo-eu'],
  mtmToken: "",
  wsToken: "",
  apiBusy: false,
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
    state.apiSuccessMessage = "Workspace sucessfully created. Enjoy!"
    state.showSubmit = false
  },

  setApiReady(state) {
    state.apiBusy = false
  },

  setApiBusy(state) {
    state.apiBusy = true
  }

}

export const actions = {
  updateList: ({ commit }, payload) => {
    commit('updateList', payload);
  },

  // API Calls //
  
  async sendConfig({ commit }, payload) {

    let configJson = JSON.stringify(payload)

    var config = {
      headers: {
        'Content-Type': 'application/json',
      },

    };
    commit('setApiBusy')
    const send = await this.$axios.$post('http://localhost/8000/createws', configJson, config)
      .then((res) => {

        if (res.status == 200) {

          commit('changeApiSuccess');
          commit('setApiReady')
        }

        else if (res.status == 400) {
          let stringErr = "400 error"
          commit('changeApiError', stringErr);
        }
      })
      .catch((res) => {

        let stringErr = String(err)

        commit('changeApiError', stringErr);
        commit('setApiReady')
      })

  }



}