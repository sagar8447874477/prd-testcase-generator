import pdfplumber

def read_text(file):
    return file.read().decode("utf-8")


def read_pdf(file):

    text = ""

    try:
        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    except Exception as e:
        text = f"Error reading PDF: {str(e)}"

    return text