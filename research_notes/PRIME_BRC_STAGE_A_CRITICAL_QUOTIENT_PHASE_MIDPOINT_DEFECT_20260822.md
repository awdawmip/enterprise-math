# Prime-BRC Stage A — Critical Quotient Phase / Midpoint-Defect Checkpoint

Status: `ACTIVE RESEARCH CHECKPOINT / L3 BRIDGE / NOT CANONICAL`  
Date: `2026-08-22`  
Researcher-ID: `EM-PRIMEBRC-7F3A21`  
Owner branch: `research/prime-brc-stage-a`  
Base seen: `main@74cacc89ec09a8af7dd7ff01c10f2baf082daf81`

## 0. Claim discipline

This checkpoint does **not** prove Legendre's conjecture.

It records a new owner-local bridge between:

- the canonical P017 consecutive-square carry machinery;
- P017 least-factor/cofactor-window and high-band results;
- canonical P018 floor-quotient path flattening;
- the pure-algebra BRC signed-collapse/residual route.

Classical ingredients remain classical. Historical novelty of the combined
Prime-BRC packaging is unverified.

The strongest new theorem-level content in this checkpoint is elementary exact
integer arithmetic. The global phase-capacity inequality introduced below is a
`CONJECTURE / COMPUTATIONAL DIAGNOSTIC`, not a theorem.

---

## 1. Square-basin BRC frame and the unit defect

Fix `k>=2` and write

\[
L=k^2,
\qquad
M=k(k+1),
\qquad
U=(k+1)^2,
\qquad
G=U-L=2k+1.
\]

Then

\[
\boxed{2M-L-U=-1.}
\]

This is the exact integer defect behind the fact that the real midpoint of the
two square boundaries is `M+1/2` rather than an integer.

For the centered mirror pair

\[
n_-=M-r,
\qquad
n_+=M+r,
\qquad 1\le r<k,
\]

the lower-square offsets are

\[
x_-=k-r,
\qquad
x_+=k+r.
\]

Using the pure-algebra BRC endpoint-collapse bit `b in {0,1}` and signed
residual

\[
\rho(n,b)=n-(L+Gb),
\]

any complementary mirror bits satisfy

\[
\boxed{b_-+b_+=1\Longrightarrow \rho_-+\rho_+=-1.}
\]

For the inward orientation `(b_-,b_+)=(0,1)`, putting `a=k-r`,

\[
\boxed{(\rho_-,\rho_+)=(a,-a-1).}
\]

This is a pure-algebra identity. No primality assumption is used.

---

## 2. PB-A1 — Ternary midpoint-defect closure under floor quotient

For an integer triple `L<=M<=U`, define

\[
\Delta(L,M,U)=2M-L-U.
\]

Suppose

\[
\Delta\in\{-1,0,+1\}.
\]

For `d>=2`, write

\[
L=d\ell+a,
\qquad
M=dm+b,
\qquad
U=du+c,
\qquad 0\le a,b,c<d.
\]

After floor quotienting,

\[
\Delta'
=2\left\lfloor\frac Md\right\rfloor
-\left\lfloor\frac Ld\right\rfloor
-\left\lfloor\frac Ud\right\rfloor.
\]

Exact remainder expansion gives

\[
\boxed{d\Delta'=\Delta+a+c-2b.}
\]

The right side lies strictly inside `(-2d,2d)` and is divisible by `d`.
Therefore

\[
\boxed{\Delta'\in\{-1,0,+1\}.}
\]

So the unit/zero midpoint-defect class is exactly closed under every floor
quotient.

### Path flattening

For positive divisors `d_1,...,d_m`,

\[
Q_{d_m}\circ\cdots\circ Q_{d_1}=Q_D,
\qquad D=\prod_i d_i,
\]

where `Q_d(x)=floor(x/d)`.

Hence the **final** ternary defect after a multiplicative quotient path depends
only on total divisor `D`, not on its factorization order.

This supplies a lawful BRC recoalescence readout for multiplicative paths.

### Mandatory no-resurrection correction

The ternary value alone is **not** an autonomous Markov state.

Small exact counterexample, both starting at defect `-1` and quotienting by `2`:

\[
(0,0,1)\mapsto(0,0,0),
\qquad -1\mapsto0,
\]

while

\[
(0,1,3)\mapsto(0,0,1),
\qquad -1\mapsto-1.
\]

Therefore the correct statement is

\[
\boxed{
\text{ternary closed defect readout + path-independent final readout},
}
\]

not a self-contained three-state automaton. Residue/carry context is required
for future prediction.

---

## 3. PB-A2 — Exact quotient phase and strict discrete lead

For an interval `L<n<U` and a divisor `d>=2` of `n`, define

\[
A_d=\left\lfloor\frac Ld\right\rfloor,
\qquad
B_d=\left\lfloor\frac Ud\right\rfloor,
\qquad
w_d=B_d-A_d,
\]

and the exact quotient index

\[
m_d(n)=\frac nd-A_d.
\]

Define the quotient phase

\[
\boxed{
\Theta_d^{[L,U]}(n)=\frac{m_d(n)}{w_d}.
}
\]

Let

\[
r_d=L\bmod d,
\qquad
s_d=U\bmod d,
\qquad
x=n-L,
\qquad
G=U-L.
\]

Then

\[
dm_d=x+r_d,
\qquad
dw_d=G+r_d-s_d.
\]

Therefore

\[
\boxed{
\Theta_d(n)-\frac{x}{G}
=
\frac{r_d(G-x)+s_dx}
{G(G+r_d-s_d)}.
}
\]

For strict interior `n` and `d>=2`, the numerator is positive: the two endpoint
remainders cannot both vanish because consecutive square endpoints are coprime.
Hence

\[
\boxed{
\Theta_d(n)>\frac{n-L}{U-L}.
}
\]

The integer quotient phase strictly leads the continuous linear position.

### Phase path flattening

If `d_1|n`, `d_2|(n/d_1)`, and the interval is quotient-transported at each
step, then

\[
\boxed{
\Theta_{d_1d_2}^{[L,U]}(n)
=
\Theta_{d_2}^{[\lfloor L/d_1\rfloor,\lfloor U/d_1\rfloor]}
(n/d_1).
}
\]

This follows from floor-division associativity. It extends to arbitrary finite
true divisor paths.

Thus quotient phase is another lawful recoalescence readout at the total-divisor
level.

---

## 4. PB-A3 — Mirror quotient-phase crossing

Return to the square frame and an anchor-surviving mirror pair

\[
n_-=M-r,
\qquad
n_+=M+r.
\]

Let `p|n_-` and `q|n_+` be visible divisors transverse to `M`. For prime-factor
use, anchor survival gives this transversality automatically.

Write

\[
m_p=\frac{n_-}{p}-\left\lfloor\frac Lp\right\rfloor,
\qquad
u_p=\left\lfloor\frac Up\right\rfloor-\frac{n_-}{p},
\]

and similarly `m_q,nu_q` on the upper side. Then `m_p+nu_p=w_p` and
`m_q+nu_q=w_q`.

Exact endpoint arithmetic gives

\[
\boxed{
p m_p-q\nu_q=(L\bmod p)+(U\bmod q)-1\ge1,}
\]

and symmetrically

\[
\boxed{
q m_q-p\nu_p=(L\bmod q)+(U\bmod p)-1\ge1.
}
\]

Multiplying the strict inequalities yields

\[
\boxed{m_pm_q>\nu_p\nu_q.}
\]

Since

\[
\Theta_p=\frac{m_p}{w_p},
\qquad
1-\Theta_p=\frac{\nu_p}{w_p},
\]

this is equivalent to

\[
\boxed{
\Theta_p(n_-)+\Theta_q(n_+)>1.
}
\]

The crossing is exact and divisor-choice independent within the transverse
visible-divisor language.

A quantized margin follows:

\[
\boxed{
\Theta_p+\Theta_q-1
=
\frac{m_pm_q-\nu_p\nu_q}{w_pw_q}
\ge\frac1{w_pw_q}.
}
\]

This is the square-basin critical replacement candidate for a generic Type-II
strip at the exact exponent `theta=1/2`.

---

## 5. PB-A4 — Midpoint defect chi and the one-bit critical event

Specialize PB-A1 to the square triple and define

\[
\boxed{
\chi_d(k)
=2\left\lfloor\frac Md\right\rfloor
-\left\lfloor\frac Ld\right\rfloor
-\left\lfloor\frac Ud\right\rfloor.
}
\]

PB-A1 gives

\[
\boxed{\chi_d(k)\in\{-1,0,+1\}.}
\]

Interpret

\[
D_d^-=\left\lfloor\frac Md\right\rfloor-\left\lfloor\frac Ld\right\rfloor,
\qquad
D_d^+=\left\lfloor\frac Ud\right\rfloor-\left\lfloor\frac Md\right\rfloor.
\]

Then

\[
\boxed{\chi_d=D_d^- -D_d^+.}
\]

So `chi=+1` says the shorter lower half receives exactly one more d-lattice
hit than the adjacent upper half; `chi=-1` is the opposite orientation; `chi=0`
is balanced.

### Lower mirror half-window bias

Suppose `p|M-r` with `p` transverse. Let the lower quotient phase have integer
index `m_p` and width `w_p`. Then

\[
2m_p-w_p
=
\frac{(L\bmod p)+(U\bmod p)-(2r+1)}{p}.
\]

If the lower phase crosses the half-window,

\[
2m_p-w_p>0,
\]

the positive integer cannot exceed one because the endpoint-remainder sum is
strictly below `2p`. Therefore

\[
\boxed{2m_p-w_p=1.}
\]

Consequences:

\[
\boxed{p\ge2r+3,}
\qquad
\boxed{w_p\text{ odd},}
\qquad
\boxed{\Theta_p(M-r)=\frac12+\frac1{2w_p}.}
\]

Thus an anomalous lower half-crossing is **one exact carry bit**, not an
unbounded phase excursion.

Moreover, `p>r` implies

\[
M-r=p\left\lfloor\frac Mp\right\rfloor.
\]

Hence a true least-factor one-bit event at prime `p` survives precisely when

\[
\left\lfloor\frac Mp\right\rfloor
\]

is `p`-rough.

---

## 6. PB-A5 — Exact bridge to canonical P017 centered square carry

Canonical P017 defines, with

\[
t=k\bmod p,
\qquad
a=t(t+1)\bmod p,
\]

the centered square carry

\[
\kappa_p
=
\mathbf1[a<t]
+
\mathbf1[a\ge p-t].
\]

For a transverse prime `p`, define

\[
b_-:=\mathbf1[a<t],
\qquad
b_+:=\mathbf1[a\ge p-t].
\]

The midpoint-defect calculation gives

\[
\boxed{\chi_p=b_- -b_+.}
\]

Therefore

\[
\boxed{
\kappa_p=b_-+b_+,
\qquad
\chi_p=b_- -b_+,
}
\]

and exactly

\[
\boxed{
b_-=(\kappa_p+\chi_p)/2,}
\qquad
\boxed{
b_+=(\kappa_p-\chi_p)/2.}
\]

This is the key Prime-BRC bridge:

- canonical P017 carry `kappa` is the **unsigned total** of the two boundary
  carry bits;
- Prime-BRC midpoint defect `chi` is their **signed orientation/polarization**.

For transverse primes:

\[
\chi=+1\iff(b_-,b_+)=(1,0),
\]

\[
\chi=-1\iff(b_-,b_+)=(0,1),
\]

while `chi=0` leaves `(0,0)` versus `(1,1)` distinguished by `kappa`.

So `(kappa,chi)` exactly recovers the two directional carry bits.

This is not a replacement for the canonical carry route; it is a signed
refinement of it.

---

## 7. PB-A6 — Radial factor-depth phase diagram for positive midpoint carries

If a lower least-factor event is positive, PB-A4 gives

\[
p\ge2r+3.
\]

Therefore:

### P3 shell

If

\[
(2r+3)^2\ge2k,
\]

then `p^2>=2k`, so canonical P017 L032 applies and

\[
\boxed{\Omega(M-r)\le3.}
\]

### P2 shell

If

\[
(2r+3)^3>(k+1)^2-1,
\]

then `p^3` exceeds the square-basin upper interior bound. Since the state is
composite,

\[
\boxed{M-r\text{ is semiprime}.}
\]

Thus positive midpoint-carry composites decompose radially into

\[
\boxed{
\text{central }O(\sqrt{k})\text{ kernel}
\to P_3\text{ shell}
\to P_2\text{ outer shell}.
}
\]

The final semiprime-only transition occurs near radius `~(1/2)k^(2/3)`.

This is a theorem-level consequence of PB-A4 plus already-canonical P017
factor-depth bounds.

---

## 8. Cube-root parity core and pair-provenance injectivity

Let

\[
U_*=U-1=(k+1)^2-1,
\qquad
z_k=\lfloor U_*^{1/3}\rfloor+1.
\]

Any `z_k`-rough composite state in the square basin can have at most two prime
factors, because three factors would give at least `z_k^3>U_*`.

Hence a `z_k`-rough state is

\[
\boxed{\text{prime or semiprime}.}
\]

If both mirror states are `z_k`-rough composite, both lie in a `P_2 x P_2`
hard core. Their least factors `p,q>=z_k` satisfy

\[
pq>k.
\]

For a fixed ordered transverse pair `(p,q)`, the mirror radius is fixed modulo
`pq` by

\[
r\equiv M\pmod p,
\qquad
r\equiv-M\pmod q.
\]

Since the allowed radius interval has length `<k<pq`, there is at most one
radius.

Therefore least-factor-pair provenance is already injective in this final
`P_2 x P_2` parity core. BRC has little further branch-recoalescence work to do
there; any final `P_2 -> P_1` step needs additional positional/bilinear
information.

---

## 9. Global quotient-phase capacity conjecture

For every composite state `n` in the square basin, let `p=spf(n)` and define

\[
F_k
=
\sum_{\substack{k^2<n<(k+1)^2\\n\text{ composite}}}
\Theta_p(n).
\]

If the basin were prime-free, every one of the `2k` interior states would be
composite. PB-A2 would then give

\[
F_k
>
\sum_{x=1}^{2k}\frac{x}{2k+1}
=k.
\]

Therefore

\[
\boxed{F_k\le k}
\]

for every `k` would imply Legendre's conjecture.

### Status

`CONJECTURE / COMPUTATIONAL DIAGNOSTIC`.

Exact finite pressure tests performed in this research session found no
counterexample through exhaustive `2<=k<=10000`; selected larger checks through
`k=10^6` also remained below capacity.

This numerical evidence is **not** a proof and may simply be another hard
re-expression of prime existence.

### Exact least-factor shell form

Writing

\[
Q_p=\left\lfloor\frac{k^2}{p}\right\rfloor,
\qquad
w_p=\left\lfloor\frac{(k+1)^2}{p}\right\rfloor-Q_p,
\]

one may reindex

\[
F_k
=
\sum_{p\le k\text{ prime}}
\frac1{w_p}
\sum_{\substack{q\in W_p(k)\\q\text{ p-rough}}}
(q-Q_p).
\]

So the conjecture is a normalized **first moment** of the exact P017 rough
cofactor windows, not an unweighted rough-number count.

---

## 10. Full-multiple phase excess is only one boundary unit per divisor

For fixed `d`, sum the strict phase lead over **all** interior multiples of `d`:

\[
E_d
=
\sum_{\substack{L<n<U\\d\mid n}}
\left(\Theta_d(n)-\frac{n-L}{G}\right).
\]

Each individual lead satisfies

\[
0<\Theta_d(n)-\frac{n-L}{G}<\frac1{w_d},
\]

and there are at most `w_d` interior multiples. Hence

\[
\boxed{0\le E_d<1.}
\]

If there is at least one interior multiple then `E_d>0`.

This is a precise form of centered-kernel cancellation: the phase reweighting
turns the `O(w_d)` raw mass of a divisor channel into an `O(1)` boundary/carry
debt.

For the least-factor shell, which is a subset of the `d=p` multiples and has
positive lead termwise, its total phase lead is also `<1` per prime shell.

This does not by itself prove the global phase-capacity conjecture; it identifies
the remaining problem as a structured sum of bounded shell discrepancies.

---

## 11. Demoted diagnostic — late-phase count

Call a composite state `late` if its least-factor phase exceeds `1/2`.

Mirror crossing implies every all-composite anchor-surviving pair has at least
one late endpoint. Finite tests found

\[
\#\{\text{late composite endpoints}\}<|S_k|
\]

through the tested range.

However this criterion hides a prime-count term. Every composite upper mirror
state automatically has phase `>1/2`, because its continuous position already
exceeds `1/2` and PB-A2 adds strict lead. Therefore

\[
\#\{\text{late endpoints}\}<|S_k|
\]

is equivalent to comparing

\[
\#\{\text{positive lower midpoint-carry composites}\}

\]

against the number of upper-side primes.

It is retained as a diagnostic, not promoted as an independent proof route.

The useful residue is the **left-hand anomaly count**, which PB-A4 reduces to
one-bit midpoint-carry least-factor events.

---

## 12. Additional structural observation — the two integer centers generate step 2

The real basin midpoint is `M+1/2`, so its two neighboring integer centers are
`M` and `M+1`.

On lower-boundary offset `x=n-L`, their reflections are

\[
J_-(x)=G-1-x,
\qquad
J_+(x)=G+1-x.
\]

Both are involutions and

\[
\boxed{J_+\circ J_-(x)=x+2,}
\qquad
\boxed{J_-\circ J_+(x)=x-2.}
\]

Thus the two unit-defect integer mirrors generate the parity-preserving
translation-by-two action on the unrestricted integer line.

This is an elementary BRC/affine structural fact, not a solution to the sieve
parity problem. Direct attempts to obtain a monotone contradiction from the two
mirror systems were negative and are not pursued as a standalone proof route.

---

## 13. External parity audit

Current external comparison reinforces the exact bottleneck.

### Short-interval prime detection

Runbo Li, `arXiv:2308.04458v8` (2025), proves primes in intervals of length
`x^0.52`. Its Type-II Lemma 4.1 requires

\[
|\alpha_1-\alpha_2|<2\theta-1.
\]

At the Legendre critical exponent `theta=1/2`, the right side is `0`, so that
generic Type-II region collapses.

This makes the exact square-basin midpoint carry a relevant object: it survives
at the critical exponent as a discrete `-1/0/+1` defect rather than a positive
continuous strip width.

### Asymptotic sieve parity lesson

Friedlander-Iwaniec's asymptotic sieve breaks the classical parity obstruction
by adding genuinely bilinear information. This supports the Prime-BRC routing
rule:

> divisor incidence / Boolean BRC alone is not enough; a successful final bridge
> must expose extra positional, bilinear, or cancellation information.

### Largest-prime-factor support

Runbo Li's 2025 working paper (not peer reviewed at posting) reports that every
sufficiently large interval `[x,x+x^(1/2)]` contains an integer with a prime
factor `>x^0.7437`.

At `x=k^2` this gives a decomposition with large prime tail `>k^1.4874` and a
remaining core `<k^0.5126`. This is structurally compatible with the Prime-BRC
strategy of routing the remaining information debt into a much smaller core,
but it does not imply primality.

### Near-equal Chen comparison

Recent working-paper results on centered Chen-type representations remain far
from the `N^(1/2)` center window relevant here (reported exponents around `0.97`
for `P_1+P_2` and `0.872` for `P_1+P_3`). The Prime-BRC mirror target is
therefore genuinely at a much sharper localization scale than current generic
near-equal Chen technology.

---

## 14. Negative results preserved

The following routes are explicitly demoted:

1. **Global root-channel uniqueness** — false; high-band cross-shell root
   collisions exist.
2. **T113 shared-offset `2^h -> h+1` compression as a new Prime-BRC theorem** —
   false novelty claim; P018 already records it.
3. **Pure `(-1)^Omega` path weighting** — rejected as Möbius/Liouville parity
   under new language.
4. **BRC-only final P2 recoalescence** — final cube-root `P2 x P2` least-factor
   pair provenance is already injective; there is little branch multiplicity
   left to collapse.
5. **Ternary defect as autonomous Markov state** — false by the exact `-1`
   counterexample in Section 2.
6. **Late-phase count as an independent proof certificate** — demoted because
   it hides upper-side prime count.
7. **Two adjacent integer mirrors alone force a contradiction** — no; their
   composition exposes parity translation but no monotone prime-free
   contradiction was found.

---

## 15. Current hard target

The strongest current route is not to expand the BRC state vocabulary further.
It is to exploit the exact signed carry refinement already obtained.

Define the positive midpoint-carry least-factor set

\[
\mathcal C_+(k)
=
\left\{
 p\le k:\ p\text{ prime},\ \chi_p(k)=1,
 \left\lfloor\frac Mp\right\rfloor\text{ is p-rough}
\right\}.
\]

Every element is one exact lower half-window carry event; its radius is

\[
r_p=M\bmod p<\frac p2,
\]

and its state is

\[
p\left\lfloor\frac Mp\right\rfloor=M-r_p.
\]

The next theorem target is:

\[
\boxed{
\text{derive a non-Möbius capacity/discrepancy bound for }\mathcal C_+(k)
\text{ using }(\kappa,\chi),
\text{ exact roughness, and quotient-path flattening.}
}
\]

Analytically, the preferred formulation is a **critical quotient-phase bilinear
bound** for the centered rough-window first moment, because the phase kernel has
only `O(1)` boundary debt per divisor channel while generic Type-II width
collapses at `theta=1/2`.

If this reduces after algebra to ordinary Buchstab/Möbius bookkeeping, it must
be demoted. The needed increment must use the signed midpoint polarization in a
way that generic one-sided sieve data does not.

---

## 16. Executable checkpoint

Owner-local exact reference code:

- `src/enterprise_math/prime_brc_phase.py`

Owner-local regressions:

- `tests/test_prime_brc_phase.py`

The reference layer covers:

- square-basin unit-defect residuals;
- ternary defect closure;
- explicit no-Markov counterexample;
- defect and quotient-phase path flattening;
- strict quotient-phase lead;
- exact mirror phase crossing;
- `(kappa,chi)` directional carry recovery;
- positive midpoint one-bit least-factor event;
- bounded global `F_k` diagnostic.

The connector environment used for this checkpoint had no local checkout, so
these newly authored repository tests were not claimed as CI-executed here.
The theorem identities were independently pressure-tested with exact integer /
rational scratch calculations before publication. CI status remains
`NOT_SNAPSHOTTED`.

---

## 17. Checkpoint verdict

Current Prime-BRC frontier:

\[
\boxed{
\text{P017 unsigned carry}
\oplus
\text{BRC signed midpoint defect}
\longrightarrow
\text{direction-resolved one-bit critical carry}
}
\]

with

\[
\boxed{
\text{multiplicative quotient paths}
\longrightarrow
\text{ternary closed, path-flat defect readout}
}
\]

and a sharply localized anomaly set whose outer radial layers are already
`P3` / `P2`.

This is a genuine structural narrowing of Prime-BRC. It is **not yet** a prime
existence proof. The next bottleneck is a critical bilinear/discrepancy bound for
the signed midpoint-carry shell.
