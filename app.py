from flask import Flask, render_template, request, send_file
from weasyprint import HTML, CSS
import io, os

app = Flask(__name__)

def transform_form_to_cv_data(data):
    # Initialize the cv_data structure
    cv_data = {
        "header": {
            "fullName": data.get("name", ""),
            "jobTitle": data.get("jobTitle", ""),
            "email": data.get("email", ""),
            "phone": data.get("phone", ""),
            "location": data.get("location", "")
        },
        "summary": {
            "professionalSummary": data.get("summary", "")
        },
        "experience": [],
        "education": [],
        "skills": [],
        "footer": {
            "accreditation": "Template designed with Canva.com"
        }
    }

    # Process experience entries
    experience_index = 0
    while f"experience[{experience_index}][jobTitle]" in data:
        responsibilities = data.get(f"experience[{experience_index}][responsibilities]", "")
        # Split responsibilities by newlines and filter out empty strings
        responsibilities_list = [r.strip() for r in responsibilities.split("\n") if r.strip()]
        
        experience_entry = {
            "jobTitle": data.get(f"experience[{experience_index}][jobTitle]", ""),
            "companyName": data.get(f"experience[{experience_index}][company]", ""),
            "location": data.get(f"experience[{experience_index}][location]", ""),
            "timePeriod": data.get(f"experience[{experience_index}][timePeriod]", ""),
            "responsibilities": responsibilities_list
        }
        cv_data["experience"].append(experience_entry)
        experience_index += 1

    # Process education entries
    education_index = 0
    while f"education[{education_index}][degree]" in data:
        education_entry = {
            "degreeTitle": data.get(f"education[{education_index}][degree]", ""),
            "institutionName": data.get(f"education[{education_index}][institution]", ""),
            "graduationYear": data.get(f"education[{education_index}][gradYear]", "")
        }
        cv_data["education"].append(education_entry)
        education_index += 1

    # Process skills
    skills_index = 0
    while f"skills[{skills_index}]" in data:
        skill = data.get(f"skills[{skills_index}]", "").strip()
        if skill:  # Only add non-empty skills
            cv_data["skills"].append(skill)
        skills_index += 1

    return cv_data


@app.route('/')
def index():
    return render_template('index.html')

from flask import send_from_directory

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.form.to_dict()
    cv_data = transform_form_to_cv_data(data)
    cv_data['template'] = data['templateKey']
    rendered = render_template('cv_template.html', cv_data=cv_data, template_style=cv_data["template"])
    pdf_io = io.BytesIO()
    css_path = os.path.join(app.root_path, 'static', 'css', f"{cv_data['template']}.css")
    HTML(string=rendered, base_url=request.base_url).write_pdf(pdf_io, stylesheets=[CSS(filename=css_path)])
    pdf_io.seek(0)
    return send_file(pdf_io, download_name=f"{cv_data['header']['fullName']}_cv.pdf", as_attachment=True)

@app.route("/builder/<template_name>")
def builder(template_name):
    css_file = f"css/{template_name}.css"
    return render_template("builder.html", template_name=template_name, css_file=css_file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
