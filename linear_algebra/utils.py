from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D, proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import itertools as itools


def plot_2D_vector(vector, with_coordinate_projections=True, color='black', lw=1):
    x, y = vector
    
    arrow = plt.arrow(
        0, 0, 
        *vector, 
        head_width=0.05, 
        head_length=0.1, 
        color=color, 
        length_includes_head=True,
        lw=lw)
        
    plt.ylim((
        min(0, min(1.2 * min(vector), plt.ylim()[0])), 
        max(1.2 * max(vector), plt.ylim()[1])
    ))
    plt.xlim((
        min(0, min(1.2 * min(vector), plt.xlim()[0])), 
        max(1.2 * max(vector), plt.xlim()[1])
    ))
    
    if with_coordinate_projections:
        plt.hlines(y, 0, x, linestyles='--', alpha=0.2, color=color)
        plt.vlines(x, 0, y, linestyles='--', alpha=0.2, color=color)
    
    if min(plt.xlim()[0], plt.ylim()[0]) < 0:
        plt.axhline(0, color='black', alpha=0.05)
        plt.axvline(0, color='black', alpha=0.05)
    
    return arrow


def plot_polygon(*args):
    triangle = plt.Polygon(np.array(args))
    plt.gca().add_patch(triangle)
    
    
def plot_vectors_and_polygon(vectors, colors=None):
    if colors:
        for vector, color in zip(vectors, colors):
            plot_2D_vector(vector, color=color)
    else:
        for vector in vectors:
            plot_2D_vector(vector)

    plot_polygon(*vectors)
    

# Originates from this StackOverflow post: 
# https://stackoverflow.com/questions/11140163/python-matplotlib-plotting-a-3d-cube-a-sphere-and-a-vector/11156353#11156353
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
        

def plot_3D_vector(ax, vector, lw=1, color='black', with_coordinate_projections=True):
    x, y, z = vector
    
    ax.set_xlim((
        min(0, min(1.2 * min(vector), ax.get_xlim()[0])), 
        max(1.2 * max(vector), ax.get_xlim()[1])
    ))
    
    ax.set_ylim((
        min(0, min(1.2 * min(vector), ax.get_ylim()[0])), 
        max(1.2 * max(vector), ax.get_ylim()[1])
    ))
    
    ax.set_zlim((
        min(0, min(1.2 * min(vector), ax.get_zlim()[0])), 
        max(1.2 * max(vector), ax.get_zlim()[1])
    ))
        
    arrow = Arrow3D(
        [0, x], 
        [0, y], 
        [0, z], 
        mutation_scale=20, 
        lw=1, 
        arrowstyle='-|>', 
        color=color)
    
    ax.add_artist(arrow)
    
    if with_coordinate_projections:
        ax.plot(*zip([x, 0, 0], vector), ls='--', alpha=0.2, color=color)
        ax.plot(*zip([0, y, 0], vector), ls='--', alpha=0.2, color=color)
        ax.plot(*zip([0, 0, z], vector), ls='--', alpha=0.2, color=color)
       
    fontsize = 15
    ax.set_xlabel('x', fontsize=fontsize)
    ax.set_ylabel('y', fontsize=fontsize)
    ax.set_zlabel('z', fontsize=fontsize)


def plot_3D_vectors_and_polyhedron(ax, vectors, colors=None):
    if colors:
        for vector, color in zip(vectors, colors):
            plot_3D_vector(ax, vector, color=color)
    else:
        for vector in vectors:
            plot_3D_vector(ax, vector)

    for combination in list(itools.combinations(vectors, 3)):
        ax.add_collection3d(Poly3DCollection(
            [combination], 
            edgecolor='black', 
            alpha=0.1, 
            facecolor='steelblue',
            linewidths=0.5))
     

