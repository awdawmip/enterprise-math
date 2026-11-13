# R702 — Joint circulation/counterflow fibers of the V29 BRC coarse observer

Date: 2026-11-11, Asia/Shanghai. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. Author-side original derivation, independent review pending; this document claims no native CLAIM/Result or Foundation admission. Scientific pins unchanged.

## Provenance and typed carrier

Read from the connected GitHub source:
- V29: `research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md` (blob `6849ebd3fc776fb7da3b46627376490aba3dad99`).
- V39: `research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md` (blob `8151d0b6a4b65225b93d858bbc8a5d7037bf9cef`).
- R701: `research_notes/portable_direct/2026-11-11_R701_V29_counterflow_fiber_and_cycle_observer.md` at `bd3449ee630dee0cacbdedccbc7990bc55e01017`.
- Formal Task input source remains frozen; current control read separately at Source `f436c6f98609d39af5c5415f375f750410a997e2`. Historical `a72226e...` source locator remained unverified in the native immutable manifest.

For n>=3 internal ports on a ring in a single V29 Cell, let the two directed PASS counts on the i-th ring edge be nonnegative integers v_i=M[i,i+1] and w_i=M[i+1,i]; all other M entries are zero. These are positive BRC path/token multiplicities, not signed probability masses. Define signed derived contrast omega_i=v_i-w_i, coarse local divergence u_i=omega_i-omega_{i-1}, and total internal PASS count P=sum_i(v_i+w_i). This result addresses the observer (u,P) and full *count* ledger recovery, not arbitrary event order, path labels, source frames or native Link/Port realizability. For matched V29 TRANSFERs, first compute internal u=u_observed-Rin+Rout using the exact boundary counts; TRANSFER leaves P and M unchanged.

## Theorem 1 — exact joint fiber for all n>=3

Let u be an n-component integer vector and P an integer. If P<0 or sum u != 0, no ledger exists. Otherwise set b_0=0 and b_i=sum_{j=1}^i u_j for 1<=i<n. Define

```
A(k)=sum_i |b_i+k|
K(u,P)={k in Z : A(k)<=P and P-A(k) is even}
Q(k)=(P-A(k))/2, k in K(u,P).
```

Then all nonnegative directed ledgers with observer (u,P) are *exactly* indexed by pairs (k,q) with k in K(u,P), q_i>=0 integers and sum_i q_i=Q(k). The inverse is

```
v_i=max(b_i+k,0)+q_i,
w_i=max(-(b_i+k),0)+q_i.
```

Consequently their number is

```
F_n(u,P)=sum_{k in K(u,P)} C(Q(k)+n-1,n-1).
```

For a full-M readout future, the optimal worst-case fixed-length exact repair memory, *conditional on a realizable observed (u,P)*, is ceil(log2 F_n(u,P)) bits (0 if F=1). The enumerative index (k,q) attains this.

**Proof.** u_i=omega_i-omega_{i-1} plus sum u=0 determines omega_i=b_i+k for the unique integer k=omega_0. For any signed integer omega_i the unique nonnegative decomposition with difference omega_i is v_i=max(omega_i,0)+q_i and w_i=max(-omega_i,0)+q_i, where q_i=min(v_i,w_i). The total count therefore equals P=sum |omega_i|+2 sum q_i=A(k)+2 sum q_i. This gives precisely the feasibility conditions. Each admissible (k,q) conversely constructs a ledger with the requested observer, and the representation is unique. Stars-and-bars counts the weak n-part compositions of Q; a b-bit representation can distinguish at most 2^b ledgers, while a canonical rank index distinguishes all F. QED.

The sum is finite. Since |b_i+k|<=P is necessary, its admissible k are contained in

```
max_i (-P-b_i) <= k <= min_i(P-b_i).
```

Scanning this finite interval gives a direct O(n P) integer-arithmetic operation algorithm for fixed input dimensions (bit complexity depends on integer sizes and binomial output).

## Theorem 2 — length generating function and unbounded hidden multiplicity

As a *formal* power series in t, for any fixed zero-sum u,

```
Z_u(t)=sum_{P>=0}F_n(u,P)t^P
      =(1-t^2)^(-n) * sum_{k in Z}t^(sum_i|b_i+k|).
```

**Proof.** The bijection separates an integer circulation k, whose minimal PASS cost is A(k), from n independently chosen symmetric PASS-pair counts q_i, each of cost two. The latter contribute (1-t^2)^(-n), and the former the displayed circulation sum. Each fixed coefficient is finite because A(k)->infinity as |k|->infinity. QED.

For four ports and u=(0,0,0,0), P must be even. Write P=2L. Then

```
F_4(0,2L)=C(L+3,3)+2*sum_{j=1}^{floor(L/2)}C(L-2j+3,3).
sum_{L>=0}F_4(0,2L)x^L=(1+x^2)/((1-x^2)*(1-x)^4).
```

For example F_4(0,4)=12 and F_4(0,12)=176. Expanding C(m+3,3)=m^3/6+O(m^2) and summing over j gives F_4(0,2L)=L^4/24+O(L^3), so exact worst-case extra memory grows as 4 log_2 L - log_2 24 + O(1). This is a scoped, rigorous unbounded-growth result for the declared count observer; no physical heartbeat-time equivalence is assumed.

## A five-ledger witness simultaneously hiding both residuals

With n=4, observed u=(1,-1,0,0) and P=3, b=(0,-1,-1,-1). Exactly two k are admissible: k=0 gives omega=(0,-1,-1,-1), Q=0, one ledger; k=1 gives omega=(1,0,0,0), Q=1, four ledgers distinguished by the location of the opposite PASS pair. All five have identical (u,P) but different directed M; the exact repair lower bound is ceil(log2 5)=3 bits. The difference between k-values is a lost circulation; the four q allocations at k=1 are lost symmetric counterflow locations.

## Executed exact verification and strength

An independently grouped Python integer enumeration checked *every* nonnegative 2n-arc ledger up to the stated PASS limits: n=3, P<=7: 1,716 ledgers, 511 (u,P) signatures; n=4, P<=7: 6,435 ledgers, 1,296 signatures; n=5, P<=6: 8,008 ledgers, 4,095 signatures. Totals: 16,159 ledgers and 5,902 signature-to-formula equalities, all passing `R702_JOINT_FIBER_EXACT_PASS`. Precise program and JSON certificate accompany this note. The general proofs above are algebraic; the enumeration is bounded cross-validation.

## Next science unit

Construct an *actually admissible* native X6 Link/Port, triadic active-frame and V39 based-loop event packet realizing a pair of distinct directed M ledgers with the same corrected (u,P), while preserving PASS/TRANSFER order and BRC token origins. Test whether a legal future V39 (j,h) continuation or a full ledger query distinguishes the alternatives. Distinguish the restricted V29 grammar's algebraically feasible histories from verified X6 native realizations.
