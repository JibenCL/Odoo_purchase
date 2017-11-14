# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2016 - Turkesh Patel. <http://www.almightycs.com>
#
#    @author Turkesh Patel <info@almightycs.com>
###########################################################################

{
    'name': "Product Purchase Details",
    'category': "Purchase",
    'version': "1.0.0",
    'summary': """Purchase Details or Purchase History on product from view.""",
    'description': """Purchase details on product from view.""",
    'author': 'Almighty Consulting Services',
    'website': 'http://www.almightycs.com',
    'depends': ['purchase'],
    'data': [
        'views/product_view.xml',
    ],
    'images': [
        'static/description/product_purchase_history_odoo_almightycs_cover.jpg',
    ],
    'installable': True,
    'application': False,
    'sequence': 1,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
