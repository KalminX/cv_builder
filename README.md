# CV Builder

![CV Builder Banner](static/images/cv-builder-banner.png)  
*Create professional CVs with ease using live previews and customizable templates.*

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-3.0.0-brightgreen)](https://flask.palletsprojects.com/)  
[![WeasyPrint](https://img.shields.io/badge/WeasyPrint-62.3-orange)](https://weasyprint.org/)  
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)

**CV Builder** is a powerful and user-friendly web application built with **Flask** that allows users to create professional CVs with real-time previews, choose from multiple templates, and download their CVs as PDFs. Designed for simplicity and responsiveness, it works seamlessly on both desktop and mobile devices.

## ✨ Features

- **Template Selection**: Choose from a variety of professionally designed CV templates with a single click on image previews.
- **Live Preview**: See your CV update in real-time as you enter your personal details, experience, skills, and education.
- **PDF Download**: Export your CV as a high-quality PDF, preserving the selected template's styling, using **WeasyPrint**.
- **Persistent Data**: Form data is saved in the browser's **LocalStorage**, ensuring your progress persists across page refreshes.
- **Responsive Design**: Optimized for a smooth experience on desktops, tablets, and smartphones.

## 🚀 Live Demo

Try the CV Builder live at: **[https://cv-builder.up.railway.app/](https://cv-builder.up.railway.app/)**  
*Note: Replace the above link with your actual deployed app URL after deployment.*

## 📸 Screenshots

### Template Selection
![Template Selection](static/images/screenshot-template-selection.png)  
*Choose from a variety of CV templates with image previews.*

### CV Builder with Live Preview
![CV Builder](static/images/screenshot-cv-builder.png)  
*Enter your details and see the CV update in real-time.*

### Downloaded PDF
![Downloaded PDF](static/images/screenshot-pdf-output.png)  
*Download your CV as a styled PDF.*

## 🛠️ Technologies Used

- **Backend**: Flask (Python) for handling routes and rendering templates.
- **Frontend**: HTML, CSS, JavaScript for dynamic and responsive interfaces.
- **PDF Generation**: WeasyPrint for converting HTML to high-quality PDFs.
- **Templating**: Jinja2 for dynamic content rendering.
- **Storage**: Browser LocalStorage for persisting form data.
- **Deployment**: Docker with Gunicorn for scalable production deployment.

## 📦 Installation

Follow these steps to set up and run the CV Builder locally using Docker, ensuring consistency with the production environment.

### Prerequisites
- **Docker**: Install [Docker Desktop](https://www.docker.com/products/docker-desktop) or Docker CLI.
- **Git**: Install [Git](https://git-scm.com/) to clone the repository.

### 1. Clone the Repository
```bash
git clone https://github.com/kalminx/cv-builder.git
cd cv-builder
```

### 2. Prepare Files
Ensure the following files are in your project directory:
- `Dockerfile`: Configures the Docker environment.
- `requirements.txt`: Lists Python dependencies.
- `app.py`: Main Flask application.
- `templates/`: HTML templates (e.g., `index.html`, `builder.html`).
- `static/`: CSS, JavaScript, and images.

### 3. Build the Docker Image
```bash
docker build -t cv-builder .
```

### 4. Run the Container
Run the app, mapping port 8000 and mounting an output directory for PDFs:
```bash
mkdir -p output
docker run --rm -p 8000:8000 -v $(pwd)/output:/app/output cv-builder
```

### 5. Access the App
Open your browser and navigate to:
```
http://localhost:8000
```
- Choose a template, build your CV, and download it as a PDF.
- PDFs will be saved in the `the users device` directory.

## 🏗️ How It Works

1. **Template Selection**:
   - The home page (`index.html`) displays image previews of available CV templates.
   - Clicking a template redirects to the CV builder page (`builder.html`) with the selected template's CSS applied.

2. **CV Building**:
   - Users enter details (name, email, experience, etc.) in a form.
   - JavaScript updates the live preview in real-time and saves data to LocalStorage.

3. **PDF Download**:
   - Clicking "Download as PDF" triggers a request to the server.
   - Flask renders the CV with the selected template and uses WeasyPrint to generate a PDF, which is downloaded to the user's device.

## 📂 Folder Structure
```
cv-builder/
├── app.py                 # Flask application
├── templates/             # Jinja2 HTML templates
│   ├── index.html         # Template selection page
│   ├── builder.html       # CV builder with live preview
├── static/                # Static assets
│   ├── css/               # Template-specific CSS files
│   ├── images/            # Template preview images
│   ├── js/                # JavaScript for live preview and LocalStorage
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── output/                # Directory for PDF outputs
└── README.md              # Project documentation
```

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

Please include tests and update documentation as needed.

## 📜 License
This project is licensed under the [MIT License](LICENSE).

## 📬 Contact
For questions or feedback, reach out to [kalminx](https://github.com/kalminx) or open an issue on the [GitHub repository](https://github.com/kalminx/cv-builder).

---

*Built with ❤️ by [kalminx](https://github.com/kalminx)*