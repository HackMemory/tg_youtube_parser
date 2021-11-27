import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from data import config

log = logging.getLogger(__name__)

db_engine = create_engine(
    'sqlite:///%s' % config.DB_FILE,
    echo=config.DEBUG,
    isolation_level='AUTOCOMMIT',
)


@contextmanager
def db_session():
    session = scoped_session(
        sessionmaker(bind=db_engine, expire_on_commit=False)
    )
    try:
        session.execute('PRAGMA foreign_keys=ON')  # sqlite cascade delete fix
        yield session
        session.commit()
    except:
        log.error('An error has occured in runtime SQL query.')
        session.rollback()
        raise
    finally:
        session.close()