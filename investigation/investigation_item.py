from odoo import models, fields
from odoo import api


class investigation_item(models.Model):
    _name = 'investigation.item'

    name = fields.Char("Name")
    mobile = fields.Char(string="Mobile No")
    patient_id = fields.Char("Patient ID")
    patient_name = fields.Many2one('patient.info', "Patient Name")
    age = fields.Char("Age")
    sex = fields.Char("Sex")
    address = fields.Char("Address")
    ref_doctors = fields.Many2one('doctors.info', 'Referred By')
    total_without_discount = fields.Float("Total Without Discount")
    discount = fields.Float("Discount (%)")
    flat_discount = fields.Float("Flat Discount")
    grand_total = fields.Float("Grand Total")
    paid = fields.Float("Paid")
    due = fields.Float("Due")
    state = fields.Selection([('pending', 'Pending'), ('confirm', 'Confirmed'), ('cancelled', 'Cancelled')], 'Status',
                             default='pending')
    investigation_item_line_id = fields.One2many('investigation.item.line', 'investigation_item_id', "Items")

    @api.onchange('patient_name')
    def onchange_patient(self):
        self.age=self.patient_name.age
        self.sex=self.patient_name.sex
        self.patient_id=self.patient_name.id
        self.address=self.patient_name.address
        self.mobile=self.patient_name.mobile

    @api.onchange('investigation_item_line_id')
    def investigation_item_line_onchange(self):
        sum=0
        total_without_discount=0
        for item in self.investigation_item_line_id:
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






    @api.model
    def create(self,vals):

        stored=super(investigation_item, self).create(vals)

        bill_name='Bill-0'+str(stored.id)
        query="update investigation_item set name=%s where id=%s"
        self._cr.execute(query,[bill_name,int(stored)])
        self._cr.commit()
        return stored




class investigation_item_line(models.Model):
    _name = 'investigation.item.line'

    name = fields.Char("Item")
    investigation_item_id = fields.Many2one('investigation.item', 'Investigation ID')
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






