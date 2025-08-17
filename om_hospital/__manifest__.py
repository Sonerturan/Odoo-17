# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Managament System',
    'version' : '1.2',
    'summary': 'Hospital',
    'sequence': -1,
    "author": "Soner Turan ",
    'description': """
Hospital Managament System Development
    """,
    'category': 'Human Resources',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': [
        'mail',
        'product',
        'account'
    ],
    'data': [
        "security/rule.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/patient_views.xml",
        "views/patient_tag_views.xml",
        "views/patient_readonly_views.xml",
        "views/appointment_views.xml",
        "views/appointment_lines_views.xml",
        "views/menu.xml"
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
