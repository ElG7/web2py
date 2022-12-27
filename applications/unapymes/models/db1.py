# -*- coding: utf-8 -*-


db.define_table('category',
                Field('name'))

db.define_table('post',
            Field('category','reference category',readable=False,writable=False),
            Field('title','string', label="Título",
            requires=IS_NOT_EMPTY(error_message="Ingrese un título.")),
            Field('body','text', label="Cuerpo",
            requires=IS_NOT_EMPTY(error_message="Escriba el contenido.")),
            Field('image', 'upload' , label="Imagen"),
            auth.signature)

db.define_table('comm',
                Field('post','reference post',readable=False,writable=False),
                Field('body','text',label="¡Comentanos sobre esta publicación!",
                requires=IS_NOT_EMPTY(error_message="Escriba el comentario.")),
                auth.signature)


def author(id):
    if id is None:
     return "Unknown"
    else:
     user= db.auth_user(id)
    return '%(first_name)s %(last_name)s' % user

from gluon.contrib.populate import populate
if db(db.comm).count()<2:
    populate(db.comm,10)
    db.commit()