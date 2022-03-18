# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models


class StockRule(models.Model):

    _inherit = "stock.rule"

    def _get_stock_move_values(
        self,
        product_id,
        product_qty,
        product_uom,
        location_id,
        name,
        origin,
        company_id,
        values,
    ):
        res = super()._get_stock_move_values(
            product_id=product_id,
            product_qty=product_qty,
            product_uom=product_uom,
            location_id=location_id,
            name=name,
            origin=origin,
            company_id=company_id,
            values=values,
        )
        if values.get("sale_line_id", False):
            res.update({"description_picking": name})
        return res
