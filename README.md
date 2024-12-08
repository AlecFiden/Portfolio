Break Down how the code works:
It starts by creating a empty list, labeled myList. 
Then using a selection command, it gathers info from every point selected. 
To remeber the order and not group numbers together, the code specifies to track the selected order at the start of the code. 
Then we create a new list, called vertex_selection, for the selected vertecies and add the list to a item for item statement.
The using a if statement we extend everything from the vertex_selection list to the orignal empty myList.
Create a new list, called curvePoints.
Then according to the length of the list, we xform every item to gain its vertex posistions.
With the new positions, we append them to the list we created called curvepoints.
Create a curve out of the list "curvePoints".
Then using the pathanimation command, we can properly orient a objects rotation according to a objects normals.
