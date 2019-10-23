# --------------------------------------------------------
# Note:                                                                                                                                                   
#     - This is the Python code used in Script Manager.                                                                                                                                                 
# Compatible:                                                                                                                                         
#     - Win / Mac                                                                                                                                 
#     - R19, R20                                                                                                                                
# --------------------------------------------------------


import c4d
from c4d import gui


# Add user data
def AddUserData(obj, name, val):
    # Create default container
    bc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_BOOL)

    # Rename the entry
    bc[c4d.DESC_NAME] = name

    # set the default value
    element = obj.AddUserData(bc)
    obj[element] = val

    c4d.EventAdd()

# Add display points index object
def displayPntIndex(obj):
    # Create null object and cloner object
    Null = c4d.BaseObject(c4d.Onull)
    Cloner = c4d.BaseObject(1018544)

    # Create null object and cloner object
    Null[c4d.NULLOBJECT_DISPLAY] = 0
    Null[c4d.ID_BASELIST_NAME] = 'dot'

    # Custom the setting of cloner object
    Cloner[c4d.ID_MG_TRANSFORM_DISPLAYMODE] = 4
    Cloner[c4d.ID_MG_MOTIONGENERATOR_MODE] = 0
    Cloner[c4d.MG_OBJECT_LINK] = obj
    Cloner[c4d.MG_POLY_MODE_] = 0
    Cloner[c4d.ID_MG_TRANSFORM_COLOR] = c4d.Vector(1, 0.986, 0.15)
    Cloner[c4d.ID_BASELIST_NAME] = 'DisplayPntIndex'

    # Insert Cloner object under the active Object
    doc.InsertObject(Cloner, obj)

    # Insert Null object under Cloner object
    doc.InsertObject(Null, Cloner)

    c4d.EventAdd()

# Add display edges index object
def displayEdgeIndex(obj):
    # Create null object and cloner object
    Null = c4d.BaseObject(c4d.Onull)
    Cloner = c4d.BaseObject(1018544)

    # Custom the setting of the null object
    Null[c4d.NULLOBJECT_DISPLAY] = 0
    Null[c4d.ID_BASELIST_NAME] = 'dot'

    # Custom the setting of cloner object
    Cloner[c4d.ID_MG_TRANSFORM_DISPLAYMODE] = 4
    Cloner[c4d.ID_MG_MOTIONGENERATOR_MODE] = 0
    Cloner[c4d.MG_OBJECT_LINK] = obj
    Cloner[c4d.MG_POLY_MODE_] = 1
    Cloner[c4d.ID_MG_TRANSFORM_COLOR] = c4d.Vector(0, 1, 0)
    Cloner[c4d.ID_BASELIST_NAME] = 'DisplayEdgeIndex'

    # Insert Cloner object under the active Object
    doc.InsertObject(Cloner, obj)

    # Insert Null object under Cloner object
    doc.InsertObject(Null, Cloner)

    c4d.EventAdd()

# Add display primitive(polygons) index object
def displayPrimIndex(obj):
    # Create null object and cloner object
    Null = c4d.BaseObject(c4d.Onull)
    Cloner = c4d.BaseObject(1018544)

    # Custom the setting of the null object
    Null[c4d.NULLOBJECT_DISPLAY] = 0
    Null[c4d.ID_BASELIST_NAME] = 'dot'

    # Custom the setting of cloner object
    Cloner[c4d.ID_MG_TRANSFORM_DISPLAYMODE] = 4
    Cloner[c4d.ID_MG_MOTIONGENERATOR_MODE] = 0
    Cloner[c4d.MG_OBJECT_LINK] = obj
    Cloner[c4d.MG_POLY_MODE_] = 2
    Cloner[c4d.ID_MG_TRANSFORM_COLOR] = c4d.Vector(1, 0, 0)
    Cloner[c4d.ID_BASELIST_NAME] = 'DisplayPrimIndex'

    # Insert Cloner object under the active Object
    doc.InsertObject(Cloner, obj)

    # Insert Null object under Cloner object
    doc.InsertObject(Null, Cloner)

    c4d.EventAdd()


# Main
def main():
    # Large Icons
    c4d.CallCommand(100004708, 100004708)

    # Lines
    c4d.CallCommand(12540, 12540)

    # seleted object
    obj = doc.GetActiveObject()

    if obj == None:
        gui.MessageDialog('Please Select the Object!')
        return
    else:
         AddUserData(obj, "Show Points Index", True)
         AddUserData(obj, "Show Edge Index", False)
         AddUserData(obj, "Show Primitive Index", False)

    # Insert the cloner object
    displayEdgeIndex(obj)
    displayPrimIndex(obj)
    displayPntIndex(obj)
    doc.GetActiveObject()

    # Add python Tag
    c4d.CallCommand(100004788, 50058)
    c4d.EventAdd()



# Execute main()
if __name__=='__main__':
    main()