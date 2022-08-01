from odoo import fields, models


class PersonalDoctorHistory(models.Model):
    _name = 'hr.hospital.personal.doctor.history'
    _description = 'History of personal doctors'

    name = fields.Char('Name', index=True, required=True)
    doctor_id = fields.Many2one('hr.hospital.doctor', string='Personal doctor',
                                index=True, required=True)
    patient_id = fields.Many2one('hr.hospital.patient', string='Patient',
                                 index=True, required=True)
    appointment_date = fields.Date('appointment date',
                                   index=True, required=True)

    def name_get(self):
        return [(tag.id, "%s - %s: %s" % (tag.patient_id.name, tag.doctor_id.name, tag.appointment_date)) for tag in self]
