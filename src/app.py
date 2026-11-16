from controller.task_controller import router as task_exorcise
from fastapi import FastAPI
from uvicorn import run
from middleware.error_middleware import register_exception_handler

server = FastAPI()

register_exception_handler(server)

server.include_router(task_exorcise)

if __name__ == "__main__":
    run ("app:server", port=4000, reload=True)