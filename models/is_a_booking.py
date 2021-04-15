from odoo import api, fields, models

class IsBooking(models.Model):
    _inherit = 'sale.order'

    is_a_booking = fields.Boolean(string='is a booking', default=False)
    team = fields.Many2one(comodel_name='booking_service.teams', string='Team')
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader')
    employee_ids = fields.One2many(comodel_name='booking_service.employees', inverse_name='employee_quo', string="Employees")
    equipment_ids = fields.One2many(comodel_name='booking_service.equipments', inverse_name='equipment_quo', string='Equipments')

    booking_start = fields.Datetime(string='Booking Start')
    booking_end = fields.Datetime(string='Booking End')

    
    
    
    
    

    
    
    
    
    
    
