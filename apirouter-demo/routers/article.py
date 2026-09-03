from fastapi import APIRouter

router = APIRouter(prefix="/article", tags=["article"])



@router.get("/list")
async def article_list():
    return {"articele": ['123456789','abcdefgh']}

@router.get("/{article_id}")
async def article_datail(article_id):
    return {"article_id": article_id}