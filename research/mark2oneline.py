markdown_content = """
# Sample Project

This is a simple project description.

- Feature 1
- Feature 2
- Feature 3

[Learn More](https://example.com)
"""

# print(markdown_content)
# Remove newlines
markdown_content_single_line = markdown_content.replace('\n', '\\n')

print(markdown_content_single_line)
