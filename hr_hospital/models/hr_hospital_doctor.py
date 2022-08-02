# -*- coding: utf-8 -*-
from odoo import models, fields


class HospitalDoctor(models.Model):
    """A class used to represent a Doctor"""
    _name = 'hr_hospital.doctor'
    _inherit = ['hr_hospital.person.mixin', ]
    _description = "Hospital doctor"

    name = fields.Char(index=True, required=True)
    specialty = fields.Char('specialty', required=True)
    is_intern = fields.Boolean('Is Intern')
    mentor_id = fields.Many2one('hr_hospital.doctor', string='Mentor',
                                domain=[('is_intern', '=', False)])
    description = fields.Text()

