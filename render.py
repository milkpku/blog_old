from mako.template import Template
from mako.lookup import TemplateLookup
import json

"""
    render article by article folder path
"""
def render_article(path):
    # load data
    data_io = open(path + "/info.json", 'rb')
    data_content = data_io.read().decode('utf-8')
    data = json.loads(data_content)

    # load template
    mylook = TemplateLookup(['.'], input_encoding='utf-8', output_encoding='utf-8');

    mytemp = Template(filename='%s/article.mako' % path, lookup=mylook)

    # render
    with open("%s/article.html" % path, 'wb') as wh:
        wh.write(mytemp.render_unicode(data=data).encode('utf-8'))

if __name__=="__main__":
    render_article("article/template")
