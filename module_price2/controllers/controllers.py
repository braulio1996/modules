# -*- coding: utf-8 -*-
# from odoo import http


# class ModulePrice2(http.Controller):
#     @http.route('/module_price2/module_price2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_price2/module_price2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_price2.listing', {
#             'root': '/module_price2/module_price2',
#             'objects': http.request.env['module_price2.module_price2'].search([]),
#         })

#     @http.route('/module_price2/module_price2/objects/<model("module_price2.module_price2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_price2.object', {
#             'object': obj
#         })
