<template >
  <header
    class="font-lix"
    
  
  >
  <div class="flex items-center justify-center h-20 w-screen bg-lix-main">
    <nav
      class="flex justify-center   "
    >
      <p class=" font-lix text-5xl font-thin text-gray-200">MI Workspace Setup</p>
     
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

  methods: {
    
  },
  created() {},

  
};
</script>

<style>
fontLIX {
  font-family: "Axiforma", sans-serif;
}
.solutions-enter-active {
  animation: fadeIn;
  animation-duration: 0.3s ;
}
.solutions-leave-active{
  animation: fadeOut;
  animation-duration: 0.5s ;
}

</style>