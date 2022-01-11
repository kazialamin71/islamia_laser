from odoo import models,fields

class investigation_item(models.Model):
    _name = 'patient.info'

    name = fields.Char("ID")
    patient_name=fields.Char("Patient Name")
    age=fields.Char("Age")
    address=fields.Char("Address")
    sex=fields.Selection([('male', 'Male'), ('female', 'Female')], 'Sex', default='male')






