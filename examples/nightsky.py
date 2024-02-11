import math
import random

from pargeo.constraint import DistanceConstraint
from pargeo.geometry import NStar, RainDrop, Rectangle
from pargeo.gmsh_utils import write_geo
from pargeo.topology import Topology


def generate_topo():
    domain = Rectangle(midpoint=(0.0, 0.0), width=2, height=1).to_polygon()
    topo = Topology(domain)

    random.random()

    n_stars = 100
    # random.seed(0)
    midpoints = [
        (2 * random.random() - 1, random.random() - 0.5) for _ in range(n_stars)
    ]
    alphas = [2 * math.pi * random.random() for _ in range(n_stars)]

    constraint = DistanceConstraint()
    constraint.set_distance(0.01, "any", "any")

    radii_in = [0.04 * random.random() + 0.005 for _ in range(n_stars)]
    radii_out = [3 * r_in for r_in in radii_in]

    Ns = [random.choice([5]) for _ in range(n_stars)]

    for M, r_in, r_out, N, alph in zip(midpoints, radii_in, radii_out, Ns, alphas):
        star = NStar(M, r_in, r_out, N, alph).to_polygon()
        topo.add(star, level=1, constraint=constraint)

    n_rain = 200
    midpoints = [
        (2 * random.random() - 1, random.random() - 0.5) for _ in range(n_rain)
    ]
    A = [0.2 * random.random() + 0.6 for _ in range(n_rain)]
    S = [0.001 * random.random() + 0.005 for _ in range(n_rain)]
    for M, a, scale in zip(midpoints, A, S):
        raindrop = RainDrop(M, a, scale).discretize(128)
        topo.add(raindrop, level=2, constraint=constraint)

    return topo


if __name__ == "__main__":
    topo = generate_topo()
    topo.plot()

    write_geo(
        topology=topo,
        file_name="stellar_samples_periodic_constrains",
        correct_curve_loops=True,
    )
