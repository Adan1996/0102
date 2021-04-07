from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'product.template'

    is_an_equipment = fields.Boolean(string='Is an Equipment', default=False)
    
