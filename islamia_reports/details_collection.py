from odoo import api, models
from odoo import models,fields

class details_collection(models.Model):
    _name = 'details.collection'

    name = fields.Char("Mr ID")



class report_detail_component(models.AbstractModel):
    _name = 'report.islamia_laser.report_details_collection'
    _description = 'Product Price List Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        data = data if data is not None else {}
        products = self.env['product.product'].browse(data.get('ids', data.get('active_ids')))
        start_date = data['form']['date_start']
        end_date = data['form']['date_end']
        query="select b.name,b.grand_total,p.name,m.paid_amount,m.p_type from investigation_bill b,patient_info p, money_receipt m " \
              "where p.id=b.patient_name and b.id=m.bill_id and b.create_date>= %s and b.create_date<=%s" \
              "and b.state='confirm' group by b.name,b.grand_total," \
              "p.name,m.paid_amount,m.p_type order by b.name desc"
        self._cr.execute(query,[start_date,end_date])
        values=self._cr.fetchall()
        return {
            'doc_ids': data.get('ids', data.get('active_ids')),
            'doc_model': 'details.collection',
            'docs': products,
            'data': dict(
                data,
                values=values,
                start_date=start_date,
                end_date=end_date
            ),
        }





