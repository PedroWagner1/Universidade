document.addEventListener("DOMContentLoaded", function () {
  const btnMenu = document.querySelector("header button");
  const menu = document.getElementById("menuLateral");
  const overlay = document.getElementById("overlay");
  const fechar = document.getElementById("fecharMenu");

  btnMenu.addEventListener("click", () => {
    menu.classList.add("aberto");
    overlay.classList.add("visivel");
  });

  fechar.addEventListener("click", () => {
    menu.classList.remove("aberto");
    overlay.classList.remove("visivel");
  });

  overlay.addEventListener("click", () => {
    menu.classList.remove("aberto");
    overlay.classList.remove("visivel");
  });
});
