from fastapi import FastAPI
from nbformat import read
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import requests
import json
import io
import sys

app = FastAPI()

def execute_notebook(notebook_content):
    # Load the notebook from content
    notebook = nbformat.reads(notebook_content, as_version=4)

    # Capture print output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(notebook)
        sys.stdout = sys.__stdout__  # Restore stdout
        return {"status": "success", "message": "Notebook executed successfully!", "output": captured_output.getvalue(), "result": json.loads(notebook_content)}
    except Exception as e:
        sys.stdout = sys.__stdout__  # Restore stdout
        return {"status": "error", "message": f"Failed to execute notebook: {str(e)}"}

@app.get("/run-notebook")
async def run_notebook():
    notebook_url = "https://raw.githubusercontent.com/nayera540/recommend_test/main/Collaborative%20Filtering%20Recommendation%20System%20Model%20-%20deploy.ipynb"
    notebook_content = requests.get(notebook_url).text
    return execute_notebook(notebook_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


