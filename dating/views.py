from slugify import slugify
from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from dating.models import *

dating = Blueprint('dating', __name__, template_folder='templates')

class Search(MethodView):

  def get(self):
    name = request.args.get('name', '')
    pet_type = request.args.get('pet_type', '')
    count = int(request.args.get('n', 0))

    try:
      pets = Pets.objects.filter(name__contains=name, pet_type__contains=pet_type)
    except Pets.DoesNotExist:
      pets = []

    if count > 0:
      return render_template('dating/pets.html', pets=pets[:count])
    else:
      return render_template('dating/pets.html', pets=pets)
      

class Home(MethodView):  

  def get(self):
    return render_template('dating/home.html')

class Users(MethodView):  

  def get(self):
    users = User.objects.all()
    return render_template('dating/users.html',users=users)

# class CreateArticle(MethodView):

#   def get(self):
#     return render_template('articles/create.html')

#   def post(self):

#     if request.method == 'POST':
#       body = request.form['body']
#       author = request.form['body']
#       title = request.form['body']
#       slug = slugify(title)
#       article = Article(body=body, author=author, title=title, slug=slug)
#       article.save()

#       return render_template('articles/show.html', article=article)
#     return render_template('articles/create.html')

# class ShowArticle(MethodView):

#   def get(self, slug):
#     article = Article.objects.get_or_404(slug=slug)
#     return render_template('articles/show.html', article=article)



dating.add_url_rule('/', view_func=Home.as_view('home'))
dating.add_url_rule('/users', view_func=Users.as_view('users'))
dating.add_url_rule('/search', view_func=Search.as_view('search'))
# articles.add_url_rule('/create', view_func=CreateArticle.as_view('create'))
# articles.add_url_rule('/view/<slug>/', view_func=ShowArticle.as_view('show'))


