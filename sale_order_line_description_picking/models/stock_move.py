# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class StockMove(models.Model):

    _inherit = "stock.move"

    def _prepare_procurement_values(self):
        res = super()._prepare_procurement_values()
        if self.sale_line_id:
            res.update(
                {
                    "description_picking": self.sale_line_id.name
                    or False,
                }
            )
        return res
