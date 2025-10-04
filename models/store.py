from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    
    items = db.relationship("ItemModel", back_populates="store", lazy='dynamic', cascade="all, delete")
    tags = db.relationship("TagModel", back_populates="store", lazy='dynamic')
    # lazy='dynamic' means that items and tags will not be loaded from the database until they are accessed. 
    # This is useful for performance optimization, 
    # especially when dealing with large collections.