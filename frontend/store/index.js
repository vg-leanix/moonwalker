export const state = () => ({
  // Form Specs
  wsOptions: ['Microservice Intelligence - Base',
    'Microservice Intelligence - Base V2',
    'Microservice Intelligence - Github',
    'Microservice Intelligence - Kubernetes',
    'Microservice Intelligence - SonarQube',
    'Showcase - All'],
  hostOptions: ['demo-eu'],


  workspace: {
    instance: "",
    apiToken: "EjFpbrBJ3ehuY8exUJcEfVcxw6KECVrTpmdz6FM4",
    workspaceName: "",
  },

  installParams: {
    techuserApiToken: "",
    edition: "",
    instance: "",
    workspaceId: "",
  },


  // API State Specs
  apiBusy: false,
  apiError: false,
  apiErrorMessage: "",
  showCreateWS: true,

  // Step Panel Specs
  firstStep: false,
  secondStep: false,
  thirdStep: false,
  firstStepError: false,
  secondStepError: false,
  thirdStepError: false,




})


export const mutations = {

  updateWorkspaceEdition(state, val) {
    state.installParams.edition = val
  },


  updateInstance(state, val) {
    state.workspace.instance = val
    state.installParams.instance = val
  },

  updateWorkspaceName(state, value) {
    let newValue = ""
    newValue = value
      .replace("[^A-Za-z]/g", "")
      .replace(" ", "")
      .replace("/d/g", "");
    state.workspace.workspaceName =
      newValue.toUpperCase();
  },

  updateApiToken(state, val) {
    state.workspace.apiToken = val
  },

  changeApiError(state, error) {
    state.apiErrorMessage = JSON.stringify(error, null, 1)
    state.apiError = true

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
    state.showCreateWS = false
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
  },
  setTechuserApiToken(state, payload) {
    state.installParams.techuserApiToken = payload
  },
  setWorkspaceId(state, payload) {
    state.installParams.workspaceId = payload
  }

}

export const actions = {
  updateList: ({ commit }, payload) => {
    commit('updateList', payload);
  },

  // API Calls //


  async installWorkspace({ commit, state }) {


    var config = {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },

    };
    commit('setApiBusy')

    let payload = state.installParams
    const send = await this.$axios.post('/v1/install', payload, config)
      .then((res) => {


        if (res.status == 200) {

          commit('changeApiSuccess');
          commit('setSecondStep')


          return this.$axios.post('/v1/proccessors', payload, config)
            .then((res) => {

              if (res.status == 200) {

                
                commit('changeApiSuccess');
                commit('setThirdStep')
                
                commit('setApiReady')

              }

            })
            .catch((res) => {
              if (err.response.status == 400) {
                console.log(err.response.data)
                commit('changeApiError', err.response.data.detail);
                commit('setThirdStepError')
                commit('setApiReady')
              }
            })

        }

      })
      .catch((err) => {
        if (err.response.status == 400) {
          console.log(err.response.data)
          commit('setSecondStepError')
          commit('changeApiError', JSON.parse(err.response.data.detail));
          commit('setApiReady')
        }




      })

  },

  async createWorkspace({ commit, state }) {

    var config = {
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },

    }
    commit('setApiBusy')
    let payload = state.workspace

    const send = await this.$axios.post('/v1/createws', payload, config)
      .then((res) => {


        if (res.status == 200) {

          let techuserApiToken = res.data.techuser.apiToken
          let workspaceId = res.data.workspace.workspaceId

          commit('setTechuserApiToken', techuserApiToken)
          commit('setWorkspaceId', workspaceId)
          commit('setFirstStep')
          commit('setApiReady')




        }


      })
      .catch((err) => {

        if (err.response.status == 400) {
          console.log(JSON.parse(err.response.data.detail))

          commit('changeApiError', JSON.parse(err.response.data.detail));
          commit('setFirstStepError')


        }




      })

  },




}