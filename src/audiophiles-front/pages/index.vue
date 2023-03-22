<template>
  <div class="hero">
    <navbar/>
  </div>
  <product-highlight1/>
  <product-highlight2bis/>
  <product-highlight3/>
  <photo-section/>
  <footer-section/>
</template>

<style>

@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;300;400;500;600;700;800&display=swap');


body {
  padding: 0;
  margin: 0;
}

.hero {
  padding-bottom: 100px;
}



/* Mobile */


/* Tablet */

@media (min-width: 768px) {

}


/* Desktop */

@media (min-width: 1200px) {

}


</style>
<script>
import FooterSection from "../components/footer-section";
import PhotoSection from "../components/photo-section";
import ProductHighlight3 from "../components/product-highlight-3";
import ProductHighlight2bis from "../components/product-highlight-2bis";
export default {
  components: {ProductHighlight2bis, ProductHighlight3, PhotoSection, FooterSection}
}
</script>