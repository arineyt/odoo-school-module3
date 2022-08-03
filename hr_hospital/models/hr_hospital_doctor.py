from odoo import models, fields


class HospitalDoctor(models.Model):
    """A class used to represent a Doctor"""
    _name = 'hr_hospital.doctor'
    _inherit = ['hr_hospital.person.mixin', ]
    _description = "Hospital doctor"

    specialty = fields.Char('specialty', required=True)
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one('hr_hospital.doctor', string='Mentor',
                                domain=[('is_intern', '=', False)])
    description = fields.Text()
