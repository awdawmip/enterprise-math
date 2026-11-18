"""Exact finite tests of local words, missed slopes, and digit correlations."""
from collections import Counter
from fractions import Fraction
from itertools import product


def digit(x, p):
    if not x:
        return 1
    while x % p == 0:
        x //= p
    return x % p


def source_words(p):
    """Primitive two-digit coefficient pairs, imposing the two prescribed cases."""
    modulus = p * p
    words = set()
    for a, b in product(range(modulus), repeat=2):
        if not (a % p or b % p):
            continue
        base = [(a*n + b) % modulus for n in range(modulus)]
        for hole in (range(1, p) if 0 in base else (1,)):
            words.add(tuple(x % p or x // p or hole for x in base))
    return words


def parameter_words(p):
    words = {(a,) * (p*p) for a in range(1, p)}
    for a, r, s, z in product(range(1, p), range(p), range(p), range(1, p)):
        w = tuple((a*(n-r)) % p if n % p != r else
                  ((s + a*((n-r)//p)) % p or z) for n in range(p*p))
        assert w not in words
        words.add(w)
        assert Counter(w) == {u: p+1+(u == z) for u in range(1, p)}
    return words


def distance_profile(words, p):
    # A one-hot symbol per position makes popcount(xor)/2 the Hamming distance.
    records = []
    for w in words:
        code = sum(1 << (i*p+a) for i,a in enumerate(w))
        if len(set(w)) == 1:
            records.append((code, ('constant',w[0]), None))
            continue
        root, = (r for r in range(p) if len(set(w[r::p])) > 1)
        a = w[(root+1) % p]
        s, count = Counter((w[root+p*k]-a*k) % p for k in range(p)).most_common(1)[0]
        assert count == p-1
        records.append((code,(root,a),s))
    best = [p*p]*3
    for i,(x,outer,inner) in enumerate(records):
        for y,outer2,inner2 in records[:i]:
            level = 2 if outer != outer2 else int(inner != inner2)
            best[level] = min(best[level], (x ^ y).bit_count()//2)
    return best


def truncated(x, p, power):
    return digit(x % power, p)


def verify_slopes(p, k, words):
    # Every shear is a relabeling of (d,e); checking all pairs covers every shift.
    power = p**k
    low = power//p
    failures = 0
    for d, e in product(range(power), repeat=2):
        w = tuple(truncated(d*n+e, p, power) for n in range(p*p))
        expected_failure = d % low == e % low == 0 and d % power != 0
        assert (w not in words) == expected_failure
        failures += expected_failure
    assert failures == p*(p-1)
    assert any(truncated(m+low, p, power) != truncated(m, p, power)
               for m in range(power))
    return power*power


def correlation(p, lag, row, col):
    """Limiting joint entry probability (multiplicative output scale is one)."""
    if not lag:
        return Fraction(row == col, p-1)
    power = 1
    while lag % (power*p) == 0:
        power *= p
    unit = lag//power % p
    forced = int(col == (row + unit) % p)
    exceptional = int(col == unit) + int(row == -unit % p)
    return (Fraction(power-1, power*(p-1)) * (row == col)
            + Fraction(forced, power*p) + Fraction(exceptional, power*p*(p-1)))


def verify_pairs(p, depth):
    # Resolve the one unknown tail digit for x=0 or x+lag=0 modulo p**depth.
    # Uniform average over nonzero tail digits is exact on these disjoint cylinders.
    modulus = p**depth
    alphabet = range(1, p)
    tests = 0
    for lag in [1, -1, 2, p, p+1, -p*p, 2*p*p]:
        assert lag % modulus
        counts = Counter()
        for x in range(modulus):
            y = (x+lag) % modulus
            if x and y:
                counts[digit(x,p), digit(y,p)] += p-1
            else:
                for t in alphabet:
                    counts[digit(x,p) if x else t, digit(y,p) if y else t] += 1
        total = modulus*(p-1)
        assert all(Fraction(counts[a,b], total) == correlation(p,lag,a,b)
                   for a,b in product(alphabet,repeat=2))
        tests += (p-1)**2
    return tests


if __name__ == '__main__':
    for prime in (5,7):
        language = source_words(prime)
        assert language == parameter_words(prime)
        assert distance_profile(language,prime) == [1, prime-2, prime*prime-prime-4]
        total = sum(verify_slopes(prime, k, language) for k in (1,2))
        print(f'p={prime}: {len(language)} words, {total} slope/intercept pairs, '
              f'{verify_pairs(prime,4)} joint probability coordinates')
    # At the source prime use two-digit arithmetic directly on a full-width word.
    p = 211
    for a,r,s,z in ((7,99,15,8),(210,210,210,2)):
        b=p*s-a*r
        w=[(a*n+b)%p or ((a*n+b)//p)%p or z for n in range(p*p)]
        assert Counter(w) == {v:p+1+(v==z) for v in range(1,p)}
    print('Two full-width words checked at p=211.')
