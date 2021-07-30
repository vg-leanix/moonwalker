export const state = () => ({
  extensionOptions: [
    { key: "mi-base", value: "MI - base" },
    { key: "mi-k8s", value: "MI K8s" },
    { key: "mi-gh", value: "MI Github" },
    { key: "mi-sq", value: "MI Sonarqube" },
    { key: "mi-and-k8s", value: "MI with K8s" },
    { key: "mi-and-gh", value: "MI with Github" },
    { key: "mi-and-sq", value: "MI with Sonarqube" }
  ],
  hostOptions: ["demo-eu", "demo-eu-1"],
  isLoading: false,
  apiErrorCode: false,
  apiError: "",
  apiSuccess: false,
  apiSuccessMessage: "",
  showSubmit: true
});

export const mutations = {
  toggleDropdownOn(state) {
    state.isDropdownVisible = true;
    const body = document.getElementsByTagName("body")[0];
    body.classList.add("overflow-hidden");
  },

  changeApiError(state, error) {
    state.apiError = error;
    state.apiErrorCode = true;
  },
  changeApiSuccess(state) {
    state.apiSuccess = true;
    state.apiSuccessMessage = "Extension sucessfully applied. Enjoy!";
    state.showSubmit = false;
  },

  setLoading(val) {
    state.isLoading = val;
  }
};

export const actions = {
  updateList: ({ commit }, payload) => {
    commit("updateList", payload);
  },

  // API Calls //

  async sendConfig({ commit }, payload) {
    const finalPayload = {
      extension: [payload.extension],
      host: payload.instance,
      apiToken: payload.apiToken,
      addBaseModel: payload.addBaseModel
    };

    var config = {
      headers: {
        "Content-Type": "application/json; charset=UTF-8"
      }
    };
    commit("setLoading", true);
    console.log("final payload", finalPayload)
    const send = await this.$axios
      .$post("/updateProvisioning", finalPayload, config)
      .then(res => {
        if (res.status == 200) {
          commit("changeApiSuccess");
          commit("setLoading", false);
        } else if (res.status == 400) {
          let stringErr = "400 error";
          commit("changeApiError", stringErr);
        }
      })
      .catch(res => {
        let stringErr = String(err);

        commit("changeApiError", stringErr);
        commit("setLoading", false);
      });
  }
};
