from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load pre-trained model
with open(r'C:\Users\hp\render\model (1).pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_files():
    # Get uploaded files
    resume_file = request.files['resume_file']
    job_file = request.files['job_file']

    # Load the files into DataFrames
    resumes = pd.read_csv(resume_file, encoding='ISO-8859-1', on_bad_lines='skip', engine='python')
    jobs = pd.read_csv(job_file, encoding='ISO-8859-1', on_bad_lines='skip', engine='python')


    # Process and compute similarities (use your existing logic)
    results = {
        "Best Matches": [{"Resume": "Resume1", "Job": "Job1", "Score": 0.85}],
        "Skill Gaps": [{"Resume": "Resume1", "Missing Skills": ["Deep Learning"]}],
        "Recommended Courses": [{"Resume": "Resume1", "Courses": ["Deep Learning Specialization"]}]
    }

    # Render results in the HTML template
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
