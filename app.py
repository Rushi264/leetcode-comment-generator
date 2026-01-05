"""
Streamlit Web Interface for LeetCode Comment Generator
"""

import streamlit as st
import sys
from pathlib import Path

# Add src to path to import our modules
sys.path.append(str(Path(__file__).parent / 'src'))
from comment_generator import CommentGenerator

# Page configuration
st.set_page_config(
    page_title="LeetCode Comment Generator",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("🤖 LeetCode Comment Generator")
st.markdown("""
Generate educational comments for your LeetCode solutions using AI!
Choose to upload a file or paste your code directly.
""")

# Sidebar for API key
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "Google API Key",
        type="password",
        help="Enter your Google Gemini API key. Get one at https://aistudio.google.com/app/apikey"
    )
    
    st.markdown("---")
    st.markdown("""
    ### 📚 Comment Styles
    
    **Beginner**: Simple, easy-to-understand explanations
    
    **Technical**: Professional documentation with detailed analysis
    
    **Interview**: Demonstrates problem-solving approach
    """)
    
    st.markdown("---")
    st.markdown("""
    ### 💡 Tips
    - Get your free API key at [Google AI Studio](https://aistudio.google.com/app/apikey)
    - Works with any Python LeetCode solution
    - Generated comments include complexity analysis
    """)

# Main content - Input method selection
st.subheader("📥 Choose Input Method")

input_method = st.radio(
    "How would you like to provide your code?",
    options=["📁 Upload File", "✍️ Paste Code"],
    horizontal=True,
    label_visibility="collapsed"
)

# Initialize code_content variable
code_content = None
filename = "solution"

# Input based on selected method
if input_method == "📁 Upload File":
    uploaded_file = st.file_uploader(
        "Upload your Python file",
        type=['py'],
        help="Upload a .py file containing your LeetCode solution"
    )
    
    if uploaded_file is not None:
        code_content = uploaded_file.read().decode('utf-8')
        filename = uploaded_file.name.rsplit('.', 1)[0]
        
else:  # Paste Code option
    code_content = st.text_area(
        "Paste your Python code here",
        height=300,
        placeholder="""def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i
    return []""",
        help="Paste your LeetCode solution code"
    )
    
    # Optional: Let user specify filename for pasted code
    if code_content:
        filename = st.text_input(
            "Filename (optional)",
            value="solution",
            help="Name for the downloaded file (without .py extension)"
        )

# Comment style selection
style = st.selectbox(
    "🎨 Comment Style",
    options=["beginner", "technical", "interview"],
    help="Choose the style of comments to generate"
)

# Display original code if provided
if code_content:
    st.subheader("📝 Your Code")
    st.code(code_content, language='python', line_numbers=True)
    
    # Generate comments button
    if st.button("✨ Generate Comments", type="primary", use_container_width=True):
        # Check if API key is provided
        if not api_key:
            st.error("⚠️ Please enter your Google API key in the sidebar!")
        else:
            try:
                with st.spinner(f"🔄 Generating {style} comments using Gemini API..."):
                    # Initialize generator
                    generator = CommentGenerator(api_key=api_key)
                    
                    # Generate comments
                    commented_code = generator.generate_comments(code_content, style)
                    
                    # Success message
                    st.success("✅ Comments generated successfully!")
                    
                    # Display commented code
                    st.subheader("💬 Commented Code")
                    st.code(commented_code, language='python', line_numbers=True)
                    
                    # Create download filename
                    download_filename = f"{filename}_commented.py"
                    
                    # Download button
                    st.download_button(
                        label="⬇️ Download Commented Code",
                        data=commented_code,
                        file_name=download_filename,
                        mime="text/plain",
                        use_container_width=True,
                        type="primary"
                    )
                    
                    # Copy to clipboard option
                    st.info("💡 Tip: You can also select and copy the code above directly!")
                    
            except ValueError as e:
                st.error(f"❌ Configuration Error: {str(e)}")
                st.info("💡 Make sure you've entered a valid Google API key in the sidebar.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("💡 Make sure your API key is valid and you have available credits.")

else:
    # Instructions when no code is provided
    st.info("👆 Choose an input method and provide your code to get started!")
    
    # Example section
    with st.expander("📖 See Example"):
        st.markdown("### Example Input")
        example_code = '''def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[nums[i]] = i'''
        st.code(example_code, language='python')
        
        st.markdown("### What You'll Get")
        st.markdown("""
        ✅ **Header comment** with problem approach and complexity  
        ✅ **Inline comments** explaining each step  
        ✅ **Clear documentation** in your chosen style  
        ✅ **Downloadable file** ready to use
        """)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style='text-align: center'>
        <p>Made with ❤️ using Google Gemini AI<br>
        <a href='https://github.com/Rushi264/leetcode-comment-generator' target='_blank'>⭐ View on GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)