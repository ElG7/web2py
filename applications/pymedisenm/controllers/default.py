# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    posts = db(db.post.id > 0).select(db.post.id, db.post.title)
    return {"posts": posts}

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    if request.args(0) == "login":
        title = "Iniciar sesión"
        form = auth.login()
    elif request.args(0) == "signup":
        title = "Registrarse"
        form = auth.register()
    else:
        raise HTTP(404)
    return {"form": form, "title": title}

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/uploads/[filename]
    """
    return response.uploads(request, db)

@auth.requires_login()
def new_post():
    form = SQLFORM(db.post, fields=["title", "description", "image"])
    form.process()
    return {"form": form}


def view_post():
    post_id = request.args(0, cast=int)
    post = db(db.post.id == post_id).select().first()
    comment_form = FORM(
        "Comentario:",
        BR(),
        TEXTAREA(_name="comment", requires=IS_LENGTH(2000, minsize=1)),
        BR(),
        BUTTON("Enviar comentario", _type="submit")
    )
    if comment_form.process().accepted:
        s = db(db.post.id == post_id)
        comments = s.select().first().comments
        if comments is None:
            comments = [comment_form.vars.comment]
        else:
            comments.append(comment_form.vars.comment)
        s.update(comments=comments)
        redirect(URL(args=request.args))
    return {"post": post, "comment_form": comment_form}


