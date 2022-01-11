from odoo import models,fields

class investigation_item(models.Model):
    _name = 'investigation.item'

    name = fields.Char("Name")
    patient_name=fields.Char(string="Name")
    rate=fields.Char("Rate")





