# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class multi-companies(models.Model):
#     _name = 'multi-companies.multi-companies'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#     new_field_ids = fields.One2many(comodel_name="", inverse_name="", string="", required=False, )
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100