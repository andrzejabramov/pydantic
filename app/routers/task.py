from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import insert, select, update
from app.schemas import CreateTask
from app.backend.db_depends import get_db
from sqlalchemy.orm import Session
from typing import Annotated
from app.models import *
from slugify import slugify

router = APIRouter(prefix="/task", tags=['task'])


@router.get("/task_id")
async def get_task_by_id():
    pass

@router.post("/create")
async def create_task():
    pass

@router.put("/update")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass