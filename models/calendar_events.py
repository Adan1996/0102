from odoo import api, fields, models


class CalendarEvents(models.Model):
    _inherit = 'event.registration'

    equipments = fields.Many2one(comodel_name='stock.production.lot', string='Equipments')
    