# -*- coding: utf-8 -*-
# intente algo como
def view_student():
    
                grid_student = SQLFORM.grid(db.student,paginate=2)
                return dict(grid=grid_student)
