from odoo import models, fields, api


class Todo(models.Model):
    _name = 'saitolab.todo'
    _description = 'El modelo principal de saitolab_todo'

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[
        ("borrador", "Borrador"),
        ("hecho", "Hecho")
    ])
