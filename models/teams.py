from odoo import api, fields, models


class Teams(models.Model):
    _name = 'booking_service.teams'
    _description = 'Teams'

    team_name = fields.Char(string='Team Name', required=True)
    team_leader = fields.Many2one(comodel_name='res.users', string='Team Leader')
    employee_ids = fields.One2many(comodel_name='booking_service.employees', inverse_name='employee_id', string="Employees")
    equipment_ids = fields.One2many(comodel_name='booking_service.equipments', inverse_name='equipment_id', string='Equipments')
    
    
    
    
    
    


class Employees(models.Model):
    _name = 'booking_service.employees'
    _description = "Employees"

    name = fields.Many2one(comodel_name='res.users', string='Employee', required=True)
    employee_id = fields.Many2one(comodel_name='booking_service.teams', string='employee_id')

class Equipments(models.Model):
    _name = 'booking_service.equipments'
    _description = 'Equipments'

    product = fields.Many2one(comodel_name='product.template', string='Equipments', domain="[('is_an_equipment', '=', True)]")
    serial_no = fields.Many2one(comodel_name='stock.production.lot', string='Serial No')
    
    equipment_id = fields.Many2one(comodel_name='booking_service.teams', string='equipment_id')
    
    
    
    
    

    
    
    

    

