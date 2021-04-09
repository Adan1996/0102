from odoo import api, fields, models


class IsBooking(models.Model):
    _inherit = 'sale.order'

    is_a_booking = fields.Boolean(string='is a booking', default=False)
    team = fields.Many2one(comodel_name='booking_service.teams', string='Team')
    

    
    
    
    
    
    
