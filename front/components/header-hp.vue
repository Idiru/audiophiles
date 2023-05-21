<template>
  <div class="container">
    <div class="container-text">
      <p><span>NEW PRODUCT</span></p>
      <h1>XX99 Mark II Headphones</h1>
      <p class="description">Experience natural, lifelike audio and exceptional build quality made for the passionate music enthusiast.</p>
      <button>See Product</button>
    </div>
    <div class="container-image"></div>
  </div>
</template>

<style scoped>

/** Mobile **/
* {
  margin: 0;
  padding: 0;
}

.container {
  background-image: url("/home/mobile/image-header.jpg");
  height: 510px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-items: center;
  justify-content: center;
  text-align: center;
  background-position: bottom;
}

h1 {
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 36px;
  line-height: 40px;
  text-align: center;
  color: #FFFFFF;
  letter-spacing: 1.28571px;
  text-transform: uppercase;
  padding-bottom: 25px;
  padding-top: 16px;
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
}

.description {
  padding-bottom: 28px;

}

span {
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
}

button {
  background: #D87D4A;
  padding: 15px 30px;
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 13px;
  line-height: 18px;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #FFFFFF;
  border: none;
}

</style>


