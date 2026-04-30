# Copyright 2026 ForgeFlow S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Sale Sequence",
        copy=False,
    )
    sequence_mismatch = fields.Boolean(
        compute="_compute_sequence_mismatch",
    )

    def _compute_sequence_mismatch(self):
        for order in self:
            order.sequence_mismatch = bool(
                order.team_id.sequence_id
                and order.sequence_id != order.team_id.sequence_id
            )

    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", _("New")) == _("New") and vals.get("team_id"):
                team = self.env["crm.team"].browse(vals["team_id"])
                if team.sequence_id:
                    seq_date = (
                        fields.Datetime.context_timestamp(
                            self, fields.Datetime.to_datetime(vals["date_order"])
                        )
                        if "date_order" in vals
                        else None
                    )
                    vals["name"] = (
                        team.sequence_id.next_by_id(sequence_date=seq_date) or _("New")
                    )
                    vals["sequence_id"] = team.sequence_id.id
        return super().create(vals_list)

    def action_renumber_from_team_sequence(self):
        self.ensure_one()
        if not self.team_id.sequence_id:
            return
        self.name = self.team_id.sequence_id.next_by_id() or self.name
        self.sequence_id = self.team_id.sequence_id
