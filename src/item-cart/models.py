

from src.common.database import db
from src.common.utils import timestamp




class Item_cart(db.Model):
    __tablename__ = 'Item_cart'
    id = db.Column(db.Integer, primary_key=True)
    Item_name = db.Column(db.String, nullable=True)

    created_at = db.Column(db.Integer, default=timestamp)


    def to_json(self):
        return {
            'item_name': self.first_name,

        }

    def __repr__(self):
        return '<INFO ID={id} NAME={first_name} UPDATED_AT={created_at}>'.format(
            id=self.id, Item_cart=self.Item_name, created_at=self.created_at
        )