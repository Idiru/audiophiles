<template>
  <div class="hero">
    <navbar />
    <header-hp/>
  </div>
  <div class="product-category-section">
    <product-category/>
  </div>
</template>

<style>

@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;300;400;500;600;700;800&display=swap');


body {
  padding: 0;
  margin: 0;
}

nav {
  width: auto;
}

@media (min-width: 1080px) {
  .hero {
    background-color: #121212;
  }

  .product-category-section {
    padding: 120px 165px 0px 165px;
    display: flex;
    gap: 30px;
    justify-content: center;
    align-content: center;
    align-items: center;
    flex-wrap: nowrap;
  }
}


@media (max-width: 1080px) {

  .hero {
    background-color: #131313;
}

  nav {
    position: relative;
    z-index: 999;
  }

  hr {
    position: relative;
    z-index: 999;
  }

}

</style>
<script>

/*
const categoriesLinks = [

 {
    name: "headphones",
    url: "../assets/shared/desktop/image-category-thumbnail-headphones.png"
  },

  {
    name: "speakers",
    url: "../assets/shared/desktop/image-category-thumbnail-speakers.png"
  },

  {
    name: "earphones",
    url: "../assets/shared/desktop/image-category-thumbnail-earphones.png"
  }
]


 */

</script>