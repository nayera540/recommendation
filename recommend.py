from fastapi import FastAPI
from nbformat import read
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import requests


app = FastAPI()

def execute_notebook(notebook_content):
    # Load the notebook from content
    notebook = nbformat.reads(notebook_content, as_version=4)


    try:
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(notebook)
        return {"status": "success", "message": "Notebook executed successfully!"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to execute notebook: {str(e)}"}

@app.get("/run-notebook")
async def run_notebook():
    notebook_url = "https://raw.githubusercontent.com/nayera540/recommendation/main/Collaborative%20Filtering%20Recommendation%20System%20Model%20-%20deploy.ipynb"
    notebook_content = requests.get(notebook_url).text
    return execute_notebook(notebook_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
