<template>

<header>
  <div class="container-header">
    <div class="container-content">
      <p class="label">NEW PRODUCT</p>
      <h1>{{ product.name }}</h1>
      <p class="description">Experience natural, lifelike audio and exceptional build quality made for the passionate music enthusiast.</p>
      <button>See Product</button>
    </div>
    <img class="image-desktop" src="/home/desktop/image-header.jpg">
    <img class="image-tablet" src="/home/tablet/image-header.jpg">
    <img class="image-mobile" src="/home/mobile/image-header.jpg">
  </div>
</header>


</template>

<style scoped>

@media (min-width: 1080px) {

  header {
    font-family: 'Manrope', sans-serif;
    display: flex;
    justify-content: center;
    margin: none;
    overflow-y: hidden;
  }

  .container-header {
    display: flex;
    gap: 46px;
  }

  .container-content {
    width: 398px;
    height: 346px;
    padding: 128px 0 158px 165px;
  }

  p, h1 {
    color: #ffff;
  }

  p {
    font-style: normal;
    font-weight: 500;
    font-size: 15px;
    line-height: 25px;
    mix-blend-mode: normal;
    opacity: 0.75;
  }

  .label {
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 19px;
    letter-spacing: 10px;
    text-transform: uppercase;
    mix-blend-mode: normal;
    opacity: 0.5;
  }

  h1 {
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 700;
    font-size: 56px;
    line-height: 58px;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 24px 0;
    margin: 0;
  }

  .description {
    padding-bottom: 40px;
    max-width: 349px;
  }

  button {
    background: #D87D4A;
    color: #ffff;
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 700;
    font-size: 13px;
    line-height: 18px;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 15px 30px;
    border-style: none;
  }

  img {
    position: relative;
    bottom: 12%;
  }

  .image-tablet, .image-mobile {
    display: none;
  }

}

@media (min-width: 650px) and (max-width: 1079px) {

  .container-header {
    display: flex;
    flex-flow: column;
  }

  .container-content {
    display: flex;
    flex-flow: column;
    align-items: center;
    z-index: 999;
    position: relative;
  }

  .label {
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 19px;
    text-align: center;
    letter-spacing: 10px;
    text-transform: uppercase;
    color: #FFFFFF;
    mix-blend-mode: normal;
    opacity: 0.5;
    margin: 0;
    padding-top: 108px;
  }

  h1 {
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 700;
    font-size: 36px;
    line-height: 40px;
    text-align: center;
    letter-spacing: 1.28571px;
    text-transform: uppercase;
    color: #FFFFFF;
    max-width: 50%;
    margin: 0;
    padding-top: 16px;
  }

  .description {
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 500;
    font-size: 15px;
    line-height: 25px;
    text-align: center;
    color: #FFFFFF;
    mix-blend-mode: normal;
    opacity: 0.75;
    max-width: 50%;
    padding: 24px 24px 28px 24px;
    margin: 0;
  }

  button {
    background: #D87D4A;
    color: #ffff;
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 700;
    font-size: 13px;
    line-height: 18px;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 15px 30px;
    border-style: none;
  }

  .image-desktop, .image-mobile {
    display: none;
  }

  .image-tablet {
    width: 100%;
    position: absolute;
    top: 0;
    z-index: 0;
  }

}

@media (max-width: 649px) {
  .image-desktop, .image-tablet {
    display: none;
  }

  .container-header {
    display: flex;
    flex-flow: column;
  }

  .container-content {
    display: flex;
    flex-flow: column;
    align-items: center;
    z-index: 999;
    position: relative;
  }

  .label {
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 19px;
  text-align: center;
  letter-spacing: 10px;
  text-transform: uppercase;
  color: #FFFFFF;
  mix-blend-mode: normal;
  opacity: 0.5;
  margin: 0;
  padding-top: 108px;
  }

  h1 {
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 700;
    font-size: 36px;
    line-height: 40px;
    text-align: center;
    letter-spacing: 1.28571px;
    text-transform: uppercase;
    color: #FFFFFF;
    margin: 0;
    padding-top: 16px;
  }

  .description {
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 500;
    font-size: 15px;
    line-height: 25px;
    text-align: center;
    color: #FFFFFF;
    mix-blend-mode: normal;
    opacity: 0.75;
    max-width: 80%;
    padding: 24px 24px 28px 24px;
    margin: 0;
  }

  button {
    background: #D87D4A;
    color: #ffff;
    font-family: 'Manrope';
    font-style: normal;
    font-weight: 700;
    font-size: 13px;
    line-height: 18px;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 15px 30px;
    border-style: none;
  }

  .image-mobile {
    width: 100%;
    position: absolute;
    top: 5%;
    z-index: 0;
  }


}



</style>

<script setup>
const { data: product } = await useFetch('http://127.0.0.1:8000/api/products/6/')
</script>
