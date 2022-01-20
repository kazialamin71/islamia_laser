from odoo import models,fields

class admission_item_entry(models.Model):
    _name = 'admission.item.entry'

    name = fields.Char("Name")
    department=fields.Many2one('islamia.department',"Department")
    rate=fields.Float("Rate")
    required_time=fields.Integer("Required Date")
    sample_req=fields.Boolean("Sample Required")
    admission_item_entry_line_id=fields.One2many('admission.item.entry.line','admission_item_entry_id',string="Parameters")



class admission_item_entry_line(models.Model):
    _name='admission.item.entry.line'

    admission_item_entry_id=fields.Many2one('bill.item.entry','Bill Item ID')
    name=fields.Char("Name")
    reference_value=fields.Char("Reference Value")
    bold=fields.Boolean("Bold")
    group_by=fields.Boolean("Group By")







