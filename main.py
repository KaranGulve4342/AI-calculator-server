# # from contextlib import asynccontextmanager
# # from fastapi import FastAPI
# # from fastapi.middleware.cors import CORSMiddleware
# # import uvicorn
# # from apps.calculator.route import router as calculator_router
# # from constants import SERVER_URL, PORT, ENV

# # @asynccontextmanager
# # async def lifespan(app: FastAPI):
# #     yield

# # app = FastAPI(lifespan=lifespan)


# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=['*'],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )


# # @app.get('/')
# # async def root():
# #     return {"message": "server is running"}

# # app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])


# # if __name__ == "__main__":
# #     uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))


# from contextlib import asynccontextmanager
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# from apps.calculator.route import router as calculator_router
# from constants import SERVER_URL, PORT, ENV

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

# app = FastAPI(lifespan=lifespan)

# # Update the CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "https://ai-calculator-client.vercel.app",
#         "http://localhost:5173"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get('/')
# async def root():
#     return {"message": "server is running"}

# app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=PORT)


# from contextlib import asynccontextmanager
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# from apps.calculator.route import router as calculator_router
# from constants import SERVER_URL, PORT, ENV

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

# app = FastAPI(lifespan=lifespan)

# # Update the CORS middleware configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get('/')
# async def root():
#     return {"message": "server is running"}

# app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=PORT)



from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "https://ai-calculator-client.vercel.app",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    "https://ai-calculator-server-taupe.vercel.app"
]

# Update the CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Access-Control-Allow-Origin: https://ai-calculator-client.vercel.app

@app.get('/')
async def root():
    return {"message": "server is running"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=PORT)