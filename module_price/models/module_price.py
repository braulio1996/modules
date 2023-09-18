# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class module_price(models.Model): 
    _name = 'ej.module_price' 
    Nombre = fields.Char(string='Nombre', required=True) 
 
    Edad = fields.Integer(string='Edad', required=True) 

    Ciudad=fields.Char(string='Ciudad', required=True)
 
