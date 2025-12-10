from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    customer_need_po_default = fields.Boolean(
        string="Default: Customer Requires PO",
        help="If True, new customers will have 'Customer Requires PO' "
        "enabled by default.",
    )
