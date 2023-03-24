
/*=========== taggle menu start ===========*/
let TaggleMenuItems = document.querySelector('.taggle-menu-items');
let TaggleMenuSubItems = document.querySelector('.dripdown1');

document.querySelector('#taggle-bar').onclick = () => {
    TaggleMenuItems.classList.toggle('active');
}


document.querySelector('#dripdown1icon').onclick = () => {
    TaggleMenuSubItems.classList.toggle('active');
}

/*=========== taggle menu end ===========*/
