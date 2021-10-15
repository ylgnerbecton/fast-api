from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app.api import crud
from app.api.models import InternationalMigrationDB, InternationalMigrationSchema
from app.db import SessionLocal


router = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/", response_model=InternationalMigrationDB, status_code=201)
def create_migration(*, db: Session = Depends(get_db), payload: InternationalMigrationSchema):
    migration = crud.post(db_session=db, payload=payload)
    return migration


@router.get("/items/", response_model=List[InternationalMigrationDB])
def read_all_visa_country(db: Session = Depends(get_db)):
    migration = crud.get_visa_country(db_session=db)

    if not migration:
        raise HTTPException(status_code=404, detail="Data not found")

    return migration


@router.get("/{value}/", response_model=List[InternationalMigrationDB])
def read_migration_by_id_or_country(*, db: Session = Depends(get_db), value):
    migration = crud.get_by_id_or_country(db_session=db, value=value)

    if not migration:
        raise HTTPException(status_code=404, detail="Data not found")

    return migration


@router.get("/", response_model=List[InternationalMigrationDB])
def read_all_migrations(db: Session = Depends(get_db)):
    return crud.get_all(db_session=db)


@router.put("/{id}/", response_model=InternationalMigrationDB)
def update_migration(*, db: Session = Depends(get_db), id: int = Path(..., gt=0), payload: InternationalMigrationSchema):
    migration = crud.get(db_session=db, id=id)

    if not migration:
        raise HTTPException(status_code=404, detail="Data not found")

    migration = crud.put(db_session=db, migration=migration, payload=payload)

    return migration


@router.delete("/{id}/", response_model=InternationalMigrationDB)
def delete_migration(*, db: Session = Depends(get_db), id: int = Path(..., gt=0)):
    migration = crud.get(db_session=db, id=id)

    if not migration:
        raise HTTPException(status_code=404, detail="Data not found")

    migration = crud.delete(db_session=db, id=id)

    return migration
