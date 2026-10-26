#!/usr/bin/env python3
"""R300: exact source-renewal and mirror-support verifier; standard library only.

Scientific model: ordered six-edge positive-count BRC auxiliary source automaton,
not X6 dynamics. No physical-time, phase cancellation, or numerical approximation.
"""
from collections import defaultdict
import json

N = 200
BLOCK_N = 66
K_BOUND = 22
EDGES = (
    ((2, -1, -1), (2, +1, -1)),
    ((0, -1, -1), (0, +1, -1)),
    ((1, +1, +1), (2, +1, -1)),
)

def raw_source(limit):
    state = {(0, 1, 0, False): 1}
    end = []
    for n in range(limit + 1):
        fibres = defaultdict(int)
        for (q, sign, shift, last_zero), count in state.items():
            if q == 0:
                fibres[(sign, shift)] += count
        end.append(dict(fibres))
        if n == limit:
            break
        nex = defaultdict(int)
        for (q, sign, shift, last_zero), count in state.items():
            for bit, (nq, eta, c) in enumerate(EDGES[q]):
                if bit == 0 and last_zero:
                    continue
                nex[(nq, eta * sign, eta * shift + c, bit == 0)] += count
        state = nex
    return end

def renewal_source(limit):
    """Independent unique q0-return block concatenation enumerator."""
    end = [defaultdict(int) for _ in range(limit + 1)]
    end[0][(1, 0)] = 1
    for n in range(limit + 1):
        for (sign, shift), count in list(end[n].items()):
            for loops in range(limit - n - 2):
                length = loops + 3
                if n + length > limit:
                    break
                end[n + length][(sign, shift - loops - 1)] += count
                if loops >= 1:
                    end[n + length][(-sign, -shift - loops - 1)] += count
    return end

def convol(a, b, maxdeg):
    z = [0] * (maxdeg + 1)
    for i, ai in enumerate(a[:maxdeg + 1]):
        if not ai:
            continue
        for j, bj in enumerate(b[:maxdeg + 1 - i]):
            if bj:
                z[i + j] += ai * bj
    return z

def shift(a, d, maxdeg):
    return [0] * d + a[:maxdeg + 1 - d]

def div_one_plus_y(a):
    out = []
    prev = 0
    for v in a:
        prev = v - prev
        out.append(prev)
    return out

def exact_kernel(limit):
    m = limit // 2 + 2
    h = [0] * (m + 1)
    for n in range(m + 1):
        value = int(n == 4)
        for d, c in ((1, 1), (2, 2), (3, 1), (4, 1)):
            if n >= d:
                value += c * h[n - d]
        for d, c in ((1, 1), (2, 2), (3, 1)):
            if n >= d:
                value += c * sum(h[j] * h[n - d - j] for j in range(n - d + 1))
        h[n] = value
    w = [int(n == 0) + int(n == 1) + h[n] + (h[n - 1] if n else 0)
         for n in range(m + 1)]
    # Check the quadratic equation y w^2 - (1 + 2 y^2 - y^3)w + 1 = 0.
    ww = convol(w, w, m)
    for n in range(m + 1):
        left = (ww[n - 1] if n >= 1 else 0) - w[n]
        if n >= 2: left -= 2 * w[n - 2]
        if n >= 3: left += w[n - 3]
        left += int(n == 0)
        assert left == 0, ("quadratic", n, left)
    # J = [T - 2 y(1+y) w]^{-1}, T=1+y+2y^2+y^3-y^4.
    T = (1, 1, 2, 1, -1)
    den = [(T[n] if n < len(T) else 0)
           -2 * (w[n - 1] if n >= 1 else 0)
           -2 * (w[n - 2] if n >= 2 else 0) for n in range(m + 1)]
    assert den[0] == 1
    J = [1]
    for n in range(1, m + 1):
        J.append(-sum(den[j] * J[n - j] for j in range(1, n + 1)))
    u_x = [0] * (limit + 1)
    J_x = [0] * (limit + 1)
    for j in range(m + 1):
        if 2*j <= limit: J_x[2*j] = J[j]
        if 2*j + 1 <= limit: u_x[2*j + 1] = w[j]
    return h, w, J, J_x, u_x

def check():
    direct = raw_source(N)
    renewal = renewal_source(BLOCK_N)
    for n in range(BLOCK_N + 1):
        assert direct[n] == dict(renewal[n]), ("source-renewal", n)
    h, w, J, Jx, ux = exact_kernel(N)
    powers = [[1] + [0] * N]
    for _ in range(K_BOUND + 3):
        powers.append(convol(powers[-1], ux, N))
    oneplus = [1] + [0] * (N // 2 + 2)
    wpower = [oneplus]
    for _ in range(K_BOUND + 2):
        wpower.append(convol(wpower[-1], w, len(oneplus) - 1))
    comparisons = 0
    mirror_comparisons = 0
    for k in range(-K_BOUND, K_BOUND+1):
        pk = powers[abs(k)]
        kp = [pk[j] + (pk[j - 2] if j >= 2 else 0)
              + (pk[j - 4] if j >= 4 else 0)
              - (powers[abs(k - 1)][j - 1] if j >= 1 else 0)
              - (powers[abs(k - 1)][j - 3] if j >= 3 else 0)
              - (powers[abs(k + 1)][j - 1] if j >= 1 else 0)
              for j in range(N + 1)]
        km = [(powers[abs(k+2)][j - 4] if j >= 4 else 0)
              - (powers[abs(k+1)][j - 5] if j >= 5 else 0)
              for j in range(N + 1)]
        fp = convol(Jx, kp, N)
        fm = convol(Jx, km, N)
        for n in range(N + 1):
            assert fp[n] == direct[n].get((1, k), 0), ("plus-fibre", n, k)
            assert fm[n] == direct[n].get((-1, k), 0), ("minus-fibre", n, k)
            comparisons += 2
    for m in range(1, K_BOUND + 1):
        positive_kernel = div_one_plus_y(wpower[m])
        if m == 1:
            minus_numer = convol(w, [w[0]-1] + w[1:], len(w)-1)
            minus_kernel = div_one_plus_y(minus_numer)
            shift_neg = 5
        else:
            inner = [1] + [0] * (len(w)-1)
            wminus = [w[0]-1] + w[1:]
            wz = convol(w, wminus, len(w)-1)
            inner = [inner[j] + (wz[j-1] if j else 0) for j in range(len(inner))]
            minus_kernel = div_one_plus_y(convol(wpower[m-1], inner, len(w)-1))
            shift_neg = m + 2
        for j in range((N - m - 2)//2 + 1):
            n = m+2+2*j
            observed = direct[n].get((1, -m), 0)-direct[n].get((1, m), 0)
            assert observed == positive_kernel[j], ("mirror-plus", m, j)
            assert (observed > 0) == (j <= m-1 or j >= 4), ("plus-support",m,j)
            mirror_comparisons += 1
        for j in range((N - shift_neg)//2 + 1):
            n = shift_neg+2*j
            observed = direct[n].get((-1, -m), 0)-direct[n].get((-1, m), 0)
            assert observed == minus_kernel[j], ("mirror-minus",m,j)
            support = (j == 1 or j >= 4) if m == 1 else ((j == 0 or j >= 2) if m==2 else True)
            assert (observed > 0) == support, ("minus-support",m,j)
            mirror_comparisons += 1
    return {
      "schema":"EM_R300_SOURCE_RENEWAL_GREEN_CERT_V1", "status":"PASS",
      "arithmetic":"exact unbounded Python integers only", "raw_source_lengths":f"0..{N}",
      "independent_return_block_lengths":f"0..{BLOCK_N}",
      "exact_laurent_fibres":f"both signs, -{K_BOUND}<=k<={K_BOUND}, 0<=n<={N}",
      "fibre_integer_equalities":comparisons,
      "mirror_range":f"1<=m<={K_BOUND}", "mirror_integer_equalities":mirror_comparisons,
      "sharp_support_positive":"j in [0,m-1] union [4,infinity)",
      "sharp_support_negative":"m=1: j=1 or j>=4; m=2: j=0 or j>=2; m>=3: all j>=0",
      "formal_infinite_proof":"q0 first-return block decomposition + group-ring Green inversion (see proof)",
      "boundaries":"positive-count BRC auxiliary, no phase, no native X6 equivalence, no Driver review",
      "samples":{"length_3_plus_minus1":str(direct[3].get((1,-1),0)),
                 "length_4_minus_minus2":str(direct[4].get((-1,-2),0)),
                 "length_80_plus_minus4":str(direct[80].get((1,-4),0))}
    }
if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2))
