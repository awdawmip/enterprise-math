"""Six inverse moments at two separate side budgets, checked by integer residues."""
import argparse
import json
from math import factorial, lcm, prod
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

BUDGET = 2331
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)
MINIMUM_TEST = {2: 5, 3: 3, 5: 2, 7: 2, 11: 2, 13: 2, 17: 2, 19: 2}
ORDERS = (6, 5, 4, 3, 2, 1)


def valuation(d, p):
    exponent = 0
    while d % p == 0:
        d //= p
        exponent += 1
    return exponent


def smooth(d):
    for p in PRIMES:
        d //= p ** valuation(d, p)
    return d == 1


def number_of_lists(denominators):
    ways = [1] + [0] * BUDGET
    for d in denominators:
        cost = d - 1
        for b in range(cost, BUDGET + 1):
            ways[b] += ways[b-cost]
    return sum(ways)


def check_layer(program, denominators, p, k):
    h = max(valuation(d, p) for d in denominators)
    shift = p ** (h-k+1)
    moduli = [shift**j * p**valuation(factorial(j), p) for j in ORDERS]
    # Retain the highest orders that fit in an injective 64-bit mixed-radix key.
    for index in reversed(range(len(moduli))):
        if prod(moduli) <= 2**64:
            break
        moduli[index] = 1
    assert prod(moduli) <= 2**64 and max(moduli) < 2**63
    count = number_of_lists(denominators)
    lines = [f'{BUDGET} {len(denominators)} {count}', ' '.join(map(str, moduli))]
    for d in denominators:
        v = valuation(d, p)
        column = []
        for j, modulus in zip(ORDERS, moduli):
            x = p**(h-v) * pow(d // p**v, -1, modulus)
            column.append(prod(x-a*shift for a in range(j)) % modulus)
        lines.append(' '.join(map(str, [d, *column])))
    result = subprocess.check_output([program], input='\n'.join(lines)+'\n', text=True)
    summary, ambiguous = result.splitlines()
    counted, distinct, repeated = map(int, summary.split())
    assert counted == count
    return dict(prime=p, threshold=k, maximum=h, denominators=denominators,
                orders=[j for j,m in zip(ORDERS,moduli) if m>1],
                lists=count, distinct_signatures=distinct, repeated_classes=repeated,
                can_differ=list(map(int, ambiguous.split())))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    active = {d for d in range(2, BUDGET+2) if smooth(d)}
    original_size = len(active)
    evidence = []
    unrestricted = []
    with TemporaryDirectory() as directory:
        program = Path(directory) / 'sieve'
        subprocess.run(['c++', '-std=c++17', '-O3', str(Path(__file__).with_name('sieve.cpp')),
                        '-o', str(program)], check=True)
        # Here every integer up to the side budget is allowed, regardless of its factors.
        # Descending induction in k makes the higher valuation rows empty.
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
            kmax = 0
            while p**(kmax+1) <= BUDGET+1:
                kmax += 1
            for k in range(kmax, 3 if p==3 else 1, -1):
                exact = [d for d in range(p**k, BUDGET+2, p**k) if d % p**(k+1)]
                row = check_layer(program, exact, p, k)
                assert not row['can_differ']
                unrestricted.append(row)
        for p in reversed(PRIMES):
            for k in range(max(valuation(d,p) for d in active), MINIMUM_TEST[p]-1, -1):
                denominators = sorted(d for d in active if d % p**k == 0)
                if denominators:
                    row = check_layer(program, denominators, p, k)
                    active.difference_update(set(denominators) - set(row['can_differ']))
                    evidence.append(row)
    assert len(active) == 327 and lcm(*active) == 1396755360
    after_p19 = sorted(d for d in active if d % 19)
    assert lcm(*after_p19) == 73513440
    report = dict(budget=BUDGET, initial_19_smooth_size=original_size, layers=evidence,
                  unrestricted_full_dictionary_layers=unrestricted,
                  support_19_smooth=sorted(active), lcm_19_smooth=lcm(*active),
                  support_using_prior_p19_exclusion=after_p19, lcm_using_prior=lcm(*after_p19))
    output = json.dumps(report, indent=2, sort_keys=True) + '\n'
    if args.out:
        args.out.write_text(output)
    else:
        print(output, end='')


if __name__ == '__main__':
    main()
