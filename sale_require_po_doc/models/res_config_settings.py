from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    customer_need_po_default = fields.Boolean(
        related="company_id.customer_need_po_default",
        readonly=False
    )
