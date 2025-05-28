import os
from jinja2 import Template

def mit(name: str, year: str):
    os.makedirs("output", exist_ok=True)
    
    if not name or not name.strip():
        name = "Anonymous"
    
    with open("templates/mit.txt", "r") as f:
        mit_templ = f.read()
        template = Template(mit_templ)
        license_text = template.render(author=name, year=year)
    
    with open("output/output.txt", "w") as q:
        q.write(license_text)
    print(license_text)
    
#def apache():

def bsd(name:str, year:str, ):
    os.makedirs("output", exist_ok=True)
    
    if not name or not name.strip():
        name = "Anonymous"
    
    with open("templates/bsd.txt", "r") as f:
        mit_templ = f.read()
        template = Template(mit_templ)
        license_text = template.render(author=name, year=year)
    
    with open("output/output.txt", "w") as q:
        q.write(license_text)
    print(license_text)