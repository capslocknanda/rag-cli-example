# llm_provider.py
from __future__ import annotations
from abc import ABC
from typing import Optional, Union, Type, TypeVar
import os
from typing import AsyncIterator
from langchain_core.language_models.chat_models import BaseChatModel
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from loguru import logger


_BM = TypeVar("_BM", bound=BaseModel)
DictOrPydantic = Union[dict, _BM]


class BaseLLMProvider(ABC):
    """
    Common logic for all LLM providers. 
    Child classes must set self.llm in their __init__.
    """
    llm: BaseChatModel 

    async def structured(
        self,
        prompt: str,
        extract_schema: Union[Type[BaseModel], BaseModel],
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> DictOrPydantic:
        messages = []
        if system_prompt:
            messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=prompt))

        active_llm = self.llm.bind(temperature=temperature) if temperature is not None else self.llm

        schema_class = extract_schema if isinstance(extract_schema, type) else extract_schema.__class__
        structured_llm = active_llm.with_structured_output(schema_class)

        return await structured_llm.ainvoke(messages)

    async def stream_generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> AsyncIterator[str]:
        messages = []
        if system_prompt:
            messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=prompt))

        active_llm = self.llm.bind(temperature=temperature) if temperature is not None else self.llm

        async for chunk in active_llm.astream(messages):
            if chunk.content:
                yield str(chunk.content)


# -------- Ollama (OpenAI-compatible) --------
class OllamaProvider(BaseLLMProvider):
    def __init__(self, host: str, model: str, timeout: float = 60.0):
        self.llm = ChatOpenAI(
            base_url=f"{host}/v1",
            api_key="ollama",
            model=model,
            timeout=timeout,
        )

# -------- Google Gemini --------
class GoogleAIProvider(BaseLLMProvider):
    def __init__(self, api_key: str, model: str, timeout: float = 60.0):
        self.llm = ChatGoogleGenerativeAI(
            api_key=api_key,
            model=model,
            timeout=timeout,
        )



def build_llm_provider(
    model_provider: Optional[str] = os.environ.get("LLM_PROVIDER"),
) -> BaseLLMProvider:
    """
    Factory method for BaseLLMProvider-derived subclasses
    """

    try:
        if model_provider == "ollama":
            llm_provider = OllamaProvider(
                host=os.environ["OLLAMA_HOST"],
                model=os.environ.get("OLLAMA_GENERATE_MODEL"),
                timeout=float(os.environ.get("OLLAMA_TIMEOUT", "60.0")),
            )
            logger.info("Initialized Ollama provider")
            return llm_provider
        elif model_provider == "gemini":
            llm_provider = GoogleAIProvider(
                api_key=os.environ["GEMINI_API_KEY"],
                model=os.environ.get("GEMINI_GENERATE_MODEL"),
                timeout=float(os.environ.get("GEMINI_TIMEOUT", "60.0")),
            )
            logger.info("Initialized Gemini provider")
            return llm_provider
        else:
            raise ValueError(f"Unsupported LLM provider: {model_provider}")
    except Exception as e:
        logger.error(f"Failed to initialize LLM provider: {str(e)}")
        raise
