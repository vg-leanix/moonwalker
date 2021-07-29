export const state = () => ({
  wsOptions: { 'mi-k8s': 'MI with K8s', 'mi-base': 'MI - base' },
  hostOptions: ['demo-eu'],
  mtmToken: "",
  wsToken: "",
  apiBusy: false,
  apiErrorCode: false,
  apiError: ""




})


export const mutations = {
  toggleDropdownOn(state) {
    state.isDropdownVisible = true
    const body = document.getElementsByTagName('body')[0];
    body.classList.add("overflow-hidden")
  },

  changeMtmToken(state, newToken) {
    state.mtmToken = newToken

  }

}

export const actions = {
  updateList: ({ commit }, payload) => {
    commit('updateList', payload);
  },

  // API Calls //
  async sendTask({ commit, rootState }) {

    let onBoardingDeck = JSON.stringify({
      "sections": this.state.userChoice,
      "user": rootState.auth.user,
      "user_id": rootState.auth.userID
    })
    var config = {
      headers: {
        'Content-Type': 'application/json',
      },

    };

    const send = await this.$axios.$post('/v1/pptx/pptxjob', onBoardingDeck, config)
      .then((res) => {


        if (res.status == "success") {
          let alert = {
            'alertType': 'Info',
            'alertID': 'Job triggered successfully',
            'alertColor': 'green'
          }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);

        }
        else if (res.status == "no_sections") {
          let alert = {
            'alertType': 'Sections',
            'alertID': "Please select sections",
            'alertColor': 'red'
          }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }
        else if (res.status == "pptx_exists") {
          let alert = {
            'alertType': 'Powerpoint',
            'alertID': "Looks the requested deck already exists under Downloads",
            'alertColor': 'red'
          }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }



      })
      .catch((err) => {
        let stringErr = String(err)
        let alert = {
          'alertType': 'API Error',
          'alertID': stringErr.replace('Error: ', ''),
          'alertColor': 'red'
        }
        commit('addTaskAlert', alert);
        commit('changeDownloadStatus');

      });


  },



}