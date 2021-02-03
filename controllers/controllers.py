# -*- coding: utf-8 -*-
# from odoo import http


# class SaitolabTodo(http.Controller):
#     @http.route('/saitolab_todo/saitolab_todo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saitolab_todo/saitolab_todo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saitolab_todo.listing', {
#             'root': '/saitolab_todo/saitolab_todo',
#             'objects': http.request.env['saitolab_todo.saitolab_todo'].search([]),
#         })

#     @http.route('/saitolab_todo/saitolab_todo/objects/<model("saitolab_todo.saitolab_todo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saitolab_todo.object', {
#             'object': obj
#         })
