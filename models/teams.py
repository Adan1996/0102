from odoo import api, fields, models


class Teams(models.Model):
    _name = 'booking_service.teams'
    _description = 'Teams'

    team_name = fields.Char(string='Team Name')
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader')
    employee_ids = fields.One2many(comodel_name='booking_service.employees', inverse_name='name', string="Employees")
    
    
    
    


class Employees(models.Model):
    _name = 'booking_service.employees'
    _description = "Employees"

    name = fields.Many2one(comodel_name='res.users', string='Employee', required=True)


# class Employees(models.Model):
#     _inherit = 'res.users'

    # name = fields.Char(string='Name')

    

    
    
    

    

