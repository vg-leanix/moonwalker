<template>
  <div>
    <div v-if="showAlert">
      <div
        v-if="alertType == 'success'"
        class="
          animate__animated animate__bounceOutLeft
          mt-14
          shadow-md
          flex
          w-auto
          z-10
          bg-green-400
          p-4
          opacity-90
          h-auto
          items-center
          fixed
          right-0
          top-8
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
    </div>
  </div>
</template>

<script>
export default {
  name: "alert",
  props: ["alertType"],
  transition: "bc",
  data() {
    return {
      showAlert: true,
    };
  },

  methods: {
    hideAlert(type) {
      this.showAlert = false;

      if (type == "success") {
        this.$store.commit("deleteApiSuccess");
      }
    },
  },

  mounted() {
    setTimeout(this.hideAlert, 4000,this.alertType );
  },
};
</script>

<style>
</style>