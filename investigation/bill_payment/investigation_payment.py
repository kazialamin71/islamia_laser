from odoo import models,fields
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from odoo import api

class investigation_payment(models.Model):
    _name = 'investigation.payment'

    name = fields.Char("Collection ID")
    bill_id=fields.Many2one('investigation.bill',string="Bill ID")
    admission_id=fields.Many2one('admission.bill',string="Admission ID")
    date=fields.Date(string='Date', required=True,default=datetime.now().strftime('%Y-%m-%d'))
    amount=fields.Float('Receive Amount', required=True)
    money_receipt_id=fields.Many2one('money.receipt','Money Receipt')


    def btn_add_payment(self):
        bill_id=self.bill_id.id
        admission_id=self.admission_id.id
        if bill_id!=False and admission_id==False:
            pay_date=self.date
            pay_amount=self.amount
            current_due=self.bill_id.due
            current_paid=self.bill_id.paid
            updated_amount=current_due-pay_amount
            updated_paid=current_paid+pay_amount

            query="update investigation_bill set due=%s,paid=%s where id=%s"
            self._cr.execute(query,[updated_amount,updated_paid,bill_id,])
            self._cr.commit()
        elif admission_id!=False and bill_id==False:
            pay_date = self.date
            pay_amount = self.amount
            current_due = self.admission_id.due
            current_paid = self.admission_id.paid
            updated_amount = current_due - pay_amount
            updated_paid = current_paid + pay_amount

            query = "update admission_bill set due=%s,paid=%s where id=%s"
            self._cr.execute(query, [updated_amount, updated_paid, admission_id, ])
            self._cr.commit()

        return "X"

    @api.model
    def create(self,vals):
        payment_id=super(investigation_payment, self).create(vals)
        if payment_id is not None:
            value={}
            value['date']=vals['date']
            value['bill_id']=vals['bill_id']
            value['paid_amount']=vals['amount']
            value['p_type']='due_pay'

            mr_obj=self.env['money.receipt'].create(value)
        return payment_id










