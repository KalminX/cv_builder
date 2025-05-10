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



# cv_data = [
#     {
#         "header": {
#             "fullName": "Alice Johnson",
#             "jobTitle": "Data Scientist",
#             "email": "alice.johnson@email.com",
#             "phone": "(555) 123-4567",
#             "location": "San Francisco, CA"
#         },
#         "summary": {
#             "professionalSummary": "Innovative Data Scientist with over 6 years of experience in machine learning and statistical analysis. Skilled in Python, R, and big data technologies, with a proven track record of delivering actionable insights."
#         },
#         "experience": [
#             {
#                 "jobTitle": "Lead Data Scientist",
#                 "companyName": "DataTech Solutions",
#                 "location": "San Francisco, CA",
#                 "timePeriod": "2021–Present",
#                 "responsibilities": [
#                     "Developed predictive models that increased customer retention by 25%.",
#                     "Led a team of 4 analysts to streamline data processing pipelines."
#                 ]
#             },
#             {
#                 "jobTitle": "Data Analyst",
#                 "companyName": "Insight Corp",
#                 "location": "San Francisco, CA",
#                 "timePeriod": "2018–2021",
#                 "responsibilities": [
#                     "Conducted A/B testing to optimize marketing campaigns.",
#                     "Built dashboards using Tableau for real-time data visualization."
#                 ]
#             }
#         ],
#         "education": [
#             {
#                 "degreeTitle": "M.S. in Data Science",
#                 "institutionName": "Stanford University",
#                 "graduationYear": "2018"
#             },
#             {
#                 "degreeTitle": "B.S. in Statistics",
#                 "institutionName": "UC Berkeley",
#                 "graduationYear": "2016"
#             }
#         ],
#         "skills": ["Python", "R", "SQL", "TensorFlow", "Tableau"],
#         "footer": {
#             "accreditation": "Template designed with Canva.com"
#         }
#     },
#     {
#         "header": {
#             "fullName": "Bob Martinez",
#             "jobTitle": "Frontend Developer",
#             "email": "bob.martinez@email.com",
#             "phone": "(555) 987-6543",
#             "location": "Austin, TX"
#         },
#         "summary": {
#             "professionalSummary": "Creative Frontend Developer with 4 years of experience building responsive and user-friendly web applications. Proficient in React, TypeScript, and modern CSS frameworks."
#         },
#         "experience": [
#             {
#                 "jobTitle": "Frontend Developer",
#                 "companyName": "WebWorks Inc.",
#                 "location": "Austin, TX",
#                 "timePeriod": "2020–Present",
#                 "responsibilities": [
#                     "Built a scalable React-based dashboard used by 10,000+ users.",
#                     "Optimized page load times by 40% through lazy loading and code splitting."
#                 ]
#             },
#             {
#                 "jobTitle": "Junior Web Developer",
#                 "companyName": "StartupX",
#                 "location": "Austin, TX",
#                 "timePeriod": "2019–2020",
#                 "responsibilities": [
#                     "Developed reusable UI components with Tailwind CSS.",
#                     "Collaborated with backend developers to integrate REST APIs."
#                 ]
#             }
#         ],
#         "education": [
#             {
#                 "degreeTitle": "B.S. in Computer Science",
#                 "institutionName": "University of Texas at Austin",
#                 "graduationYear": "2019"
#             }
#         ],
#         "skills": ["React", "TypeScript", "JavaScript", "Tailwind CSS", "Webpack"],
#         "footer": {
#             "accreditation": "Template designed with Canva.com"
#         }
#     },
#     {
#         "header": {
#             "fullName": "Clara Thompson",
#             "jobTitle": "Project Manager",
#             "email": "clara.thompson@email.com",
#             "phone": "(555) 456-7890",
#             "location": "New York, NY"
#         },
#         "summary": {
#             "professionalSummary": "Results-driven Project Manager with 8 years of experience leading cross-functional teams in delivering complex projects on time and within budget. Certified PMP with expertise in Agile and Scrum methodologies."
#         },
#         "experience": [
#             {
#                 "jobTitle": "Senior Project Manager",
#                 "companyName": "Global Enterprises",
#                 "location": "New York, NY",
#                 "timePeriod": "2019–Present",
#                 "responsibilities": [
#                     "Managed a $5M software implementation project, completed 10% under budget.",
#                     "Implemented Agile practices, reducing delivery time by 20%."
#                 ]
#             },
#             {
#                 "jobTitle": "Project Coordinator",
#                 "companyName": "TechTrend Innovations",
#                 "location": "Boston, MA",
#                 "timePeriod": "2016–2019",
#                 "responsibilities": [
#                     "Coordinated schedules and resources for teams of 10–15 members.",
#                     "Prepared detailed project reports for stakeholder reviews."
#                 ]
#             }
#         ],
#         "education": [
#             {
#                 "degreeTitle": "M.B.A.",
#                 "institutionName": "Columbia University",
#                 "graduationYear": "2016"
#             },
#             {
#                 "degreeTitle": "B.A. in Business Administration",
#                 "institutionName": "New York University",
#                 "graduationYear": "2014"
#             }
#         ],
#         "skills": ["Project Management", "Agile", "Scrum", "MS Project", "Jira"],
#         "footer": {
#             "accreditation": "Template designed with Canva.com"
#         }
#     }
# ]
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
    app.run(debug=True)
