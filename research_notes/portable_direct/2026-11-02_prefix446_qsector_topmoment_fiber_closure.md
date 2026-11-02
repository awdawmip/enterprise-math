# PREFIX-446 — Sharp q-sector BRC top-moment closure and minimal linear repair

Author result, 2026-11-02 (Asia/Shanghai). Scientific input frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`; continuation of PREFIX-445 (`2756638e2568dd502f96f55fd28ead161ae09a22`). Project normative read: `main@80f47c5080f82e11f23708516aa337f3504ff261`. Account-rule read: `main@41469f7a38c888c0cba5a7324b90d92ac2664700`. Native owner/CLAIM unconfirmed (`CONTROL_QUOTA`; static read-only Site scope). This is an author-level derivation, exact computation and reproducible certificate, pending independent Review/Admission.

## Typed problem and data

Use ordered signed paths along `±e1` embedded in P000's six-axis X6 Cell torsor. Each path has length `n`, `k` negative steps, relative endpoint `x=n-2k`, and an auxiliary history-control residue `r=k mod q`, where `q>=2`. The residue is not an extra spatial axis or an asserted native physical dynamics. A finite positive rational BRC path bag has aggregated masses `c_k>=0` for `0<=k<=n`; its ordered-word provenance is retained for the unit-weight witnesses below.

Fix integer `d>=1` and the `qd+1`-coordinate linear observer `J_(q,d)`, consisting of

`T_(r,j)=sum_(k≡r mod q) c_k (n-2k)^j` for `0<=r<q, 0<=j<d`,

plus one total top-degree moment `U_d=sum_k c_k(n-2k)^d`.

A permitted typed one-step BRC kernel assigns incoming residue `r` positive rational weights `a_r` for step `+e1` (new k unchanged) and `b_r` for step `-e1` (new k=k+1); all `a_r,b_r>0`. Define `m_r=a_r+b_r`, `h_r=#{k in [0,n]:k≡r mod q}`, and `A={r:h_r>=d+1}`. Source length n is a separately typed time/step count, and all coefficients are exact rational numbers.

## Theorem 446.1 — exact rank for every length

For all integers `n>=0,q>=2,d>=1`,

`rank_Q J_(q,d)(n) = sum_(r=0)^(q-1) min(h_r,d) + 1_(A nonempty)`.

**Proof.** Within residue r, the sample points `n-2(r+qj)`, `j=0,...,h_r-1`, are pairwise distinct. The rows of powers 0 through d-1 form a Vandermonde block of rank `min(h_r,d)`. Blocks are supported on disjoint k-coordinates, so their ranks add. The extra total degree-d row is in the blockwise row span exactly when every sector has at most d support points, since `x^d` is interpolable by lower powers on at most d points and linearly independent on any d+1 distinct points. QED.

## Theorem 446.2 — necessary and sufficient one-step closure

For the fixed tuple `(n,q,d,a,b)`, the entire next observer `J_(q,d)(n+1)` is uniquely determined by the current `J_(q,d)(n)` for **every** admissible positive rational bag if and only if

`m_r = m_s` for all `r,s in A`.

At n<=qd, A contains at most one residue, so this holds for every positive kernel. At `n=qd+1`, residues 0 and 1 first become jointly active. At `n>=qd+q-1`, all residues are active, and closure requires equality of all outgoing total masses. For a kernel family with equal m across all q residues, the same observer closes under arbitrary finite serial compositions and positive parallel alternatives.

**Proof.** Put `V_r=sum_(k≡r) c_k x^d`; the source retains only `sum_r V_r=U_d`. For j<d, the output sector moments are exactly

`T'_(s,j)=sum_(t=0)^j binom(j,t) [a_s T_(s,t)+(-1)^(j-t) b_(s-1) T_(s-1,t)]`

with residue subscripts modulo q. Binomial expansion of the full degree d gives

`U'_d=sum_r m_r V_r + sum_r sum_(t=0)^(d-1) binom(d,t) [a_r+(-1)^(d-t)b_r]T_(r,t)`.

For `h_r<=d`, Vandermonde inversion of the retained lower sector moments uniquely determines `V_r`. For `h_r>=d+1`, the signed coefficient vector `(-1)^j binom(d,j)`, placed on any d+1 consecutive sector sample points, fixes all lower sector moments and changes `V_r` by `(2q)^d d!`. Independent sector perturbations combined with the retained U constraint yield precisely the ambiguity space `{(ΔV_r)_(r in A):sum ΔV_r=0}`. Signed rational perturbations can be embedded in pairs of nonnegative rational BRC bags around a strictly positive baseline. Therefore `U'_d` is constant on each observer fiber exactly when the vector `(m_r)_(r in A)` annihilates this hyperplane, i.e., is constant over A. All lower updated coordinates are already determined. QED.

## Theorem 446.3 — sharp linear repair and exact unit-weight path witnesses

At **fixed** length n, exactly `max(|A|-1,0)` independent additional linear moment coordinates are necessary and sufficient to recover the next declared observer for the full family of positive rational residue-conditioned kernels. Save the degree-d sector moments V of all but one active residue; the missing value follows from U and the inactive sector moments (recoverable from lower degrees). Necessity follows from the `|A|-1`-dimensional ambiguity hyperplane and arbitrary positive mass vectors m separating all its nonzero directions.

For a **uniform all-length** port the sharp linear-moment repair uses `q-1` extra coordinates, yielding `q(d+1)` scalars `J+ = (T_(r,j))_(r<q,j<=d)`. Its exact update is the preceding binomial formula also for j=d. It is closed under arbitrary positive rational serial kernels and positive parallel alternatives. At `n>=qd+q-1`, every sector is active, so q-1 is necessary even at one step. Minimality here is *within linear moment ports extending J* and counts coordinates, not bits, nonlinear codes or complete provenance.

An explicit pair of **unit-weight, distinct ordered native-path bags** exists for every `n>=qd+1`, with exactly `2^d` paths in each. At `k=r+qj` for r=0,1 and j=0,...,d, define the signed difference `Δc_(r+qj)=(-1)^(r+j)binom(d,j)`, putting positive coefficients into bag A and negative ones (absolute value) into bag B. The finite-difference identity annihilates each sector's degrees <d; the two degree-d differences are `((2q)^d d!, -(2q)^d d!,0,...)`, so the global degree-d moment also matches. Each bag has `2^d` words. At base length `n0=qd+1`, there are `binom(n0,k)>=binom(d,j)` ordered ±e1 words with the required k (choose j of d designated positions and k-j of the remaining n0-d). At any larger n append common positive steps, retaining unique paths and k. Under a kernel with m0 unequal m1, the next global top-degree observation differs by exactly `(2q)^d d! (m0-m1)`. QED.

## New concrete q=3 quadratic example

For q=3,d=2,n=7, the four-path bags are A=(0,6,4,4) and B=(3,3,1,7) in negative-step-count notation. Their common seven coordinates are

`J_(3,2)(A)=J_(3,2)(B)=(2,2; 2,-2; 0,0; 76)`.

Their sector top-degree moment differences are `(72,-72,0)`. With positive rational kernel `a=(2/3,1/2,4/5)` and `b=(3/5,1/3,7/10)`,

`U'_2(A)-U'_2(B)=72(19/15-5/6)=156/5`.

At n=7, the exact additional-coordinate requirement is 1; at n=8 it is 2. The all-length q=3,d=2 port has 9 exact rational coordinates, compared with the n+1 count locations in the complete endpoint distribution. Full input representation, provenance, integer numerator and denominator bit lengths, and serialized metadata remain separate resource costs.

## Execution, scope, and next work

The author expanded exact program `prefix446_qsector_closure_certificate.py` (local complete evidence pack) actually imported the unchanged pinned X6 `signed_brc.py` after confirming Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Its verbatim log recorded 117 rational rank checks, 351 observer factorization checks, 45 unit-ordered-word witnesses, 246 source BRC endpoint-capacity checks, 126 arbitrary rational full-sector updates, and exact q3 output `156/5`; all PASS. The repository companion compact checker independently executed with output `PASS: rank 117 one-step closure 351 unit path witnesses 45 q3-example 156/5`. The displayed universal results rest on the proofs above, with bounded exact tests corroborating implementation.

**Direct upstream runtime test pending:** the pinned original `ControlPacket`, `EffectHistogram`, and `MomentState` classes have been source-reviewed but were not imported in this execution environment. Next PREFIX-447: version-match the real upstream package, inject the q=3 four-path witness with typed control residues, run `from_edges/then/alternatives/evaluate/moment_action`, exhibit the failing or preserving state quotient and extend the minimal typed moment port, followed by actual bit and time resource measurements. This result concerns an auxiliary legal X6 path and BRC observer calculus; native heartbeat field dynamics and independent admission remain open.

**Research status:** AUTHOR_PROVED / EXACT_CHECKED / PROJECT_SOURCE_PUBLICATION (verify commit and remote readback separately) / UNREVIEWED / NOT_ADMITTED. GitHub login `awdawmip`; native Researcher-ID/Owner/CLAIM unconfirmed under static read-only Site permissions and `CONTROL_QUOTA`.
