<template>
  <div v-for="category in categories" class="container">
    <img :src="category.image" :alt="category.name">
    <div class="container-content">
      <p class="label">{{ category.name }}</p>
      <button>SHOP<svg width="8" height="12" xmlns="http://www.w3.org/2000/svg"><path d="M1.322 1l5 5-5 5" stroke="#D87D4A" stroke-width="2" fill="none" fill-rule="evenodd"/></svg></button>
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
  width: 350px;
  height: 284px;
  border: solid red;
  display: flex;
  flex-flow: column;
  text-align: center;
}

.container-content {
  width: 350px;
  height: 204px;
  background-color: #F1F1F1;
  border-radius: 8px;
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
}

.container-content {
  display: flex;
  flex-flow: column;
  align-items: center;
}

button {
  font-family: 'Manrope';
  font-style: normal;
  font-weight: 700;
  font-size: 13px;
  line-height: 18px;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #000000;
  mix-blend-mode: normal;
  opacity: 0.5;
  border: none;
  display: flex;
  gap: 13px;
  align-items: center;
}

</style>