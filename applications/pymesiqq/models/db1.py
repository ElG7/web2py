# -*- coding: utf-8 -*-


db.define_table('category',
                Field('name'))

db.define_table('post',
            Field('posted_by','reference auth_user',readable=True,writable=False),
            Field('category','reference category',readable=False,writable=False),
            Field('title','string', label="Título",
            requires=IS_NOT_EMPTY(error_message="Ingrese un título.")),
            Field('body','text', label="Cuerpo",
            requires=IS_NOT_EMPTY(error_message="Escriba el contenido.")),
            Field('image', 'upload' , label="Imagen"),
            Field('posted_on','datetime',readable=False,writable=False),
            auth.signature)

db.define_table('comm',
                Field('post','reference post',readable=False,writable=False),
                Field('body','text',label="Cuerpo",
                requires=IS_NOT_EMPTY(error_message="Escriba el comentario.")),
                Field('posted_on','datetime',readable=False,writable=False),
                Field('posted_by','reference auth_user',readable=False,writable=False))

"""from gluon.contrib.populate import populate
if db(db.auth_user).count()<2:
    populate(db.auth_user,100)
    db.commit()
if db(db.post).count()<2:
    populate(db.post,500)
    db.commit()
if db(db.comm).count()<2:
    populate(db.comm,1000)
    db.commit()"""