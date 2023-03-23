<template>
<div class="container-section-highlight-3">
    <div class="container-image"></div>
    <div class="container-text">
    <h3>YX1 EARPHONES</h3>
    <primary-button/>
  </div>
</div>
</template>

<script setup>
import PrimaryButton from "./primary-button";
</script>

<style scoped>

/* Mobile */

* {
  margin: 0;
  padding: 0;
}

.container-section-highlight-3 {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container-image {
  width: 80%;
  min-width: 327px;
  height: 200px;
  border-radius: 8px;
  background-size: cover;
  background-position: center;
  background-image: url("/home/mobile/image-earphones-yx1.jpg");
  display: flex;
  justify-content: center;
  margin: 24px 24px 0 24px;
}

.container-text {
  background: #F1F1F1;
  width: 80%;
  min-width: 327px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  margin: 24px 24px 0 24px;
}

h3 {
  padding: 41px 58px 32px 24px;
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 28px;
  line-height: 38px;
  letter-spacing: 2px;
  text-transform: uppercase;
}

button {
  margin-left: 24px;
}

/* Tablet */

@media (min-width: 768px) {
  .container-section-highlight-3 {
    flex-direction: row;
    justify-content: center;
  }

  .container-image {
    height: 320px;
    background-image: url("/home/tablet/image-earphones-yx1.jpg");
    background-size: cover;
    margin-right: 5px;
  }
  .container-text {
    height: 320px;
    justify-content: center;
    margin-left: 6px;
  }
}

/* Desktop */

@media (min-width: 1200px) {

  .container-section-highlight-3 {
    flex-direction: row;
    justify-content: center;
    padding-bottom: 56px;
    margin-left: 141px;
    margin-right: 141px;
  }

  .container-image {
    width: 540px;
    height: 320px;
    margin-right: 15px;
    background-image: url("/home/desktop/image-earphones-yx1.jpg");
  }

   .container-text {
    width: 540px;
    height: 320px;
    margin-left: 15px;
  }

   h3 {
     padding-left: 95px;
   }

   button {
     margin-left: 95px;
   }

}


</style>