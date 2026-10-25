# D25/LIFT — universal collision moments of a tangent-blind marked-source observer

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Date: 2026-10-25. Research lane: `chatgpt-research-hourly-enterprise-math-20260923` (Research, NOT CONTROL_PLANE_MAINTENANCE).
Mother D25/LIFT/JT2: OPEN. Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## Exact predecessor and the new question

Consumes without recrediting the exact tangent-blind affine-observer **individual fiber** theorem and square-residue **image count** established at immutable project commit `37c278b02a0b33e1e0f3600a4432e6e60e4916d8`, file `research_notes/portable_direct/20261025_hourly_d25_affine_blind_observer_ramified_fiber_counts.md` (and its checker). That theorem already supplies each fiber size as a square-root count. The distinct new question here is the exact *collision energy*: how many ordered q-tuples of different or identical marked inputs become indistinguishable after projecting to the same scalar observation? Compute the full finite positive-branch moment sequence and a closed second-moment formula, independent of the particular tangent-blind coefficients.

This is a theorem inside an auxiliary finite quadratic **coefficient ring**, not an authenticated CM/divided-power calculation, not an original-source kappa bridge, and not a native Enterprise-X6 geometric transfer.

## Assumptions and carrier

Let p be any odd prime, r >= 2, m = r-2, A_r = Z/p^r Z and R_r = A_r[T]/(T^2-2), with sigma(T)=-T. Choose the *marked, source-frame* unit alpha=a+bT with norm a^2-2b^2 a unit; choose u,v in A_r and the linear scalar observer f(a,b)=ua+vb. Set

    F=ua+vb,                  L=4ub+2va,

and require F a unit, L divisible by p. These are genuinely essential hypotheses; do not extend the formulas to a nonunit F or an unverified native coefficient ring.

The fixed-norm, fixed-mod-p marked disk is

    beta(t)=alpha(1+tT)/(1-tT), t in p A_r,

with N=p^(r-1)=p^(m+1) source elements. The retained observer label is the full scalar f(beta(t)) modulo p^r. By the tangent-blind condition this label equals F+p^2 y for a unique y in A_m=Z/p^m Z. Write h_y for the number of input t mapped to y. In particular, the input path/source labels are NOT quotiented merely because two y values coincide.

As proved in the exact predecessor, with ell=L/p,

    h_y=p R_m(D(y)),
    D(y)=ell^2+16F y+8p^2 y^2 mod p^m,

where R_m(d)=#{z mod p^m: z^2=d mod p^m}, and D is a bijection on A_m. For m=0 use the singleton quotient convention R_0(0)=1.

## New theorem 1: ALL finite positive collision moments

For every integer q>=1 define

    C_q = #{(t_1,...,t_q) in (pA_r)^q:
             f(beta(t_1))=...=f(beta(t_q)) mod p^r}
        = sum_{y in A_m} h_y^q.

Then, exactly and without asymptotics,

    C_q(p,r) = p^q [
         p^(q floor(m/2))
         + 2^(q-1)(p-1) *
           SUM_{e=0}^{floor((m-1)/2)}
                p^(m-2e-1+q e)
         ].

An empty sum is zero. In particular this formula holds at r=2 (m=0), where C_q=p^q. For q=1 it returns the exact input count p^(m+1).

**Proof.** Since D permutes A_m, sum_y h_y^q=p^q sum_{d mod p^m} R_m(d)^q. The unique zero square d=0 has p^floor(m/2) roots. Every nonzero square d has even valuation 2e<m and a square unit: its number of distinct possible d is (p-1)p^(m-2e-1)/2, while it has exactly 2p^e roots. Nonsquare d contribute zero. Summing the q-th powers gives precisely the displayed expression. Every counting operation is finite exact integer arithmetic; no division by a nonunit or replacement of a square-root multiset by Boolean support occurs. QED.

## New theorem 2: the universal pair collision law

For all r>=2 (m>=0),

    C_2 = p^(m+1) [p+m(p-1)].

Thus two independently uniform marked inputs have exactly

    Pr[same full tangent-blind scalar]
       = [p+m(p-1)] / p^(m+1).

The count of unordered *distinct* colliding source pairs is

    [C_2-p^(m+1)]/2
       = p^(m+1)(m+1)(p-1)/2.

**Independent proof of the pair formula (not relying on the q-moment sum).**
For m>=1, sum_d R_m(d)^2 counts ordered pairs (z,w) in A_m^2 satisfying z^2=w^2. Since p is odd the invertible coordinate change (z,w) -> (s=z-w,t=z+w) reduces the congruence to st=0 mod p^m. The case s=0 permits all p^m values of t. For each valuation e=0,...,m-1, there are (p-1)p^(m-e-1) choices for s and p^e possible t, producing (p-1)p^(m-1) pairs at each e. Therefore

    sum_d R_m(d)^2=p^m+m(p-1)p^(m-1),

and multiplication by p^2 gives C_2=p^(m+1)[p+m(p-1)]. For m=0 direct singleton counting gives C_2=p^2, the same displayed formula. This second derivation is an independent algebraic consistency check, not an independent reviewer. QED.

## Explicit BRC moment interface and information boundary

Reuse the existing verified `WBRC-T33` power-sum and `WBRC-T36` finite positive-rational histogram interface at `definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md` (current project source), **not** a proposed new BRC axiom. The explicit finite branch family here is the set of *attained observer output labels* y, each assigned the positive-integer multiplicity weight h_y (number of distinct marked input paths). Its exact histogram is

    H = SUM_{y:h_y>0} [h_y] in N[Q_{>0}^{x}].

The existing moment readout P_q(H)=sum_y h_y^q is exactly C_q. This is `REUSE_APPLIED / COMPOSE_APPLIED`: construct a typed finite histogram from the proven square-root fibers, then apply the established BRC moment character; the new algebraic identity evaluates it for this specific quadratic fiber family. Unlike support count or total count, C_2 detects multi-source collisions after irreversible observer compression. The weights are **integer source multiplicities**, not physical probability amplitudes or signed CM coefficients. Source frame, the t labels, exact coefficient ring, observer, and finite precision horizon are retained.

The compressed scalar is not a sufficient statistic for arbitrary future operations accessing the original marked pair (a,b). A genuine transverse extra source port, authenticated from the same original CM class, is still required for invertible recovery. Nor does the entropy-like collision probability automatically prove an information channel or physical model in the P000 native six-axis Cell world.

## Author exact certificates

The sibling executable `20261025_hourly_d25_blind_observer_collision_moments_check.py` enumerates every marked beta(t) via its two original finite-ring coordinates, independently enumerates all quadratic roots of D(y), compares every fiber, and checks the first FOUR moment identities plus the separate pair formula. It uses only exact modular integers; no floating point or native CM runtime.

All seven finite test cases passed:

| p,r | N marked inputs | nonempty fiber-size histogram: multiplicity -> output count | C_2 | C_3 |
| --- | ---: | --- | ---: | ---: |
| 13,2 | 13 | 13 -> 1 | 169 | 2197 |
| 13,3 | 169 | 13 -> 1; 26 -> 6 | 4225 | 107653 |
| 13,4 | 2197 | 26 -> 78; 169 -> 1 | 81289 | 6197737 |
| 13,5 | 28561 | 26 -> 1014; 169 -> 1; 338 -> 6 | 1399489 | 254335705 |
| 19,3 | 361 | 19 -> 1; 38 -> 9 | 13357 | 500707 |
| 19,4 | 6859 | 38 -> 171; 361 -> 1 | 377245 | 56428993 |
| 373,3 | 139129 | 373 -> 1; 746 -> 186 | 103651105 | 77271829213 |

For p=373,r=3, the input alpha=92060+21788T and f=302a-308b is the earlier **ordinary Hesse** marked coefficient witness, represented at a specifically declared formal lift modulo 373^3, not an authenticated CM lift. Here N=139129, 187 of the 373 potential y labels are attained, the input-fiber histogram is exactly `H=186[746]+[373]`, and

    Pr[observer collision] = 745/139129.

These are author's exact checks of a conditional abstract coefficient-ring theorem, NOT native H_0/B_0, [X]U, Frobenius, or original kappa measurements, and not independent mathematical review. The general result follows from the proof, not from the seven finite cases.

## Durable frontier and next nonrepeating unit

Current result: universal positive collision moments and a second, direct zero-product proof of the pair law. New contribution does not redo the already completed Jacobian/noninjectivity or per-fiber/image-size results.

The original D25/LIFT/JT2 hard target remains OPEN: authenticate **same prime, same original CM class** divided-power H_0/B_0 and [X]U mod p^2, determine genuine Frobenius rank, sigma direction, source normalization and lawful relation to original kappa and Delta_p-R_p. Native CM experiment NOT_RUN. No claimed current own winning CLAIM/open/run or new native Source checkpoint; portable proof is UNREVIEWED / NOT_ADMITTED and Research activity registration/identity is not asserted from historical conversations.

Research next action after authentic native observation is available: derive its source-frame scalar f or full matrix; prove whether the tangent-blind linear hypotheses really hold. If they do, apply this exact C_q/histogram formula at the *actual* p,r, and obtain a separately source-certified transverse observer before discarding fibers. If not, retain the uncompressed original data. Control recovery belongs to existing Issue #1558; do not confuse `CONTROL_QUOTA` with `NO_DISPATCH`. Preserve frozen source pin and old checkpoint, and only perform native continuation/CLAIM/OPEN/publish under fresh verified Source authority.

No acceptance, reviewer independence, additional scheduler or platform authorization is created by this portable artifact.
