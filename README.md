# CV Builder with Live Preview and Template Selection

A simple and powerful **CV Builder** app built using **Flask**, **HTML**, **CSS**, and **JavaScript**. This web application allows users to:

- Build and customize their CV with a **live preview**.
- Choose from multiple **templates** for the CV layout.
- **Download the final CV** as a PDF to their local system.

## Features

- **Live Preview**: As users fill out their CV details, the preview is updated in real time.
- **Template Selection**: Users can choose from various templates with a simple click on image previews.
- **Download as PDF**: Once the user is satisfied with their CV, they can download it as a PDF, keeping the selected template and styling intact.
- **Responsive Design**: The app is built to be responsive and works seamlessly on both desktop and mobile.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**: 
    - **weasyPrint**: For generating PDF downloads
    - **Jinja**: Flask's templating engine for dynamic content rendering
- **Storage**: LocalStorage (for persisting form data across page refreshes)

## Installation

To get started with this CV Builder project, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/kalminx/cv-builder.git
cd cv-builder
````

### 2. Install Dependencies

Make sure you have **Python** installed (version 3.6+). Then, create a virtual environment and install the required packages.

```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

### 3. Running the Application

Once the dependencies are installed, you can start the Flask server:

```bash
flask run
```

This will start the application locally at `http://127.0.0.1:5000`.

### 4. Open the Application

Visit `http://127.0.0.1:5000` in your browser, and you're ready to start building your CV!

## How It Works

1. **Choosing a Template**:
   On the first page, users are presented with a choice of templates represented by images. When they click on any template image, they are directed to the main CV building page, where the selected template’s CSS is applied.

2. **Filling in the Form**:
   Users can fill out their personal information such as name, email, phone, experience, skills, and education. The form data is saved even after page refreshes using the browser’s LocalStorage.

3. **Live Preview**:
   As the user types in the form, a live preview of the CV is displayed in real-time, allowing them to see how the changes look immediately.

4. **Download as PDF**:
   Once the user is satisfied with their CV, they can click the "Download as PDF" button. The app uses **jsPDF** to generate a PDF of the CV with the selected template and form data, which can be downloaded to the user's device.

## Folder Structure

```bash
cv-builder/
│
├── app.py                 # Main Flask application file
├── templates/             # HTML templates (Jinja2)
│   ├── index.html         # Home page for template selection
│   ├── builder.html       # CV Builder form page
│
├── static/                # Static files (CSS, JavaScript, Images)
│   ├── css/               # CSS templates for each layout
│   ├── images/            # Template preview images
│   ├── js/                # JavaScript files (jsPDF, form handling)
│
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, feel free to fork the repository and create a pull request.

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test your changes
5. Submit a pull request

---

## License

This project is open-source and available under the MIT License.

```

---

### Key Sections Breakdown:

- **Features**: Describes the core functionalities of your app (CV creation, live preview, download).
- **Technologies Used**: Lists the tools and libraries you’ve used (Flask, JavaScript, etc.).
- **Installation**: Provides easy-to-follow setup instructions.
- **How It Works**: Gives an overview of how the user interacts with the app.
- **Folder Structure**: Helps anyone who wants to dive into your project understand the directory setup.
- **Contributing**: Encourages others to contribute.
- **License**: Sets a clear licensing expectation for the project.

