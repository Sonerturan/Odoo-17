from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(
        string="Name", required=True, tracking=True
    )
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender", tracking=True
    )
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string='Tags')
    #tag_ids = fields.Many2many('patient.tag', string='Tags')

    # Silme işlemini inherit alma
    # def unlink: Model Bazlı silme kuralı / @api.ondelete de kullanılabilir: ilişkisel kayıt kontrolü (One2many, Many2one)
    def unlink(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(_("You cannot delete the patient now.\nAppointment existing for this patient: %s"% rec.name))
        return super().unlink() # Yeni Odoo sürümüyle gelen kısaltma özelliği -> eski hali: return super(HospitalPatient, self).unlink()
