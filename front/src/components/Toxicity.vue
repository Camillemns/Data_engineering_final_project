<template>
  <div id="container" class="container">
    <div class="row mb-5">
      <div class="col-12">
        <h1>Toxicity analyzer</h1>
      </div>
    </div>
    <div class="row mb-5">
      <div class="col-12 col-md-8 offset-md-2">
        <div id="form">
          <div class="form-floating mb-4">
            <textarea
                class="form-control"
                v-model="message"
                placeholder="Enter your sentence"
                id="floatingTextarea2"
                style="height: 100px"
                :class="`${message ? 'has-text' : ''}`"
            ></textarea>
            <label for="floatingTextarea2">Enter your sentence</label>
          </div>
          <button
              v-on:click="submit"
              class="btn btn-custom px-5 py-2 rounded-pill"
              :disabled="submitting"
          >
            <span
                v-if="submitting"
                class="spinner-border text-light"
                role="status"
            >
              <span class="visually-hidden">Loading...</span>
            </span>
            <span v-else>Predict</span>
          </button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <div v-if="error" id="error">An error happened</div>
        <div v-else-if="result" id="result">
          <h4 class="fw-bold mb-2">Toxicity statitics :</h4>
          <div v-for="(proba, label) in result" :key="proba">
            <span class="fw-bold text-capitalize">{{ stringify(label) }}</span> : {{ toPercentage(proba) }}%
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { ref } from "vue";
import axios from "axios";

export default {
  name: "Toxicity",
  setup() {
    const result = ref(null);
    const message = ref("");
    const submitting = ref(false);
    const error = ref(false);

    return {
      message,
      result,
      submitting,
      error,
    };
  },
  methods: {
    async submit() {
      this.result = "";
      this.error = false;
      this.submitting = true;
      try {
        const response = await axios.post("http://localhost:8000/get_toxicity", {
          text: this.message,
        });
        this.result = response.data.result;
        this.submitting = false;
      } catch (e) {
        this.error = true;
        this.submitting = false;
      }
    },
    stringify(label) {
      return label.replace(/_/g, " ")
    },
    toPercentage(proba) {
      return (proba * 100).toFixed(2)
    }
  },
};
</script>


<style scoped>
.container {
  padding-top: 100px;
}

.btn-custom {
  background: #24cc88 !important;
  border-color: #24cc88 !important;
  color: #fff !important;
}

textarea.has-text {
  border: 3px solid #24cc88 !important;
}
</style>