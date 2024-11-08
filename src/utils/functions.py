from pathlib import Path
from string import Template

def list_pdf_files(folder_path):
    base_path = Path(__file__).resolve().parents[2]
    pdf_folder = base_path / folder_path

    if pdf_folder.exists():
        pdf_files = [str(pdf) for pdf in pdf_folder.glob("*.pdf")]
        return pdf_files
    else:
        print("La carpeta db/files no se encontró.")
        return []

def leer_txt(nombre_archivo : str) -> str:
    with open(nombre_archivo, 'r', encoding='UTF-8') as archivo:
        contenido = archivo.read()
    return contenido

def generate_prompt(importants_chunks,user_question: str) -> str:
    chunks = [doc.page_content for doc in importants_chunks]
    context_string = '\n*******************************\n'.join(chunks)
    prompt_template = leer_txt('prompt.txt')
    template = Template(prompt_template)
    prompt = template.substitute(
        context_string=context_string,
        user_question=user_question,
    )

    return prompt
