from odoo import models,fields

class money_receipt(models.Model):
    _name = 'money.receipt'

    name = fields.Char("Mr ID")
    date = fields.Date("Date")
    bill_id=fields.Many2one('investigation.bill',string="Bill ID")
    admission_id=fields.Many2one('admission.bill',string="Admission ID")
    total_amount=fields.Float("Total Amount")
    paid_amount=fields.Float("Paid Amount")
    due_amount=fields.Float("Due Amount")
    p_type=fields.Selection([('adv','Advance'),('due_pay','Due Payment')],"Payment Type")
    already_collected=fields.Boolean("Already collected")
    user_id=fields.Many2one('res.users','Current User',default=lambda self: self.env.user.id)
    state = fields.Selection([('confirm', 'Confirmed'), ('cancelled', 'Cancelled')], 'Status',
                             default='confirm')






