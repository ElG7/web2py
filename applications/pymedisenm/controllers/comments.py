# -*- coding: utf-8 -*-
# intente algo como
def view_comments():
    
                grid_comments = SQLFORM.grid(db.comments,paginate=2)
                return dict(grid=grid_comments)
