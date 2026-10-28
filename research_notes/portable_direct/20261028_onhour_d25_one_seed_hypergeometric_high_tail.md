# D25/LIFT — one-seed hypergeometric compression of the original 216 middle/high tail

Date: 2026-10-28. Research-onhour logical lane: chatgpt-research-onhour-enterprise-math-20260923.
Classification: AUTHOR-SIDE / EXACT CONDITIONAL ALGEBRAIC CONSEQUENCE / 80 EXECUTED EXACT PRIME TESTS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED.

## Frozen object and novelty boundary

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication: TP2-B6F4FC938FF94941C1B7.
Scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
P000, ACTIVE Heartbeat X6 semantics and the signed/odd port are unchanged. This is an auxiliary scalar p-adic observer, not native H0/B0 data.

Consume, without recredit: author-side endpoint identity W_p = J_p - 4 (mod p^3), commit d8dee3c159b5c991272d50e29165b357ae8718cf; and the exact indexed middle/high pairing, commit a4a706832aec5351ab7cfd36b76daef4b1ac7e28. The new unit eliminates the need to store m independent middle units in that pairing: the entire high tail is determined by ONE explicit original middle unit and a universal finite hypergeometric kernel.

For each prime p = 6m+1 > 3, work in Z_(p) and let

\[
t_n=\frac{(2n)!(3n)!}{(n!)^5 216^n},\quad
a_n=\frac{66n^2+113n+49}{9(n+1)^3}t_n,\quad
J_p=\sum_{n=0}^{p-2}a_n,\quad
W_p=\sum_{n=0}^{p-1}(6n+1)t_n.
\]

Let j_r=2m+1+r, k_r=4m-r, and u_r=(t_{j_r}/p) mod p for 0 <= r < m. Each u_r is nonzero in F_p.

## Theorem: exact one-seed transport for the high tail

Define in F_p

\[
u_0\equiv-\frac{2(4m+2)!}{((2m+1)!)^5\,216^{2m+1}}\pmod p,
\]
\[
V_r=2^r\frac{(5/3)_r^3}{(7/6)_r(1)_r(4/3)_r},
\qquad
\mathcal R(r)=\frac{9(66r^2-25r+3)}
{4(1-3r)^3(3r+2)^3},
\]
\[
S_m=\sum_{r=0}^{m-1}\mathcal R(r)V_r\pmod p.
\]

Here (x)_r is the finite rising factorial; all displayed denominators are units at the indicated index range. Then

\[
\boxed{u_r^{-1}=u_0^{-1}V_r\pmod p}
\]

termwise and, for the original nonsingular interior observer,

\[
\boxed{
J_p\equiv \sum_{n=0}^{3m}a_n+
p^2u_0^{-1}S_m\pmod{p^3}.
}
\tag{1}
\]

For the frozen target residue classes p=13,19 (mod 24), the original LIFT claim is therefore equivalent to

\[
\boxed{
\sum_{n=0}^{3m}a_n+
p^2u_0^{-1}S_m\equiv p+4\pmod{p^3}.
}
\tag{2}
\]

The new part is the explicit single-seed reduction and its universal kernel, not the endpoint/pairing lemmas already available at the cited commits. Equation (2) is an exact reduction, not an all-prime evaluation or a proof of LIFT.

### Proof

At j_0=2m+1 we have 3j_0=p+2. Wilson gives (p+2)!/p = (p+1)(p+2)(p-1)! = -2 (mod p). Substitution into the original exact factorial definition of t_{j_0} yields the displayed expression for u_0. None of the remaining factorials is divisible by p.

In the complete middle range j_r in (p/3,p/2), the original exact coefficient recurrence is

\[
\frac{t_{j+1}}{t_j}=
\frac{(2j+1)(3j+1)(3j+2)}{36(j+1)^3}.
\]

Since j_r = (p+2)/3+r, reduction of the *unit* quotients after dividing t_j by p gives

\[
\frac{u_{r+1}}{u_r}\equiv
\frac{3(6r+7)(r+1)(3r+4)}{4(3r+5)^3}
=\frac12\frac{(r+7/6)(r+1)(r+4/3)}{(r+5/3)^3}
\pmod p.
\]

Iterating the identity with initial u_0 gives u_r=u_0/V_r. This is exact in F_p for 0 <= r < m; it does not infer an unknown higher p-adic digit from a mod-p scalar.

The already proved termwise high-band identity at commit a4a7068 is
\(a_{k_r}/p^2=\mathcal R(r)u_r^{-1}\) modulo p. Substitution proves the high contribution \(p^2u_0^{-1}S_m\) modulo p^3. Original factorial valuation bands eliminate the indices n >= 4m+1 at this precision; the remaining low and middle terms are n <= 3m. Thus (1). Compose with the exact endpoint identity \(W_p=J_p-4\) modulo p^3 to obtain (2). QED.

## Observer/provenance scope (BRC COMPOSE_APPLIED)

Population: all original indexed terms (0 <= n < p) with the middle/high correspondence j_r <-> k_r. Observer: the signed scalar W_p, or J_p, modulo p^3. Allowed future operations in this compression: deterministic forward middle-index shift 0 <= r < m and high-tail accumulation modulo p^3. The sufficient carrier is (p,m,u_0), plus the explicit recurrence and rational kernel retaining every index and signed factor. Its sufficiency is PROVED by the unit recurrence and termwise reconstruction; individual middle u_r may be recomputed exactly modulo p for this declared horizon.

The compression is *not* valid for recovering middle terms modulo p^2, native H0/B0 operators, complete provenance beyond the deterministic recurrence, signed/odd Green-Hesse ports or arbitrary future operations. Those remain separate. In particular, u_0 is a scalar arithmetic source, not a claimed native Frobenius coefficient. No p-adic digit or native direction is invented.

## Executed exact checks and fixed certificate

Local standard-library Python source: research_notes/portable_direct/d25_middle_unit_seed_hypergeometric_guard_20261028.py.

Executed 80 primes p < 1000 with p=1 (mod 6), comprising 6098 individual j_r/k_r pairs. The checker independently evaluates original binomial factorial terms, the one-seed transport recurrence, high-band signed terms, the original W_p hypergeometric recurrence, and the full J/W endpoint readout; all assertions passed:

~~~text
PASS_D25_ONE_SEED_HYPERGEOMETRIC_TRANSPORT 80 primes; 6098 indexed pairs
~~~

At p=373, m=62:

\[
u_0=320,\quad S_{62}=230,\quad
u_0^{-1}S_{62}=59\pmod{373}.
\]
Thus the original high tail is \(59\cdot373^2=8208611\pmod{373^3}\).
Independently J_373=377 and W_373=373 modulo 373^3. Finite verification is an instance-level certificate, not universal evaluation of (2).

## Current boundary and continuation

Gateway em_status version 0.6.11 was read on 2026-10-28. The current Site adapter reports research_authority_granted=false and write_relay_enabled=false. An exact read-only Source continuation request returned CONTROL_QUOTA; no Source CLAIM, run, Research-Activity, formal checkpoint or Result was issued. Historical bridge Issue #6575 (recovery_status) records an ACTIVE local session pointer with no runs/claims and source_authority_verified=false; Issue #6576 ended FAILED/TimeoutExpired. Neither is current proof of winning ownership. Historical staging remains separate. No maintenance-lane identity was used.

Native support #1559 remains the unchanged highest evidence gap: original same-class H0/B0 divided-power [X]U (mod 139129), module rank, semilinear direction/eta, signed odd Green/Hesse, kappa and Delta_p-R_p, with actual native code, raw outputs and independent reproducibility. The ticket has no assigned executor at read time. Do not claim native completion from this scalar result.

NEXT SCIENTIFIC ACTION: directly evaluate the finite *single-seed* kernel S_m (or prove a character/CM relation coupling it to the low+middle sum) for both target classes; a proposed equation must be tested against p=373 and other exact inputs before promotion. Original LIFT remains open. Source registration and formal admission require current role-bound authority, receipt and independent review.