# -*- coding: utf-8 -*-
# Copyright 2013-2014 Camptocamp SA - Guewen Baconnier
# © 2016 Eficent Business and IT Consulting Services S.L.
# © 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{'name': 'Sale Sourced by Line',
 'summary': 'Multiple warehouse source locations for Sale order',
 'version': '9.0.1.0.0',
 'author': "Camptocamp,Odoo Community Association (OCA)",
 'category': 'Warehouse',
 'license': 'AGPL-3',
 'complexity': 'expert',
 'images': [],
 'website': "http://www.camptocamp.com",
 'description': """
Sale Sourced by Line
====================

Adds the possibility to source a line of sale order from a specific
warehouse instead of using the warehouse of the sale order.

This will create one procurement group per warehouse set in sale
order lines.

It will only supports routes such as MTO and Drop Shipping.

Contributors
------------

* Guewen Baconnier <guewen.baconnier@camptocamp.com>
* Yannick Vaucher <yannick.vaucher@camptocamp.com>

""",
 'depends': ['sale_stock',
             'sale_procurement_group_by_line',
             ],
 'demo': [],
 'data': ['view/sale_view.xml',
          ],
 'test': ['test/sale_order_source.yml',
          'test/sale_order_multi_source.yml',
          'test/sale_order_not_sourced.yml',
          ],
 'auto_install': False,
 'installable': True,
 }
