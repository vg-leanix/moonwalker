<template>
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
    <div class=" w-full h-full p-5">
      <form action="" class="flex flex-col items-center" v-on:submit.prevent="">
        <div class="w-1/2">
          
          <div class="mt-1 relative rounded-md shadow-sm">
            <label for="instance" class="block text-sm font-medium text-gray-700">Choose an instance:</label>

            <select name="instance" id="instance" v-model="instance" class="
                focus:ring-indigo-500
                focus:border-indigo-500
                block
                pl-7
                pr-12
                sm:text-sm
                border-gray-300
                rounded-md
                p-2
                w-full">
                
              <option v-for="key in this.$store.state.hostOptions" :key="key">{{key}}</option>
              

              
            </select>
          </div>
          <div class="mt-6 relative rounded-md shadow-sm">
            <label for="wsEdition" class="block text-sm font-medium text-gray-700">Choose an workspace edition:</label>

            <select name="wsEdition" v-model="edition" id="mtmToken" class="
                focus:ring-indigo-500
                focus:border-indigo-500
                block
                pl-7
                pr-12
                sm:text-sm
                border-gray-300
                rounded-md
                p-2
                w-full">
                
              <option v-for="key in this.$store.state.wsOptions" :key="key">{{key}}</option>
              

              
            </select>
          </div>
        </div>
        <div class="w-1/2">
          <label
            for="price"
            class="block text-sm font-medium text-gray-700 mt-6"
            >Enter Superadmin MTM Token:</label
          >
          <div class="mt-1 relative rounded-md shadow-sm">
            <input
              type="password"
              name="MtmToken"
              id="MtmToken"
              v-model="mtmToken"
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

        <button class="mt-6 bg-white rounded-md py-2 w-1/4" type="submit">
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
      edition: "",
      mtmToken: "",
      instance: "",
      
      
    };
  },
  methods: {
      updateMtmToken(){
          this.$store.commit('changeMtmToken',this.mtmToken)
      }
  },
  mounted() {
      console.log(this)
  },
};
</script>

<style>
</style>