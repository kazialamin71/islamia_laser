from odoo import models,fields

class bill_item_entry(models.Model):
    _name = 'bill.item.entry'

    name = fields.Char("Name",required=True)
    department=fields.Many2one('islamia.department',"Department")
    rate=fields.Float("Rate", required=True)
    required_time=fields.Integer("Required Date")
    sample_req=fields.Boolean("Sample Required")
    bill_item_entry_line_id=fields.One2many('bill.item.entry.line','bill_item_entry_id',string="Parameters")



class bill_item_entry_line(models.Model):
    _name='bill.item.entry.line'

    bill_item_entry_id=fields.Many2one('bill.item.entry','Bill Item ID')
    name=fields.Char("Name")
    reference_value=fields.Char("Reference Value")
    bold=fields.Boolean("Bold")
    group_by=fields.Boolean("Group By")







