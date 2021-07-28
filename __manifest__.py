# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Res partner custom',
    'version': '1.1',
    'category': 'Custom',
    'summary': 'Res partner custom',
    'description': """
    ...
    """,
    'depends': ['base'],
    'data': [
        'views/res_partner_view.xml',
        ],
    #===========================================================================
    # 'qweb': [
    #     "static/src/xml/account_reconciliation.xml",
    # ],
    #===========================================================================
    'installable': True,
    'auto_install': False
}