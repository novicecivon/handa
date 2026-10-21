from fastapi import FastAPI

from handa import __version__
from handa.api.routes import health

app = FastAPI(
    title="Handa API",
    version=__version__,
    description="Flood and earthquake readiness data for Philippine communities.",
)

app.include_router(health.router)
