# -*- coding: utf-8 -*-
{
    'name': "library_app",

    'summary': """
        This is an app for creating a Library!
    """,

    'description': """
        Create books, add and checkout books and things.
    """,

    'author': "Precision Solutions, Patrick",
    'website': "http://www.precisonline.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '12.0.1.6',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # module or extension
    'application': True,

    # always loaded
    'data': [
        'views/library_menu.xml',
        'views/book_view.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}