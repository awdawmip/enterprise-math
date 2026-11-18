"""Exact Gaussian atom enumeration and an independent frozen pair-scan regression."""
import argparse
from array import array
from collections import Counter
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import gcd, isqrt
from pathlib import Path
from random import Random


def split_catalog(bound, seed):
    """Euler's linear rational sieve; Cornacchia with checked square roots."""
    composite = bytearray(bound + 1)
    primes = []
    split = []
    rng = Random(seed)
    attempts = 0
    euclidean_steps = 0
    for p in range(2, bound + 1):
        if not composite[p]:
            primes.append(p)
            if p % 4 == 1:
                # A complete deterministic fallback makes the seeded run total.
                # With fresh uniform draws, the fallback probability is at most 1/p^2.
                random_limit = max(32, 2 * p.bit_length())
                for j in range(random_limit + p - 1):
                    g = rng.randrange(1, p) if j < random_limit else j - random_limit + 1
                    root = pow(g, (p - 1) // 4, p)
                    attempts += 1
                    if root * root % p == p - 1:
                        break
                else:
                    raise ArithmeticError(p)
                x, y = p, min(root, p - root)
                while y * y > p:
                    x, y = y, x % y
                    euclidean_steps += 1
                z = isqrt(p - y * y)
                assert y * y + z * z == p and min(y, z) > 0
                split.append((p, max(y, z), min(y, z)))
        for q in primes:
            product = q * p
            if product > bound:
                break
            composite[product] = 1
            if p % q == 0:
                break
    return split, attempts, euclidean_steps


def fold(x, y):
    # Only the strict images enter this function; sigma conjugates all entries.
    for j in range(4):
        if x > abs(y):
            if y > 0:
                return x, y, 2*j, 1
            if y < 0:
                return x, -y, (-2*j) % 8, -1
        x, y = -y, x
    raise ArithmeticError((x, y))


class VerifyBox:
    """A compact exact comparison table; unnecessary to stream emitted atoms."""
    def __init__(self, height):
        self.height = height
        self.slots = array('Q', [0]) * (height * (height - 1) // 2)
        self.stats = Counter()
        self.support = Counter()
        self.present = [[] for _ in range(height + 1)]

    def emit(self, b, a, eps, pos, path, sign):
        positive = negative = 1
        previous = 0
        for prime, exponent in path:
            assert previous < prime and exponent != 0
            previous = prime
            if sign * exponent > 0:
                positive *= prime**abs(exponent)
            else:
                negative *= prime**abs(exponent)
        norm = a*a + b*b
        assert positive == pos and positive*negative == (norm if norm % 2 else norm//2)
        index = (b - 1) * (b - 2) // 2 + a - 1
        self.present[b].append(a)
        # The odd norm determines every missing negative-oriented exponent.
        code = 1 + (pos << 3) + eps
        assert not self.slots[index], ('duplicate', b, a)
        self.slots[index] = code
        self.support[len(path)] += 1
        self.stats['atoms'] += 1

    def certificate(self):
        digest = sha256()
        for b in range(2, self.height + 1):
            offset = (b - 1) * (b - 2) // 2
            for a in sorted(self.present[b]):
                code = self.slots[offset + a - 1] - 1
                digest.update(f'{b},{a},{code & 7},{code >> 3}\n'.encode('ascii'))
        return digest.hexdigest()


def generate(height, emit, seed=1160):
    """Each callback receives (b,a,eps,positive product,live path,global sign).
    With (p,e) in the live path, the signed valuation is sign*e. Consume the
    mutable path in the callback, or copy it if the consumer retains it.
    """
    bound = height*height + (height-1)*(height-1)
    catalog, attempts, steps = split_catalog(bound, seed)
    stats = Counter()
    max_power = bound.bit_length()
    powers_gcd = [[gcd(i, j) for j in range(max_power + 1)] for i in range(max_power + 1)]
    path = []

    def visit(index, norm, x, y, pos, earlier_gcd, depth):
        p, exponent = path[-1]
        stats['odd_disk_nodes'] += 1
        stats['max_factors_with_multiplicity'] = max(stats['max_factors_with_multiplicity'], depth)
        b, a, eps, sign = fold(x, y)
        if b <= height:
            stats['odd_box_atoms'] += 1
            content = powers_gcd[earlier_gcd][abs(exponent)]
            if content == 1:
                stats['free_direction_groups'] += 1
            elif content % 2 == 0:
                stats['odd_box_squares'] += 1
            else:
                stats['odd_box_nonsquare_powers'] += 1
            positive = pos if sign == 1 else norm // pos
            emit(b, a, eps, positive, path, sign)
            if b + a <= height:
                stats['even_box_atoms'] += 1
                emit(b+a, b-a, (1-eps) % 8, norm // positive, path, -sign)
        else:
            stats['outside_height'] += 1
        remaining = bound // norm
        # The current prime can recur only with the previously chosen orientation.
        if p > remaining:
            return
        _, u, v = catalog[index]
        if exponent < 0:
            v = -v
        delta = 1 if exponent > 0 else -1
        path[-1] = (p, exponent + delta)
        visit(index, norm*p, x*u-y*v, x*v+y*u,
              pos*p if delta > 0 else pos, earlier_gcd, depth+1)
        path[-1] = (p, exponent)
        prefix_gcd = powers_gcd[earlier_gcd][abs(exponent)]
        for k in range(index+1, len(catalog)):
            q, u, v = catalog[k]
            if q > remaining:
                break
            for orientation in (1, -1):
                w = orientation * v
                path.append((q, orientation))
                visit(k, norm*q, x*u-y*w, x*w+y*u,
                      pos*q if orientation == 1 else pos, prefix_gcd, depth+1)
                path.pop()

    for k, (p, u, v) in enumerate(catalog):
        path.append((p, 1))
        visit(k, p, u, v, p, 0, 1)
        path.pop()
    stats.update(split_primes=len(catalog), root_attempts=attempts, cornacchia_steps=steps)
    return dict(stats)


def frozen_oracle(repo):
    directory = repo / 'research_notes' / 'experiments'
    base = directory / 'gregory_machin_rational_support2_h1000_census_20260904.py'
    inner = directory / 'gregory_machin_gaussian_triple_census_20260903.py'
    assert sha256(base.read_bytes()).hexdigest() == 'f786eddf8606b1faeb6109ff4a68b5c0cbe3d3500a5a3756c033edf5fd8154b5'
    assert sha256(inner.read_bytes()).hexdigest() == '662d099f92c0f940e91f72b575c53cce88f9f9b2e3c6f8bf4fcb9a03eabab200'
    spec = spec_from_file_location('atom_reference', base)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def full_comparison(box, oracle):
    groups = set()
    rows = squares = 0
    h = box.height
    for b in range(2, h + 1):
        offset = (b-1)*(b-2)//2
        for a in range(1, b):
            code = box.slots[offset + a - 1]
            if gcd(a, b) > 1:
                assert code == 0
                continue
            eps, entries = oracle.general_signature(b, a)
            positive = 1
            for prime, exponent in entries:
                if exponent > 0:
                    positive *= prime**exponent
            assert code == 1+(positive << 3)+eps, (b, a, entries, eps)
            normalized, scalar = oracle.normalized_free_direction(entries)
            groups.add(normalized)
            if (b-a) % 2 and scalar % 2 == 0:
                squares += 1
            rows += 1
    return rows, len(groups), squares


def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument('--repo', type=Path, default=Path('.'), help='root of frozen reference repo')
    parser.add_argument('--heights', type=int, nargs='+', default=[1000, 1500])
    parser.add_argument('--generator-only', action='store_true', help='skip independent pair/valuation oracle')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    oracle = None if args.generator_only else frozen_oracle(args.repo)
    results = []
    for h in args.heights:
        if not 2 <= h <= 2**29:
            parser.error('the regression table uses bounded 64-bit slots and requires 2 <= H <= 2^29')
        box = VerifyBox(h)
        stats = generate(h, box.emit)
        stats.update(box.stats)
        stats.update(height=h, duplicate_atoms=0, nonzero_support_sizes=dict(sorted(box.support.items())),
                     coordinate_order_sha256=box.certificate())
        if oracle:
            rows, groups, squares = full_comparison(box, oracle)
            root_count = sum(
                1 for x in range(2, isqrt(2*h) + 1) for y in range(1, x)
                if (x-y) % 2 and gcd(x, y) == 1 and max(x*x-y*y, 2*x*y) <= h
            )
            assert squares == stats.get('odd_box_squares', 0) == root_count
            stats['square_root_region_count'] = root_count
            assert rows == stats['atoms'] and groups == stats['free_direction_groups']
            stats['oracle_matched_atoms'] = rows
            stats['oracle_matched_free_groups'] = groups
        if h == 1000:
            assert stats['atoms'] == 304191 and stats['free_direction_groups'] == 202662
        results.append(stats)
    content = json.dumps(results, indent=2, sort_keys=True) + '\n'
    print(content, end='')
    if args.output:
        args.output.write_text(content)


if __name__ == '__main__':
    main()
