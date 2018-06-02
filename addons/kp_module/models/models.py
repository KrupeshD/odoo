# -*- coding: utf-8 -*-

from odoo import models, fields, api

class kp_module(models.Model):
    _inherit='sale.order'
    new_field = fields.Char(string='Order Number')
