# -*- coding: utf-8 -*-
from odoo import http

# class KpModule(http.Controller):
#     @http.route('/kp_module/kp_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kp_module/kp_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kp_module.listing', {
#             'root': '/kp_module/kp_module',
#             'objects': http.request.env['kp_module.kp_module'].search([]),
#         })

#     @http.route('/kp_module/kp_module/objects/<model("kp_module.kp_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kp_module.object', {
#             'object': obj
#         })