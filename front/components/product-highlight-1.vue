<template>
    <div class="container-section-highlight-1">
    <div class="container-content">
      <div class="product-image"></div>
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
  width: 90%;
  min-width: 327px;
  height: 600px;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.product-image {
  background-image: url("/home/mobile/image-speaker-zx9.png");
  background-position: center;
  background-size: cover;
  height: 207px;
  width: 172.25px;
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
  max-width: 280px;
}

button {
  color: #FFFFFF;
  background-color: #000000;
}

button:hover {
  background: transparent;
  color: #000000;
}

/* Tablet */

@media (min-width: 768px) {

  .container-section-highlight-1 {
  padding: 96px 40px 32px 40px;
}

  .container-content {
    width: 100%;
    padding-top: 55px;
  }

  .product-image {
    background-image: url("/home/tablet/image-speaker-zx9.png");
    background-size: contain;
    background-repeat: no-repeat;
    height: 237px;
    width: 197.21px;
  }

  h3 {
    padding-top: 64px;
    font-size: 56px;
    line-height: 58px;
  }

  p {
    padding-bottom: 40px;
  }


}

/* Desktop */

@media (min-width: 1200px) {

  .container-section-highlight-1 {
  padding: 169px 165px 48px 165px;
  }

  .container-content {
    flex-direction: row;
    justify-content: space-evenly;
    align-items: normal;
    height: 520px;
    width: 1110px;
    overflow: hidden;
  }

  .container-text {
    align-items: normal;
  }

  h3 {
    padding-top: 79px;
  }

  h3, p {
    text-align: inherit;
  }

  .product-image {
    background-image: url("/home/desktop/image-speaker-zx9.png");
    background-size: contain;
    background-repeat: no-repeat;
    height: 493px;
    width: 410px;
    top: 8%;
    position: relative;
  }

}

</style>