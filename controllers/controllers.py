# -*- coding: utf-8 -*-
# from odoo import http


# class GasformModul(http.Controller):
#     @http.route('/gasform_modul/gasform_modul', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gasform_modul/gasform_modul/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gasform_modul.listing', {
#             'root': '/gasform_modul/gasform_modul',
#             'objects': http.request.env['gasform_modul.gasform_modul'].search([]),
#         })

#     @http.route('/gasform_modul/gasform_modul/objects/<model("gasform_modul.gasform_modul"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gasform_modul.object', {
#             'object': obj
#         })
