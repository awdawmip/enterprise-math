#!/usr/bin/env python3
import json

from enterprise_math.triaxial_directional_defect import (
    declare_frame, euler_phi, exposed_vertex_sampling_matrix, family_width,
    finite_support_left_inverse_possible, frame_census_law, gram_factor_kernel,
    gram_matrix, hex_box, hive_bridge_values, kernel_matrix,
    laplacian_product_kernel, matmul, rank_mod, rank_q,
    six_point_endpoint_stencil, triple_defect_kernel, xray_matrix,
    y_delta_is_additive_counterexample,
)

PRIMES = (2, 3, 5, 7)


def check_tomography(seeds, radius):
    x, points = xray_matrix(seeds, radius)
    p, domain, codomain = kernel_matrix(seeds, radius)
    assert points == codomain
    xp = matmul(x, p) if x and p else []
    assert all(v == 0 for row in xp for v in row)
    expected = len(hex_box(radius - family_width(seeds)))
    assert len(points) - rank_q(x) == expected
    assert rank_q(p) == len(domain)
    modular = {}
    for prime in PRIMES:
        nullity = len(points) - rank_mod(x, prime)
        image_rank = rank_mod(p, prime)
        assert nullity == expected
        assert image_rank == len(domain)
        modular[str(prime)] = {"xray_nullity": nullity, "image_rank": image_rank}
    return {"seeds": [list(s) for s in seeds], "radius": radius, "width": family_width(seeds), "box_size": len(points), "kernel_dim": expected, "modular": modular}


def main():
    result = {"schema": "TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_CHECK_V1", "phase": "PHASE_A_INDEPENDENT", "tomography": [], "census": [], "gram_characteristics": {}, "exposed_sampling": [], "hive": {}, "y_delta": {}, "deghosting": {}}

    for seed in ((1, 0, 0), (2, 1, 0), (3, 1, 0)):
        frame = declare_frame(seed)
        stencil = six_point_endpoint_stencil(frame)
        assert len(stencil) == 6 and all(abs(c) == 1 for c in stencil.values())
        assert gram_factor_kernel(frame) == laplacian_product_kernel(frame)
        for radius in range(max(0, frame.width - 1), frame.width + 3):
            result["tomography"].append(check_tomography((seed,), radius))

    for seeds, radius in ((((1, 0, 0), (2, 1, 0)), 4), (((2, 1, 0), (3, 1, 0)), 6)):
        result["tomography"].append(check_tomography(seeds, radius))

    for width in range(1, 33):
        u, o = frame_census_law(width)
        phi = euler_phi(width)
        assert u == phi and o == 2 * phi
        result["census"].append({"width": width, "phi": phi, "unoriented": u, "oriented": o})

    for radius in (1, 2, 3):
        gram, domain = gram_matrix(((1, 0, 0),), radius)
        assert rank_q(gram) == len(domain)
        result["gram_characteristics"][str(radius)] = {"amplitude_dim": len(domain), "q_rank": len(domain), "modular_ranks": {str(p): rank_mod(gram, p) for p in PRIMES}}
    assert result["gram_characteristics"]["1"]["modular_ranks"]["2"] == 0
    assert result["gram_characteristics"]["1"]["modular_ranks"]["3"] == 0
    assert result["gram_characteristics"]["2"]["modular_ranks"]["5"] < 7
    assert result["gram_characteristics"]["3"]["modular_ranks"]["7"] < 19

    for seeds, radius in ((((1, 0, 0),), 4), (((2, 1, 0),), 5), (((1, 0, 0), (2, 1, 0)), 5)):
        m, domain, exposed, q = exposed_vertex_sampling_matrix(seeds, radius)
        assert rank_q(m) == len(domain)
        assert all(rank_mod(m, p) == len(domain) for p in PRIMES)
        assert all(m[i][i] in (-1, 1) for i in range(len(m)))
        assert all(m[i][j] == 0 for i in range(len(m)) for j in range(i + 1, len(m)))
        result["exposed_sampling"].append({"seeds": [list(s) for s in seeds], "radius": radius, "amplitude_dim": len(domain), "exposed_vertex": list(exposed), "functional": list(q)})

    frame = declare_frame((1, 0, 0))
    field = {p: p[0] * p[1] * (p[0] + p[1]) for p in hex_box(5)}
    a, b, c, g = hive_bridge_values(field, frame)
    assert a == b == c == g and any(v != 0 for v in g.values())
    result["hive"] = {"same_operator_bridge": True, "nonzero": True}

    assert y_delta_is_additive_counterexample()
    result["y_delta"] = {"general_star_triangle_parameter_map_is_not_additive": True}

    for seed in ((1, 0, 0), (2, 1, 0), (3, 2, 0)):
        assert not finite_support_left_inverse_possible(triple_defect_kernel(declare_frame(seed)))
    result["deghosting"] = {"finite_support_translation_invariant_left_inverse": False}

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
