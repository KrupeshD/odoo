# -*- coding: utf-8 -*-
{
    'name': "kp_module",

    'summary': """
        Inheriting models and odoo view""",

    'description': """
        nheriting models and odoo view
    """,

    'author': "Venus Informatics",
    'website': "http://www.venusinformatics.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
