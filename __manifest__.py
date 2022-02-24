# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Islamia',
    'version': '1.1',
    'category': '',
    'sequence': 145,
    'summary': 'Islamia Eye Laser Center',
    'description': "",
    'website': 'https://www.odoo.com/page/employees',
    'images': [
    ],
    'depends': [
        'base_setup',
    ],
    'data': [
        'menu_item_islamia.xml',
        'security/islamia_security.xml',
        'security/ir.model.access.csv',
        'investigation/investigation_bill_view.xml',
        'configuration/patient_profile_view.xml',
        'configuration/doctors_profile_view.xml',
        'configuration/examinee_profile_view.xml',
        'configuration/department_view.xml',
        'configuration/bill_item_entry_view.xml',
        'configuration/admission_item_entry_view.xml',
        'admission/admission_bill_view.xml',
        'money_receipt/money_receipt_view.xml',
        'investigation/report/investigation_report_btn.xml',
        'investigation/report/report_investigation_bill.xml',
        'investigation/bill_payment/investigation_payment_view.xml',
        'admission/report/admission_report_btn.xml',
        'admission/report/report_admission_bill.xml',
        'wizard/daily_collection_view.xml',
        'wizard/daily_collection_mgt_view.xml',
        'islamia_reports/details_collection_report.xml',
        'islamia_reports/detail_report_template.xml',
        'islamia_reports/mgt/details_collection_report_mgt.xml',
        'islamia_reports/mgt/detail_report_template_mgt.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': ['static/src/xml/hr_templates.xml'],
    'license': 'LGPL-3',
}
