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

function request(url, data, method) {
    let json_data = {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
    };

    if (method == 'POST') {
        json_data.body = JSON.stringify(data);
    }

    let resposta = fetch(url, json_data).then(function (response) {
            return response.json();
        }).then(function (data) {
            return data;
        });
    return resposta;
};

class contextObject {
    constructor() {
        this.actualContext = '';

        this.initalBehavior();
    };

    async initalBehavior() {
        this.data = await request('/api/manager/context/get', {}, 'GET');
                
        if (this.data.status == 'ok') {
            let localOfInsert = document.getElementById('gridContexto');

            Object.keys(this.data.avaliable).forEach(element => {
                let div = elementContructor('div', '', 'card', '', `<div>${this.data.avaliable[element]}</div>`);
                div.style.height = '50px';
                div.style.justifyContent = 'center';
                div.style.cursor = 'pointer';

                div.addEventListener('click', () => {
                    this.modalContext(element);
                    this.actualContext = element;
                });

                localOfInsert.appendChild(div);
            });
        }
    };    

    modalContext(context) {
        let backgroundContext = elementContructor('div', 'backgroundContext', 'login-background', '', '');
        let modalContext = elementContructor('div', 'modalContext', 'login-modal-window', '', '');
        modalContext.style.height = '7em';


        let title = elementContructor('label', '', 'title', `${this.data.avaliable[context]}`);
        title.style.marginTop = '0.75em';
        modalContext.appendChild(title);

        let rowCrud = elementContructor('div', '', 'row-crud', '', '');

        let btnCreate = elementContructor('button', 'create', '', 'Adicionar');
        let btnUpdate = elementContructor('button', 'update', '', 'Atualizar');
        let btnDelete = elementContructor('button', 'delete', '', 'Deletar');
        let btnArray = [btnCreate, btnUpdate, btnDelete];
        btnArray.forEach(element => {
            element.addEventListener('click', (el) => {
                this.formContextInit(el.target.id)
            });
            rowCrud.appendChild(element);
        });

        modalContext.appendChild(rowCrud);

        let rowForm = elementContructor('div', 'rowForm', 'row-form', '', '');

        modalContext.appendChild(rowForm);

        document.body.appendChild(backgroundContext);
        document.body.appendChild(modalContext);

        setTimeout(() => {
            backgroundContext.style.opacity = '1';
            modalContext.style.opacity = '1';
        }, 100);

        backgroundContext.addEventListener('click', this.closeModalContext);
    };

    async formContextInit(btn) {
        document.getElementById('rowForm').remove();

        this.result = await request(`/api/manager/context/${this.actualContext}`, {}, 'GET');

        let contexts = {
            a_oper : {
                create : `${7.5 + (3 * 5)}em`,
                update : `${7.5 + (3 * 6.25)}em`,
                delete : `${7.5 + (3 * 2.5)}em`,
            },
            b_duv : {
                create : `${7.5 + (3 * 6.25)}em`,
                update : `${7.5 + (3 * 7.75)}em`,
                delete : `${7.5 + (3 * 2.5)}em`,
            },
            c_fin : {
                create : `${7.5 + (3 * 7.50)}em`,
                update : `${7.5 + (3 * 9)}em`,
                delete : `${7.5 + (3 * 2.5)}em`,
            }
        }

        let modalContext = document.getElementById('modalContext');
        modalContext.style.height = contexts[this.actualContext][btn];
        console.log(modalContext.style.height);

        let rowForm = this.crudSectorDefine(btn);
        modalContext.appendChild(rowForm);

        let text = document.getElementById(btn).textContent;
        let btnApply = elementContructor('button', 'save', '', text);

        btnApply.addEventListener('click', () => {
            console.log(btn);
        });

        rowForm.appendChild(btnApply);
    };

    crudSectorDefine(btn) {
        if (btn == 'create') {
            return this.crudSectorCreate();
        } else if (btn == 'update') {
            return this.crudSectorUpdate();
        } else if (btn == 'delete') {
            return this.crudSectorDelete();
        }
    }

    crudSectorCreate() {
        let rowForm = elementContructor('div', 'rowForm', 'row-form');
        
        Object.keys(this.result.avaliable).forEach(element => {
            let label = elementContructor('label', `label${element}`, '', `${this.result.avaliable[element]}`);
            let input = elementContructor('input', `input${element}`);
            rowForm.appendChild(label);
            rowForm.appendChild(input);
        });

        return rowForm;
    };

    crudSectorUpdate() {
        let rowForm = elementContructor('div', 'rowForm', 'row-form');

        let arrayOptions = Object.keys(this.result.avaliable);

        let firstLabel
        if (this.actualContext == 'a_oper') {
            firstLabel = elementContructor('label', '', '', this.result.avaliable[arrayOptions[2]]);
        } else if (this.actualContext == 'b_duv') {
            firstLabel = elementContructor('label', '', '', this.result.avaliable[arrayOptions[1]]);
        } else if (this.actualContext == 'c_fin') {
            firstLabel = elementContructor('label', '', '', this.result.avaliable[arrayOptions[0]]);
        }
        
        let firstSelect = elementContructor('select', 'firstSelect');
        let option = elementContructor('option', '', '', 'Selecione');
        firstSelect.appendChild(option);

        let setOptions = new Set();

        Object.keys(this.result.data).forEach(element => {
            let text
            if (this.actualContext == 'a_oper') {
                text = `${this.result.data[element][0]} - ${this.result.data[element][2]}`
            } else if (this.actualContext == 'b_duv') {
                text = `${this.result.data[element][0]} - ${this.result.data[element][1]}`
            } else if (this.actualContext == 'c_fin') {
                text = `${this.result.data[element][0]}}`
            }

            let option = elementContructor('option', `${element}`, '', text);
            firstSelect.appendChild(option);
        });

        rowForm.appendChild(firstLabel);
        rowForm.appendChild(firstSelect);

        
        Object.keys(this.result.avaliable).forEach(element => {
            let label = elementContructor('label', `label${element}`, '', `${this.result.avaliable[element]}`);
            let input = elementContructor('input', `input${element}`);

            rowForm.appendChild(label);
            rowForm.appendChild(input);
        });

        let arraySubOptions = [];
        this.result.data.forEach(element => {
            arraySubOptions.push(element);
        });
    
        firstSelect.addEventListener('change', (el) => {
            let index = el.target.selectedIndex;
            let subOptions = arraySubOptions[index - 1];

            Object.keys(this.result.avaliable).forEach((element, index) => {
                let input = document.getElementById(`input${element}`);
                input.value = subOptions[index];
            });
        });

        return rowForm;
    };

    crudSectorDelete() {
        let rowForm = elementContructor('div', 'rowForm', 'row-form');
        
        let arrayOptions = Object.keys(this.result.avaliable);

        let firstLabel
        if (this.actualContext == 'a_oper') {
            firstLabel = elementContructor('label', '', '', this.result.avaliable[arrayOptions[2]]);
        } else if (this.actualContext == 'b_duv') {
            firstLabel = elementContructor('label', '', '', this.result.avaliable[arrayOptions[1]]);
        } else if (this.actualContext == 'c_fin') {
            firstLabel = elementContructor('label', '', '', this.result.avaliable[arrayOptions[0]]);
        }
        
        let firstSelect = elementContructor('select', 'firstSelect');
        let option = elementContructor('option', '', '', 'Selecione');
        firstSelect.appendChild(option);

        let setOptions = new Set();

        Object.keys(this.result.data).forEach(element => {
            let text
            if (this.actualContext == 'a_oper') {
                text = `${this.result.data[element][0]} - ${this.result.data[element][2]}`
            } else if (this.actualContext == 'b_duv') {
                text = `${this.result.data[element][0]} - ${this.result.data[element][1]}`
            } else if (this.actualContext == 'c_fin') {
                text = `${this.result.data[element][0]}}`
            }

            let option = elementContructor('option', `${element}`, '', text);
            firstSelect.appendChild(option);
        });

        rowForm.appendChild(firstLabel);
        rowForm.appendChild(firstSelect);

        return rowForm;
    };
    
    closeModalContext() {
        let backgroundContext = document.getElementById('backgroundContext');
        let modalContext = document.getElementById('modalContext');
        backgroundContext.style.opacity = '0';
        modalContext.style.opacity = '0';
        setTimeout(() => {
            backgroundContext.remove();
            modalContext.remove();
        }, 500);
    };
};

class authorizationObject {
    constructor() {
        this.url = '/api/manager/auth/';

        this.btnsArray = this.buttonsArray();
        this.btnsArray.forEach(botao => {
            botao.addEventListener('click', (event) => {
                this.authBehavior({"pc_id": event.target.id});
            });
        });
    };
    
    buttonsArray () {
        let btn_conf_array = Array.from(document.querySelectorAll('.btn-confirm'));
        let btn_decl_array = Array.from(document.querySelectorAll('.btn-decline'));

        return btn_conf_array.concat(btn_decl_array);
    };

    authDefining(pc_id, auth) {
        request(this.url + 'post/', {
            "pc_id": pc_id,
            "auth": 1 ? auth == 0 : 0,
        }, 'POST');

        let options = {
            0: 'Autorizado.',
            1: 'Desautorizado.'
        };

        let btn = document.getElementById(pc_id).parentElement
        btn.innerHTML = options[auth];
    };

    async authBehavior(data) {
        let resp = await request(this.url + 'req/', data, 'POST');
        if (resp.status == 'error') {
            alert(resp.msg);
        } else {
            this.authDefining(resp.pc_id, resp.auth);
        }
    };
};

const context = new contextObject();
const auth = new authorizationObject();