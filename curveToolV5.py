import maya.cmds as cmds

#retaining order of selected verticies
cmds.selectPref(tso=True)

#deleting window
if cmds.window('Vertex to Curve', exists=True):
    cmds.deleteUI('Vertex to Curve')
    
#defining for UI
def create_curve(args):
    
    myList = []

#selecting object
    selected_objects = cmds.ls( flatten=True, os=True)

#creates list of every selected vert
    vertex_selection = [item for item in selected_objects]

#moves items back into main list
    if vertex_selection:
        myList.extend(vertex_selection)


    #print(myList)

#create a curve list
    curvePoints = []

#xform all items in list to find point number 
    for i in range(len(myList)):
        bloc = cmds.xform(myList[i], q=True, ws=True, t=True)

        if bloc:
#add these xformed values into the new list       
            curvePoints.append(bloc)
    #print(curvePoints)

    cmds.curve(p=curvePoints, n='curve1')

#motion path creator
def create_path(args):
    startNum = cmds.floatFieldGrp( Null, q=True, v=True)
    endNum = cmds.floatFieldGrp( Null2, q=True, v=True)
    worldUpT = cmds.textFieldGrp( Null3, q=True, tx=True)
    cmds.pathAnimation( su=0, stu=startNum, etu=endNum, f=True, wuo=f'{worldUpT}', wut='object')



#window

cmds.window('Vertex to Curve')
cmds.columnLayout(columnAttach=('left', 2), rowSpacing=10, columnWidth=5000, bgc=(1,0.5,1), w=320, h=300)
cmds.text(label='Maya Vertex to Curve Creator')
cmds.text(label='')
cmds.text('Make sure to select verts in order of curve creation')
cmds.button(label='Create Curve', command=create_curve, bgc=(0.3,0.3,0.3), w=100)

Full = cmds.floatFieldGrp(label='Degree', value1=3)

cmds.button(label='Attatch Object to Path', command=create_path, bgc=(0.3,0.3,0.3), w=150)

Null = cmds.floatFieldGrp(label='Start')
Null2 = cmds.floatFieldGrp(label='End')
cmds.text('Input selected object whom normals to orient')
Null3 = cmds.textFieldGrp( label='Mesh Name')



cmds.showWindow()
