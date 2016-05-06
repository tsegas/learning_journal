import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime,
    )


from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    #__tablename__ = 'models'
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    title = Column(Unicode(255), unique=True, primary_key=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
