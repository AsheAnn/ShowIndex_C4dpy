# ----------------------------------------------------------------------
# Note:                                                                                                                                                   
#     - This is the Python code used in the Python Tag for ShowIndex.py                                                                                                                                                  ##
# Compatible:                                                                                                                                         
#     - Win / Mac                                                                                                                                 
#     - R19, R20, R21                                                                                                                                
# ----------------------------------------------------------------------


import c4d
from c4d import gui


# Main 
def main():
    # Get object
    obj = op.GetObject()

    # set the user data
    x = obj[c4d.ID_USERDATA, 1]
    y = obj[c4d.ID_USERDATA, 2]
    z = obj[c4d.ID_USERDATA, 3]

    # Get childrens from object
    objList = obj.GetChildren()
    prim = objList[1]
    edge = objList[2]
    pnts = objList[0]

    # Select Object
    ao = doc.GetActiveObject()
    
    # Link object to cloners
    if ao == None:
        pass
    else:
        pnts[c4d.MG_OBJECT_LINK] = ao
        prim[c4d.MG_OBJECT_LINK] = ao
        edge[c4d.MG_OBJECT_LINK] = ao
    
    # Set the control to the user data
    if x == False:
        # off
        pnts[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1 
    else:
        # on
        pnts[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 0 

    if y == False:
        # off
        edge[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1 
    else:
        # on
        edge[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 0

    if z == False:
        # off
        prim[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
    else:
        # on
        prim[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 0 