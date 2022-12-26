# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

### http://server/pymesiqq/default/index
### http://server/pymesiqq/default/new_post
### http://server/pymesiqq/default/edit_post/<id>
### http://server/pymesiqq/default/list_posts_by_author/<user_id>/<page>
### http://server/pymesiqq/default/view_post/<id>

posts_on_screen = 5

def get_category():
    category_name = request.args(0)
    category = db.category(name=category_name)
    if not category:
        session.flash = 'La pagina que buscas no existe.' 
        redirect(URL('index'))
    return category

def index():
    rows = db(db.category).select()
    return locals()


def new_post():
    category = get_category()
    db.post.category.default = category.id
    form= SQLFORM(db.post).process(next='view_post/[id]')
    return locals()

def edit_post():
    id= request.args(0,cast=int)
    form= SQLFORM(db.post, id).process(next='view_post/[id]')
    return locals()

def list_posts_by_datetime():
    category = get_category()
    page = request.args(1,cast=int,default=0)
    start = page*posts_on_screen
    stop = start+posts_on_screen
    rows = db(db.post.category==category.id).select(orderby=~db.post.posted_on,limitby=(start,stop))
    return locals()


def list_posts_by_author():
    user_id = request.args(0,cast=int)
    page = request.args(1,cast=int,default=0)
    start = page*posts_on_screen
    stop = start+posts_on_screen
    rows = db(db.post.posted_by==user_id).select(orderby=~db.post.posted_on,limitby=(start,stop))
    return locals()

def view_post():
    id= request.args(0,cast=int)
    post = db.post(id) or redirect(URL('index'))
    comments = db(db.comm.post==post.id).select(orderby=~db.comm.posted_on)
    return locals()



def error():
    return dict()

@auth.requires_login()
def post_manage():
    form = SQLFORM.smartgrid(db.t_post,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def comm_manage():
    form = SQLFORM.smartgrid(db.t_comm,onupdate=auth.archive)
    return locals()

