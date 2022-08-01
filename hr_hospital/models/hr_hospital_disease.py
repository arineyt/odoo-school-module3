from odoo import fields, models


class Disease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease'

    name = fields.Char('Name', index=True, required=True)
    active = fields.Boolean(default=True)
    disease_type_id = fields.Many2one('hr.hospital.disease.type',
                                      string='Disease type',
                                      index=True,
                                      required=True,
                                      )
    description = fields.Text('Description')
