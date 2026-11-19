"""Prime-power carry layers. No external packages, no tables of zeta values."""
import argparse
import json
from fractions import Fraction
from math import comb, fsum, isqrt, log
from pathlib import Path


def root(n, j):
    """Return floor(n**(1/j)) by integer Newton iteration."""
    if n < 2 or j == 1:
        return n
    if j == 2:
        return isqrt(n)
    guess = 1 << ((n.bit_length() + j - 1) // j)
    while True:
        nxt = ((j - 1) * guess + n // guess ** (j - 1)) // j
        if nxt >= guess:
            assert guess ** j <= n < (guess + 1) ** j
            return guess
        guess = nxt


def primes_upto(n):
    flags = bytearray([1]) * (n + 1)
    flags[:2] = b'\0\0'
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            flags[p*p::p] = bytes((n - p*p) // p + 1)
    return [p for p in range(2, n + 1) if flags[p]]


def gamma_interval(terms=64):
    log2 = 2 * sum(Fraction(1, (2*n+1) * 3**(2*n+1)) for n in range(terms))
    tail = Fraction(2 * 9, 8 * (2*terms+1) * 3**(2*terms+1))
    return 2*log2-1, 2*(log2+tail)-1


def constant(j, terms=86, digits=44):
    """Euler transformation of sum (-1)^i (2/(i+3))^(1/j)."""
    scale = 10**digits
    powers = [root(2*scale**j // (i+3), j) for i in range(terms)]
    lo = hi = Fraction(0)
    for t in range(terms):
        delta = sum((-1)**i * comb(t,i)*powers[i] for i in range(t+1))
        pos = sum(comb(t,i) for i in range(0,t+1,2))
        neg = (1 << t) - pos
        lo += Fraction(delta-neg, scale*2**(t+1))
        hi += Fraction(delta+pos, scale*2**(t+1))
    g_lo, g_hi = gamma_interval()
    return lo - g_hi, hi + Fraction(1, 2**terms) - g_lo


def bounds(x, digits=20):
    scale = 10**digits
    lo, hi = x
    return {'lower_numerator': lo.numerator*scale//lo.denominator,
            'upper_numerator': -((-hi.numerator*scale)//hi.denominator),
            'denominator': scale}


def intervals(n, j, max_base):
    """Group by floor(2n/p^j), counting inclusive endpoints with integers."""
    out = set()
    for u in range(1, n//(2**j) + 1):
        lo = root(n // (u+1), j)
        hi = root((2*n) // (2*u+1), j)
        if hi > lo:
            out.update(range(max(2,lo+1), min(max_base,hi)+1))
    return out


def run():
    gamma = 2*log(2)-1
    js = [2,3,4,5,6,8,12,20,40,80]
    certs = [constant(j) for j in js]
    assert all(a[1] < b[0] for a,b in zip(certs,certs[1:]))
    assert certs[0][0] > 0
    checked_pairs = 0
    for n in range(1, 385):
        for j in range(2,10):
            cap = root(n,j)
            via_windows = intervals(n,j,cap)
            via_residues = {b for b in range(2,cap+1) if 2*(n % b**j) >= b**j}
            assert via_windows == via_residues
            checked_pairs += cap-1 if cap else 0
    ps = primes_upto(32768)
    samples = []
    for j in [2,3,5,8,16,32]:
        for radix in [512, 4096, 32768]:
            n = radix**j
            # Avoid float exponentiation of n; n^(1/j) equals the chosen radix.
            hits = [p for p in ps if p <= radix and 2*(n % p**j) >= p**j]
            lows = [p for p in ps if p <= radix]
            value = (fsum(log(p) for p in hits) - gamma*fsum(log(p) for p in lows))/radix
            samples.append({'j': j, 'n_exact': str(n), 'root': radix,
                            'number_of_carry_primes':len(hits),
                            'layer_over_root_approx':round(value,10)})
    for j in [2,3,8,32,128,512]:
        assert root(2**j,j)==2 and 2*((2**j) % 2**j)<2**j
    return {'method':'Euler forward differences with certified integer radical and log bounds; layer samples use real prime logarithms.',
            'euler_terms':86, 'radical_decimal_places':44, 'log_series_terms':64,
            'K_intervals':{str(j):bounds(c) for j,c in zip(js,certs)},
            'carry_window_set_audit':{'all_n':[1,384], 'all_j':[2,9],
                    'all_integer_bases_checked':checked_pairs},
            'finite_layer_samples':samples,
            'j_growing_counterexample':{'n':'2^j','prime':2,'carry':0,
                        'layer_over_2':'-gamma*log(2)/2','tested_j':[2,3,8,32,128,512]}}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path)
    args = ap.parse_args()
    content = json.dumps(run(),ensure_ascii=False,indent=2) + '\n'
    if args.out:
        args.out.write_text(content,encoding='utf-8')
    else:
        print(content,end='')
