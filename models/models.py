# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class saitolab_todo(models.Model):
#     _name = 'saitolab_todo.saitolab_todo'
#     _description = 'saitolab_todo.saitolab_todo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
