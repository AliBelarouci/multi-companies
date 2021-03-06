from odoo import api, fields, models


class ResCompny(models.Model):
    _inherit = 'res.company'

    # active = fields.Boolean(string="Active")
    numSS = fields.Char(string="Num Sécurité Sociale", required=True, )
    nom = fields.Char(string="Raison sociale", required=True, )
    gerant = fields.Char(string="Gerant", required=True, )

    dateAff = fields.Char(string="Date Affiliation", required=True, )
    raison = fields.Selection([
        ('raison1', 'raison1'),
        ('raison2', 'raison2'),
    ], string='Raison sociale', default='raison1')
    caisseCnas = fields.Selection([
        ('cnas39', 'Agence Cnas Eloued'),
        ('cnas30', 'Agence Cnas Ouargla'),
    ], string='Caisse Cnas', default='cnas39')
    centre = fields.Selection([
        ('ctr39', 'Eloued'),
        ('ctr30', 'Ouargla'),
    ], string='Centre', default='ctr39')
    dec_cnas = fields.Selection([
        ('mens', 'Mensuelle'),
        ('tri', 'Trimestrielle'),

    ], string='Declaration Cnas', default='tri')
    dec_g29 = fields.Selection([
        ('tri', 'Trimestrielle'),
    ], string='Declaration G29', default='tri')

    def Active_company(self):
        for c in self:
            id=c.read()[0]['id']
            context = self._context
            current_uid = context.get('uid')
            user = self.env['res.users'].sudo().browse(current_uid).write({'company_id': id})
    def GetCurrentCompany(self):
        context = self._context
        current_uid = context.get('uid')
        self.env['res.users'].sudo().browse(current_uid)
        return self.env['res.company'].search(['id','=','1'])

        return
class ResCompanyYearFisc(models.Model):
    _name = 'year_fisc'
    year = fields.Integer(string="Year Fiscal", required=False, )
    active_year = fields.Boolean(string="Active",  )
    def Active_yearFct(self):

        for record in self.env['year_fisc'].search([]):
            record.active_year=False
        for record in self:
            record.write({'active_year': not record.active_year})


        return
    def getActive(self):
        for record in self.env['year_fisc'].search([]):
            if(record.active_year):
                return record.year
        return




