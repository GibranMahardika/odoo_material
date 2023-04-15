# -*- coding: utf-8 -*-
{
    'name': "showroom",

    'summary': """
        Module custom for Showroom
    """,

    'description': """

        1. Material Code
        2. Material Name
        3. Material Type (dropdown 3 pilihan: Fabric, Jeans, Cotton)
        4. Material Buy Price
        5. Related Supplier (dropdown : Nama supplier)
        
        Seluruh informasi tersebut harus terisi, dan untuk material buy price tidak boleh nilainya < 100.
    """,

    'author': "Gibran Mahardika",
    'website': "https://www.linkedin.com/in/gibranmahardika/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'sequence': 10,
    'installable': True,
    'application': True,
    'auto-install': False,
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/material_group.xml',
        'security/ir.model.access.csv',

        'views/menu_action.xml',
        'views/menu_item.xml',

        'views/master_data.xml',
        # 'views/res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
