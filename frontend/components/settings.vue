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
          :class="{'step-error':this.$store.state.firstStepError}"
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
          :class="{'step-error':this.$store.state.secondStepError}"
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
          :class="{'step-error':this.$store.state.thirdStepError}"
          class="step"
          data-content="✕"
          
        >
          Upload Processors
        </li>
      </ul>
    </div>
    <div class="w-full h-full p-5">
      <form
        class="flex flex-col items-center"
        v-on:submit.prevent=""
        v-on:submit="sendConfig"
        @input="capitalizeLetter"
      >
        <div class="w-1/2">
          <div class="mt-1 relative rounded-md shadow-sm">
            <label
              for="instance"
              class="block text-sm font-medium text-gray-700"
              >Choose an instance:</label
            >

            <select
              name="instance"
              required
              id="instance"
              v-model="workspace.instance"
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
          <div class="mt-6 relative rounded-md shadow-sm">
            <label
              for="wsEdition"
              class="block text-sm font-medium text-gray-700"
              >Choose an workspace edition:</label
            >

            <select
              name="wsEdition"
              v-model="workspace.edition"
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
          <div class="mt-6 relative rounded-md shadow-sm">
            <label for="workspaceName" class="block text-sm font-medium text-gray-700"
              >Choose a workspace name:</label
            >

            <input
              name="workspaceName"
              v-model="workspace.workspaceName"
              id="workspaceName"
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
            />
          </div>
        </div>

        <div class="w-1/2">
          <label
            for="apiToken"
            class="block text-sm font-medium text-gray-700 mt-6"
            >Enter Technical User API Token:</label
          >
          <div class="mt-1 relative rounded-md shadow-sm">
            <input
              type="password"
              name="apiToken"
              id="apiToken"
              required
              v-model="workspace.apiToken"
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
        <div
          v-show="this.$store.state.apiErrorCode"
          class="flex flex-col mt-6 w-1/2 bg-red-600 rounded-md h-auto p-4"
        >
          <p class="font-bold text-white">Error</p>
          <div
            class="flex flex-wrap w-full bg-gray-100 rounded-md opacity-80 p-3"
          >
            <p class="text-black text-xs font-light">
              {{this.$store.state.apiError}}
            </p>
          </div>
        </div>
        <div
          v-show="this.$store.state.apiSuccess"
          class="
            mt-6
            flex
            w-1/2
            bg-green-400
            p-4
            opacity-80
            h-auto
            items-center
          "
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6 stroke-current text-white"
            fill="none"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <p
            class="
              text-white text-lg
              flex
              justify-left
              ml-6
              items-center
              text-justify
              w-full
              font-semibold
            "
          >
            {{ this.$store.state.apiSuccessMessage }}
          </p>
        </div>
        <button
          v-show="this.$store.state.showSubmit && !this.$store.state.apiBusy"
          class="mt-6 bg-white rounded-md py-2 w-1/4"
          type="submit"
        >
          Create Workspace
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "settings",
  data() {
    return {
      workspace: {
        instance: "",
        apiToken: "DJHVwgKQS4sswPZPrUtLbamVHD6xFueGcjwpQkO3",
        workspaceName:"",
      },
      config:{
        // CONTINUE HERE
      }
    };
  },
  methods: {
    sendConfig() {
      this.$store.dispatch("sendConfig", this.config);
    },
    capitalizeLetter() {
      if (this.config.workspaceName) {
        this.config.workspaceName = this.config.workspaceName
          .replace("[^A-Za-z]/g", "")
          .replace(" ", "")
          .replace("/d/g", "");
        this.config.workspaceName = this.config.workspaceName.toUpperCase();
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
        "step-primary": this.$store.state.thirdStep
        
      };
    },
  },
};
</script>

<style>
</style>