"""Independent exact checks for layer increments and future-equivalence partitions.

Run with Python 3.10 or newer. Uses only the standard library.
"""
import json
from itertools import product


def log_prime_power(value, prime):
    exponent = 0
    while value > 1 and value % prime == 0:
        value //= prime
        exponent += 1
    assert value == 1
    return exponent


def check_all_submodules(prime, length, dimension):
    """Generate every submodule of (Z/p^k)^t by adjoining arbitrary vectors."""
    modulus = prime**length
    ambient = list(product(range(modulus), repeat=dimension))

    def multiple(scalar, vector):
        return tuple(scalar * entry % modulus for entry in vector)

    multiples = {z: [multiple(i, z) for i in range(modulus)] for z in ambient}
    origin = frozenset([ambient[0]])
    pending = [origin]
    submodules = {origin}
    transitions = []
    while pending:
        before = pending.pop()
        for z in ambient:
            after = before
            if z not in before:
                after = frozenset(
                    tuple((a + b) % modulus for a, b in zip(v, offset))
                    for v in before for offset in multiples[z]
                )
            transitions.append((before, z, after))
            if after not in submodules:
                submodules.add(after)
                pending.append(after)

    filtration = {
        module: [{multiple(prime**j, v) for v in module} for j in range(length + 1)]
        for module in submodules
    }
    layers = {
        module: [log_prime_power(len(lower) // len(upper), prime)
                 for lower, upper in zip(powers, powers[1:])]
        for module, powers in filtration.items()
    }
    for before, z, after in transitions:
        # Compute g_j as an element order from membership, separately from layer sizes.
        orders = [
            next(h for h in range(length + 1)
                 if multiple(prime**(j+h), z) in filtration[before][j])
            for j in range(length + 1)
        ]
        changes = [b-a for a, b in zip(layers[before], layers[after])]
        assert changes == [a-b for a, b in zip(orders, orders[1:])]
        assert set(changes) <= {0, 1} and sum(changes) == orders[0]
    return {"p": prime, "k": length, "dimension": dimension,
            "submodules": len(submodules), "transitions": len(transitions)}


def class_ids(keys):
    """Canonical class labels in order of first appearance, to compare full partitions."""
    labels = {}
    return tuple(labels.setdefault(key, len(labels)) for key in keys)


def future_partition(outputs, actions):
    """Refine a deterministic Moore machine by outputs and all one-letter successors."""
    classes = class_ids(outputs)
    while True:
        refined = class_ids(
            (classes[h], tuple(classes[action[h]] for action in actions))
            for h in range(len(outputs))
        )
        if refined == classes:
            return refined
        classes = refined


def check_all_scalar_systems(prime, columns):
    """Exhaust all pairs of scalar observation and target rows over the prime field."""
    masks = range(1 << columns)
    names = [1 << i for i in range(columns)]
    set_actions = [tuple(h | name for h in masks) for name in names]
    clear_actions = [tuple(h & ~name for h in masks) for name in names]
    row_vectors = list(product(range(prime), repeat=columns))
    systems = 0
    for observation, target in product(row_vectors, repeat=2):
        # Over a field the zero target coefficient is always preserved.
        # Every nonzero scalar target coefficient has the same answer as 1.
        agrees = [
            sum(name for name, x, y in zip(names, observation, target)
                if (s*x - y) % prime == 0)
            for s in range(prime)
        ]
        preserved = [any(h & a == h for a in agrees) for h in masks]
        obstructions = [
            h for h in masks if not preserved[h]
            and all(preserved[h ^ name] for name in names if h & name)
        ]
        influence = 0
        for obstruction in obstructions:
            influence |= obstruction

        residuals = []
        for h in masks:
            differences = {c & ~h for c in obstructions}
            residuals.append(tuple(sorted(
                c for c in differences
                if not any(d != c and d & c == d for d in differences)
            )))
        assert future_partition(preserved, set_actions) == class_ids(residuals)
        assert future_partition(preserved, set_actions + clear_actions) == class_ids(
            h & influence for h in masks
        )
        systems += 1
    return {"p": prime, "columns": columns, "systems": systems}


def main():
    modules = [check_all_submodules(*case) for case in [(2, 3, 2), (3, 2, 2), (2, 2, 3)]]
    machines = [check_all_scalar_systems(*case) for case in [(2, 4), (3, 3)]]
    result = {
        "module_cases": modules,
        "machine_cases": machines,
        "total_transitions": sum(case["transitions"] for case in modules),
        "total_systems": sum(case["systems"] for case in machines),
        "full_partitions_compared": 2 * sum(case["systems"] for case in machines),
    }
    assert [case["submodules"] for case in modules] == [37, 23, 129]
    assert result["total_transitions"] == 12487 and result["total_systems"] == 985
    print(json.dumps(result, separators=(",", ":")))


if __name__ == "__main__":
    main()
