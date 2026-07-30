# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Speciality(models.Model):
    _name = "speciality.speciality"
    _description = "Business Speciality"
    _order = "sequence, name, id"

    name = fields.Char(
        string="Name",
        required=True,
        translate=True,
        help="Display name of the speciality.",
    )
    code = fields.Char(
        string="Code",
        required=True,
        help="Short unique technical code for the speciality.",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        help="Uncheck to archive the speciality without deleting it.",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=10,
        help="Used to order specialities in lists.",
    )
    description = fields.Text(
        string="Description",
        translate=True,
        help="Optional longer description of the speciality.",
    )

    _sql_constraints = [
        (
            "speciality_code_uniq",
            "unique(code)",
            "The speciality code must be unique.",
        ),
    ]

    @api.constrains("code")
    def _check_code(self):
        for record in self:
            code = (record.code or "").strip()
            if not code:
                raise ValidationError(_("Speciality code cannot be empty."))
            if " " in code:
                raise ValidationError(
                    _("Speciality code cannot contain spaces. Use dashes or underscores instead.")
                )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("code"):
                vals["code"] = vals["code"].strip()
            if vals.get("name"):
                vals["name"] = vals["name"].strip()
        return super().create(vals_list)

    def write(self, vals):
        vals = dict(vals)
        if "code" in vals and vals["code"]:
            vals["code"] = vals["code"].strip()
        if "name" in vals and vals["name"]:
            vals["name"] = vals["name"].strip()
        return super().write(vals)
