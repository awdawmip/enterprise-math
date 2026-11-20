# PREFIX-956 — Dyadic source-gap sieve and directional rigidity for adjacent odd cores

Date: 2026-11-20. Frozen scientific input inherited without rebasing: f42f2906d77f24085c123f3ccfe9667d41caa96d. Direct predecessor: PREFIX-955, with immutable off-diagonal certificate SHA-256 1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75. Model: auxiliary named XOR observer, not native X6/BRC/Heartbeat rotation. Status: author proof plus independently checked finite computation; mathematical Review and activity association not claimed.

## 1. A dyadic source-conservation theorem

Fix p>=3 and H=2^(p-1). Let a,b be odd members of Q_p={H+1,H+3,...,2H-1}, and k be positive odd. Suppose both named collisions exist:

    (ka XOR 2^j)-2^i = tb,
    ((k+2)a XOR 2^J)-2^I = Tb,

with named indices in {0,...,p-1} and positive t,T. Put m=T-t, s=1-2 bit_j(ka), S=1-2 bit_J((k+2)a), c=2^i-s2^j and C=2^I-S2^J. All four named indices and actual XOR signs remain part of the witness.

**Theorem 956.1 (dyadic gap residue and source parity).** Set Delta=C-c. Then

    Delta=2a-mb.

Consequently:

* If m is odd, Delta is odd. More sharply, c = 1-t (mod 2) and C = t (mod 2). The two source-term parities are opposite and encode the parity of t.
* If m=0 (mod 4), Delta=2 (mod 4).
* If m=2 (mod 4), Delta=0 (mod 4).

These conditions apply to all valid named joint witnesses regardless of the quotient sizes.

**Proof.** Expand each XOR by its *actual* source-bit sign. Subtraction gives 2a-(T-t)b=C-c. Because a,b are odd, reduction modulo 4 yields the three residue cases. Each individual equation reduced modulo 2 gives c=1-t and C=1-T. If m is odd, T=t+m has opposite parity to t, giving C=t modulo 2. QED.

For source terms, c and C each lie in the interval [1-H,2H], hence Delta lies in [1-3H,3H-1].

**Corollary 956.2 (directional rigidity).** In the same model, if m>=5, then a>b. If m=0, then a <= (3H-1)/2. In particular, a positive gap of at least 5 cannot occur with a<=b.

**Proof.** If a<=b and m>=5, Delta=2a-mb <=(2-m)b <=-3b<-3H, contrary to the source interval. For m=0, 2a=Delta<=3H-1. QED.

## 2. Exact two-adic determinant filter

For a nonresonant witness set d=2t-km, and put

    N_a=tC-Tc,       N_b=kC-(k+2)c.

The determinant inverse is a=N_a/d, b=N_b/d. Because a and b are odd, every actual nonresonant witness must satisfy

    v_2(N_a)=v_2(N_b)=v_2(d),

including negative nonzero integers by applying the valuation to their absolute values. Here d !=0 and neither numerator can vanish. Equivalently, for v=v_2(d), both numerators have remainder 2^v modulo 2^(v+1). These are **necessary** fast filters; ordinary integer divisibility, valid Q_p bounds, actual source signs and original XOR equalities are still checked.

This filter separates structural residual information (named i,j,I,J and signed source terms) from lossy quotient membership. It is an auxiliary arithmetic result; no native spatial transfer is asserted.

## 3. Complete Q19 experiment (k=21 and 23)

The C++17 verifier enumerates all s,S in {-1,+1}, all 19-bit source positions, t in 1..42 and m in 0..6 with T=t+m<=46, excluding d=0. The counting units below are **candidate signed-source/quotient tuples**, not distinct modulus pairs.

| Stage | Candidate tuples |
|---|---:|
| Total nonresonant candidates | 150,651,076 |
| After Theorem 956.1 modulo-4 sieve | 46,506,920 |
| After v2(N_a)=v2(N_b)=v2(d) sieve | 11,834,665 |
| After exact integer divisibility | 1,884,076 |
| After odd Q19 domain | 33,761 |
| After true source-bit and XOR checks | 8,711 |

The dyadic checks therefore reduce candidates reaching full divisibility and range operations by a factor 150651076/11834665 = approximately 12.73, without dropping any valid witness. This is a *candidate-work reduction*, not an asserted end-to-end runtime improvement.

The valid witness counts by gap m=0..6 are [6,644,6513,1314,231,3,0]. Pair memberships by gap, excluding the one nonresonant diagonal, are [6,442,4724,839,190,3,0]. There are exactly 6203 distinct off-diagonal pairs because one pair appears in gaps 1 and 2. The output binary, serialized as sorted little-endian unsigned 64-bit pair IDs, agrees **byte for byte** with PREFIX-955's 49,624-byte off-diagonal certificate:

    SHA-256: 1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75

The existing 137274-pair whole intersection is not counted as new coverage.

## 4. Finite directional census

The independent direct-XOR Q19 certificate classification gives the following off-diagonal memberships. The only repeat is the established pair (278529,290817) in gap classes 1 and 2.

| gap m | a < b | a > b | membership total |
|---:|---:|---:|---:|
| 0 | 6 | 0 | 6 |
| 1 | 421 | 21 | 442 |
| 2 | 2127 | 2597 | 4724 |
| 3 | 10 | 829 | 839 |
| 4 | 0 | 190 | 190 |
| 5 | 0 | 3 | 3 |
| 6 | 0 | 0 | 0 |

The all-positive direction for m=4 is an **exact finite observation** for cores 21/23 in Q19; the universal proved directional statement begins at m>=5.

## 5. Independent validation and next experiment

* C++17 full determinant re-enumeration with two dyadic prefilters reproduces all source witness counts, gap masks and 6203 off-diagonal IDs. Compile with g++ -O3 -std=c++17 -Wall -Wextra -Werror.
* An independent Python direct-XOR check covers **every** odd adjacent core pair 1<=k<=2^(p-1)-3 and every pair a,b in Q_p for p=4,5,6,7, testing 23354 joint named witness combinations. Every combination passes the dyadic, parity, determinant and directional assertions.
* The established PREFIX-955 direct-XOR audit covers the full published Q19 intersection and is reused as separate historical evidence. The current new verifier reconstructs its non-diagonal binary independently.

Next discriminating direction: derive a CRT/floor-sum count of the m=2 band directly from the congruence Delta=2(a-b), with signed source footprints and actual bit predicates, and compare complete preprocessing and enumeration costs. Do not re-enumerate the existing 6203 pairs as if they were new certification, and retain the unique double-gap history. Mother objective B_fix,odd(32) in {19,20} remains open.

Historical R6 source attribution: EM-DIRECT-58C410 / MCP-31edc522830749ad8775ca012e02ef30 / RA-25432C4AAE9BF66A907F5115; these source labels alone do not prove current private authority, active CLAIM, reviewer independence, or activity write permission. Control read r6-20261120-1436-x6-control-read-01 was queued with EVENT_READ_CONTROL_BUSY during this work. Portable research Source publication is separate from native shared-task execution.
