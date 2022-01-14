let menuBtn = document.getElementById('navbar-btn');

let menuExpnd1 = menuBtn.nextElementSibling;
let menuExpnd2 = menuBtn.nextElementSibling.nextElementSibling;

menuExpnd1.style.display = 'none';
menuExpnd2.style.display = 'none';

menuBtn.parentElement.addEventListener('mouseover', function () {
    menuExpnd1.style.display = 'flex';
    menuExpnd1.style.animation = 'slideIn 0.5s';
    menuExpnd2.style.display = 'flex';
    menuExpnd2.style.animation = 'slideIn 0.5s';
});
menuBtn.parentElement.addEventListener('mouseout', function () {
    menuExpnd1.style.display = 'none';
    menuExpnd2.style.display = 'none';
});