let cardTrigger = document.getElementById('cardTrigger');
let cardCarrouselArray = [document.getElementById('card')];

cardTrigger.addEventListener('click', function () {
    let textCard = document.querySelector('.content-scroll-box-text');
    textCard.style.opacity = '0';

    setTimeout(function () {
        let card = document.getElementById('card');
        card.classList.remove('animation');
        card.classList.add('card-active');
        card.style.zIndex = '10';

        let cardClone1 = document.getElementById('card').cloneNode(true);
        document.getElementById('card').parentNode.appendChild(cardClone1);
        cardClone1.id = 'cardClone1';
        cardClone1.style.zIndex = '9';
        cardClone1.querySelector('.card-title').innerText = 'JS can insert a element';
        cardClone1.querySelector('.card-descr').innerText = "dinamically in the document body only cloning it and changing it's text.";
        cardCarrouselArray.unshift(document.getElementById('cardClone1'));
        let cardClone2 = document.getElementById('card').cloneNode(true);
        document.getElementById('card').parentNode.appendChild(cardClone2);
        cardClone2.id = 'cardClone2';
        cardClone2.style.zIndex = '8';
        cardClone2.querySelector('.card-title').innerText = "It's only a mutation";
        cardClone2.querySelector('.card-descr').innerText = "and can be captured with a mutation observer.";
        cardCarrouselArray.push(document.getElementById('cardClone2'));
    }, 1000);

    setTimeout(function () {
        cardClone1.style.left = '22.5%';
        cardClone2.style.left = '77.5%';
    }, 2000);

    setTimeout(function () {
        activatingCarrousel();
    }, 2000);
});

function movingCards() {
    cardCarrouselArray[0].style.left = '22.5%';
    cardCarrouselArray[0].style.zIndex = '9';
    cardCarrouselArray[1].style.left = '50%';
    cardCarrouselArray[1].style.zIndex = '10';
    cardCarrouselArray[2].style.left = '77.5%';
    cardCarrouselArray[2].style.zIndex = '8';
}

function activatingCarrousel() {
    cardCarrouselArray.forEach(function (card) {
        card.addEventListener('click', function () {
            if (card == cardCarrouselArray[0]) {
                elementMoving = cardCarrouselArray[2];
                cardCarrouselArray.pop();
                cardCarrouselArray.unshift(elementMoving);
                movingCards();
            } else if (card == cardCarrouselArray[2]) {
                elementMoving = cardCarrouselArray[0];
                cardCarrouselArray.shift();
                cardCarrouselArray.push(elementMoving);
                movingCards();
            }
        });
    });
}




// contact section

let iconsArray = document.querySelectorAll('.contact');
let target = document.querySelector('.contact-label');

iconsArray.forEach(function (icon) {
    icon.addEventListener('mouseover', function () {
        target.setAttribute('data-label', icon.id);
        target.classList.toggle('contact-label-active');
    });
    icon.addEventListener('mouseout', function () {
        target.classList.toggle('contact-label-active');
    });
});


// navbar mobile

class NavbarSelector {
    constructor() {
        this.selector = document.getElementById('selector');

        this.actualSection = 'menuHome';

        this.activeSection('menuHome');
    }

    activeSection(section) {
        document.getElementById(this.actualSection).classList.remove('menu-item-active');
        
        this.actualSection = section;
        this.moveSelector(section);
        document.getElementById(this.actualSection).classList.add('menu-item-active');
    }

    moveSelector(section) {
        this.selector.classList.add('selector-moving');
        this.selector.style.left = `${this.getSectionPosition(section) + 16}px`;
        setTimeout(() => {
            this.selector.classList.remove('selector-moving');
        }, 500);
    }

    getSectionPosition(section) {
        return document.getElementById(section).offsetLeft;
    }
}

let navbarSelector = new NavbarSelector();

let navbarItemsArray = document.querySelectorAll('.menu-item');
navbarItemsArray.forEach(function (item) {
    item.addEventListener('click', function () {
        navbarSelector.activeSection(item.id);
    });
});