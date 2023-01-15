<template>
  <nav>
    <img class="burger-menu-mobile" src="/shared/tablet/icon-hamburger.svg" alt="burger menu">
    <div class="sub-navbar">
      <img class="burger-menu" src="/shared/tablet/icon-hamburger.svg" alt="burger menu">
      <img class="logo" src="/shared/desktop/logo.svg" alt="logo navbar">
    </div>
    <ul class="categories">
      <li v-for="category in categories">{{ category.name }}</li>
    </ul>
    <svg class="icon-cart" width="23" height="20" xmlns="http://www.w3.org/2000/svg"><path d="M8.625 15.833c1.132 0 2.054.935 2.054 2.084 0 1.148-.922 2.083-2.054 2.083-1.132 0-2.054-.935-2.054-2.083 0-1.15.922-2.084 2.054-2.084zm9.857 0c1.132 0 2.054.935 2.054 2.084 0 1.148-.922 2.083-2.054 2.083-1.132 0-2.053-.935-2.053-2.083 0-1.15.92-2.084 2.053-2.084zm-9.857 1.39a.69.69 0 00-.685.694.69.69 0 00.685.694.69.69 0 00.685-.694.69.69 0 00-.685-.695zm9.857 0a.69.69 0 00-.684.694.69.69 0 00.684.694.69.69 0 00.685-.694.69.69 0 00-.685-.695zM4.717 0c.316 0 .59.215.658.517l.481 2.122h16.47a.68.68 0 01.538.262c.127.166.168.38.11.579l-2.695 9.236a.672.672 0 01-.648.478H7.41a.667.667 0 00-.673.66c0 .364.303.66.674.66h12.219c.372 0 .674.295.674.66 0 .364-.302.66-.674.66H7.412c-1.115 0-2.021-.889-2.021-1.98 0-.812.502-1.511 1.218-1.816L4.176 1.32H.674A.667.667 0 010 .66C0 .296.302 0 .674 0zm16.716 3.958H6.156l1.797 7.917h11.17l2.31-7.917z" fill="#FFF" fill-rule="nonzero"/></svg>
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

  li:hover {
    color: #D87D4A;
  }

   path:hover {
    fill: #D87D4A;
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

    li:hover {
    color: #D87D4A;
  }

  path:hover {
    fill: #D87D4A;
  }

    .icon-cart {
      width: 23px;
      height: 20px;
    }

    .icon-cart:hover {
    color: #D87D4A;
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