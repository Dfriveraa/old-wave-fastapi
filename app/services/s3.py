from typing import List

import boto3
from fastapi import HTTPException, UploadFile

from app.config import settings


class BucketService:
    def __init__(self):

        self.__client = boto3.client(
            "s3",
            aws_access_key_id=settings.ACCESS_KEY_ID,
            aws_secret_access_key=settings.SECRET_ACCESS_KEY_PASSWORD,
        )

    def upload_file(self, file: UploadFile) -> str:
        if settings.ENVIRONMENT != "test":
            self.__client.upload_fileobj(file.file, settings.BUCKET_NAME, file.filename)
        return (
            f"https://{settings.BUCKET_NAME}.s3.amazonaws.com/{file.filename}".replace(
                " ", "+"
            )
        )

    def validate_format(self, files: List[UploadFile]):
        for file in files:
            if file.content_type not in [
                "image/gif",
                "image/png",
                "image/jpeg",
                "image/bmp",
                "image/webp",
            ]:
                raise HTTPException(status_code=422, detail="Invalid images format")


s3_service = BucketService()
