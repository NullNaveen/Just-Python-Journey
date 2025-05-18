from pathlib import Path

# Define the output directory
output_dir = Path(r"C:\Users\Nike\Documents\Programming\Python\Chat GPT codes")  # Replace with your desired path
output_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

# Data Science Roadmap
xmind_structure = """
# Data Science Roadmap
## Fundamentals
### Mathematics for Data Science
#### Linear Algebra
#### Statistics
#### Calculus Basics
### Programming Foundations
#### Python Basics
#### Python Tools for Data Science
##### NumPy
##### Pandas
##### Matplotlib & Seaborn
### Introduction to Data Analysis
#### Exploratory Data Analysis
#### Practice Basic Data Projects

## Core Data Science
### Machine Learning Basics
#### ML Concepts & Algorithms
#### Scikit-Learn
### Data Visualization Techniques
#### Advanced Visualization Tools
### Advanced Python Tools
#### SQL for Data Science
#### Regular Expressions

## Specialization & Advanced Topics
### Deep Learning
#### DL Frameworks (TensorFlow, PyTorch)
#### Convolutional Neural Networks (CNN)
#### Natural Language Processing (NLP)
### Big Data Tools
#### Hadoop Ecosystem
#### Apache Spark
### Domain Knowledge
"""

# Save to a plain text file for XMind
xmind_file_path = output_dir / "Data_Science_Roadmap_XMind.txt"
with open(xmind_file_path, "w") as file:
    file.write(xmind_structure)

print(f"File saved at: {xmind_file_path}")
