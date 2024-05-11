from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read

def execute_notebook(notebook_path, kernel_name):
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = read(f, as_version=4)
    
    # Execute the notebook with the specified kernel
    executor = ExecutePreprocessor(timeout=-1, kernel_name=kernel_name)
    executor.preprocess(notebook, {'metadata': {'path': ''}})

if __name__ == "__main__":
    notebook_path = 'demo_part1.ipynb'
    kernel_name = 'python3'  
    execute_notebook(notebook_path, kernel_name)
