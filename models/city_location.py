from odoo import models, fields, api




class city_location(models.Model):
    _name = 'city.location'


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

    name = fields.Char("City Name")


    gasform_name=fields.Selection(
        selection=[('Select Gas','Select Gas'),
        ('BUTANE','BUTANE'),
        ('LPG','LPG'),
        ('PROPANE','PROPANE')
        ],
        string='Gas',
        default='Select Gas',)

    
