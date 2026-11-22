"""Exact rational checks of the declared sample-only source-class lower bound."""
from fractions import Fraction as F
from pathlib import Path
import json


def make_road(blocks):
    end = blocks[-1][1][-1]
    q = [F(0) for _ in range(end + 2)]
    cells = []
    for scale, points in blocks:
        assert points[0] == scale and points[-1] == 2 * scale
        for left, right in zip(points, points[1:]):
            h = right - left
            for n in range(left, right + 1):
                r = n - left
                q[n] = F(r * r * (h - r) ** 2, 8 * scale * h * h)
            cells.append((scale, left, right))
    return q, cells


def energy(q, left, right):
    return sum((q[n] * q[n] / (n * n)
                for n in range(left, right + 1)), F(0))


def decimal_interval(v, digits=30):
    scale = 10 ** digits
    lo = v.numerator * scale // v.denominator
    hi = -((-v.numerator * scale) // v.denominator)
    def fmt(z):
        a, b = divmod(z, scale)
        return f"{a}.{b:0{digits}d}"
    return {"lower": fmt(lo), "upper": fmt(hi), "digits": digits}


def check_road(blocks):
    q, cells = make_road(blocks)
    end = blocks[-1][1][-1]
    for n in range(1, end + 1):
        assert abs(q[n + 1] - 2 * q[n] + q[n - 1]) <= F(1, n)
    for _, points in blocks:
        assert all(q[n] == 0 for n in points)
    cell_lower = F(0)
    for scale, left, right in cells:
        h = right - left
        direct = energy(q, left, right)
        lower = F(h ** 5 - h, 161280 * scale ** 4)
        assert direct >= lower
        cell_lower += lower
    total = energy(q, blocks[0][0], end)
    assert total >= cell_lower
    jensen_lower = F(0)
    for scale, points in blocks:
        k = len(points) - 1
        m, remainder = divmod(scale, k)
        phi = (k - remainder) * m ** 5 + remainder * (m + 1) ** 5 - scale
        shape = sum((right - left) ** 5 - (right - left)
                    for left, right in zip(points, points[1:]))
        assert shape >= phi
        assert total >= F(phi, 161280 * scale ** 4)
        jensen_lower += (F(scale, k ** 4) - F(1, scale ** 3)) / 161280
    assert total >= jensen_lower
    return total, jensen_lower, end, len(cells)


def main():
    partition_count = source_checks = cell_checks = 0
    for scale in range(2, 13):
        for mask in range(1 << (scale - 1)):
            points = [scale]
            points += [scale + r for r in range(1, scale)
                       if mask & (1 << (r - 1))]
            points += [2 * scale]
            _, _, count, cells = check_road([(scale, points)])
            partition_count += 1
            source_checks += count
            cell_checks += cells
    assert partition_count == 4094
    power_sum_checks = 0
    for h in range(1, 257):
        lhs = sum(r ** 4 * (h - r) ** 4 for r in range(1, h))
        rhs = F(h ** 9, 630) + F(2 * h ** 3, 63) - F(h, 30)
        assert lhs == rhs
        assert lhs >= F(h ** 9 - h, 630)
        power_sum_checks += 1
    blocks = [(8, [8, 9, 13, 16]), (16, [16, 21, 22, 31, 32])]
    total, lower, boundary_checks, _ = check_road(blocks)
    witnesses = []
    for s in [2, 4, 8]:
        scale = s ** 4
        points = list(range(scale, 2 * scale + 1, s ** 3))
        e, b, _, _ = check_road([(scale, points)])
        witnesses.append({"s": s, "X": scale, "intervals": s,
                          "step": s ** 3,
                          "energy": decimal_interval(e),
                          "analytic_lower": decimal_interval(b)})
    result = {
        "status": "PASS",
        "arithmetic": "fractions.Fraction; all assertions exact; displayed witness energies outward rounded",
        "scope": "General scalar source class |Delta^2 q_n|<=1/n; not the actual arithmetic road",
        "complete_partition_domain": {"X_min": 2, "X_max": 12,
            "partitions": partition_count, "integer_source_checks": source_checks,
            "cell_energy_checks": cell_checks},
        "power_sum_identity_checks": power_sum_checks,
        "dyadic_join_example": {"blocks": blocks,
            "integer_source_checks": boundary_checks,
            "energy": decimal_interval(total),
            "analytic_lower": decimal_interval(lower)},
        "equal_step_witnesses": witnesses,
        "analytic_theorems": {
            "single_block_lower": "M^2/161280*(X/k^4-1/X^3)",
            "single_block_balanced_upper": "2*M^2*X/(15*k^4)",
            "all_k_zero_observation_shape": "Phi=(k-r)*m^5+r*(m+1)^5-X; m=floor(X/k), r=X-m*k; minimax bracket M^2*Phi/(161280*X^4) to M^2*Phi/(120*X^4)",
            "power_window_mesh_threshold": "alpha>1/4 for uniform vanishing error in the stated source class and per-block mesh-scale family"
        }
    }
    path = Path(__file__).with_name("point_sample_lower_bound_certificate.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "output": str(path),
                      "partitions": partition_count, "source_checks": source_checks,
                      "cell_checks": cell_checks}, ensure_ascii=False))


if __name__ == "__main__":
    main()
