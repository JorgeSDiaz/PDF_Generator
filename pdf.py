import subprocess
import jinja2
import pdfkit

def get_wkhtmltopdf_bin():
    return subprocess.run(['which', 'wkhtmltopdf'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

def render_pdf(template: str, context: dict):
    rendered_html = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath='templates')
    ).get_template(template).render(context)
    config = pdfkit.configuration(wkhtmltopdf=get_wkhtmltopdf_bin())
    pdfkit.from_string(rendered_html, 'pdfs/' + context["Full_Name"] + '.pdf', configuration=config)