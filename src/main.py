# main logic

from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import asyncio

app = FastAPI(
    title="GenAI Studio API",
    version="1.0.0",
    description="API for simplifying technical concepts"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic Models
class ExplanationRequest(BaseModel):
    concept: str = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Quantum Computing",
        description="Technical concept to explain"
    )
    audience: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="High School Student",
        description="Target audience for explanation"
    )

    @validator('*', pre=True)
    def check_empty_strings(cls, value):
        if isinstance(value, str) and not value.strip():
            raise ValueError("Field cannot be empty or contain only whitespace")
        return value


class ExplanationResponse(BaseModel):
    concept: str
    audience: str
    explanation: str


# Endpoints
@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "system": "macOS"
    }


@app.post("/explain",
          response_model=ExplanationResponse,
          status_code=status.HTTP_200_OK,
          tags=["Explanation"],
          responses={
              422: {"description": "Validation error"},
              500: {"description": "Internal server error"},
              504: {"description": "Service timeout"}
          })
async def explain_concept(request: ExplanationRequest):
    try:
        explanation = await get_mock_explanation(request.concept, request.audience)
        return {
            "concept": request.concept,
            "audience": request.audience,
            "explanation": explanation
        }
    except asyncio.TimeoutError:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Explanation service timed out"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate explanation"
        ) from e


# Helper Functions
async def get_mock_explanation(concept: str, audience: str) -> str:
    """Simulates LLM API call with configurable delay"""
    try:
        await asyncio.sleep(1)  # Simulated network delay

        if "fail" in concept.lower():
            raise RuntimeError("Simulated LLM failure")

        return (
            f"Okay, imagine explaining '{concept}' to a '{audience}'. "
            f"It's basically a simulated explanation showing how the system works!"
        )
    except asyncio.CancelledError:
        raise TimeoutError("Request cancelled due to timeout")