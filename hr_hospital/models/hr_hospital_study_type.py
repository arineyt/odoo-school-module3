from odoo import fields, models


class StudyType(models.Model):
    _name = 'hr.hospital.study.type'
    _description = 'Type of study'
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char('Name', index=True, required=True)
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('hr.hospital.study.type', 'Parent Type', index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hr.hospital.study.type', 'parent_id', 'Child Type')