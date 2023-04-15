from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class masterData(models.Model):
    _name = 'master.data'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'material_name'
    
    @api.constrains('material_price')
    def _date_check(self):
        for x in self:
            if x.material_price < 100:
                raise ValidationError(
                    'Material Buy Price tidak boleh nilainya < 100')

    material_name = fields.Char(
        string="Material Name", tracking=True, required=True)
    material_code = fields.Char(
        string="Material Code", tracking=True, required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string="Material Type", tracking=True)
    material_price = fields.Integer(
        string="Material Buy Price", tracking=True)
    supplier_id = fields.Many2one(
        'res.partner', string="Related Supplier", tracking=True)
