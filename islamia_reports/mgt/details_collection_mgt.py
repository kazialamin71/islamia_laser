from odoo import api, models
from odoo import models,fields
from datetime import datetime
from datetime import timedelta

class details_collection_mgt(models.Model):
    _name = 'details.collection.mgt'

    name = fields.Char("Mr ID")



class report_detail_component_mgt(models.AbstractModel):
    _name = 'report.islamia_laser.report_details_collection_mgt'
    _description = 'Product Price List Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        data = data if data is not None else {}
        products = self.env['product.product'].browse(data.get('ids', data.get('active_ids')))
        start_date = data['form']['date_start']
        end_date = data['form']['date_end']
        query="select b.name,b.total_without_discount,b.grand_total,p.name,m.paid_amount,m.p_type,m.doctors_payment,b.flat_discount,b.discount_amount,d.name,pro.name from investigation_bill b" \
              " LEFT JOIN examinee_info pro ON pro.id= b.professionals_name LEFT JOIN patient_info p ON b.patient_name = p.id LEFT JOIN doctors_info d ON b.ref_doctors = d.id LEFT JOIN money_receipt m ON b.id = m.bill_id where b.create_date>= %s and b.create_date<=%s" \
              "and b.state='confirm' group by b.name,b.grand_total,m.doctors_payment," \
              "p.name,m.paid_amount,m.p_type,b.flat_discount,b.discount_amount,d.name,b.total_without_discount ,pro.name order by b.name"

        self._cr.execute(query,[start_date,end_date])
        values=self._cr.fetchall()

        query="select b.name,bie.name from investigation_bill_line ibl LEFT JOIN bill_item_entry bie ON bie.id=ibl.bill_item_entry_id LEFT JOIN investigation_bill b ON ibl.investigation_bill_id=b.id group by b.name,bie.name"

        self._cr.execute(query,[start_date,end_date])
        value=self._cr.fetchall()
        DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        date_field1 = datetime.strptime(start_date, DATETIME_FORMAT)

        date_field2 = datetime.strptime(end_date, DATETIME_FORMAT)

        start_date = date_field1 + timedelta(hours=6, minutes=0)
        end_date = date_field2 + timedelta(hours=6, minutes=0)

        return {
            'doc_ids': data.get('ids', data.get('active_ids')),
            'doc_model': 'details.collection',
            'docs': products,
            'data': dict(
                data,
                values=values,
                value=value,
                start_date=start_date,
                end_date=end_date,
            ),
        }





