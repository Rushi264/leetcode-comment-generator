"""
LeetCode Comment Generator - Main CLI Entry Point
"""

import argparse
import sys
from pathlib import Path
from comment_generator import CommentGenerator


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Generate educational comments for LeetCode solutions using AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --file solution.py
  python main.py --file solution.py --output commented_solution.py
  python main.py --file solution.py --style technical
        """
    )
    
    parser.add_argument(
        "--file", "-f",
        type=str,
        required=True,
        help="Path to Python file containing LeetCode solution"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path (default: prints to console)"
    )
    
    parser.add_argument(
        "--style", "-s",
        type=str,
        choices=["beginner", "technical", "interview"],
        default="beginner",
        help="Comment style (default: beginner)"
    )
    
    parser.add_argument(
        "--api-key",
        type=str,
        help="Anthropic API key (overrides .env file)"
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    input_path = Path(args.file)
    if not input_path.exists():
        print(f"❌ Error: File not found: {args.file}")
        sys.exit(1)
    
    if not input_path.suffix == ".py":
        print(f"⚠️  Warning: {args.file} doesn't appear to be a Python file")
    
    try:
        # Initialize generator
        generator = CommentGenerator(api_key=args.api_key)
        
        # Process the file
        print(f"📝 Processing: {args.file}")
        print(f"🎨 Style: {args.style}")
        print(f"⏳ Calling Claude API...")
        print()
        
        commented_code = generator.process_file(
            input_path=str(input_path),
            output_path=args.output,
            style=args.style
        )
        
        # If no output file specified, print to console
        if not args.output:
            print("=" * 80)
            print("COMMENTED CODE:")
            print("=" * 80)
            print(commented_code)
            print("=" * 80)
        else:
            print(f"✅ Success! Commented code saved to: {args.output}")
        
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\n💡 Make sure your .env file contains:")
        print("   ANTHROPIC_API_KEY=your-key-here")
        sys.exit(1)
    
    except FileNotFoundError as e:
        print(f"❌ File Error: {e}")
        sys.exit(1)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 
