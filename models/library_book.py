from odoo import api, fields, models
from odoo.exceptions import Warning

class Book (models.Model):
    _name = 'library.book'
    _description = 'Book'
    _order = 'name, date_published desc'
    
    @api.multi
    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check =  10 -remain if remain != 0 else 0
            return digets[-1] == check
    
    @api.multidef button_check_isbn(self):
    for book in self:
        if not book.isbn:
            raise Warning('Please provide an ISBN for %s' % book.name)
        if book.ispn and not book._check_isbn():
            raise Warning('%s is an invalid ISBN' % book.isbn)
        return True
        
    # these are text fields
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    notes = fields.Text('internal notes')
    desc = fields.Html('Description')
    # date fields
    date_published = fields.Date()
    # other fields
    active = fields.Boolean('active?', default=True)
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')

