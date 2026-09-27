# Local hits of the aggregate determinant's extra sections

Status: **PURE_SYMBOLIC_DERIVATION / NOT_EXECUTED / NOT_ADMITTED**. Shared author context `EM-DIRECT-C6438C`, activity `RA-CAAAC604CB513AEA8BBC1DFC`. This note uses no scientific run, host numerical grid, external provider or remote write. It concerns the unstopped modular aggregate in `AGGREGATE_WITNESS_PROBE_AUDIT.md`, SHA-256 `c76465057ce793825916c3d22c85acc83703becfeb5154c05b362468dd5933fd`, read in full. Its moment determinant is distinct from RP8's signed-mode frame/Gram norm observer.

The useful conclusions are precise. The additional one-layer roots are exactly a quadratic section, which is either empty or has two simple roots over each prime field. At a general fixed horizon, a low-degree root bound limits uniform-random-base hits. There is also an exact odd-local-order family in which the determinant becomes a public-base exponent test. None of these statements excludes large-horizon or guided selection; they identify the missing selection mechanism.

## 1. Polynomial separation before interpreting geometry

Let `a` be a unit modulo an odd `N`, `Q=2^t`, `t>=1`, and `A=a^Q`. The primes below are proof variables, not supplied factors. Write

`G=G_Q(a)`, `H=G_Q(a^2)`, `G_m(X)=sum_(j=0..m-1) X^j`,

`D_minus=QH-G^2`, `D_plus=QH+G^2`,

`C=a^(-2(Q-1)) D_minus D_plus`.

Define the integer polynomials

`F_minus=Q(a-1)(a^Q+1)-(a+1)(a^Q-1)`,

`F_plus =Q(a-1)(a^Q+1)+(a+1)(a^Q-1)`.

Because Q is even,

`J=G_(Q/2)(a^2)`, `G=(a+1)J`, `H=(a^Q+1)J`.

Also define, by exact polynomial division in `Z[a]`,

`B_minus=F_minus/(a-1)^3`, `B_plus=F_plus/(a-1)`.

These are polynomials, including at a=1: this notation does not authorize modular division by a-1. For F_minus, its value and first two formal derivatives at 1 vanish over the integers; division by the monic `(a-1)^3` therefore leaves an integer polynomial. F_plus vanishes at 1. Direct substitution now gives

`D_minus=J(a-1)^2 B_minus`, `D_plus=J B_plus`,

`C_tilde := a^(2(Q-1)) C = J^2 (a-1)^2 B_minus B_plus`.       (1)

Thus there are three distinguishable local sources: the nontrivial dyadic-order roots in J, the trivial a=1 root, and the two extra-section polynomials B_minus/B_plus. Repeated powers also distinguish prime support from valuation. For `p^e || N`, the gcd exponent of C is

`min(e, 2 v_p(J) + 2 v_p(a-1) + v_p(B_minus) + v_p(B_plus))`,  (2)

with the usual infinity convention. Saturation from the displayed squares is algebraic multiplicity; it is not evidence that a full branch observer was retained or corrupted.

This yields a practical algebraic simplification, not a new success theorem. If a-1 and a+1 have paid unit certificates, the division-free identity

`(a-1)^4(a+1)^2 C = a^(-2(Q-1))(A-1)^2 F_minus F_plus`

shows that separate probes `A-1, F_minus, F_plus` have, in union, exactly C's prime support. Maintaining just `A=a^Q` and `q=Q mod N`, with the fixed a, permits their direct evaluation by typed squaring and polynomial operations. Individual unsquared gcds need not equal gcd(C,N) at prime powers. To claim the same entire gcd value, the product must retain `(A-1)^2 F_minus F_plus` and its multiplicities. Separate probes can reveal a proper factor hidden by product saturation, but can also all fail.

## 2. Cayley interpretation and its exact domain

At a prime p where `a+1` and `A+1` are nonzero, put

`x=(a-1)/(a+1)`, `y=(A-1)/(A+1)`.

Then `F_minus=0` is `y=Qx`, and `F_plus=0` is `y=-Qx`. Conic powering in this chart is the rational map

`y = ((1+x)^Q-(1-x)^Q) / ((1+x)^Q+(1-x)^Q)`.       (3)

The minus section is tangent to this map at x=0: the map is odd and its linear coefficient there is Q, so the difference begins at degree at least three. This explains the forced `(a-1)^3` factor; it does not produce many distinct roots. Exceptional characteristics can raise multiplicity further.

For any nontrivial extra root with `a!=1,-1`, `A+1` is automatically nonzero: if A=-1, F_minus and F_plus reduce to nonzero multiples of `2(a+1)`. Nevertheless an implementation modulo composite N cannot silently invert chart denominators. It must check them or use the polynomial probes, which already avoid that inversion.

Equation (3) is an interpretation of an evaluated probe. Solving its intersection over an unknown prime factor, or selecting a base concentrated on its roots, is a separate algorithmic task. The chart grants neither operation.

## 3. A finite-Q root bound valid in every odd characteristic

The expansions are

`F_minus=(Q-1)a^(Q+1)-(Q+1)a^Q+(Q+1)a-(Q-1)`,

`F_plus =(Q+1)a^(Q+1)-(Q-1)a^Q+(Q-1)a-(Q+1)`.

For Q>=2 the four exponents are distinct. No odd prime divides both Q-1 and Q+1. Consequently neither F polynomial, and hence neither B polynomial, is identically zero after reduction modulo an odd p. Their degrees are at most

`deg B_minus <= Q-2`, `deg B_plus <= Q`.

A nonzero degree-d polynomial over a field has at most d roots, by repeated division by distinct linear factors. Therefore the union of the two extra root sets has at most `2Q-2` elements, including any exceptional-characteristic overlaps or roots at a=1. This is an upper bound, not a promise of that many roots.

The roots of J in `F_p^*` are exactly the Q-th roots of unity other than 1 and -1. At either excluded point J equals `Q/2`, which is nonzero. Their number is `gcd(Q,p-1)-2`: this follows equivalently by taking the polynomial gcd of `X^Q-1` and `X^(p-1)-1`; all these roots are simple since p does not divide Q. From (1), the number `Z_p(Q)` of unit residues at which C vanishes obeys

`Z_p(Q) <= min(p-1, 2Q+gcd(Q,p-1)-3) <= min(p-1, 3Q-3)`.  (4)

At a=-1 the determinant is `Q^4`, so that point never contributes at an odd prime. The bound may overcount other overlapping roots. The separate F root sets cannot intersect away from a=1,-1: adding and subtracting their equations would force both A+1 and A-1 to vanish.

For a uniformly sampled unit modulo N, reduction modulo any p dividing N is uniform on `F_p^*`. A proper gcd from this C probe requires a local zero at some prime. Thus, for a fixed, predeclared Q,

`Pr(proper factor from C) <= min(1, sum_(p|N) (3Q-3)/(p-1))`.  (5)

This needs no independence assumption and is only an upper bound. It remains valid for prime powers, where local vanishing need not give a proper divisor because of saturation. The probability is over the ideal specified uniform-unit input law; an actual sampler, nonunit prechecks and their receipts have not been implemented here.

For a fixed list of horizons, the corresponding bounds add by a union bound, even if the same random base is reused. For every horizon `1<=t<=T`, the coarse numerator is `3(2^(T+1)-2-T)`. One must not apply this calculation after conditioning on acceptance of a base-selection rule; such conditioning can change the distribution. A fixed candidate list can be charged before selection, but an unrestricted adaptive search is outside this bound.

In particular, polynomially many uniform trials whose Q values and total degree are polynomial in log N have negligible hit probability on inputs with a bounded number of prime factors each comparable to a positive power of N. This does **not** constrain all short recurrences: Q can be exponentially large in t, while evaluating A and q still takes O(t) ring operations. At such horizons (4) can be wholly uninformative. A high-degree compact formula is allowed; it still needs a proved root-density and component-separation mechanism.

## 4. One layer: exact extra-hit and failure classes

For Q=2, `J=B_minus=1`, and

`C=(a-1)^2 B_plus/a^2`, `B_plus=3a^2+2a+3`.

For p>3,

`B_plus=0 <=> (3a+1)^2=-8`,

or, in the allowed Cayley chart,

`B_plus/(a+1)^2 = x^2+2 = 0`.                      (6)

If -2 is a nonsquare in `F_p`, **no extra root exists at all**. If -2 is a square, there are exactly two extra roots. Both are units, neither is 1 or -1, and they are simple: the discriminant is -32, nonzero at every odd p. In the latter case they form a reciprocal pair, as the polynomial has equal nonzero leading and constant coefficients.

Consequently C has exactly one unit root when -2 is a nonsquare and exactly three when -2 is a square. A uniform unit has local C-hit probability respectively `1/(p-1)` or `3/(p-1)`. The extra section alone has probability 0 or `2/(p-1)`. If a!=1 is already guaranteed locally, the nonsquare case is a strict one-layer failure for every remaining base. No distributional guess or asymptotic argument is involved.

The simple extra roots each lift uniquely from `p^j` to `p^(j+1)`: writing a lift as `a+p^j h`, its next polynomial residue is affine in h with nonzero derivative coefficient modulo p. This proves the usual one-step lifting assertion directly. Valuation can therefore be checked separately from root support; a root modulo p is not automatically a root modulo all powers of p.

For an illustrative exact probability statement, let `N=pq` be squarefree, with distinct p,q>3. Set `e_p=1` if -2 is a square modulo p and 0 otherwise, and `rho_p=(1+2e_p)/(p-1)`. CRT makes the reductions of a uniform unit independent. Then

`Pr(1<gcd(C,N)<N) = rho_p(1-rho_q)+rho_q(1-rho_p)`.

For the separated polynomial probe B_plus, replace rho_p by `2e_p/(p-1)`. These are exact statements for this declared distribution, not factorization guarantees or measured frequencies. They also show why a hand-picked successful example does not establish useful success on large unknown factors.

## 5. A second exact failure family: odd-order endpoint resonance

Let a have odd order r>1 modulo an odd prime p, with r used only in the proof. If `Q=1 or -1 mod r`, complete periods in each geometric sum cancel. For any nontrivial x of order dividing r,

`G_Q(x)G_Q(x^-1)=1`.

For Q=1 mod r the two residual sums are 1. For Q=-1 mod r they are `-x^-1` and `-x`, respectively. Both x=a and x=a^2 are nontrivial because r is odd. Hence

`M_1=M_2=1`, `C=Q^2-1 mod p`.                     (7)

In particular, when r=3 this holds at every dyadic horizon. The aggregate zero is then exactly `4^t=1 mod p`, a characteristic-dependent exponent resonance, rather than discovery of the local order 3. It is impossible whenever `p>Q^2-1`. At horizons satisfying the congruence it does hit p, subject to separation from the other prime-power components before a proper factor can be reported.

This gives a concrete local mechanism with a strict failure range. It neither inputs r to the algorithm nor supplies a factor-blind way to arrange the required resonance. It also prevents interpreting all determinant zeros as either old dyadic-order hits or successful old individual branches.

## 6. What a useful next tool must certify

The immediate reusable component is small and exact: a typed recurrence for A,q and separated, division-free probes; or the G,H recurrence when exact multiplicity/valuation reconstruction is wanted. A result must retain the selected horizon/base, all typed construction and gcd costs, and either a verified proper divisor or an honest unit/saturated/incomplete outcome. This is **REUSE/DOMAIN EXTENSION** of the existing algebraic recurrence and marked-section viewpoint. It is not a new name for a root solver or a native Cell compression.

The unsolved component is a **factor-blind section-selection rule with a separation certificate**. A useful, testable interface would specify:

1. How bases/horizons or a fixed family of lawful sections are chosen using only N and already paid native observations, without unknown prime/order inputs.
2. A proved probability or deterministic bound for one component's section value to vanish while the total gcd remains proper. Local root density alone does not prove this; simultaneous hits can saturate.
3. The complete cost of preparing that selection law, evaluating its compact high-degree sections, gcd probes, failed probes and restarts. Conditional success on a postselected base must not be reported as unconditional success.

For a family of predeclared nonzero low-degree sections evaluated at a uniform base, the sum-of-degrees root bound is a readily checkable barrier to any claimed density amplification. A viable improvement must therefore justify a substantially different base law, a high-degree family with genuinely proved useful root density/separation, or an adaptive native observation that earns the selection information. Merely changing to Cayley or HBW coordinates provides none of these by itself.

There is a useful implementation distinction: probing the separated factors can avoid avoidable product saturation, and the inverse-free A,q recurrence avoids reconstructing a full branch histogram. Those are actual algebraic savings once implemented and accounted. A general probability of hitting an unknown factor, an order certificate, and the native Shor endpoint remain open. No such implementation or success claim is made in this note.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
