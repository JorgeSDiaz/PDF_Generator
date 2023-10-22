import subprocess
import jinja2
import pdfkit

def get_wkhtmltopdf_bin():
    return subprocess.run(['which', 'wkhtmltopdf'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

def render_pdf(template: str, context: dict):
    template = jinja2.Environment(loader=jinja2.FileSystemLoader("templates")).get_template(template)
    config = pdfkit.configuration(wkhtmltopdf=get_wkhtmltopdf_bin())
    
    pdfkit.from_string(template.render(context), 'pdfs/' + context["Full_Name"].replace(" ", "_") + '.pdf', configuration=config)