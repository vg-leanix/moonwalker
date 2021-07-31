<template>
  <div
    class="
      w-full
      flex-row
      justify-center
      h-full
      min-h-screen
      py-12
      px-6
      bg-gray-300 bg-opacity-50
      font-lix
      overflow-hidden
    "
  >
    <!-- Step Overview -->
    <div data-theme="vg" class="flex w-full h-full p-5">
      <ul class="steps w-full">
        <li
          :class="stepOne"
          class="step"
          v-if="!this.$store.state.firstStepError"
        >
          Create Workspace
        </li>
        <li
          v-if="this.$store.state.firstStepError"
          :class="{ 'step-error': this.$store.state.firstStepError }"
          class="step"
          data-content="✕"
        >
          Create Workspace
        </li>

        <li
          :class="stepTwo"
          class="step"
          v-if="!this.$store.state.secondStepError"
        >
          Provision Data Model
        </li>
        <li
          v-if="this.$store.state.secondStepError"
          :class="{ 'step-error': this.$store.state.secondStepError }"
          class="step"
          data-content="✕"
        >
          Provision Data Model
        </li>
        <li
          :class="stepThree"
          class="step"
          v-if="!this.$store.state.thirdStepError"
        >
          Upload Processors
        </li>
        <li
          v-if="this.$store.state.thirdStepError"
          :class="{ 'step-error': this.$store.state.thirdStepError }"
          class="step"
          data-content="✕"
        >
          Upload Processors
        </li>
      </ul>
    </div>

    <!-- Input Form -->
    <div class="w-full h-full p-5">
      <form
        class="flex flex-col items-center"
        v-on:submit.prevent=""
        v-on:submit="sendConfig"
      >
        <div class="w-1/2">
          <!-- Instance Selector -->
          <div class="mt-1 relative rounded-md shadow-sm">
            <label
              for="instance"
              class="block text-sm font-medium text-gray-700"
              >Choose an instance:</label
            >

            <select
              name="instance"
              required
              :disabled="this.$store.state.firstStep"
              id="instance"
              v-model="instance"
              class="
                focus:ring-indigo-500
                focus:border-indigo-500
                block
                pl-7
                pr-12
                sm:text-sm
                border-gray-300
                rounded-md
                p-2
                w-full
              "
            >
              <option v-for="key in this.$store.state.hostOptions" :key="key">
                {{ key }}
              </option>
            </select>
          </div>

          <!-- Workspace Name Selector -->
          <div class="mt-6 relative rounded-md shadow-sm">
            <label
              for="workspaceName"
              class="block text-sm font-medium text-gray-700"
              >Choose a workspace name:</label
            >

            <input
              name="workspaceName"
              v-model="workspaceName"
              id="workspaceName"
              :class="{
                'bg-gray-100': !this.$store.state.showCreateWS,
                'text-gray-600': !this.$store.state.showCreateWS,
              }"
              required
              :disabled="this.$store.state.firstStep"
              class="
                focus:ring-indigo-500
                focus:border-indigo-500
                block
                pl-7
                pr-12
                sm:text-sm
                border-gray-300
                rounded-md
                p-2
                w-full
              "
            />
          </div>
        </div>

        <!-- API Token Select -->
        <div class="w-1/2" v-if="this.$store.state.showCreateWS">
          <label
            for="apiToken"
            class="block text-sm font-medium text-gray-700 mt-6"
            >Enter Superadmin API Token:</label
          >
          <div class="mt-1 relative rounded-md shadow-sm">
            <input
              type="password"
              name="apiToken"
              id="apiToken"
              required
              v-model="apiToken"
              class="
                focus:ring-indigo-500
                focus:border-indigo-500
                block
                pl-7
                pr-12
                sm:text-sm
                border-gray-300
                rounded-md
                p-2
                w-full
              "
              placeholder=""
            />
          </div>
        </div>

        <!-- Workspace Edition Selector -->
        <div class="w-1/2" v-if="!this.$store.state.showCreateWS">
          <div class="mt-6 relative rounded-md shadow-sm">
            <label
              for="wsEdition"
              class="block text-sm font-medium text-gray-700"
              >Choose an workspace edition:</label
            >

            <select
              name="wsEdition"
              v-model="edition"
              id="wsEdition"
              required
              class="
                focus:ring-indigo-500
                focus:border-indigo-500
                block
                pl-7
                pr-12
                sm:text-sm
                border-gray-300
                rounded-md
                p-2
                w-full
              "
            >
              <option v-for="key in this.$store.state.wsOptions" :key="key">
                {{ key }}
              </option>
            </select>
          </div>
        </div>

        <!-- Error Message -->
        <div
          v-show="this.$store.state.apiErrorCode"
          class="flex flex-col mt-6 w-1/2 bg-red-600 rounded-md h-auto p-4"
        >
          <p class="font-bold text-white">Error</p>
          <div
            class="flex flex-wrap w-full bg-gray-100 rounded-md opacity-80 p-3"
          >
            <pre class="text-black text-xs font-light w-full">
              {{ this.$store.state.apiError }}
            </pre>
          </div>
        </div>

        <!-- Success Message -->
        <!-- <apiMessage
          v-if="this.$store.state.apiSuccess"
          :alertType="this.$store.state.apiMessageType"
        /> -->

        <!-- Create Workspace Button -->
        <button
          data-theme="vg"
          v-if="this.$store.state.showCreateWS"
          :class="{ loading: this.$store.state.apiBusy }"
          class="mt-6 btn btn-primary rounded-md py-2 w-1/4 btn"
          type="submit"
        >
          Create Workspace
        </button>

        <!-- Install Workspace -->
        <button
          data-theme="vg"
          v-if="!this.$store.state.showCreateWS"
          class="btn btn-primary mt-6 rounded-md py-2 w-1/4"
          :class="{ loading: this.$store.state.apiBusy }"
          type="submit"
        >
          Install Edition
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import apiMessage from "./apiMessage.vue";
export default {
  components: {
    apiMessage,
  },

  name: "settings",
  data() {
    return {};
  },
  methods: {
    sendConfig() {
      let apiBusy = this.$store.state.apiBusy;

      // dont allow for click bashing
      if (!apiBusy) {
        if (this.$store.state.firstStep) {
          // if workspace has already been created

          this.$store.dispatch("sendConfig");
        } else {
          // if workspace has not already been created
          this.$store.dispatch("sendWorkspace");
        }
      }
    },
  },
  computed: {
    stepOne: function () {
      return {
        "step-primary": this.$store.state.firstStep,
      };
    },
    stepTwo: function () {
      return {
        "step-primary": this.$store.state.secondStep,
      };
    },
    stepThree: function () {
      return {
        "step-primary": this.$store.state.thirdStep,
      };
    },

    instance: {
      get() {
        return this.$store.state.workspace.instance;
      },
      set(value) {
        this.$store.commit("updateInstance", value);
      },
    },

    workspaceName: {
      get() {
        return this.$store.state.workspace.workspaceName;
      },
      set(value) {
        this.$store.commit("updateWorkspaceName", value);
      },
    },

    edition: {
      get() {
        return this.$store.state.installParams.edition;
      },
      set(value) {
        this.$store.commit("updateWorkspaceEdition", value);
      },
    },

    apiToken: {
      get() {
        return this.$store.state.workspace.apiToken;
      },
      set(value) {
        this.$store.commit("updateApiToken", value);
      },
    },
  },
};
</script>

<style>
</style>