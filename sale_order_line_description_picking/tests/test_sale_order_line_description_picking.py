# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common


class TestSaleOrderLineDescriptionPicking(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.warehouse = cls.env.ref("stock.warehouse0")
        cls.sale_obj = cls.env["sale.order"]
        cls.sale_order_line_obj = cls.env["sale.order.line"]
        cls.product1 = cls.env.ref("product.product_product_12")
        cls.product2 = cls.env.ref("product.product_product_13")
        cls.agrolait = cls.env.ref("base.res_partner_2")

        # Create a MTO Rule on Stock - Avoid depending on purchase
        # Create another Stock location
        vals = {
            "name": "Stock MTO",
            "location_id": cls.env.ref("stock.stock_location_locations").id,
            "usage": "internal",
        }
        loc_mto = cls.env["stock.location"].create(vals)

        vals = {
            "name": "New MTO",
        }
        cls.route_mto = cls.env["stock.location.route"].create(vals)

        vals = {
            "name": "STOCK MTO -> Stock",
            "action": "pull",
            "picking_type_id": cls.env.ref("stock.picking_type_internal").id,
            "location_src_id": loc_mto.id,
            "location_id": cls.env.ref("stock.stock_location_stock").id,
            "route_id": cls.route_mto.id,
        }
        cls.env["stock.rule"].create(vals)
        cls.product1.route_ids |= cls.route_mto

    def _create_sale_order(self):

        vals = {
            "partner_id": self.agrolait.id,
        }
        self.order = self.sale_obj.create(vals)
        self.order.onchange_partner_id()
        vals = {
            "order_id": self.order.id,
            "product_id": self.product1.id,
            "product_uom_qty": 10.0,
        }
        self.sale_line = self.sale_order_line_obj.create(vals)
        self.sale_line.product_id_change()
        vals = {
            "order_id": self.order.id,
            "product_id": self.product2.id,
            "product_uom_qty": 20.0,
        }
        self.sale_line_2 = self.sale_order_line_obj.create(vals)
        self.sale_line_2.product_id_change()

    def test_00_keep_description_picking_same_as_in_order(self):
        self._create_sale_order()
        self.sale_line_2.name = (
            "This is a custom description picking for that product"
        )
        self.sale_line.name = (
            "This is a custom description picking for that product"
        )
        self.order.action_confirm()
        self.assertTrue(
            all(
                value == "This is a custom description picking for that product"
                for value in self.order.order_line.move_ids.mapped(
                    "description_picking"
                )
            )
        )
        self.sale_line_2.name = (
            "This is a custom description picking for that product 2"
        )
        self.assertTrue(self.sale_line_2.move_ids[0].description_picking == self.sale_line_2.name)
