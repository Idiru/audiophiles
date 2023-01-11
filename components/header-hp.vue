<template>

<header>
  <div class="container-header">
    <div class="container-content">
      <p class="label">NEW PRODUCT</p>
      <h1>XX99 Mark II Headphones</h1>
      <p class="description">Experience natural, lifelike audio and exceptional build quality made for the passionate music enthusiast.</p>
      <button>See Product</button>
    </div>
    <img src="~/assets/home/desktop/bitmap.png">
  </div>
</header>


</template>

<style scoped>

header {
  font-family: 'Manrope', sans-serif;
  display: flex;
  justify-content: center;
  margin: none;
}

.container-header {
  display: flex;
}

.container-content {
  width: 398px;
  height: 346px;
  padding: 128px;
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

</style>
