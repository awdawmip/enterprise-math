# S23/AV — exact finite-horizon saturation through H=3000

Date: 2026-11-08 Asia/Shanghai  
Status: AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED  
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34  
Research mode: TASK_RESEARCH  
Local Researcher-ID: EM-R01-BE5667  
Activity: RA-712877729F925CDB  
Local session key: chatgpt-automation-run11-20261108T055650+0800 (locally assigned; not a server-issued session)

## 1. New theorem

For the two-point S23/AV iid auxiliary likelihood-sign observer, define

\[
T_h=\{10^i/7^s:0\le i\le s\le h\},
\]

and let \(N(h)\) be the least common padded prefix length whose attainable likelihood-sign values meet every open cell of the threshold partition induced by \(T_h\).

Then

\[
\boxed{N(h)=2\,455\,069\qquad
\text{for every integer }510\le h\le3000.}
\]

The exact predecessor theorem is \(N(510)=2\,455\,069\). The new result is a complete exact upper certificate at \(H=3000\), followed by threshold nesting.

## 2. Auxiliary model and observer

The ordered one-step laws on labels \((1,3,4)\) are

\[
P_0=(1/2,1/4,1/4),\qquad
P_1=(5/7,1/4,1/28).
\]

A prefix with \(k\) occurrences of label 1 and \(\ell\) occurrences of label 4 has likelihood ratio

\[
\Lambda(k,\ell)=\frac{7^{k+\ell}}{10^k}.
\]

Label 3 pads the prefix without changing this ratio. Put

\[
r=\frac{\log 7}{\log(10/7)},\qquad E(k,\ell)=k-r\ell.
\]

A threshold \(10^i/7^s\) is represented by

\[
t(v,j)=rv-j,\qquad v=s-i,\quad j=i,\quad v+j=s\le h.
\]

Thus the ordered threshold set is the set of \(t(v,j)\) with \(v,j\ge0\) and \(v+j\le h\). A prefix occupies an open threshold cell exactly when \(E(k,\ell)\) lies strictly between its two endpoint coordinates.

This remains the two-point S23/AV auxiliary observer. It is not the full six-source/ten-label mother experiment.

## 3. Lower bound inherited from the exact N(510) theorem

The predecessor file

- research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/FULL_SATURATION.md
- immutable commit 85b53d06d6ba775e516c566c1d79828b6ca9bb1f

proves the exact equality

\[
N(510)=2\,455\,069.
\]

For \(h\ge510\), \(T_{510}\subseteq T_h\). Refining the threshold partition cannot reduce the least prefix length needed to hit every open cell. Therefore

\[
N(h)\ge N(510)=2\,455\,069
\qquad(h\ge510).
\]

It remains to prove \(N(3000)\le2\,455\,069\).

## 4. Exact rational enclosure

The verifier uses only Python standard-library Fraction and integer arithmetic. With \(Q=10^{26}\), it proves

\[
\frac{545569623581288298975349314}{Q}
<r<
\frac{545569623581288298975349315}{Q}.
\]

For \(0<z<1\),

\[
2\operatorname{atanh}(z)
=2\sum_{j=0}^{44}\frac{z^{2j+1}}{2j+1}+R,
\qquad
0<R<\frac{2z^{91}}{91(1-z^2)}.
\]

The exact identities used are

\[
\log2=2\operatorname{atanh}(1/3),\quad
\log(5/4)=2\operatorname{atanh}(1/9),\quad
\log(8/7)=2\operatorname{atanh}(1/15),
\]

\[
\log7=3\log2-\log(8/7),\qquad
\log(10/7)=\log(5/4)+\log(8/7).
\]

All series bounds and quotient bounds are rational. No floating-point logarithm is used for a mathematical decision.

## 5. Complete endpoint certificate at H=3000

There are

\[
\frac{3001\cdot3002}{2}=4\,504\,501
\]

distinct thresholds and \(4\,504\,502\) open cells. Irrationality of \(r\) follows because a rational \(r=p/q>0\) would imply \(7^{p+q}=10^p\), contrary to prime factorization.

### 5.1 Complete threshold order

The verifier sorts all threshold pairs by the rational lower key \(lo\cdot v-Q\cdot j\), then checks all 4,504,500 adjacent strict comparisons. For adjacent pairs with difference \((\Delta v,\Delta j)\), it checks

\[
(lo\text{ if }\Delta v\ge0\text{ else }hi)\Delta v>Q\Delta j.
\]

Since \(lo/Q<r<hi/Q\), these inequalities certify the true strict order of every adjacent pair, including both unbounded outer cells.

### 5.2 Determinant-one translated near-resonance cells

Reuse the exact integer basis

\[
u=(79,431),\qquad w=(380295,2074774),
\qquad \det(u,w)=1.
\]

Write \(p=2\,074\,774\), \(q=380\,295\), and \(n_*=p+q=2\,455\,069\).

For every nonnegative shift \((v_0,j_0)\) satisfying

\[
v_0+j_0\le H-510=2490,
\]

the verifier checks that \((v_0,j_0)\) and \((v_0+79,j_0+431)\) are consecutive thresholds in the complete \(T_{3000}\) ordering.

The number of such special cells is

\[
\frac{2491\cdot2492}{2}=3\,103\,786.
\]

For each special cell, the explicit prefix counts

\[
(k,\ell)=(p-j_0,\ q-v_0)
\]

are nonnegative and have length

\[
k+\ell=n_*-(v_0+j_0)\le n_*.
\]

Both strict cell-membership inequalities are checked at the adverse rational endpoints. The ordered special-witness stream digest is

09c75d5b112d60f9f4af260bac0159a609ad0b71f081ad385ce15280f4feab72.

### 5.3 Short-prefix cover

For every remaining cell, the verifier searches prefixes with \(k+\ell\le15\,000\). The rational key only locates a candidate cell; a candidate is accepted only after both applicable strict integer inequalities pass.

This produces 1,365,279 distinct certified cell witnesses. The maximum short-witness length is 15,000, the maximum label-4 count is 553, and the left outer cell is witnessed by \((k,\ell)=(0,550)\).

The short-witness stream digest is

95a0d040384b9fd934e1f7fdcd0b2355af55fc5269f7f9a6bb47d0abd36ce97f.

### 5.4 Exact first-entry witnesses for the remaining 35,436 interior cells

After the special-cell and short-prefix passes, exactly 35,436 interior cells remain. For an adjacent cell with endpoints \((v_L,j_L)\) and \((v_R,j_R)\), set

\[
\Delta v=v_R-v_L,\qquad \Delta j=j_R-j_L,
\]
\[
L=\ell+v_L,\qquad K=k+j_L.
\]

The cell condition becomes

\[
0<K-rL<r\Delta v-\Delta j.
\]

For each fixed \(L\), the smallest admissible integer \(K\) is

\[
K(L)=\max(\lfloor rL\rfloor+1,\ j_L).
\]

The verifier establishes the floor exactly from the rational enclosure. For every earlier \(L\), it proves using the adverse upper endpoint that

\[
r(L+\Delta v)\le K(L)+\Delta j,
\]

so the cell's upper inequality fails even for the smallest admissible \(K\); every larger \(K\) fails as well. At the first successful \(L\), the lower and upper inequalities are both certified using the rational endpoints. Since \(K(L)\) is nondecreasing and \(L\) strictly increases, this first successful \(L\) minimizes \(K+L\), hence minimizes \(k+\ell\) for that cell.

All 35,436 first-entry witnesses are found within 10,000 increments of \(v_L\). Their exact prefix lengths range from 15,001 to 16,396; the maximum label-4 count is 78 and the maximum label-1 count is 16,362.

A representative newly exposed gap has adjacent endpoints

\[
(2676,102)\longrightarrow(2687,162),
\]

with \((\Delta v,\Delta j)=(11,60)\) and width \(11r-60\). Its exact first-entry prefix is

\[
(k,\ell)=(14923,78),\qquad k+\ell=15001.
\]

The verifier also checks that no earlier \(L\) enters this cell. The complete first-entry witness stream digest is

769db1bdd09407b4f043a184c1ac0118c210a2eabd09263077b018a0c29a00d5.

### 5.5 Right outer cell and exhaustion

The right outer cell \((rH,+\infty)\) is witnessed by

\[
(k,\ell)=(16368,0),
\]

with the strict inequality certified from the rational enclosure.

The four disjoint classes exhaust all 4,504,502 open cells:

| Witness class | Cells |
|---|---:|
| Determinant-one translated cells | 3,103,786 |
| Short-prefix witnesses | 1,365,279 |
| Exact first-entry interior witnesses | 35,436 |
| Right outer cell | 1 |
| Total | 4,504,502 |

Every cell therefore has a prefix of length at most \(n_*=2\,455\,069\). Label-3 padding gives a common prefix length \(n_*\), so \(N(3000)\le n_*\). Together with the inherited lower bound, \(N(3000)=n_*\). Threshold nesting then gives the theorem for every integer \(510\le h\le3000\).

## 6. Actual verification evidence

The exact file VERIFY_H3000.py was executed in-kernel under CPython 3.13.5. It uses only the standard library. The executed file SHA-256 is

c748aa25993843b7492008aedb74cfd690cd7b14cd305d986ced130159a034ba

Actual stdout:

~~~text
PASS_RATIONAL_R_INTERVAL 545569623581288298975349314 545569623581288298975349315 100000000000000000000000000
PASS_ALL_ADJACENT_THRESHOLD_ORDER 4504500
PASS_TRANSLATED_GAP_CELLS 3103786
PASS_SHORT_PREFIX_COVER 1365279 MAX_LENGTH 15000 MAX_ELL 553 LEFT_OUTER (0, 550)
PASS_RIGHT_OUTER 16368 0 LENGTH 16368
PASS_FIRST_ENTRY_CELLS 35436 MIN_LENGTH 15001 MAX_LENGTH 16396 MAX_ELL 78 MAX_K 16362
PASS_SAMPLE_NEW_GAP (2676,102)->(2687,162) (14923, 78, 15025, 2754, 15001)
SPECIAL_WITNESS_SHA256 09c75d5b112d60f9f4af260bac0159a609ad0b71f081ad385ce15280f4feab72
SHORT_WITNESS_SHA256 95a0d040384b9fd934e1f7fdcd0b2355af55fc5269f7f9a6bb47d0abd36ce97f
FIRST_ENTRY_WITNESS_SHA256 769db1bdd09407b4f043a184c1ac0118c210a2eabd09263077b018a0c29a00d5
CERTIFIED_EXACT_N 3000 2455069 TOTAL_CELLS 4504502 SPECIAL 3103786 SHORT 1365279 FIRST_ENTRY 35436 RIGHT_OUTER 1
PASS_S23_AV_EXACT_N_H3000_ENDPOINT 51.62 sec
~~~

## 7. Reproducible checker source

The following is the complete source of VERIFY_H3000.py. It was executed exactly as stored locally; its SHA-256 is recorded above.

~~~python
#!/usr/bin/env python3
"""Exact rational-interval certificate for the S23/AV endpoint H=3000.

No floating-point arithmetic is used for mathematical decisions.  The proof
inherits the exact lower bound N(510)=2,455,069 and certifies every open
threshold cell at H=3000 with a prefix of length at most that bound.
"""
from bisect import bisect_right
from fractions import Fraction
from hashlib import sha256
from time import perf_counter


def log_bounds(z, terms=45):
    term = z
    total = Fraction(0)
    for j in range(terms):
        total += 2 * term / (2 * j + 1)
        term *= z * z
    remainder = 2 * term / ((2 * terms + 1) * (1 - z * z))
    return total, total + remainder


# Exact rational enclosure for r = log(7) / log(10/7).
l2, u2 = log_bounds(Fraction(1, 3))
l9, u9 = log_bounds(Fraction(1, 9))
l15, u15 = log_bounds(Fraction(1, 15))
ln7_lo, ln7_hi = 3 * l2 - u15, 3 * u2 - l15
ln107_lo, ln107_hi = l9 + l15, u9 + u15

Q = 10**26
lo = ln7_lo * Q // ln107_hi
hi = ln7_hi * Q // ln107_lo + 1
assert Fraction(lo, Q) < ln7_lo / ln107_hi
assert ln7_hi / ln107_lo < Fraction(hi, Q)
assert hi - lo == 1
print("PASS_RATIONAL_R_INTERVAL", lo, hi, Q)

H = 3000
p, q = 2074774, 380295
nstar = p + q
short_budget = 15000
started = perf_counter()

# T_H in reflected logarithmic coordinates t(v,j)=r*v-j.
thresholds = [(v, j) for v in range(H + 1) for j in range(H - v + 1)]
thresholds.sort(key=lambda pair: lo * pair[0] - Q * pair[1])
keys = [lo * v - Q * j for v, j in thresholds]
assert len(thresholds) == (H + 1) * (H + 2) // 2 == 4504501
assert all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1))

# Strictly certify the complete order of all 4,504,501 thresholds.
for idx in range(len(thresholds) - 1):
    v1, j1 = thresholds[idx]
    v2, j2 = thresholds[idx + 1]
    dv, dj = v2 - v1, j2 - j1
    assert (lo if dv >= 0 else hi) * dv > Q * dj, (
        idx, thresholds[idx], thresholds[idx + 1]
    )
assert thresholds[0] == (0, H)
assert thresholds[-1] == (H, 0)
print("PASS_ALL_ADJACENT_THRESHOLD_ORDER", len(thresholds) - 1)

# The old determinant-one near-resonance basis supplies a complete
# translated special-cell family.
index = {pair: i for i, pair in enumerate(thresholds)}
special = set()
special_hash = sha256()
shift_limit = H - 510
for v0 in range(shift_limit + 1):
    for j0 in range(shift_limit - v0 + 1):
        cell = index[(v0, j0)] + 1
        assert thresholds[cell] == (v0 + 79, j0 + 431), (
            v0, j0, thresholds[cell]
        )
        special.add(cell)
        k, ell = p - j0, q - v0
        assert k >= 0 and ell >= 0 and k + ell <= nstar
        v_left, j_left = thresholds[cell - 1]
        v_right, j_right = thresholds[cell]
        assert (k + j_left) * Q > hi * (ell + v_left)
        assert (k + j_right) * Q < lo * (ell + v_right)
        special_hash.update(
            f"{cell},{k},{ell}\n".encode("ascii")
        )

expected_special = (shift_limit + 1) * (shift_limit + 2) // 2
assert len(special) == expected_special == 3103786
print("PASS_TRANSLATED_GAP_CELLS", len(special))

# Find and exactly certify every remaining cell with a short prefix
# (k+ell <= 15,000).  The rational key only locates a candidate cell;
# adverse endpoint inequalities decide whether it is accepted.
flags = bytearray(len(thresholds) + 1)
covered = 0
short_hash = sha256()
short_count = 0
max_short_length = 0
max_short_ell = 0
left_outer_witness = None

for ell in range(short_budget + 1):
    k_start = max(0, lo * ell // Q - H - 2)
    k_end = min(short_budget - ell, hi * (ell + H) // Q + 2)
    if k_start > k_end:
        continue
    for k in range(k_start, k_end + 1):
        cell = bisect_right(keys, Q * k - lo * ell)
        if cell in special or flags[cell] or cell == len(thresholds):
            continue
        if cell:
            v_left, j_left = thresholds[cell - 1]
            if (k + j_left) * Q <= hi * (ell + v_left):
                continue
        if cell < len(thresholds):
            v_right, j_right = thresholds[cell]
            if (k + j_right) * Q >= lo * (ell + v_right):
                continue
        flags[cell] = 1
        covered += 1
        short_count += 1
        max_short_length = max(max_short_length, k + ell)
        max_short_ell = max(max_short_ell, ell)
        if cell == 0:
            left_outer_witness = (k, ell)
        short_hash.update(f"{cell},{k},{ell}\n".encode("ascii"))

assert short_count == 1365279
assert flags[0] == 1 and left_outer_witness == (0, 550)
assert max_short_length == 15000
assert max_short_ell == 553
print(
    "PASS_SHORT_PREFIX_COVER",
    short_count,
    "MAX_LENGTH", max_short_length,
    "MAX_ELL", max_short_ell,
    "LEFT_OUTER", left_outer_witness,
)

# The right outer cell (r*H,+infinity) has the direct prefix
# (ceil(r*H),0), certified by the same rational enclosure.
floor_lo = lo * H // Q
floor_hi = (hi * H - 1) // Q
assert floor_lo == floor_hi
k_right = floor_lo + 1
assert k_right * Q > hi * H
assert k_right <= nstar
print("PASS_RIGHT_OUTER", k_right, 0, "LENGTH", k_right)

# Every cell still unmarked is now an interior cell.  For an adjacent
# cell with endpoints (vL,jL),(vR,jR), put L=ell+vL, K=k+jL.
# Its prefix condition is exactly:
#       0 < K-r*L < r*(vR-vL)-(jR-jL).
# For each L, the smallest admissible K is max(floor(rL)+1,jL).
# The first L satisfying the upper inequality gives the minimum k+ell:
# K_L is nondecreasing and L strictly increases.  Earlier L values are
# rejected with the adverse upper endpoint hi/Q.
missing = [
    (thresholds[cell - 1], thresholds[cell], cell)
    for cell, flag in enumerate(flags)
    if not flag and cell not in special and cell < len(thresholds)
]
assert len(missing) == 35436


def first_witness(left, right):
    v_left, j_left = left
    v_right, j_right = right
    dv, dj = v_right - v_left, j_right - j_left

    for L in range(v_left, v_left + 10001):
        floor_lo = lo * L // Q
        floor_hi = (hi * L - 1) // Q
        assert floor_lo == floor_hi, (
            left, right, L, floor_lo, floor_hi
        )
        K = max(floor_lo + 1, j_left)

        # Candidate satisfies K-rL < r*dv-dj.
        assert K * Q > hi * L
        if lo * (L + dv) > Q * (K + dj):
            k = K - j_left
            ell = L - v_left
            assert k >= 0 and ell >= 0

            # Every earlier L fails even at the adverse upper endpoint.
            for L0 in range(v_left, L):
                f0 = lo * L0 // Q
                f1 = (hi * L0 - 1) // Q
                assert f0 == f1
                K0 = max(f0 + 1, j_left)
                assert hi * (L0 + dv) <= Q * (K0 + dj), (
                    left, right, L0, K0
                )
            return k, ell, K, L

    raise AssertionError(("no first-entry witness within 10,000 steps", left, right))


first_hash = sha256()
first_count = 0
first_min_length = 10**30
first_max_length = 0
first_max_ell = 0
first_max_k = 0
sample = None

for left, right, cell in missing:
    k, ell, K, L = first_witness(left, right)
    length = k + ell
    assert length <= nstar
    first_count += 1
    first_min_length = min(first_min_length, length)
    first_max_length = max(first_max_length, length)
    first_max_ell = max(first_max_ell, ell)
    first_max_k = max(first_max_k, k)
    first_hash.update(
        f"{cell},{k},{ell},{K},{L}\n".encode("ascii")
    )
    if left == (2676, 102) and right == (2687, 162):
        sample = (k, ell, K, L, length)

assert first_count == 35436
assert first_min_length == 15001
assert first_max_length == 16396
assert first_max_ell == 78
assert first_max_k == 16362
assert sample == (14923, 78, 15025, 2754, 15001)
print(
    "PASS_FIRST_ENTRY_CELLS",
    first_count,
    "MIN_LENGTH", first_min_length,
    "MAX_LENGTH", first_max_length,
    "MAX_ELL", first_max_ell,
    "MAX_K", first_max_k,
)
print("PASS_SAMPLE_NEW_GAP", "(2676,102)->(2687,162)", sample)

# The four disjoint witness classes exhaust all open cells.
total_cells = len(thresholds) + 1
assert len(special) + short_count + first_count + 1 == total_cells
assert total_cells == 4504502

print("SPECIAL_WITNESS_SHA256", special_hash.hexdigest())
print("SHORT_WITNESS_SHA256", short_hash.hexdigest())
print("FIRST_ENTRY_WITNESS_SHA256", first_hash.hexdigest())
print(
    "CERTIFIED_EXACT_N",
    H,
    nstar,
    "TOTAL_CELLS", total_cells,
    "SPECIAL", len(special),
    "SHORT", short_count,
    "FIRST_ENTRY", first_count,
    "RIGHT_OUTER", 1,
)
print(
    "PASS_S23_AV_EXACT_N_H3000_ENDPOINT",
    round(perf_counter() - started, 2),
    "sec",
)
~~~

## 8. BRC, P000 and scope

The applied BRC observer retains the joint count \((\#1,\#4)\), with label 3 as a distinct no-change padding operation. The exact likelihood ratio factors through this joint count for the declared two-point iid likelihood-sign observer. This is an observer- and horizon-typed sufficient statistic, not a general deletion of a joint/composite relation direction.

Current P000 V5, the ACTIVE Heartbeat World worldview, and the joint-relation observer-preservation contract are unchanged. This auxiliary statistical theorem does not establish native X6 geometry, a native three-dimensional slice, the full-lawful four-copy minimax value \(\delta_4\), or the lawful source/time/observer map to the six-source/ten-label mother model.

No external literature claim is made. The result is an author-side exact finite certificate combined with the inherited analytic lower-bound theorem. Independent mathematical review remains pending; the result is not an admitted Result or Working Truth.

## 9. Source and control provenance

- Frozen S23 scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
- Frozen mother-model proof: research_notes/brc_n4_s23_asymmetric_hull_gap_sqrt43_20261101_research1/PROOF.md at the frozen commit; Git blob 766a1cd3f0be000c6d14a96c7c16d7ad5e02647c.
- Exact lower-bound predecessor: research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/FULL_SATURATION.md at 85b53d06d6ba775e516c566c1d79828b6ca9bb1f; Git blob 6c685aa08461643bf7283d18ba4784bb5b80079a.
- Exact previous endpoint: research_notes/brc_s23_av_endpoint_plateau_h2500_20261108_r1/PROOF.md at 82b7f4d6dfea840cfe7ec20db2dfbba5e035a0f7.
- Current GLOBAL_KNOWLEDGE canonical main snapshot read in this run: 8eaa94592d1edc323704d877919813f5559b8fc5; 00_BOOTSTRAP.md blob bc9e1b3065eae7947850a0aa2261dc201a43265c, OPERATING_MANUAL.md blob 9ce8584221f83f3de369af7239b029e4b36621c4.
- Current Enterprise Math canonical main snapshot read in this run: 4efef1592c0e576b11478352e8ca97c835ebd3ee; continuation protocol blob 79002ab20e30abb464837dc4c980cf5b5b68e001, portable research protocol blob 5633f5fa72097fb4d6afcf7ff23a0df3797fd4d0, P000 V5 machine blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488, joint-relation observer contract blob 3923890d77a02d84b772f789e6912dd14f220d14, research method blob b1c3555220bccce46db84363af94e4a3e0d0df9c, and BRC priority policy blob 721ea6b559ca8a4ac11c7ed90e715219581d319b.
- Local TASK_RESEARCH activity record: research_activity_records/RA-712877729F925CDB.json, immutable commit 29ae1ce5a9596fea439289f3efe021f5dc31b5c0, remotely read back. Its authority fields explicitly set task registration, claim, review, Working Truth and mathematical acceptance to false. The session key is locally assigned, not a server-issued execution session.
- GitHub authenticated identity awdawmip has repository admin/write permission. This is distinct from native Enterprise Math research authority.
- Native control reads and session start returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, UPSTREAM_STATUS_TOOL_ERROR, STATUS_DATABASE_UNAVAILABLE, operation_sent=false. The Sites gateway reported CONFIGURED_NOT_LIVE_VERIFIED, backend_connected=false, research_authority_granted=false, owner_binding_matches=true, and required a separate Site-bound backend client with secure user-entered credential. The active Owner, formal CLAIM and native Researcher-Activity therefore remain unconfirmed.

## 10. Next research unit

1. Continue from \(H=3001\) and find the first horizon where the exact saturation length exceeds \(2\,455\,069\), inspecting new adjacent threshold gaps rather than assuming the old determinant-one family is exhaustive.
2. Classify the new gap vectors by continued-fraction neighbors and unimodular bases. The \((11,60)\) gap and its exact first-entry witness provide a concrete new seed.
3. Keep the full-lawful \(\delta_4\) minimax equality and the six-source/ten-label mother-model source/time/observer bridge as separate unresolved units.
