const bindPreview = (inputId, previewId, defaultText = "") => {
  const input = document.getElementById(inputId);
  const preview = document.getElementById(previewId);

  input.addEventListener("input", () => {
    preview.textContent = input.value || defaultText;
  });
};

bindPreview("nameInput", "namePreview", "Your Name");
bindPreview("emailInput", "emailPreview");
bindPreview("phoneInput", "phonePreview");
bindPreview("summaryInput", "summaryPreview");
bindPreview("experienceInput", "experiencePreview");
bindPreview("educationInput", "educationPreview");
bindPreview("skillsInput", "skillsPreview");

let button = document.getElementById("downloadBtn");
button.addEventListener("click", async () => {
  const cvElement = document.getElementById("cvPreview");

  // Render the CV preview to canvas
  const canvas = await html2canvas(cvElement, {
    scale: 2, // higher scale = better quality
    useCORS: true, // in case of external images or fonts
  });

  const imgData = canvas.toDataURL("image/png");

  // Set PDF dimensions
  const pdf = new jspdf.jsPDF({
    orientation: "portrait",
    unit: "mm",
    format: "a4",
  });

  const pdfWidth = pdf.internal.pageSize.getWidth();
  const pdfHeight = (canvas.height * pdfWidth) / canvas.width;

  pdf.addImage(imgData, "PNG", 0, 0, pdfWidth, pdfHeight);
  pdf.save("cv_preview.pdf");
});

const fields = [
  "nameInput",
  "emailInput",
  "phoneInput",
  "summaryInput",
  "experienceInput",
  "educationInput",
  "skillsInput",
];

const previewMap = {
  nameInput: "namePreview",
  emailInput: "emailPreview",
  phoneInput: "phonePreview",
  summaryInput: "summaryPreview",
  experienceInput: "experiencePreview",
  educationInput: "educationPreview",
  skillsInput: "skillsPreview",
};

// Load data from localStorage on page load
window.addEventListener("DOMContentLoaded", () => {
  fields.forEach((id) => {
    const savedValue = localStorage.getItem(id);
    if (savedValue !== null) {
      document.getElementById(id).value = savedValue;
      document.getElementById(previewMap[id]).textContent = savedValue;
    }
  });
});

// Save data to localStorage on input
fields.forEach((id) => {
  document.getElementById(id).addEventListener("input", (e) => {
    localStorage.setItem(id, e.target.value);
  });
});

console.log("This is the button: ", button);
