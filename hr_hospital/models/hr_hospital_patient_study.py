from odoo import fields, models


class PatientStudy(models.Model):
    _name = 'hr.hospital.patient.study'
    _description = 'Studies of patients'

    name = fields.Char(string='Name', index=True, required=True)
    patient_id = fields.Many2one('hr.hospital.patient', string='Patient',
                                 index=True, required=True)
    doctor_id = fields.Many2one('hr.hospital.doctor', string='Doctor',
                                index=True, required=True)
    study_id = fields.Many2one('hr.hospital.study.type', string='Study',
                               index=True, required=True)
    sample_id = fields.Many2one('hr.hospital.sample.type', string='Sample type',
                                index=True, required=True)
    conclusion = fields.Text('Conclusion', required=True)
