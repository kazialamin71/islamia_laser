from odoo import models,fields

class doctors_info(models.Model):
    _name = 'doctors.info'

    name=fields.Char("Doctor Name")
    education=fields.Char("Education")
    designation=fields.Char("Designation")
    department=fields.Char("Department")
    sex=fields.Selection([('male', 'Male'), ('female', 'Female')], 'Sex', default='male')







