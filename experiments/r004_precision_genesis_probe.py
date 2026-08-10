from __future__ import annotations

import json

from enterprise_math.precision_genesis import (
    collision_spectrum,
    exhaustive_hidden_geometry_counts,
    exhaustive_history_resurrection_counts,
    first_geometry_scale,
    history_balance,
    propagate_history_multiplicities,
    toy_universe,
)


def main() -> None:
    layers = toy_universe()
    n0 = {0: 1}
    open_relation = frozenset({(0, 0), (0, 1)})
    n1 = propagate_history_multiplicities(n0, open_relation)
    collapse_relation = frozenset({(0, 0), (1, 0)})
    n2 = propagate_history_multiplicities(n1, collapse_relation)
    reopen_relation = frozenset({(0, 0), (0, 1)})
    n3 = propagate_history_multiplicities(n2, reopen_relation)

    payload = {
        "status": "EXECUTABLE_CHECKED_DISCOVERY_ONLY",
        "scales": [layer.scale for layer in layers],
        "lambda_geom": first_geometry_scale(layers),
        "hidden_geometry_counterexample": exhaustive_hidden_geometry_counts(3),
        "history_resurrection_exhaustion": exhaustive_history_resurrection_counts(3),
        "history_multiplicities": [n0, n1, n2, n3],
        "collision_spectra_W1_W2": [
            dict(collision_spectrum(n, 2)) for n in (n0, n1, n2, n3)
        ],
        "open_balance": history_balance(n0, open_relation),
        "collapse_balance": history_balance(n1, collapse_relation),
        "reopen_balance": history_balance(n2, reopen_relation),
    }
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
