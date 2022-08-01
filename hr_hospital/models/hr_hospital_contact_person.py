from odoo import models, fields


class ContactPerson(models.Model):
    _name = 'hr.hospital.contact.person'
    _inherit = ['hr.hospital.person.mixin', ]
    _description = 'Contact person'

    description = fields.Text()
