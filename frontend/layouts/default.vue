<template>
  
    <div class="z-10 overflow-hidden">
      <AppHeader />

      <Nuxt />
    </div>
  
</template>


<script>
import AppHeader from "../components/AppHeader";

export default {
  components: {
    AppHeader,
  },
};
</script>

