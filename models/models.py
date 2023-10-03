# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class gasform_modul(models.Model):
    _name = 'gasform.modul'   
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'gasform module with suppiler and loction'


    suppiler_name=fields.Selection(
        selection=[('Select Supplier','Select Supplier'),
        ('IOCL ','IOCL '),
        ('RELIANCE ','RELIANCE'),
        ('HPCL ','HPCL'),
        ('AEGIS ','AEGIS'),
        ('ADANI ','ADANI'),
        ('GAIL ','GAIL')         
        ],
        string="Supplier",
        default='Select Supplier')


    gasform_name=fields.Selection(
        selection=[('Select Gas','Select Gas'),
        ('BUTANE','BUTANE'),
        ('LPG','LPG'),
        ('PROPANE','PROPANE')
        ],
        string='Gas',
        default='Select Gas',)

    location_gasform=fields.Many2many('city.location',string="Supplier Location")
    price_pr = fields.Float(string='Price', required=True)
    active=fields.Boolean(string="Active", default='True')
   




