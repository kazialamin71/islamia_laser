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
        'configuration/investigation_item_view.xml',
        'menu_item_islamia.xml',
        'security/islamia_security.xml',
        'security/ir.model.access.csv',
        'configuration/patient_profile_view.xml',
        'configuration/doctors_profile_view.xml',
        'configuration/department_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': ['static/src/xml/hr_templates.xml'],
    'license': 'LGPL-3',
}
