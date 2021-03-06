from datetime import timedelta
from odoo import models, fields

class LibraryBook(models.Model):
    _inherit = 'library.book'

    date_return = fields.Date('Date to return')

    max_borrow_days = fields.Integer(
        'Maximum borrow days',
        help="For how many days book can be borrowed",
        default=10
    )

    def make_borrowed(self):
        day_to_borrow = self.category_id.max_borrow_days or 10
        self.date_return = fields.Date.today() + timedelta(days=day_to_borrow)
        return super(LibraryBook, self).make_borrowed()

    def make_avaliable(self):
        self.date_return = False
        return super(LibraryBook, self).make_avaliable()

        