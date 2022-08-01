# -*- coding: utf-8 -*-
from odoo import models, fields


class HospitalDiagnosis(models.Model):
    """A class used to represent a Diagnosis"""
    _name = 'hr.hospital.diagnosis'
    _description = "Hospital diagnosis"

    name = fields.Char(index=True, required=True)
    active = fields.Boolean(default=True)
    doctor_id = fields.Many2one('hr.hospital.doctor', string='Doctor',
                                 index=True, required=True)
    patient_id = fields.Many2one('hr.hospital.patient', string='Patient',
                                 index=True, required=True)
    disease_id = fields.Many2one('hr.hospital.disease', string='Disease',
                                 index=True, required=True)
    date_of_diagnosis = fields.Date('Date of diagnosis')
    study_ids = fields.Many2many('hr.hospital.patient.study', string='Studies')
    prescribed_treatment = fields.Text(string='Prescribed treatment')
    comments_of_mentor = fields.Text('Comments of mentor', required=False)