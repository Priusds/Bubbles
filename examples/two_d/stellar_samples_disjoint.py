import random
import shapely
from bubbles.gmsh_api import topology_to_gmsh_entities, write_geo
from bubbles.two_d.hole import Rectangular, Stellar
from bubbles.two_d.topology import Bubble, Topology


def generate_topo():
    """Generate a rectangular topology with many stellar inclusions."""
    domain =  shapely.Polygon(Rectangular(midpoint=(.5,.5), width=1, height=1).discretize_hole(refs=4))
    topo = Topology(domain)

    n_stellar = 100
    random.seed(0)
    levels = [random.choice([1,2,3,4,5]) for _ in range(n_stellar)]
    midpoints = [(random.random(), random.random()) for _ in range(n_stellar)]
    radii = [min((0.09, random.random() * 0.5)) for _ in range(n_stellar)]

    for mid, rad, lvl in zip(midpoints, radii, levels):
        C = shapely.Polygon(Stellar(midpoint=mid, radius=rad).discretize_hole(refs=50))
        topo.add(Bubble(polygon=C, level=lvl, is_hole=False), bubble_distance=.01, domain_distance=0)

    return topo

if __name__ == "__main__":
    topo = generate_topo()
    topo.plot()
    gmsh_entities = topology_to_gmsh_entities(topo)
    write_geo(
        gmsh_entities=gmsh_entities, file_name="stellar_samples_disjoint", correct_curve_loops=True
    )