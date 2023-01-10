<template>
  <nav>
    <img class="burger-menu-mobile" src="~/assets/shared/tablet/icon-hamburger.svg" alt="burger menu">
    <div class="sub-navbar">
      <img class="burger-menu" src="~/assets/shared/tablet/icon-hamburger.svg" alt="burger menu">
      <img class="logo" src="~/assets/shared/desktop/logo.svg" alt="logo navbar">
    </div>
    <ul class="categories">
      <li v-for="category in categories">{{ category.name }}</li>
    </ul>
    <img class="icon-cart" src="~/assets/shared/desktop/icon-cart.svg" alt="icon cart">
  </nav>
  <hr>
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

@media (min-width: 1080px) {

  .burger-menu-mobile {
    display: none;
  }

  .burger-menu {
    display: none;
  }

  nav {
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    font-size: 13px;
    line-height: 25px;
    letter-spacing: 2px;
    padding: 32px;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
  }

  ul {
    display: flex;
    gap: 34px;
  }

  li {
    color: white;
    display: inline;
  }

  hr {
    width: 70%;
    color: white;
    mix-blend-mode: normal;
    opacity: 0.2;
  }
}

@media (min-width: 375px) and (max-width: 1080px) {

    nav {
      padding: 32px 40px;
      display: flex;
      justify-content: space-between;
    }

    .burger-menu-mobile {
    display: none;
    }

    .sub-navbar {
      display: flex;
      align-items: center;
      gap: 42px;
    }

    .burger-menu {
      width: 16px;
      height: 15px;
      display: block;
    }

    ul, li {
      display: none;
    }

    .icon-cart {
      width: 23px;
      height: 20px;
    }

    hr {
    width: 90%;
    color: white;
    mix-blend-mode: normal;
    opacity: 0.2;
    }
}

@media (max-width: 375px) {

    nav {
      padding: 32px 24px;
      display: flex;
      gap: 42px;
      justify-content: space-between;
      align-items: center;
    }

    .burger-menu-mobile {
      width: 16px;
      height: 15px;
      display: block;
    }

    .sub-navbar {
      display: flex;
      align-items: center;
      gap: 42px;
    }

    .burger-menu {
      display: none;
    }

    ul, li {
      display: none;
    }

    .icon-cart {
      width: 23px;
      height: 20px;
    }

    hr {
    width: 100%;
    color: white;
    mix-blend-mode: normal;
    opacity: 0.2;
    }
}

</style>