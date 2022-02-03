from odoo import models,fields
from odoo import api

class patient_profile(models.Model):
    _name = 'patient.info'

    def name_get(self):
        if not self.ids:
            return []
        res=[]
        for elmt in self:
            name=elmt.name
            name=name+ ' ' + str(elmt.patient_id)
            res.append((elmt.id,name))
        return res

    patient_id=fields.Char("Patient Id",readonly=True)
    name=fields.Char("Patient Name",required=True)
    age=fields.Char("Age")
    sex=fields.Selection([('male', 'Male'), ('female', 'Female')], 'Sex', default='male')
    mobile=fields.Char("Mobile No", required=True)
    address=fields.Char("Address")

    @api.model
    def create(self,vals):

        stored=super(patient_profile, self).create(vals)

        patient_name='P-0'+str(stored.id)
        query="update patient_info set patient_id=%s where id=%s"
        self._cr.execute(query,[patient_name,int(stored)])
        self._cr.commit()
        return stored

    @api.model
    def name_search(self,name,args=None, operator='ilike',limit=100):
        args=args or []
        recs=self.browse()
        if name:
            recs=self.search([('patient_id','=',name)]+args,limit=limit)

        if not recs:
            recs=self.search([('patient_id',operator,name)]+args,limit=limit)
        if not recs:
            recs=self.search([('name',operator,name)]+args,limit=limit)
        return recs.name_get()







