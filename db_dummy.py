usuarios = [
    ('Usuario 1', '01/01/2021 00:00:00', '00000000-0000-0000-0000-000000000000', '1.00'),
    ('Usuario 2', '01/01/2021 00:00:00', '00000000-0000-0000-0000-000000000000', '1.00'),
    ('Usuario 3', '01/01/2021 00:00:00', '00000000-0000-0000-0000-000000000000', '1.00'),
    ('Usuario 4', '01/01/2021 00:00:00', '00000000-0000-0000-0000-000000000000', '1.00'),
    ('Usuario 5', '01/01/2021 00:00:00', '00000000-0000-0000-0000-000000000000', '1.00'),
    ('Usuario 6', '01/01/2021 00:00:00', '00000000-0000-0000-0000-000000000000', '1.00'),
    ('Usuario 7', '01/01/2021 00:00:00', '00000000-0000-0000-0000-000000000000', '1.00'),
]

dicti = [
    ['00000000-0000-0000-0000-000000000000', 1],
    ['00000000-0000-0000-0000-000000000001', 0],
    ['00000000-0000-0000-0000-000000000002', 1],
    ['00000000-0000-0000-0000-000000000003', 1],
    ['00000000-0000-0000-0000-000000000004', 0],
    ['00000000-0000-0000-0000-000000000005', 1],
]

oper = {
    'oper' : [
        ('120', 'cancelamento', 'cancelamento'),
        ('126', 'recolhe_equipo_faturado', 'recolher_equipamento_faturado'),
        ('175', 'Monitoramento CCRI', 'suspeita_de_fraude'),
        ('180', 'transferencia_interna', 'transferencia_interna'),
        ('191', 'alteracao_de_plano', 'alteracao_de_plano')
        ],
    'duv_fin' : [
        ('Suspensão Temporária - Antes de 365 dias', 'Cliente entrou em contato solicitando a Suspensão Temporária.\nInformado que só pode solicitar uma suspensão após 365 dias do retorno da ultima suspensão.\n\n', 'RES DUV SERV'),
        ('Suspensão Temporária - Com débito', 'Cliente entrou em contato solicitando a Suspensão Temporária.\nInformado que só é possivel solicitar a suspensão sem débitos ativos no cadastro.\nOrientado a realizar o pagamento das faturas.\n\n', 'RES DUV SERV'),
        ('Suspensão Temporária - Orientação', 'Cliente entrou em contato solicitando informações sobre o processo de Suspensão Temporária.\nInformado sobre os passos e que somente o titular deve fazê-lo.\n\n', 'RES DUV SERV'),
        ('Fatura - Contrato dividido em 2 ou mais partes', 'Cliente entrou em contato solicitando informações sobre o seu chamado estar sendo divido em duas (ou mais) partes.\nExplicado ao cliente que a divisão é feito por questões tributárias.\n\n', 'res duv fat dat'),
        ('Fatura - Pagamento por PIX', 'Cliente entrou em contato solicitando a chave PIX para efetuar o pagamento da fatura.\nOrientado ao cliente que o pagamento é feito exclusivamente pelo pagamento da fatura.\n\n', 'res duv fat dat')
        ],
    'duv_ret' : [
        ('Fatura de Negociação em Atraso.', 'Cliente entrou em contato solicitando a fatura em atraso.\nExplicado que uma fatura de negociação em atraso é automaticamente cancelada, caracterizando quebra de acordo.\nOrientado a a entrar em contato novamente com a 2Safe.\n\n', 'RES DUV ATENDIM'),
        ('2ª via da Fatura de Negociação.', 'Cliente entrou em contato solicitando a segunda via da fatura.\nExplicado que somente a instituição quem fez o acordo que pode emitir a fatura.\nOrientado a a entrar em contato novamente com a 2Safe.\n\n', 'RES DUV ATENDIM'),
        ('Fatura abrangidas na Negociação', 'Cliente entrou em contato solicitando sobre quais faturas estão cobertas na Negociação feita.\nInformado ao mesmo.\n\n', 'RES DUV ATENDIM')
    ],
    'duv_tec' : [
        ('WiFi - Alcance', 'Cliente questiona a área de cobertura da WiFi.\nInformado à mesma que a area de cobertura é de 10m², em área livre, em torno do roteador.\n\n', 'CT DUVID TECNIC'),
        ('WiFi - Troca de Senha - Não é o Titular', 'Cliente solicita a troca da senha da WiFi.\nCliente que entrou em contato não é o titular.\nInformado que somente o titular pode estar requerendo a troca de senha.\n\n', 'CT DUVID TECNIC'),
        ('WiFi - Troca de Senha - É o Titular', 'Cliente solicita a troca da senha da WiFi.\nDados do titular foram validados.\nAlterado.\n\n', 'ct config exec'),
        ('WiFi - Velocidades 2.4GHz/5GHz', 'Cliente com duvidas a respeito das velocidades transmitidas via WiFi.\nExplicado ao mesmo sobre as velocidades de transmissão das redes WiFi.\n\n', 'CT DUVID TECNIC'),
        ('Consulta dos dados de Redirecionamento', 'Cliente entrou em contato solicitando os dados do redirecionamento de portas.\nInformado ao mesmo sobre o endereço de acesso externo e as portas de acesso.\n\n', 'CT DUVID TECNIC')
    ],
}