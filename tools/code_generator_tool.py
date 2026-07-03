# forge/tools/code_generator_tool.py
import re
import json

class CodeGeneratorTool:
    def __init__(self, llm):
        self.llm = llm

    def generate(self, prompt: str) -> str:
        """Generates raw text (used for writing code files)."""
        return self.llm.generate(prompt)

    def generate_json(self, prompt: str) -> dict:
        """Generates, cleans, and safely extracts JSON from LLM responses."""
        raw_response = self.llm.generate(prompt)
        
        try:
            # Matches the first outer '{' to the last outer '}'
            match = re.search(r'(\{.*\})', raw_response, re.DOTALL)
            if not match:
                raise ValueError("LLM response did not contain a valid JSON object block.")
            
            clean_json_str = match.group(1).strip()
            return json.loads(clean_json_str)
        except Exception as e:
            print("\n--- JSON Parsing Error Debug ---")
            print(f"Raw Output Received:\n{raw_response}")
            print("--------------------------------")
            raise e