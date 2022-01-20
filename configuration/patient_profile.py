from odoo import models,fields

class investigation_item(models.Model):
    _name = 'patient.info'

    name=fields.Char("Patient Name")
    age=fields.Char("Age")
    sex=fields.Selection([('male', 'Male'), ('female', 'Female')], 'Sex', default='male')
    mobile=fields.Char("Mobile No")
    address=fields.Char("Address")








