from odoo import models,fields

class investigation_bill(models.Model):
    _name = 'islamia.department'

    name = fields.Char("Department")
    parent=fields.Many2one('islamia.department',string="Department Name")






