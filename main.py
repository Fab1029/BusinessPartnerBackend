import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controller.BusinessInformationController import router as business_router

app = FastAPI(
    title="Business Partner",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(business_router)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port= 5000,
        reload= True
    )
