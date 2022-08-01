# -*- coding: utf-8 -*-
from odoo import models, fields


class HospitalDoctor(models.Model):
    """A class used to represent a Doctor"""
    _name = 'hr.hospital.doctor'
    _inherit = ['hr.hospital.person.mixin', ]
    _description = "Hospital doctor"

    specialty = fields.Char('specialty', required=True)
    is_intern = fields.Boolean('Is Intern')
    mentor_id = fields.Many2one('hr.hospital.doctor', string='Mentor',
                                domain=[('is_intern', '=', False)])
    description = fields.Text()

    def name_get(self):
        return [(rec.id,
                 "phD %s %s" % (rec.last_name,
                                rec.first_name)
                 ) for rec in self]
