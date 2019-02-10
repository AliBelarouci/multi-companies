# -*- coding: utf-8 -*-
from odoo import http

# class Multi-companies(http.Controller):
#     @http.route('/multi-companies/multi-companies/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multi-companies/multi-companies/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('multi-companies.listing', {
#             'root': '/multi-companies/multi-companies',
#             'objects': http.request.env['multi-companies.multi-companies'].search([]),
#         })

#     @http.route('/multi-companies/multi-companies/objects/<model("multi-companies.multi-companies"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multi-companies.object', {
#             'object': obj
#         })