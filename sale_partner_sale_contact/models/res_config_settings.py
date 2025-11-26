# Copyright 2026 OpenStudio SAS
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sale_display_contact_on_reports = fields.Boolean(
        string="Display sale contact on reports",
        related="company_id.sale_display_contact_on_reports",
        readonly=False,
        help=(
            "If enabled, the sale contact will be displayed on "
            "sale orders and invoices PDF reports."
        ),
    )

    # Module installation checkboxes
    module_sale_order_partner_company_only = fields.Boolean(
        string="Restrict customer selection to company only in quotation and order",
    )
    module_account_invoice_partner_company_only = fields.Boolean(
        string="Restrict customer selection to company only on invoice",
    )
    module_project_partner_company_only = fields.Boolean(
        string="Restrict customer selection to company only in projects",
    )
