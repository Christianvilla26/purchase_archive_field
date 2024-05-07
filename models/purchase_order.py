from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean("Active", default=True)
