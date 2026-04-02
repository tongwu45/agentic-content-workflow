from pydantic import BaseModel, Field
from typing import List, Dict

class ProductInput(BaseModel):
    product_name: str
    category: str
    audience: str
    features: List[str]
    tone: str
    constraints: List[str]

class StrategyOutput(BaseModel):
    target_audience: str
    pain_points: List[str]
    key_message: str
    trust_angles: List[str]

class GeneratedContent(BaseModel):
    landing_page_copy: str
    linkedin_post: str
    x_post: str
    faq_snippet: str

class CritiqueOutput(BaseModel):
    clarity_score: int = Field(ge=1, le=5)
    trustworthiness_score: int = Field(ge=1, le=5)
    specificity_score: int = Field(ge=1, le=5)
    empathy_score: int = Field(ge=1, le=5)
    platform_fit_score: int = Field(ge=1, le=5)
    spamminess_score: int = Field(ge=1, le=5)
    strengths: List[str]
    weaknesses: List[str]
    revision_instructions: List[str]

class WorkflowResult(BaseModel):
    strategy: Dict
    draft: Dict
    critique: Dict
    refined: Dict
    adapted: Dict
