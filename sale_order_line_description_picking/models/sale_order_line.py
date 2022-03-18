# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def write(self, vals):
        """Align sale order description with move picking description
            when description is updated on the sale order"""
        res = super().write(vals)
        if vals.get("name") and self.move_ids.ids:
            moves = self.env["stock.move"].browse(self.move_ids.ids)
            moves.description_picking = vals.get("name")
        return res
