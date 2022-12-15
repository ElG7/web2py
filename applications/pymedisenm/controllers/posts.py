# -*- coding: utf-8 -*-
# intente algo como
def view_posts():
    
                grid_posts = SQLFORM.grid(db.posts,paginate=2)
                return dict(grid=grid_posts)
