from fastapi import FastAPI, HTTPException, Request, Response
from mangum import Mangum

from .api.v1 import router as v1_router


DISPLAY_TRACEBACK_ON_500 = True

app = FastAPI()
app.include_router(v1_router, prefix="/v1")

if DISPLAY_TRACEBACK_ON_500:

    @app.exception_handler(Exception)
    async def debug_exception_handler(request: Request, exc: Exception):
        import traceback

        return Response(
            content="".join(
                traceback.format_exception(
                    etype=type(exc), value=exc, tb=exc.__traceback__
                )
            )
        )


def handler(event, context):
    event["requestContext"] = {}  # Adds a dummy field; mangum will process this fine

    asgi_handler = Mangum(app)
    response = asgi_handler(event, context)

    return response