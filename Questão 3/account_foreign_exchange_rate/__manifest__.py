# -*- coding: utf-8 -*-
{
    'name': 'Contabilidade com Conversão de Moeda',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Adiciona a funcionalidade de conversão de moeda a lançamentos contábeis',
    'author': 'Gustavo Kertisz Maciel',
    'website': 'https://github.com/kertisz',
    'depends': ['base', 'account', 'res.currency'],
    'data': [
        'views/account_foreign_exchange_rate.xml',
        'views/account_move.xml',
    ],
    
}
