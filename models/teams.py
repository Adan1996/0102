from odoo import api, fields, models


class Teams(models.Model):
    _name = 'booking_service.teams'
    _description = 'Teams'

    team_name = fields.Char(string='Team Name', required=True)
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader')
    employee_ids = fields.One2many(comodel_name='booking_service.employees', inverse_name='employee_id', string="Employees")
    equipment_ids = fields.One2many(comodel_name='booking_service.equipments', inverse_name='equipment_id', string='Equipments')


    
    
    
    
    

    
    
    

    

