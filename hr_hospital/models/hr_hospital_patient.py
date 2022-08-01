# -*- coding: utf-8 -*-
from datetime import date

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class HospitalPatient(models.Model):
    """A class used to represent a Patient"""
    _name = 'hr.hospital.patient'
    _inherit = ['hr.hospital.person.mixin', ]
    _description = "Hospital patient"

    name = fields.Char('Name', index=True, required=True)
    date_of_birth = fields.Date(string='Date of birth', required=True)
    age = fields.Integer(string='Age',
                         compute='_compute_age',
                         compute_sudo=True, store=True)

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

    passport_series = fields.Char('Passport series', size=2, )
    passport_number = fields.Char('Passport number', size=6, )
    passport_issued = fields.Date('Passport issued', )
    passport_issued_by = fields.Char('Passport issued by', )

    contact_person_id = fields.Many2one('hr.hospital.contact.person',
                                        string='Contact person')
    personal_doctor_id = fields.Many2one('hr.hospital.doctor', string='Personal doctor', )
    description = fields.Text(string='Description')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for man in self:
            man.age = \
                relativedelta(fields.Date.today(), man.date_of_birth).years \
                if man.date_of_birth else 0

    @api.model
    def create(self, vals):
        new_record = super().create(vals)
        if 'personal_doctor_id' in vals:
            self.env['hr.hospital.personal.doctor.history'].create({
                'doctor_id': vals['personal_doctor_id'],
                'patient_id': new_record.id,
                'appointment_date': date.today(), })
        return new_record

    def write(self, vals):
        if 'personal_doctor_id' not in vals:
            return super().write(vals)
        for obj in self:
            if obj.personal_doctor_id.id != vals.get('personal_doctor_id'):
                self.env['hr.hospital.personal.doctor.history'].create({
                    'doctor_id': vals.get('personal_doctor_id'),
                    'patient_id': obj.id, 'appointment_date': date.today(), })
            val = vals.deepcopy()
            if obj.contact_person_id:
                val['passport_number'] = '1111 {}'.format(obj.passport_series)
            super('Patient', obj).write(val)
        return True

