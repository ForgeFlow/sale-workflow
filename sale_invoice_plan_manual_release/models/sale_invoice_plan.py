from odoo import api, fields, models


class SaleInvoicePlan(models.Model):
    _inherit = "sale.invoice.plan"

    released = fields.Boolean()

    @api.depends("released")
    def _compute_to_invoice(self):
        """If any invoice is in draft/open/paid do not allow to create inv.
        Only if the user has manually indicated as released will it be set as
        to invoice.
        """
        super(SaleInvoicePlan, self)._compute_to_invoice()
        for rec in self:
            rec.to_invoice = False
        for rec in self.sorted("installment"):
            if rec.state != "sale":  # Not confirmed, no to_invoice
                continue
            if not rec.invoiced:
                if rec.invoice_type == "advance":
                    rec.to_invoice = True
                elif rec.released:
                    rec.to_invoice = True
