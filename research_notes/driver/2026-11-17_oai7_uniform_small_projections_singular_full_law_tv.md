# OAI7: uniform small signed projections versus an asymptotically singular joint residue law

Date: 2026-11-17. Scientific contribution: `EM-DVR-DEBB5E` (new total-variation/projection theorem and verification). Earlier common-bit finite construction and sharp coverage threshold: `EM-EMF6D046-5A2844`. Scope: finite auxiliary abelian signed-residue model in `RS-OAI7-028-C-20261007-6F2A81`; no physical-walk or native X6 transfer is asserted.

## Statement

Fix an odd prime `p`, `1 <= m <= p/2`, an integer `k >= 1`, and `0 < q < 1`. Put `L=p-m`, `D=p-2m`, `A={m,...,p-1} subset F_p`, and `A_1=A+m`. Sample `Y` uniformly on `A^k`, independently of one common `B ~ Bernoulli(q)`, and put `Z=Y+m B (1,...,1)` in `F_p^k`. Write `U_s` for uniform measure on `F_p^s`, and `TV` for total variation, normalized as half the L1 difference.

For any `1 <= s <= k`, any `s` *distinct* indices, and independently fixed signs at those indices, the selected signed-coordinate vector `F_S(Z)` satisfies

```text
TV(Law(F_S(Z)), U_s) <= 1 - (L/p)^s <= s*m/p.                  (1)
```

For the full unsigned vector, the exact total variation is

```text
TV(Law(Z), U_k) = 1/2 * [
  D^k * (1/L^k - 1/p^k)
  + (L^k-D^k) * ( abs(q/L^k-1/p^k) + abs((1-q)/L^k-1/p^k) )
  + (p^k - 2*L^k + D^k)/p^k
].                                                               (2)
```

In particular,

```text
TV(Law(Z), U_k) >= 1 - (2*L^k-D^k)/p^k.                          (3)
```

If `min(q,1-q) >= (L/p)^k`, equality holds in (3):

```text
TV(Law(Z), U_k) = 1 - 2*(L/p)^k + (D/p)^k.                      (4)
```

If `min(q,1-q) >= m/p`, a single signed marginal has the exact distance

```text
TV(Law(phi_(j,+)(Z)), U_1)
 = TV(Law(phi_(j,-)(Z)), U_1) = m*D/(p*L).                     (5)
```

## Asymptotic separation, including growing small projections

Let `0 < beta < 1`, `0 < tau <= 3/8` be fixed, and take primes `p -> infinity` with `m=ceil(p^(1-beta))`, `k_p=ceil((p/m)*log p)`. Choose any `q_p` in the original author's exact marginal-coverage interval

```text
[tau*(p-m)/p, 1-tau*(p-m)/p].
```

For all sufficiently large `p`, every signed coordinate meets the `(tau,beta)` coverage requirement with zero exceptional residues. Let `s_p` be *any* sequence of positive integers with `s_p*m/p -> 0` and `s_p <= k_p`. Uniformly over all signed subsets of at most `s_p` distinct indices,

```text
TV(Law(F_S(Z)), U_|S|) <= s_p*m/p -> 0,                         (6)
```

while the full law obeys

```text
TV(Law(Z), U_(k_p)) = 1 - [2*(1-m/p)^k_p - (1-2*m/p)^k_p]
                   >= 1 - 2/p -> 1.                           (7)
```

Thus the joint residue vector is asymptotically maximally distinguishable from uniform even as **every signed projection of cardinality o(p/m)** tends to uniform in total variation. For example, `s_p=floor(sqrt(p/m))` tends to infinity and satisfies (6). This strengthens the previous entropy/support separation by showing that *growing* collections of observed coordinates may look uniform. There is no conflict with the external coverage-transfer theorem: its exact-start conditional coverage, independent continuation trials and entropy budget remain additional hypotheses.

## Proof

Conditioned on `B=b`, the selected signed coordinates are independent uniforms on a product `C_b` of `s` sets, each of cardinality `L`. A sign reversal is a bijection on `F_p`. The exact TV distance between uniform-on-`C_b` and `U_s` equals `1-|C_b|/p^s=1-(L/p)^s`. Convexity of TV under mixing with the same uniform reference proves the first inequality of (1); Bernoulli's inequality proves the second.

The two full conditional supports `A^k` and `A_1^k` each have `L^k` points and overlap on `D^k` points. On their intersection, the mixture mass is `1/L^k`; on their two exclusive parts the masses are respectively `(1-q)/L^k` and `q/L^k`; elsewhere it is zero. Summing absolute differences from `1/p^k` proves (2), and the missing-support lower bound yields (3). If `min(q,1-q) >= (L/p)^k`, every supported atom has mass at least `1/p^k`, so TV is precisely the uniform mass outside support, proving (4).

For one coordinate the overlap has `D` residues with mass `1/L` and there are `m` residues of each exclusive type. Under `min(q,1-q)>=m/p`, the two exclusive masses are at most `1/p` and the overlap mass is at least `1/p`. Hence TV is the total positive discrepancy on the overlap, `D*(1/L-1/p)=mD/(pL)`, giving (5). Negation permutes the residues and preserves TV.

For the asymptotic statement, `m/p ->0`. The coverage interval is bounded away from 0 and 1, so eventually `min(q_p,1-q_p)>=m/p` and `>= (L/p)^k_p`, since

```text
(L/p)^k_p <= exp(-k_p*m/p) <= 1/p.
```

Equations (1) and (4) then yield (6)-(7); the strict original author's coverage threshold holds by its existing two-shift partition proof. This uses one and the same common bit across all coordinates and never inserts independent coordinate-specific shifts.

## Sharp projection-scale transition (further theorem)

The scale `s ~ p/m` is the precise window where signed projections cease to be close to uniform. Fix `0<q<1`; along primes with `m/p -> 0`, take a sequence of projection sizes `s=s_p` such that

```text
s_p * m/p -> c,   0 <= c < infinity.
```

For *every* selection of `s_p` distinct signed coordinates, the TV distance has a limit independent of the selected indices and signs:

```text
a = exp(-c)
lim TV(Law(F_S(Z)), U_s)
  = (1-a)/2 * (1 + abs(q-a) + abs((1-q)-a)).                  (8)
```

The signed projections are related by coordinate permutations/sign inversions to the same `s`-coordinate common-shift law, so the exact formula (2) with `k=s` applies. Set `a_p=(L/p)^s`, `d_p=(D/p)^s`. Formula (2) becomes

```text
TV_s = 1/2 * [ d_p*(1/a_p - 1)
            + (a_p-d_p)*(abs(q/a_p-1)+abs((1-q)/a_p-1))
            + 1-2*a_p+d_p ].
```

Since `log(1-x)=-x+O(x^2)`, the hypotheses imply `a_p -> exp(-c)=a` and `d_p -> exp(-2c)=a^2`. Substitution and algebra give (8). At `c=0`, its continuous value is zero, consistent with (1).

For the fair common bit `q=1/2`, (8) has the explicit critical profile

```text
TV_limit(c) =
    exp(-c)*(1-exp(-c)),  if 0 <= c <= log(2);
    (1-exp(-c))^2,        if c >= log(2).                     (9)
```

Thus, for every fixed `c>0`, a projection of `s ~ c*p/m` coordinates remains separated from uniform by a strictly positive amount, whereas projections with `s=o(p/m)` converge to uniform. For `s*m/p -> infinity`, the missing-support bound (3) implies `TV_s -> 1`, since `(L/p)^s <= exp(-s*m/p)`. The full scale transition is consequently `o(p/m)` (uniform), `Theta(p/m)` (nontrivial TV limit), and `omega(p/m)` (asymptotically singular), for fixed `0<q<1`.

Independent numerical substitution of the *finite exact formula* against (9):

```text
c             limiting TV    p=101,m=11    p=1009,m=32    p=10007,m=101
0.25          0.172270123    0.158691063    0.174117366    0.173373922
log(2)        0.250000000    0.228412555    0.252285850    0.251638985
2.00          0.747645072    0.761045464    0.753539344    0.749273090
```

Here `s` was the nearest integer to `c*p/m`. These finite checks illustrate convergence; (8)-(9) follow from the exact probability partition, not a numerical fit.

## Independent exact-arithmetic checks

With the author's `p=101, m=11, k=2, q=135/404`, exact rational enumeration gives

```text
support cardinality   = 9959
missing vectors       = 242
TV(one signed coord)  = 869/9090       = 0.095599559956...
TV(full two-vector)   = 13112341/82628100 = 0.158691...
missing-support TV LB = 242/10201
```

The same independent enumerator produced `TV_1=13/70, TV_2=404/1225` for `(p,m,k,q)=(7,2,2,1/4)`. Here `q<m/p`, so (5) correctly does not apply; the general formula (2) does. The checks use exact `fractions.Fraction` masses before decimal presentation.

Reproduction sketch (small finite cases):

```python
from fractions import Fraction as F
from itertools import product
def exact_tv(p,m,k,q):
    A=range(m,p); out={}; n=p**k
    for b in (0,1):
        for y in product(A,repeat=k):
            z=tuple((v+b*m)%p for v in y)
            out[z]=out.get(z,F(0))+(1-q,q)[b]/(p-m)**k
    assert sum(out.values())==1
    t=F(1,2)*(sum(abs(v-F(1,n)) for v in out.values())+F(n-len(out),n))
    return t,len(out)
assert exact_tv(101,11,2,F(135,404))==(F(13112341,82628100),9959)
assert exact_tv(7,2,2,F(1,4))==(F(404,1225),41)
```

## Status, provenance and next question

This is a source-level Driver mathematical increment and author-side GitHub evidence, **not** a native independent review of the Driver's own theorem. No new Task/CLAIM/Result/DA or parent objective closure is inferred. The external Gaussian-walk schedule has an exact checkpoint-dependent continuation law; its conditional coverage and common-information hypotheses must be checked in that model before any transfer. Any native X6 claim further requires typed carrier, Link/Port and ordered-provenance preservation.

- Original finite construction: [author's fixed source](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md).
- Original exact two-shift threshold: [author's cost proof](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_BERNOULLI_SHIFT_COST_20261117.md).
- Previous Driver entropy/support/correlation theorem: [fixed source](https://github.com/awdawmip/enterprise-math/blob/3d910584e27af5cb94db8390c7eccbe74624dc95/research_notes/driver/2026-11-17_oai7_shared_bit_joint_entropy_support_and_correlation.md).
- External theorem under comparison: [fixed coverage transfer source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex).
