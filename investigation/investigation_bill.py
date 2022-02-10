from odoo import models, fields
from odoo import api
# import time
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
# from dateutil.relativedelta import relativedelta
# from odoo import date,datetime,time,timedelta
# from openerp.tools.amount_to_text_en import amount_to_text


class investigation_bill(models.Model):
    _name = 'investigation.bill'

    # date=fields.Datetime('Date current action', default=fields.Datetime.now, required=False, readonly=False, select=True)
    date=fields.Date(string='First Day Month', required=True,default=datetime.now().strftime('%Y-%m-%d'))
    name = fields.Char("Name")
    mobile = fields.Char(string="Mobile No")
    patient_id = fields.Char("Patient ID",readonly=True)
    patient_name = fields.Many2one('patient.info', "Patient Name",required=True)
    age = fields.Char("Age")
    sex = fields.Char("Sex")
    address = fields.Char("Address")
    ref_doctors = fields.Many2one('doctors.info', 'Referred By',required=True)
    total_without_discount = fields.Float("Total Without Discount")
    discount = fields.Float("Discount (%)")
    discount_amount=fields.Float("Discounted Amount",readonly=True)
    flat_discount = fields.Float("Flat Discount")
    grand_total = fields.Float("Grand Total")
    paid = fields.Float("Paid")
    due = fields.Float("Due")
    state = fields.Selection([('pending', 'Pending'), ('confirm', 'Confirmed'), ('cancelled', 'Cancelled')], 'Status',
                             default='pending')
    investigation_bill_line_id = fields.One2many('investigation.bill.line', 'investigation_bill_id', "Items",required=True)

    def confirm_bill(self):
        if self.state=='confirm':
            raise ValidationError("Bill is already confirmed.")
        query="update investigation_bill set state=%s where id=%s"
        self._cr.execute(query,['confirm',int(self.id)])
        self._cr.commit()
        mr_value={}
        if self.paid>0:
            mr_value={
                'date':self.date,
                'bill_id':int(self.id),
                'total_amount':self.grand_total,
                'paid_amount':self.paid,
                'due_amount':self.due,
                'p_type':'adv'
            }

        mr_id=self.env['money.receipt'].create(mr_value)
        return self.env.ref('islamia_laser.action_report_investigation_bill').report_action(self)

        # import pdb
        # pdb.set_trace()
        # call_the_report =  self.env.ref('islamia_laser.action_report_investigation_bill').report_action(self)
        # import pdb
        # pdb.set_trace()
        # return call_the_report.update({'close_on_report_download': True})

        # return self.env['ir.actions.report']._get_report_from_name('islamia_laser.report_investigation_bill')

        # report = self.env['ir.actions.report']._get_report_from_name('islamia_laser.report_investigation_bill')
        #
        # records = self.env['investigation.bill'].browse(self.ids)
        # data=None
        # return {
        #     'doc_ids': self._ids,
        #     'doc_model': report.model,
        #     'docs': records,
        #     'data': data,
        #     'execute_code': None,
        #     'datetime': datetime
        # }

    def cancel_bill(self):
        query="update investigation_bill set state=%s where id=%s"
        self._cr.execute(query,['cancelled',int(self.id)])
        query="update money_receipt set state=%s where bill_id=%s"
        self._cr.execute(query,['cancelled',int(self.id)])
        self._cr.commit()


    def add_payment(self):
        if self.state == 'pending':
            raise ValidationError("First Confirm the Bill")
        if self.grand_total<=self.paid:
            raise ValidationError("The bill is already Paid")
        ir_model_data = self.env['ir.model.data']
        template_id = ir_model_data.get_object_reference('islamia_laser', 'investigation_payment_view')[1]
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': template_id,
            'res_model': 'investigation.payment',
            'target': 'new',
            'context':{
                'default_bill_id':self.id,
                'default_amount':self.due
            }
        }


    @api.onchange('patient_name')
    def onchange_patient(self):
        self.age=self.patient_name.age
        self.sex=self.patient_name.sex
        self.patient_id=self.patient_id
        self.address=self.patient_name.address
        self.mobile=self.patient_name.mobile

    @api.onchange('investigation_bill_line_id')
    def investigation_bill_line_onchange(self):
        sum=0
        total_without_discount=0
        for item in self.investigation_bill_line_id:
            sum=sum+item.total
            total_without_discount=total_without_discount+item.rate
            self.total_without_discount=total_without_discount
            self.grand_total=sum
            self.due=self.grand_total-self.paid


    @api.onchange('paid')
    def onchnage_paid(self):
        self.due=self.grand_total-self.paid
    #
    # @api.onchange('discount')
    # def onchange_percent_discount(self):

    @api.onchange('discount')
    def onchange_discount(self):
        self.discount_amount=self.total_without_discount * self.discount/100
        self.grand_total=self.grand_total-(self.total_without_discount * self.discount/100)


    @api.onchange('flat_discount')
    def onchnage_discount(self):
        self.grand_total=self.grand_total-self.flat_discount

    @api.onchange('grand_total')
    def onchnage_grandtotal(self):
        self.due = self.grand_total - self.paid

    @api.model
    def create(self,vals):
        if vals['due']>=0 and vals['paid']>0:
            stored=super(investigation_bill, self).create(vals)
        else:
            raise ValidationError("What!you put wrong value in paid")

        bill_name='Bill-0'+str(stored.id)
        query="update investigation_bill set name=%s where id=%s"
        self._cr.execute(query,[bill_name,int(stored)])
        self._cr.commit()
        return stored




class investigation_bill_line(models.Model):
    _name = 'investigation.bill.line'

    name = fields.Char("Item")
    investigation_bill_id = fields.Many2one('investigation.bill', 'Investigation ID')
    bill_item_entry_id = fields.Many2one("bill.item.entry", "Item Name")
    department = fields.Char("Department")
    rate = fields.Float("Rate")
    discount = fields.Float("Discount")
    total = fields.Float("Total")

    @api.onchange('bill_item_entry_id')
    def onchange_item(self):
        self.department=self.bill_item_entry_id.department.name
        self.rate=self.bill_item_entry_id.rate
        self.total=self.rate-self.discount


    @api.onchange('rate')
    def onchange_rate(self):
        self.total=self.rate

    @api.onchange('discount')
    def onchange_discount(self):
        self.total=self.total-(self.rate*self.discount)/100







