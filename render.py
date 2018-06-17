from mako.template import Template
from mako.lookup import TemplateLookup
import json
import os

TEMPLATE_DIR = 'article/template/'

"""
  load json data from info.json
"""
def load_json(path):
  data_io = open(path + "/info.json", 'rb')
  data_content = data_io.read().decode('utf-8')
  data = json.loads(data_content)

  data["content_ref"] = "../../" + path + '/' + data["content_ref"]
  data["dir_path"] = path

  return data


"""
  render article by article folder path
"""
def render_article(data):
  path = data["dir_path"]
  # load template
  mylook = TemplateLookup(['.', path], input_encoding='utf-8', output_encoding='utf-8');

  mytemp = Template(filename=TEMPLATE_DIR + "article.mako", lookup=mylook)

  # render
  with open("%s/article.html" % path, 'wb') as wh:
    wh.write(mytemp.render_unicode(data=data).encode('utf-8'))

def render_card(data):
  path = data["dir_path"]

  # load template
  mylook = TemplateLookup(['.', path], input_encoding='utf-8', output_encoding='utf-8');

  mytemp = Template(filename=TEMPLATE_DIR + "card.mako", lookup=mylook)

  # render
  with open("%s/card.html" % path, 'wb') as wh:
    wh.write(mytemp.render_unicode(data=data).encode('utf-8'))

"""
  final render
"""
def render(path):
  print("generating %s ... " % path)

  data = load_json(path)
  
  render_article(data)

  render_card(data)


if __name__=="__main__":
  #render("article/template")
  #render("article/2017-12-16-linear-lib_test")
  #from IPython import embed; embed()

  BLOG_DIR = "article"
  for dirname in os.listdir(BLOG_DIR):
    filename = os.path.join(BLOG_DIR, dirname, "info.json")
    if (os.path.isfile(filename)):
      render(os.path.join(BLOG_DIR, dirname))
