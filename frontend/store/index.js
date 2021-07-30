export const state = () => ({
  wsOptions: ['Microservice Intelligence - Base',
    'Microservice Intelligence - Base V2',
    'Microservice Intelligence - Github',
    'Microservice Intelligence - Kubernetes',
    'Microservice Intelligence - SonarQube',
    'Showcase - All'],
  hostOptions: ['demo-eu'],
  mtmToken: "",
  wsToken: "",
  apiBusy: false,
  apiErrorCode: false,
  apiError: "",
  apiSuccess: false,
  apiSuccessMessage: "",
  showSubmit: true,
  firstStep: false,
  secondStep: false,
  thirdStep: false,
  firstStepError: false,
  secondStepError: false,
  thirdStepError: false,




})


export const mutations = {


  changeApiError(state, error) {
    state.apiError = JSON.stringify(JSON.parse(error), null, 4)
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
  },

  setFirstStep(state) {
    state.firstStep = true
    state.firstStepError = false
  },
  setSecondStep(state) {
    state.secondStep = true
    state.secondStepError = false
  },
  setThirdStep(state) {
    state.thirdStep = true
    state.thirdStepError = false
  },
  setFirstStepError(state) {
    state.firstStepError = true
  },
  setSecondStepError(state) {
    state.secondStepError = true
  },
  setThirdStepError(state) {
    state.thirdStepError = true
  }

}

export const actions = {
  updateList: ({ commit }, payload) => {
    commit('updateList', payload);
  },

  // API Calls //


  async sendConfig({ commit }, payload) {

    // let configJson = JSON.stringify(payload)

    var config = {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },

    };
    commit('setApiBusy')
    const send = await this.$axios.$post('/createws', payload, config)
      .then((res) => {


        if (res.status_code_int_api == 200 || res.status_code_int_api == 204) {

          commit('changeApiSuccess');
          commit('setFirstStep')
          commit('setApiReady')
        }

      })
      .catch((err) => {
        if (err.response.status == 400) {
          console.log(err.response.data)
          commit('changeApiError', err.response.data.detail);
          commit('setFirstStepError')
          commit('setApiReady')
        }




      })

  }



}