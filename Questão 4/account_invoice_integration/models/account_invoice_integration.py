from odoo import models, fields, api



class AccountInvoiceIntegration(models.Model):
    _name = 'account.invoice.integration'
    _description = 'Integração de Faturas'
    
    
    invoice_id = fields.Many2one(
        'account.move', 
        string='Fatura'
        )
    external_system_id = fields.Char(
        string='ID da Fatura Externa'
        )
    status = fields.Selection([
        ('pendente', 'Pendente'),
        ('sucesso', 'Sucesso'),
        ('erro', 'Erro')
        ], 
        string='Status'
        )
    response_message = fields.Text(
        string='Resposta API'
        )