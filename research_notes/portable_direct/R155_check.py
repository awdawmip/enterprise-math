"""R155: exact integer/rational checks for multi-one Sturmian fiber aliases."""
from fractions import Fraction
from collections import defaultdict
import json
from pathlib import Path

def cuts(w):
    m = len(w)
    s = [0]
    for bit in w:
        s.append(s[-1] + int(bit))
    ln, ld, hn, hd = 0, 1, 1, 1
    for i in range(m):
        for j in range(i + 1, m + 1):
            n, d = s[j] - s[i], j - i
            if (n-1)*ld > ln*d: ln, ld = n-1, d
            if (n+1)*hd < hn*d: hn, hd = n+1, d
            if ln*hd >= hn*ld: return None
    lo, hi = Fraction(ln, ld), Fraction(hn, hd)
    U = min(lo.denominator * (sj + 1) - j * lo.numerator for j, sj in enumerate(s))
    V = max(hi.denominator * sj - j * hi.numerator for j, sj in enumerate(s))
    return lo, hi, U, V

def phase_count(sig, L):
    a, b = sig[0].numerator, sig[0].denominator
    c, d = sig[1].numerator, sig[1].denominator
    U, V = sig[2:]
    ceil_B = -((-(c * L - V)) // d)
    floor_A = (a * L - U) // b
    return ceil_B - floor_A - 1

def predicted_count(k, L):
    b = 2*k + 1
    if L % 2:
        t = (L-1)//2
        return (t+1 + b-1)//b
    t = L//2
    # ceil((t+k+1)/b)-1
    return (t + k + 1 + b - 1)//b - 1

summary = {'status':'R155_MULTI_ONE_ALIAS_EXACT_PASS', 'family_k_range':[1,100], 'pattern_lengths_checked':[8,404], 'finite_enumeration_m':[1,14]}
family_pairs = 0
family_checks = 0
last_absence_checks = 0
for k in range(1,101):
    wa = '01'*k + '0010' + '10'*k
    wb = '01'*k + '0100' + '10'*k
    expected = (Fraction(k, 2*k+1), Fraction(1,2), k+1, 0)
    assert wa != wb and cuts(wa) == cuts(wb) == expected, (k, cuts(wa),cuts(wb),expected)
    family_pairs += 1
    trials = sorted(set(list(range(1, max(2*k+6, 15))) + [2*k,2*k+1,2*k+2,10000+k,10**30+37]))
    for L in trials:
        v = phase_count(expected, L)
        assert v == predicted_count(k,L), (k,L,v,predicted_count(k,L))
        assert (v == 0) == (L%2==0 and 2<=L<=2*k)
        family_checks += 1
    for L in range(1,2*k+4):
        assert (phase_count(expected,L)==0)==(L%2==0 and L<=2*k)
        last_absence_checks += 1
summary.update(family_pairs=family_pairs, phase_formula_checks=family_checks, absence_window_checks=last_absence_checks)
finite={}
for m in range(1,15):
    clusters=defaultdict(list)
    for x in range(1<<m):
        w=format(x,f'0{m}b')
        sig=cuts(w)
        if sig is not None:
            clusters[sig].append(w)
    counts={str(n):sum(1 for v in clusters.values() if len(v)==n) for n in sorted(set(map(len,clusters.values())))}
    finite[str(m)]={'candidate_words':1<<m,'admissible_words':sum(map(len,clusters.values())),'distinct_cut_signatures':len(clusters),'multiplicity':counts}
    assert max(map(len,clusters.values()))<=2
summary['finite_cut_collision_counts']=finite
print(json.dumps(summary,ensure_ascii=False,indent=2))
with Path(__file__).with_name('R155_verification.json').open('w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
    f.write('\n')
