from odoo import api, fields, models


class Equipments(models.Model):
    _name = 'booking_service.equipments'
    _description = 'Equipments'

    product = fields.Many2one(comodel_name='product.template', string='Equipments', domain="[('is_an_equipment', '=', True)]")
    serial_no = fields.Many2one(comodel_name='stock.production.lot', string='Serial No')
    
    equipment_id = fields.Many2one(comodel_name='booking_service.teams', string='equipment_id')
    equipment_quo = fields.Many2one(comodel_name='booking_service.is_booking', string='equipment_quo')
    
