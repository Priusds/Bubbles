from topology.two_d.topology import Topology
from topology.two_d.hole import Stellar, Circle
from dolfin import *
import matplotlib.pyplot as plt
import os
import random as rd
from topology.geo_utils.utils import write_geo


def dolfin_mesh(file_name):
    # creates .xml mesh from .geo mesh and returns dolfin mesh
    os.system("gmsh -2 " + file_name + ".geo")  # -v 0
    os.system("dolfin-convert " + file_name + ".msh " + file_name + ".xml")
    return Mesh(file_name + ".xml")


def test_2d_1():
    width = 2
    height = 2
    rect_out = [(0,0),(2,2)]
    rect_in_1 = [(.25,.25),(.75,.75)]
    rect_in_2 = [(1.25,.25),(1.75,.75)]
    rect_in_3 = [(1.25,1.25),(1.75,1.75)]
    rect_in_4 = [(.25,1.25),(.75,1.75)]

    topo = Topology(rect_out, [rect_in_1, rect_in_2,rect_in_3,rect_in_4])
    
    N = 100
    counter = 0
    i = 0
    while counter < N and i < 1000:
        i+=1
        print(i)
        midpoint_s = rd.uniform(0, width), rd.uniform(0, height)
        #midpoint_s = (.5,1) # TODO: check error!
        # this way you define a Stellar hole
        stellar_hole = Stellar(midpoint_s, .02) 
        
        if topo.add_hole(stellar_hole,refs=20):
            counter += 1

    
    print("Needed ", i, "runs for ",N, "holes")
    geo = topo.get_geometry(filled=True)
    write_geo(geo,"test")


def test_2d_2():
    file_name = "test"
    mesh = dolfin_mesh("test")
    subdomains_hole = MeshFunction("size_t", mesh, "test" + "_physical_region.xml")
    plot(subdomains_hole)
    #plot(mesh)
    plt.show()


def test_2d_3():
    width = 2
    height = 2
    rect_out = [(0,0),(2,2)]
    rect_in = [(.5,.5),(1.5,1.5)]
    rect_in_1 = [(.25,.25),(.75,.75)]
    rect_in_2 = [(1.25,.25),(1.75,.75)]
    rect_in_3 = [(1.25,1.25),(1.75,1.75)]
    rect_in_4 = [(.25,1.25),(.75,1.75)]

    #topo = Topology(rect_out, [rect_in_1, rect_in_2,rect_in_3,rect_in_4])
    topo = Topology(rect_out,[rect_in])

    #midpoint_s = rd.uniform(0, width), rd.uniform(0, height)
    midpoint_s = (.5,1) # TODO: check error!
    ## this way you define a Stellar hole
    stellar_hole = Circle(midpoint_s, .05) 
    
    topo.add_hole(stellar_hole,refs=10)

    midpoint_s = (.51,1.51) # TODO: check error!
    # this way you define a Stellar hole
    stellar_hole = Circle(midpoint_s, .05) 
    
    topo.add_hole(stellar_hole,refs=10)

    #midpoint_s = (.51,.51) # TODO: check error!
    # this way you define a Stellar hole
    #stellar_hole = Circle(midpoint_s, .05) 
    
    #topo.add_hole(stellar_hole,refs=10)

    #midpoint_s = (.01,.01) # TODO: check error!
    # this way you define a Stellar hole
    #stellar_hole = Circle(midpoint_s, .05) 
    
    #topo.add_hole(stellar_hole,refs=10)
   

    topo.write_geo("test",flag = "hole")

def test_2d_4():
    rect_out = [(0,0),(2,2)]
    
    rect_in_1 = [(.25,.25),(.75,.75)]
    rect_in_2 = [(1.25,.25),(1.75,.75)]
    rect_in_3 = [(1.25,1.25),(1.75,1.75)]
    rect_in_4 = [(.25,1.25),(.75,1.75)]

    topo = Topology(rect_out, [rect_in_1, rect_in_2,rect_in_3,rect_in_4])
    
    midpoint_s = (1,.01) 
    stellar_hole = Circle(midpoint_s, .05) 
    added = topo.add_hole(stellar_hole,refs=10)

    midpoint_s = (.01,.01) 
    stellar_hole = Circle(midpoint_s, .05) 
    added = topo.add_hole(stellar_hole,refs=20)

    midpoint_s = (.251,.251) 
    stellar_hole = Circle(midpoint_s, .05) 
    added = topo.add_hole(stellar_hole,refs=10)

    midpoint_s = (.251,.51) 
    stellar_hole = Circle(midpoint_s, .05) 
    added = topo.add_hole(stellar_hole,refs=10)

    midpoint_s = (.251,1.1) 
    stellar_hole = Circle(midpoint_s, .05) 
    added = topo.add_hole(stellar_hole,refs=10)

    midpoint_s = (.4,.4) 
    stellar_hole = Circle(midpoint_s, .05) 
    added = topo.add_hole(stellar_hole,refs=10)

    
    geo = topo.get_geometry(filled=True)
    write_geo(geo, "test")