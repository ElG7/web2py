# -*- coding: utf-8 -*-
# intente algo como

def view_pyme():
    
                grid_pyme = SQLFORM.grid(db.pyme,paginate=2)
                return dict(grid=grid_pyme)
