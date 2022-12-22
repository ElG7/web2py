# -*- coding: utf-8 -*-
# intente algo como
def view_posts():
    
                grid_post = SQLFORM.grid(db.post,paginate=2)
                return dict(grid=grid_post)
