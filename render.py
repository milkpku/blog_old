from mako.template import Template
from mako.lookup import TemplateLookup
import json
import os
import csv

TEMPLATE_DIR = 'article/'

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
  dict to json
"""
def load_csv(path):
  with open(path) as fh:
    reader = csv.DictReader(fh)
    data = []
    for row in reader:
      row["article_path"] = "article/%s/article.html" % row["dir_name"]
      row["card_path"] = "article/%s/card.html" % row["dir_name"]

      json_str = json.dumps(row)
      json_data = json.loads(json_str)
      data.append(json_data)

  return data

"""
  render article by article folder path
"""
def render_article(data):
  # load template
  mylook = TemplateLookup(['.', 'article'], input_encoding='utf-8', output_encoding='utf-8')

  mytemp = Template(filename=TEMPLATE_DIR + "article.mako", lookup=mylook)

  # render
  filename = data["article_path"]
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, 'wb') as wh:
    wh.write(mytemp.render_unicode(data=data).encode('utf-8'))

"""
  render card by article folder path
"""
def render_card(data):
  # load template
  mylook = TemplateLookup(['.', "article"], input_encoding='utf-8', output_encoding='utf-8')

  mytemp = Template(filename=TEMPLATE_DIR + "card.mako", lookup=mylook)

  # render
  filename = data["card_path"]
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  with open(filename, 'wb') as wh:
    wh.write(mytemp.render_unicode(data=data).encode('utf-8'))


"""
  render index page
"""
def render_index():
  print("generating index page ... ")
  data_io = open("index.json", 'rb')
  data_content = data_io.read().decode('utf-8')
  data = json.loads(data_content)

  mylook = TemplateLookup(['.'], input_encoding='utf-8', output_encoding='utf-8')
  mytemp = Template(filename="./index.mako", lookup=mylook)

  # render
  with open("index.html", 'wb') as wh:
    wh.write(mytemp.render_unicode(data=data).encode('utf-8'))

"""
  final render
"""
def render(data):
  print("generating %s ... " % data["dir_name"])
  
  render_article(data)

  render_card(data)


if __name__=="__main__":
  #render("article/template")
  #render("article/2017-12-16-linear-lib_test")
  #from IPython import embed; embed()

  # BLOG_DIR = "article"
  # for dirname in os.listdir(BLOG_DIR):
  #   filename = os.path.join(BLOG_DIR, dirname, "info.json")
  #   if (os.path.isfile(filename)):
  #     render(os.path.join(BLOG_DIR, dirname))

  # #from IPython import embed; embed()
  # render_index()

  data = load_csv("article/article_list.csv")
  for item in data:
    render(item);

  render_index()