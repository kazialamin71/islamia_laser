from odoo import models,fields

class back_page(models.Model):
    _name = 'back.page'
    _order = 'id desc'

    name=fields.Char("Name")
    drop1 = fields.Char("Drop1")
    drop2 = fields.Char("Drop2")
    drop3 = fields.Char("Drop3")
    drop4 = fields.Char("Drop4")
    tab1 = fields.Char("Tab1")
    tab2 = fields.Char("Tab2")
    tab3 = fields.Char("Tab3")
    tab4 = fields.Char("Tab4")
    operation_note = fields.Char("Operation Note")
    date=fields.Date("Date")
    surgeon=fields.Many2one("doctors.info","Admitted Under")
    department=fields.Char("Department of")








