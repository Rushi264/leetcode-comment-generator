"""
AI-powered code comment generator using Google Gemini API.
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class CommentGenerator:
    """Generates educational comments for code using Google Gemini AI."""
    
    def __init__(self, api_key: str = None):
        """
        Initialize the comment generator.
        
        Args:
            api_key: Google API key. If None, reads from GOOGLE_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key not found. Set GOOGLE_API_KEY in .env file or pass it directly."
            )
        self.client = genai.Client(api_key=self.api_key)
    
    def generate_comments(self, code: str, style: str = "beginner") -> str:
        """
        Generate educational comments for the provided code.
        
        Args:
            code: The Python code to comment
            style: Comment style - 'beginner', 'technical', or 'interview'
        
        Returns:
            The code with generated comments added
        """
        # Create the appropriate prompt based on style
        style_instructions = {
            "beginner": """You are an expert programming tutor. Generate clear, educational comments 
            for LeetCode solutions that help beginners understand the code. Include:
            1. A header comment with approach overview and complexity analysis
            2. Inline comments explaining key logic and algorithm steps
            3. Simple language that's easy to understand""",
            
            "technical": """You are a senior software engineer. Generate precise technical comments 
            for LeetCode solutions. Include:
            1. A header with algorithm name, time/space complexity with explanation
            2. Inline comments for complex operations
            3. Technical terminology and best practices""",
            
            "interview": """You are an interview coach. Generate comments that demonstrate 
            clear thinking for LeetCode solutions. Include:
            1. A header explaining the approach and why it's optimal
            2. Comments highlighting key insights and trade-offs
            3. Complexity analysis with reasoning"""
        }
        
        style_instruction = style_instructions.get(style, style_instructions["beginner"])
        
        # Create the full prompt
        prompt = f"""{style_instruction}

Add educational comments to this Python code. 

IMPORTANT: Return ONLY the commented code with NO explanation before or after. Do NOT wrap the code in markdown code blocks or backticks.

Code to comment:
{code}

Generate comments following these guidelines:
- Add a header comment block at the top
- Include time and space complexity analysis
- Add inline comments for key logic
- Keep the original code structure intact
- Make comments clear and educational

Return ONLY the Python code with comments added, nothing else."""

        try:
            # Call Gemini API using the new client
            response = self.client.models.generate_content(
                model='gemini-2.0-flash-exp',
                contents=prompt
            )
            
            # Extract the commented code from response
            response_text = response.text.strip()
            
            # Remove markdown code blocks if present
            if "```python" in response_text:
                # Extract code between ```python and ```
                start = response_text.find("```python") + len("```python")
                end = response_text.find("```", start)
                commented_code = response_text[start:end].strip()
            elif "```" in response_text:
                # Extract code between ``` and ```
                start = response_text.find("```") + len("```")
                end = response_text.find("```", start)
                commented_code = response_text[start:end].strip()
            else:
                commented_code = response_text
            
            return commented_code
            
        except Exception as e:
            raise Exception(f"Error generating comments: {str(e)}")
    
    def process_file(self, input_path: str, output_path: str = None, style: str = "beginner") -> str:
        """
        Process a Python file and add comments.
        
        Args:
            input_path: Path to input Python file
            output_path: Path to save commented code. If None, returns the code
            style: Comment style to use
        
        Returns:
            The commented code as a string
        """
        # Read the input file
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                original_code = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file not found: {input_path}")
        except Exception as e:
            raise Exception(f"Error reading file: {str(e)}")
        
        # Generate comments
        print(f"Generating comments for {input_path}...")
        commented_code = self.generate_comments(original_code, style)
        
        # Save to output file if path provided
        if output_path:
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(commented_code)
                print(f"Commented code saved to: {output_path}")
            except Exception as e:
                raise Exception(f"Error writing file: {str(e)}")
        
        return commented_code