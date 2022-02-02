/*menu visible, reponsive */
const navButton = document.querySelector(".div-nav-button");
const navMenu = document.querySelector(".div-nav-menu");

navButton.addEventListener("click",()=>{
    navMenu.classList.toggle("div-nav-menu_visible");
});


/* boton contador de agregar en carrito en <span> */
const addCarrito =()=>{
    document.getElementById("cartCount").innerHTML ++;
}

/* verificando si las contraseñas coinciden*/
