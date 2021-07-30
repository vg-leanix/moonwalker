<template>
<div>
  <div
    class="
      w-full
      flex
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
    <div class="w-full h-full p-5">
      <form
        class="flex flex-col items-center"
        v-on:submit.prevent=""
        v-on:submit="sendConfig"
      >
        <div class="w-1/2">
          <div class="mt-1 relative rounded-md shadow-sm">
            <label
              for="instance"
              class="block text-sm font-medium text-gray-700"
              >Choose the instance on which WS exists:</label
            >

            <select
              name="instance"
              id="instance"
              v-model="config.instance"
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
              for="wsExtension"
              class="block text-sm font-medium text-gray-700"
              >Choose provisioning extension to be applied:</label
            >

            <select
              name="wsExtension"
              v-model="config.extension"
              id="mtmToken"
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
              <option v-for="key in this.$store.state.extensionOptions" :key="key">
                {{ key }}
              </option>
            </select>
          </div>
        </div>

        <div class="w-1/2">
          <label
            for="apiToken"
            class="block text-sm font-medium text-gray-700 mt-6"
            >Enter API Token created on WS (superadmin):</label
          >
          <div class="mt-1 relative rounded-md shadow-sm">
            <input
              type="password"
              name="apiToken"
              id="apiToken"
              v-model="config.apiToken"
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
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book. It has
              survived not only five centuries, but also the leap into
              electronic typesetting, remaining essentially unchanged. It was
              popularised in the 1960s with the release of Letraset sheets
              containing Lorem Ipsum passages, and more recently with desktop
              publishing software like Aldus PageMaker including versions of
              Lorem Ipsum.
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
</div>
</template>

<script>

export default {
  name: "settings",
  data() {
    return {
      config: {
        extension: "",
        host: "",
        apiToken: "",
        addBaseModel: false
      },
    };
  },
  methods: {
    sendConfig() {
      if(this.config.extension.contains('mi-')){
        this.config.addBaseModel = true
      }
      this.$store.dispatch("sendConfig", this.config);
    },
    capitalizeLetter() {
      

      if (this.config.wsName) {
        this.config.wsName = this.config.wsName.replace("[^A-Za-z]/g", "").replace(" ","").replace("/\d/g","")
        this.config.wsName = this.config.wsName.toUpperCase();
        
        
      }
    },
  },
  mounted() {
    
  },
};
</script>

<style>
</style>