from odoo import models,fields

class examinee_info(models.Model):
    _name = 'examinee.info'

    name=fields.Char("Name",required=True)
    education=fields.Char("Education")
    sex=fields.Selection([('male', 'Male'), ('female', 'Female')], 'Sex', default='male')
    bill_info=fields.One2many('investigation.bill','professionals_name',"Bill Info")







