from odoo import fields, models


class BookingOrders(models.Model):
    _name = 'booking_service.booking_orders'
    _description = 'Booking Orders Service'

    name = fields.Char(string='Name')
