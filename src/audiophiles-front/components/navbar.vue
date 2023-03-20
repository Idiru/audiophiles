<template>
  <nav>
    <div class="container">
      <img class="burger-menu" src="/shared/tablet/icon-hamburger.svg" alt="burger menu">
      <div class="sub-navbar">
        <img class="logo" src="/shared/desktop/logo.svg" alt="logo navbar">
      </div>
      <ul class="categories">
        <li v-for="category in categories">{{ category.name }}</li>
      </ul>
      <svg class="icon-cart" width="23" height="20" xmlns="http://www.w3.org/2000/svg"><path d="M8.625 15.833c1.132 0 2.054.935 2.054 2.084 0 1.148-.922 2.083-2.054 2.083-1.132 0-2.054-.935-2.054-2.083 0-1.15.922-2.084 2.054-2.084zm9.857 0c1.132 0 2.054.935 2.054 2.084 0 1.148-.922 2.083-2.054 2.083-1.132 0-2.053-.935-2.053-2.083 0-1.15.92-2.084 2.053-2.084zm-9.857 1.39a.69.69 0 00-.685.694.69.69 0 00.685.694.69.69 0 00.685-.694.69.69 0 00-.685-.695zm9.857 0a.69.69 0 00-.684.694.69.69 0 00.684.694.69.69 0 00.685-.694.69.69 0 00-.685-.695zM4.717 0c.316 0 .59.215.658.517l.481 2.122h16.47a.68.68 0 01.538.262c.127.166.168.38.11.579l-2.695 9.236a.672.672 0 01-.648.478H7.41a.667.667 0 00-.673.66c0 .364.303.66.674.66h12.219c.372 0 .674.295.674.66 0 .364-.302.66-.674.66H7.412c-1.115 0-2.021-.889-2.021-1.98 0-.812.502-1.511 1.218-1.816L4.176 1.32H.674A.667.667 0 010 .66C0 .296.302 0 .674 0zm16.716 3.958H6.156l1.797 7.917h11.17l2.31-7.917z" fill="#FFF" fill-rule="nonzero"/></svg>
    </div>
    <hr>
  </nav>

</template>

<script setup>

const categories = [
  {
    name: "HOME"
  },

  {
    name: "HEADPHONES"
  },

  {
    name: "SPEAKERS"
  },

  {
    name: "EARPHONES"
  },
]

</script>

<style scoped>

/* Mobile */

* {
  padding: 0;
  margin: 0;
}

nav {
  background-color: #101010;
  display: flex;
  flex-flow: column;
}

.container {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.logo {
  padding: 32px 0;
}

.categories {
  font-family: 'Manrope', sans-serif;
  font-weight: 700;
  font-size: 13px;
  line-height: 25px;
  letter-spacing: 2px;
  color: #FFFFFF;
  display: none;
}

hr {
  border: solid 1px #2D2D2D;
  width: 100vw;
  margin: auto;
  display: flex;
  align-items: center;
}

li:hover {
    color: #D87D4A;
}

path:hover  {
    fill: #D87D4A;
}


/* Tablet */

@media (min-width: 768px) {

  nav {
    justify-content: flex-start;
  }

  .sub-navbar {
    display: flex;
    align-items: center;
  }

  .burger-menu {
    padding-right: 42px;
    padding-left: 39px;
    flex-grow: 0;

  }

  .sub-navbar {
    flex-grow: 15;
  }

  .icon-cart {
    flex-grow: 1;
  }

  hr {
    width: 80vw;
  }
}


/* Desktop */

@media (min-width: 1200px) {

  .burger-menu {
    display: none;
  }

  nav {
    align-items: center;
  }

  .container{
    max-width: 1110px;
    display: flex;
    align-items: center;
  }

  .logo {
    flex-grow: 0;
    padding-right: 15vw;
  }

  .categories {
    display: flex;
    list-style-type: none;
    gap: 34px;
    flex-grow: 4;
    padding-right: 20vw;
  }

  .icon-cart {
    flex-grow: 0;
  }

}

</style>