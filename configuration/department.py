from odoo import models,fields

class investigation_item(models.Model):
    _name = 'islamia.department'

    name = fields.Char("Department")
    parent=fields.Many2one('islamia.department',string="Doctor Name")






