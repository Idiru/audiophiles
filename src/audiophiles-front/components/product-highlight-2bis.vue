<template>
  <div class="container-section-highlight-2">
    <div class="container-content">
      <div class="container-text">
        <h3>ZX7 SPEAKER</h3>
        <primary-button/>
      </div>
    </div>
  </div>
</template>

<script setup>

import PrimaryButton from "./primary-button";

</script>

<style scoped>

/* Mobile */

.container-section-highlight-2 {
  display: flex;
  justify-content: center;
}

.container-content {
  width: 80%;
  min-width: 327px;
  height: 327px;
  display: flex;
  background-image: url("/home/mobile/image-speaker-zx7.jpg");
  background-position: center;
  background-size: cover;
  border-radius: 8px;
}

.container-text {
    padding-left: 24px;
}

h3 {
  padding-top: 101px;
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 28px;
  line-height: 38px;
  letter-spacing: 2px;
  text-transform: uppercase;
}


/* Tablet */

@media (min-width: 768px) {
  .container-content {
  height: 320px;
  width: 95%;
  display: flex;
  background-image: url("/home/tablet/image-speaker-zx7.jpg");
  }

  .container-text {
    padding-left: 62px;
  }

}

/* Desktop */

@media (min-width: 1200px) {

  .container-content {
    width: 1110px;
    height: 320px;
    background-image: url("/home/desktop/image-speaker-zx7.jpg");
  }

  .container-section-highlight-2 {
    margin: 48px 165px 24px 165px;
  }

}


</style>