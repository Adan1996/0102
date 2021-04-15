from odoo import api, fields, models


class Employees(models.Model):
    _name = 'booking_service.employees'
    _description = "Employees"

    name = fields.Many2one(comodel_name='res.users', string='Employee', required=True)
    employee_id = fields.Many2one(comodel_name='booking_service.teams', string='employee_id')
    employee_quo = fields.Many2one(comodel_name='booking_service.is_booking', string='employee_quo')
    
    
