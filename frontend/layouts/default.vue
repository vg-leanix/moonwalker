<template>
  
    <div class="">
      <AppHeader />
      <div
      class="z-20"
      @click="openTooltip"
      
      :class="{
        'bg-gray-800 ': this.$store.state.superAdminToolTip,
        'bg-opacity-50': this.$store.state.superAdminToolTip,
        'fixed':this.$store.state.superAdminToolTip,
        'w-full':this.$store.state.superAdminToolTip,
        'h-full':this.$store.state.superAdminToolTip
      }"
    ></div>

      <Nuxt />
    </div>
  
</template>


<script>
import AppHeader from "../components/AppHeader";

export default {
  components: {
    AppHeader,
  },
  methods: {
    openTooltip() {
      this.$store.commit("setTooltipSuperAdmin");
    }
  },
};
</script>

