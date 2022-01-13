// DEFININDO VARIAVEIS
// definindo o objeto de controle
let btn_conf_array = Array.from(document.querySelectorAll('.btn-confirm'));
let btn_decl_array = Array.from(document.querySelectorAll('.btn-decline'));

let botoes_array = btn_conf_array.concat(btn_decl_array);

const urlSearchParams = new URLSearchParams(window.location.search);
const urlQuery = Object.fromEntries(urlSearchParams.entries());


// Interatividade da sessão contexto.
let combobox_target = document.getElementById('target-select');
let oper_section = document.getElementsByClassName('select-oper');
let combobox_oper = document.getElementById('oper-select');

let cicleArray = [
    "oper-add-behavior",
    "oper-edit-behavior",
    //"oper-del-behavior",
];

// DEFININDO FUNÇÕES
function postRequest(url, data) {
    let resposta = fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            return data;
        });
    return resposta;
};

function sectionToggle (section) {
    let varTemp = document.getElementsByClassName(section);
    varTemp[0].style.display = varTemp[0].style.display === '' || varTemp[0].style.display === 'none' ? 'block' : 'none';
};

function sectionDeactive (section) {
    let varTemp = document.getElementsByClassName(section);
    varTemp[0].style.display = 'none';
};

function sectionCicle (section) {
    cicleArray.forEach (element => {
        if (element === section && element != '') {
            sectionToggle(element);
        } else {
            sectionDeactive(element);
        };
    });
};


// Interatividade da sessão contexto.
combobox_target.onchange = (value) => {
    if (value.target.value != '') {
        oper_section[0].style.display = 'flex';
        oper_section[0].style.justifyContent = 'right';
        combobox_oper.value = '';
    } else {
        oper_section[0].style.display = 'none';
        sectionCicle('');
    };
};
combobox_oper.onchange = (value) => {
    if (combobox_target.value != '' && value.target.value != '') {
        currentSection = `${combobox_target.value}-${value.target.value}-behavior`
        sectionCicle(currentSection);
    } else {
        sectionCicle('');
    };
};






// Função para confirmar ou revogar a permissao de um computador
botoes_array.forEach(function(botao) {
    botao.addEventListener('click', function(event) {

        let data = {
            "oper": "id_auth",
            "pc_id": event.target.id,
            "token":urlQuery.token
        }
        let validar_auth = postRequest('/api/manager/req', data);

        validar_auth.then(function(data) {
            if (data.auth == 1) {
                data.auth = 0;
                let resposta = postRequest('/api/manager/auth', data);
                let btn = document.getElementById(botao.id).parentElement;
                btn.innerHTML = 'Desautorizado.';

            } else {
                data.auth = 1;
                let resposta = postRequest('/api/manager/auth', data);
                let btn = document.getElementById(botao.id).parentElement;
                btn.innerHTML = 'Autorizado.';
            }
        });
    })
});