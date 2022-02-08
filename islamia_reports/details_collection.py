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
        quantities = data['form']['date_start']
        return {
            'doc_ids': data.get('ids', data.get('active_ids')),
            'doc_model': 'details.collection',
            'docs': products,
            'data': dict(
                data,
                pricelist=quantities
            ),
        }





