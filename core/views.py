import fitz  
import os
from openai import OpenAI
from django.shortcuts import render
from .forms import UploadForm

# Load OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def generate_summary(text):
    try:
        prompt = f"Summarize the following document clearly:\n\n{text[:12000]}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating summary: {e}"

def upload_file(request):
    summary = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save()
            if upload.file_type == 'pdf':
                file_path = upload.file.path
                full_text = extract_text_from_pdf(file_path)
                summary = generate_summary(full_text)
    else:
        form = UploadForm()
    return render(request, 'core/upload.html', {'form': form, 'summary': summary})
