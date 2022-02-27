from odoo import models,fields
from datetime import datetime, timedelta

class daily_collection_mgt(models.Model):
    _name = 'daily.collection.mgt'

    date_start = fields.Datetime("Start Date")
    date_end = fields.Datetime("End Date")

    def print_report(self):
        datas = {'ids': self.env.context.get('active_ids', [])}
        res=self.read(['date_start','date_end'])
        res=res and res[0] or {}
        datas['form']=res
        return self.env.ref('islamia_laser.action_report_details_collection_mgt').report_action([], data=datas)

    def cancel(self):
        return True

















































































































































































