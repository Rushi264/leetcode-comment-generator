# LeetCode Comment Generator 🤖💬

An AI-powered Python tool that automatically generates educational comments for your LeetCode solutions using Google Gemini AI. Perfect for learning, interview prep, and building a well-documented code portfolio!

## 🌟 Features

- **Web Interface**: Beautiful Streamlit UI with file upload and code paste options
- **AI-Powered Comments**: Uses Google Gemini to generate intelligent, context-aware comments
- **Multiple Comment Styles**: Choose between beginner-friendly, technical, or interview-focused comments
- **Complexity Analysis**: Automatically includes time and space complexity explanations
- **Easy to Use**: Both web interface and command-line options
- **Preserves Code Structure**: Keeps your original code intact while adding helpful documentation

## 📸 Demo

![LeetCode Comment Generator Demo](images/demo.png)

*Web interface showing file upload, comment style selection, and instant preview*

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free tier available)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rushi264/leetcode-comment-generator.git
   cd leetcode-comment-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a `.env` file in the project root:
     ```
     GOOGLE_API_KEY=your-api-key-here
     ```

## 💻 Usage

### Web Interface (Recommended)

Launch the interactive web app:

```bash
streamlit run app.py
```

Features:
- 📁 Upload Python files or ✍️ paste code directly
- 🎨 Choose from 3 comment styles
- 💬 View generated comments instantly
- ⬇️ Download commented code

### Command Line Interface

Generate comments for a Python file:

```bash
cd src
python main.py --file path/to/your/solution.py
```

Save to a new file:

```bash
python main.py --file solution.py --output commented_solution.py
```

Choose comment style:

```bash
# Beginner-friendly (default)
python main.py --file solution.py --style beginner

# Technical/Professional
python main.py --file solution.py --style technical

# Interview-focused
python main.py --file solution.py --style interview
```

## 📚 Example

**Input (two_sum.py):**
```python
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i
```

**Output:**
The tool will add:
- Header comment with approach explanation
- Time and space complexity analysis
- Inline comments explaining each step
- Clear, educational descriptions

## 🎨 Comment Styles

### Beginner Style
- Simple, easy-to-understand language
- Step-by-step explanations
- Great for learning

### Technical Style
- Professional terminology
- Detailed complexity analysis
- Best practices and optimizations

### Interview Style
- Demonstrates clear thinking
- Highlights key insights and trade-offs
- Shows problem-solving approach

## 🛠️ Project Structure

```
leetcode-comment-generator/
├── src/
│   ├── main.py              # CLI entry point
│   ├── comment_generator.py # Core AI logic
│   └── __init__.py
├── examples/
│   ├── input/               # Sample input files
│   └── output/              # Generated output files
├── tests/
│   └── test_generator.py    # Unit tests
├── .env                     # API key (not in git)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔧 Development

### Running Tests
```bash
python -m pytest tests/
```

### Adding New Features
Contributions are welcome! Feel free to:
- Add support for more programming languages
- Implement batch processing
- Create a web interface
- Add more comment style options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Powered by [Google Gemini AI](https://ai.google.dev/)
- Inspired by the need for better code documentation in competitive programming
- Built as a learning project to explore GenAI applications

## 📧 Contact

Rushi264 - [@Rushi264](https://github.com/Rushi264)

Project Link: [https://github.com/Rushi264/leetcode-comment-generator](https://github.com/Rushi264/leetcode-comment-generator)

## 🚀 Future Enhancements

- [x] Web interface using Streamlit ✅
- [ ] Support for Java, C++, JavaScript
- [ ] Batch processing for multiple files
- [ ] Integration with LeetCode API
- [ ] VS Code extension
- [ ] Customizable comment templates
- [ ] User authentication and history tracking
- [ ] API rate limiting and caching

---

Made with ❤️ by Rushi264