import bpy
import csv
import math
import mathutils
import random
from colorhash import ColorHash
from numpy import interp

path=""
filename="Carbonara_Edit2.csv"
reader=csv.reader(open(path+filename, "rt"))
time=[]
time.append([0,0,0])
c=0
min=0
day=0
hour=0
CollDay=0

for row in reader:
    print(c)
    print(row[0])
    print(bpy.context.view_layer.active_layer_collection.name)
    if c%144==0:
        CollDay=CollDay+1
        bpy.context.view_layer.active_layer_collection.exclude=True
        bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["Day "+str(CollDay)]
    col=ColorHash(row[1])
    
    d=int(row[0].split("-")[2].split(" ")[0]) #day
    h=int(row[0].split(" ")[1].split(":")[0]) #hour
    m=int(row[0].split(" ")[1].split(":")[1]) #minute
    time.append([d,h,m])
    c=c+1
    if time[c][0]!=time[c-1][0]:
        day=day+10
    if time[c][1]!=time[c-1][1]:
        hour=hour+10
    if time[c][2]!=time[c-1][2]:
        min=min+10
    sum=0.0
    for k in range(3,30,3):
        if row[k]==0 or row[k]=="":
            break
        else:
            sum=sum+float(row[k])
    rad=interp(sum,[0.0,2000.0],[1.0,2.5])
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=rad,\
        location=(math.sin(5*min)*10,math.cos(hour+min)*25,(day+hour/24+min/10)/10),\
        rotation=(random.randint(0,360),random.randint(0,360),random.randint(0,360)))
    bpy.context.object
    
    bpy.ops.apply.transformall()
    curIco=bpy.context.object.name
    
    cluster=str(c)+"_"+row[1]
    mat=bpy.data.materials["master"].copy()
    #mat=bpy.data.materials.new(name=cluster)
    
    if row[1]=="Facebook":
        col1=(0.063, 0.546, 0.692, 1.0)
        col2=(0.01, 0.018, 1.0, 1.0)
    elif row[1]=="Updates":
        col1=(0.103, 0.38, 0.072, 1.0)
        col2=(0.787, 0.787, 0.787, 1.0)
    elif row[1]=="Netflix":
        col1=(1.0, 0.0, 0.013, 1.0)
        col2=(0.0, 0.185, 1.0, 1.0)
    elif row[1]=="YouTube":
        col1=(0.787, 0.046, 0.016, 1.0)
        col2=(1.0, 0.371, 0.161, 1.0)
    elif row[1]=="Google":
        col1=(0.036, 1.0, 0.447, 1.0)
        col2=(0.8, 0.205, 0.608, 1.0)
    elif row[1]=="Mail":
        col1=(0.3, 0.1, 0.0, 1.0)
        col2=(1.0, 0.7, 0.5, 1.0)
    elif row[1]=="Skype":
        col1=(0.0, 0.9, 0.7, 1.0)
        col2=(0.06, 0.8, 0.28, 1.0)
    elif row[1]=="United We Stream":
        col1=(0.3, 1.0, 0.05, 1.0)
        col2=(0.8, 0.08, 0.8, 1.0)
    else:
        cH=ColorHash(row[1])
        col1=(cH.rgb[0]/255,cH.rgb[0]/255,cH.rgb[0]/255,1.0)
    
    mat.node_tree.nodes["Volume Scatter"].inputs[0].default_value=col1
    mat.node_tree.nodes["Volume Absorption"].inputs[0].default_value=col2
    vert=bpy.context.object.data.vertices
    for k in range(10):
        if row[3+(3*k)]==0 or row[3+(3*k)]=="":
            break
        rad=interp(row[3+(3*k)],[1.0,90000.0],[0.5,2.5])
        bpy.ops.object.metaball_add(type="BALL", radius=rad,location=(vert[k].co))
        bpy.context.object.name=cluster
        bpy.context.object.data.materials.append(mat)
        
    bpy.data.objects.remove(bpy.context.scene.objects[curIco], do_unlink = True)
    #if c==145:
    #    break