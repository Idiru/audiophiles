<template>
  <div class="container">
    <div class="container-image"></div>
    <div class="text">
      <h3>Bringing you the <span>best</span> audio gear</h3>
      <p>Located at the heart of New York City, Audiophile is the premier store for high end headphones, earphones, speakers, and audio accessories. We have a large showroom and luxury demonstration rooms available for you to browse and experience a wide range of our products. Stop by our store to meet some of the fantastic people who make Audiophile the best place to buy your portable audio equipment.</p>
    </div>
  </div>

</template>

<script setup>

</script>

<style scoped>

/* Mobile */

* {
  margin: 0;
  padding: 0;
}

.container {
  padding: 120px 24px;
}

.container-image {
  min-width: 327px;
  width: 80%;
  text-align: center;
  background-image: url("/shared/mobile/image-best-gear.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 327px;
  border-radius: 10px;
  margin: auto;
}

.text {
  text-align: center;
  font-family: 'Manrope';
  font-style: normal;
}

h3   {
  padding: 40px 0 32px 0;
  font-weight: 700;
  font-size: 28px;
  line-height: 38px;
  letter-spacing: 1px;
  text-transform: uppercase;
}

span {
  color: #D87D4A;
}

p {
  font-weight: 500;
  font-size: 15px;
  line-height: 25px;
  mix-blend-mode: normal;
  opacity: 0.5;
}

/* Tablet */

@media (min-width: 768px) {

  .container-image {
      background-image: url("/shared/tablet/image-best-gear.jpg");
      width: 100%;
  }

  h3 {
    font-size: 40px;
  }

}

/* Desktop */

@media (min-width: 1200px) {

  .container {
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    gap: 125px;
    margin-right: 125px;
    margin-left: 125px;
  }

  .container-image {
    background-image: url("/shared/desktop/image-best-gear.jpg");
    width: 540px;
    height: 588px;
    margin: 0;

  }

  .text {
    text-align: initial;
    max-width: 445px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

}

</style>