from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(
        string="Name", required=True, tracking=True
    )
    description = fields.Char(string="Description")
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender", tracking=True
    )
    tag_ids = fields.Many2many('patient.tag', 'patient_tag_rel', 'patient_id', 'tag_id', string='Tags')
    #tag_ids = fields.Many2many('patient.tag', string='Tags')
    is_minor = fields.Boolean(string="Minor")
    guardian = fields.Char(string="Guardian") # readonly=True
    weight = fields.Float(string="Weight")

    # Silme işlemini inherit alma
    # @api.ondelete: ilişkisel kayıt kontrolü (One2many, Many2one) / def unlink de kullanılabilir: Model Bazlı silme kuralı
    @api.ondelete(at_uninstall=False) # at_uninstall=False: Model kaldırılırken uygulanmaz
    def _check_patient_appointments(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(
                    _("You cannot delete the patient now.\nAppointment existing for this patient: %s" % rec.name))
    """
    def unlink(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(_("You cannot delete the patient now.\nAppointment existing for this patient: %s"% rec.name))
        return super().unlink() # Yeni Odoo sürümüyle gelen kısaltma özelliği -> eski hali: return super(HospitalPatient, self).unlink()
    """

