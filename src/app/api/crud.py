from sqlalchemy.orm import Session
from sqlalchemy import func

from app.api.models import InternationalMigration, InternationalMigrationSchema


def post(db_session: Session, payload: InternationalMigrationSchema):
    migration = InternationalMigration(year_month=payload.year_month,
        month_of_release=payload.month_of_release,
        passenger_type=payload.passenger_type,
        direction=payload.direction,
        citizenship=payload.citizenship,
        visa=payload.visa,
        country_of_residence=payload.country_of_residence,
        estimate=payload.estimate,
        standard_error=payload.standard_error,
        status=payload.status)

    db_session.add(migration)
    db_session.commit()
    db_session.refresh(migration)

    return migration


def get_by_id_or_country(db_session: Session, value):
    if value.isdigit():
        return db_session.query(InternationalMigration).filter(InternationalMigration.id == value).all()
    else:
        return db_session.query(InternationalMigration).filter(func.lower(InternationalMigration.country_of_residence) == value.lower()).all()
   

def get_all(db_session: Session):
    return db_session.query(InternationalMigration).all()


def put(db_session: Session, migration: InternationalMigration, year_month: str, month_of_release: str, passenger_type: str, direction: str, citizenship: str, visa: str, country_of_residence: str, estimate: int, standard_error: int, status: str):
    migration.year_month = year_month,
    migration.month_of_release = month_of_release,
    migration.passenger_type = passenger_type,
    migration.direction = direction,
    migration.citizenship = citizenship,
    migration.visa = visa,
    migration.country_of_residence = country_of_residence,
    migration.estimate = estimate,
    migration.standard_error = standard_error,
    migration.status = status

    db_session.commit()

    return migration


def delete(db_session: Session, id: int):
    migration = db_session.query(InternationalMigration).filter(InternationalMigration.id == id).first()

    db_session.delete(migration)
    db_session.commit()

    return migration


def get_visa_country(db_session: Session):
    return db_session.query(InternationalMigration).filter(InternationalMigration.visa != None, InternationalMigration.country_of_residence != None).all()


def get_by_country(db_session: Session, country: str):
    return db_session.query(InternationalMigration).filter(InternationalMigration.country_of_residence == country).all()
