//tools 
function elementContructor(element, id = '', className = '', innerText = '', innerHTML = '') {
    let elementContructed = document.createElement(element);
    if (className !== '') {
        elementContructed.className = (className);
    }
    if (id !== '') {
        elementContructed.id = id;
    }
    if (innerText !== '') {
        elementContructed.innerText = innerText;
    }
    if (innerHTML !== '') {
        elementContructed.innerHTML = innerHTML;
    }
    return elementContructed;
}

function creatingM() {
    let background = elementContructor('div', 'loginBackground', 'login-background');

    document.body.appendChild(background);

    let loginModal = elementContructor('div', 'loginModalWindow', 'login-modal-window');

    let loginIcon = elementContructor('h1', 'loginIcon', 'icon icon-user');
    loginModal.appendChild(loginIcon);

    let userLoginLabel = elementContructor('label', 'userLoginLabel', 'login-label', 'Login');
    let userLoginInput = elementContructor('input', 'userLoginInput', 'login-input');

    let userPasswordLabel = elementContructor('label', 'userPasswordLabel', 'login-label', 'Senha');
    let userPasswordInput = elementContructor('input', 'userPasswordInput', 'login-input');
    userPasswordInput.type = 'password';

    let loginButton = elementContructor('button', 'loginButton', 'login-button', 'Login');

    loginModal.appendChild(userLoginLabel);
    loginModal.appendChild(userLoginInput);
    loginModal.appendChild(userPasswordLabel);
    loginModal.appendChild(userPasswordInput);
    loginModal.appendChild(loginButton);

    document.body.appendChild(loginModal);

    setTimeout(() => {
        background.style.opacity = '1';
        loginModal.style.opacity = '1';
    }, 100);

    loginButton.addEventListener('click', logIn);
    background.addEventListener('click', closeModal);
}

function onClick() {
    creatingM();
}

function closeModal() {
    let background = document.getElementById('loginBackground');
    let loginModal = document.getElementById('loginModalWindow');
    background.style.opacity = '0';
    loginModal.style.opacity = '0';
    setTimeout(() => {
        background.remove();
        loginModal.remove();
    }, 500);
}

async function logIn() {
    let username = document.getElementById('userLoginInput').value;
    let password = document.getElementById('userPasswordInput').value;

    let data = {
        "username": username,
        "password": password
    };

    let resposta = await fetch('/login/request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
    let data_json = await resposta.json();

    if (data_json.status == 'ok') {
        window.location.href = `manager`;
    } else {
        alert(data_json.message);
    }
}


let login = document.getElementById('loginTrigger');
login.addEventListener('click', onClick);
//onClick();