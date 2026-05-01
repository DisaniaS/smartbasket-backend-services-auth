from fastapi import APIRouter, status

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK
)
def check():
    return "200"
