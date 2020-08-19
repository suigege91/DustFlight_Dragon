from . import blog
from flask import render_template


@blog.route('/')
@blog.route('/index')
def index():
    tempalte_html = "index.html"
    template_title = "DustFlight VNS Dragon - Blog _ Index"
    template_content = "Welcome to DustFlight Dragon - Blog System"
    # return render_template(tempalte_html, title=template_title, content=template_content)
    return template_content
