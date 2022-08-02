from odoo import fields, models


class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Visit'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor',
                                index=True, required=True)
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient',
                                 index=True, required=True)
    date_of_visit = fields.Date('Date of visit', required=True)
    time_reception = fields.Integer('Time reception')
    study_ids = fields.Many2many('hr_hospital.patient.study', string='Studies')
    diagnosis_id = fields.Many2one('hr_hospital.diagnosis', string='Diagnosis')
    recommendation = fields.Text('Recommendation', required=True)
