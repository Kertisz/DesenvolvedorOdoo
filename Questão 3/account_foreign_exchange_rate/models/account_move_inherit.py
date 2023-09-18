from odoo import models, fields, api


class InheritAccountMove(models.Model):
    _inherit = 'account.move'
    
    
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        
    )
    
    @api.onchange('currency_id')
    def _onchange_currency_id(self):
        if self.currency_id and self.currency_id != self.company_id.currency_id:
            exchange_rate = self.env['account.foreign.exchange.rate'].search([
                ('currency_from_id', '=', self.currency_id.id),
                ('currency_to_id', '=', self.company_id.currency_id.id),
                ('date', '<=', self.date),
            ], order='date DESC', limit=1)
            if exchange_rate:
                self.amount_total = self.amount_total * exchange_rate.exchange_rate
