<template >
  <header class="font-lix antialiased">
    <div class="h-20 w-screen bg-lix-main flex items-center">
      <nav class="flex flex-row w-full justify-center items-center">
        <p
          class="
            w-4/5
            flex
            justify-center
            font-lix
            text-5xl
            font-thin
            text-gray-200
          "
        >
          Workspace Setup
        </p>
        <div class="flex w-1/5 justify-center">
          <button
            class="
              w-2/5
              font-lix
              font-bold
              hover:font-bold
              flex
              justify-center
              text-sm
              
              text-gray-200
              border border-white
              hover:bg-indigo-600
              hover:text-white
              hover:font-black
              rounded-full
            "
          >
            <a
              href="https://leanix.atlassian.net/secure/RapidBoard.jspa?rapidView=146&projectKey=CSEC&view=planning.nodetail&issueLimit=100&selectedEpic=CSEC-35"
              target="_blank"
              rel="noopener noreferrer"
              >Report Bug</a
            >
          </button>
        </div>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: "AppHeader",

  data() {
    return {};
  },

  methods: {},
  created() {},
};
</script>

<style>
fontLIX {
  font-family: "Axiforma", sans-serif;
}
.solutions-enter-active {
  animation: fadeIn;
  animation-duration: 0.3s;
}
.solutions-leave-active {
  animation: fadeOut;
  animation-duration: 0.5s;
}
</style>