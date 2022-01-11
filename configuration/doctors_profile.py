from odoo import models,fields

class investigation_item(models.Model):
    _name = 'doctors.info'

    name = fields.Char("ID")
    doctor_name=fields.Char("Doctor Name")
    education=fields.Char("Education")
    designation=fields.Char("Designation")
    department=fields.Char("Department")
    sex=fields.Selection([('male', 'Male'), ('female', 'Female')], 'Sex', default='male')







