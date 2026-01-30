from langchain_openai import ChatOpenAI
from pydantic import BaseModel


class ICalResponse(BaseModel):
    ical: str


class LLM:
    def __init__(self, model: str, base_url: str = None, api_key: str = None):
        self.llm = ChatOpenAI(model=model, base_url=base_url, api_key=api_key)

    def request(self, prompt: str) -> ICalResponse:
        structured_llm = self.llm.with_structured_output(ICalResponse)
        return structured_llm.invoke(prompt)
