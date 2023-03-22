<template>
    <div class="container-section-highlight-1">
    <div class="container-content">
      <div class="container-circle-1">

      </div>
      <img src="/home/mobile/image-speaker-zx9.png" alt="speaker">
      <div class="container-text">
        <h3>ZX9<br>SPEAKER</h3>
        <p>Upgrade to premium speakers that are phenomenally built to deliver truly remarkable sound.</p>
        <primary-button/>
      </div>
    </div>
  </div>

</template>

<script setup>

</script>

<style scoped>

/** Mobile **/

* {
  margin: 0;
  padding: 0;
}

.container-section-highlight-1 {
  display: flex;
  justify-content: center;
  padding: 120px 24px 24px 24px;
}

.container-content {
  display: flex;
  flex-direction: column;
  background-color: #D87D4A;
  width: 100%;
  height: 600px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

img {
  height: 207px;
}

.container-text {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h3 {
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 36px;
  line-height: 40px;
  text-align: center;
  letter-spacing: 1.28571px;
  text-transform: uppercase;
  color: #FFFFFF;
  padding-top: 32px;
}

p {
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 500;
  font-size: 15px;
  line-height: 25px;
  text-align: center;
  color: #FFFFFF;
  mix-blend-mode: normal;
  opacity: 0.75;
  padding: 24px 0;
}

button {
  color: #FFFFFF;
  background-color: #000000;
}

button:hover {
  background: transparent;
  color: #000000;
}

</style>