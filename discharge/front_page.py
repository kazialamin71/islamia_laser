from odoo import models,fields
from odoo import api

class front_page(models.Model):
    _name = 'front.page'
    _order = 'id desc'

    name=fields.Char("Name")
    patient_name = fields.Many2one('patient.info', "Patient Name", required=True)
    age = fields.Char("Age")
    sex = fields.Char("Sex")
    ward = fields.Char("Ward/Cabin")
    reg = fields.Char("Reg")
    address = fields.Char("Address")
    admit_date=fields.Date("Admission Date")
    discharge_date=fields.Date("Discharge Date")
    admit_by=fields.Many2one("doctors.info","Admitted Under")
    department=fields.Char("Department of")
    # back_page
    drop1 = fields.Char("Drop1")
    drop2 = fields.Char("Drop2")
    drop3 = fields.Char("Drop3")
    drop4 = fields.Char("Drop4")
    tab1 = fields.Char("Tab1")
    tab2 = fields.Char("Tab2")
    tab3 = fields.Char("Tab3")
    tab4 = fields.Char("Tab4")
    operation_note = fields.Char("Operation Note")
    diagnosis = fields.Char("Diagnosis")
    date=fields.Date("Operation Date")
    # surgeon=fields.Many2one("doctors.info","Admitted Under")

    @api.onchange('patient_name')
    def onchange_patient(self):
        self.age=self.patient_name.age
        self.sex=self.patient_name.sex
        self.address=self.patient_name.address
        self.mobile=self.patient_name.mobile


    @api.model
    def create(self,vals):
        stored = super(front_page, self).create(vals)
        discharge_name = 'Discharge-0' + str(stored.id)
        query = "update front_page set name=%s where id=%s"
        self._cr.execute(query, [discharge_name, int(stored)])
        self._cr.commit()
        return stored









