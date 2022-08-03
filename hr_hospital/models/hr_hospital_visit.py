from odoo import fields, models


class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Visit'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor',
                                index=True, required=True)
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient',
                                 index=True, required=True)
    date_of_visit = fields.Date(required=True)
    time_reception = fields.Integer()
    study_ids = fields.Many2many('hr_hospital.patient.study', string='Studies')
    diagnosis_id = fields.Many2one('hr_hospital.diagnosis', string='Diagnosis')
    recommendation = fields.Text(required=True)
