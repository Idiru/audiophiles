<template>
<div class="container">
    <div v-for="category in categories" class="container-product">
    <div class="container-content">
      <div>
        <img :src="category.image" :alt="category.name">
      </div>
      <div class="container-text">
        <p class="label">{{ category.name }}</p>
        <button>SHOP<svg width="8" height="12" xmlns="http://www.w3.org/2000/svg"><path d="M1.322 1l5 5-5 5" stroke="#D87D4A" stroke-width="2" fill="none" fill-rule="evenodd"/></svg></button>
      </div>
    </div>
  </div>
</div>

</template>

<script setup>

const categories = [
  {
    name: "headphones",
    image: "/shared/desktop/image-category-thumbnail-headphones.png"
  },

  {
    name: "speakers",
    image: "/shared/desktop/image-category-thumbnail-speakers.png"
  },

  {
    name: "earphones",
    image: "/shared/desktop/image-category-thumbnail-earphones.png"
  }
]

/*
const fileName = this.categorie.toLowerCase()

return require(`~/assets/shared/desktop/${fileName}.png`)
*/

</script>

<style scoped>

.container {
  display: flex;
  text-align: center;
  gap: 10px;

}

.container-product {
  width: 350px;
  height: 284px;
  display: flex;
  flex-flow: column;
  text-align: center;
  margin-top: 30px;
}

img {
  position: relative;
  z-index: 999;
  width: 70%;
}

.container-content {
  display: flex;
  flex-flow: column;
  align-items: center;
  justify-content: flex-end;
  z-index: 0;
}

.container-text {
  width: 350px;
  height: 174px;
  margin-top: -40%;
  padding-bottom: 30px;
  background-color: #F1F1F1;
  border-radius: 8px;
  position: relative;
  display: flex;
  flex-flow: column;
  align-items: center;
  justify-content: flex-end;
}

.label {
  padding-bottom: 16px;
}

p {
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 18px;
  line-height: 25px;
  text-align: center;
  letter-spacing: 1.28571px;
  text-transform: uppercase;
  padding: 0;
  margin: 0;
}


button {
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 13px;
  line-height: 18px;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #797979;
  mix-blend-mode: normal;
  border: none;
  display: flex;
  gap: 13px;
  align-items: center;
}

@media (max-width: 1080px) {
  .container {
    width: 327px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
    position: relative;

  }

}

</style>