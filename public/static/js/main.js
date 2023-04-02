/*=========== taggle menu start ===========*/
let TaggleMenuItems = document.querySelector('.taggle-menu-items');
let TaggleMenuSubItems1 = document.querySelector('.dripdown1');
let TaggleMenuSubItems2 = document.querySelector('.dripdown2');


document.querySelector('#taggle-bar').onclick = () => {
    TaggleMenuItems.classList.toggle('active');
}


document.querySelector('#dripdown1icon').onclick = () => {
    TaggleMenuSubItems1.classList.toggle('active');
}

document.querySelector('#dripdown2icon').onclick = () => {
    TaggleMenuSubItems2.classList.toggle('active');
}

/*=========== taggle menu end ===========*/
