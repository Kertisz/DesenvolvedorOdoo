from odoo import models, fields

class AccountForeignExchangeRate(models.Model):
    _name = 'account.foreign.exchange.rate'
    _description = 'Foreign Exchange Rate'
    
    date = fields.Date(
        string='Date',
    )
    currency_from_id = fields.Many2one(
        'res.currency',
        string='Moeda de Origem',
    )
    currency_to_id = fields.Many2one(
        'res.currency',
        string='Moeda de Destino',
    )
    exchange_rate = fields.Float(
        string='Taxa de Cambio',
    )
    