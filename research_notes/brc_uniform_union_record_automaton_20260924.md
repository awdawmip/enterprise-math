# BRC uniform-union record automaton

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note consumes the already-established per-branch port-event automaton and base-branch dominance criteria. It does not allocate a Researcher identity, does not alter formal D24/UR ownership, and does not promote portable evidence while control issue #1511 remains unresolved.

## 1. Consumed exact branch weights

For a finite exponent vector `m=(m_j)`, let

`g(j)=2j+1`,

`W_inf(m)=sum_j m_j g(j)`.

For every target prime `p == 13 or 19 (mod 24)`, the consumed port-event automaton gives an exact branch weight

`W_p(m)=sum_j m_j beta_p(j) - sum_j v_p(m_j!)`.

Write

- `E_p(j)=1` when `(p-1)/2 | j`, else `0`;
- `a_p(j)=v_p(j)`;
- for `p == 13 (mod24)`, `C_p(j)=1` on the exact source-coefficient cancellation progression and `c_p=v_p(1+4^{s_p})` there; for `p == 19 (mod24)`, `C_p(j)=0`.

Then the exact defect/gain relative to the generic observer is

`Delta_p(m) := W_inf(m)-W_p(m)`

and hence

`Delta_p(m) = sum_j m_j [E_p(j)+a_p(j)-C_p(j)(a_p(j)+c_p)] + sum_j v_p(m_j!).`

The endpoint and cancellation progressions are disjoint. Therefore every term retains its provenance: endpoint lowering, denominator lowering, cancellation raising, and factorial lowering are not collapsed before the observer is fixed.

## 2. Uniform-union weight is a record problem

Let the observer be `UNIFORM_EARLIEST_VISIBILITY`, i.e. a monomial is visible if it survives in at least one target branch or in the generic branch.

Define

`D(m)=max(0, sup_p Delta_p(m))`.

Then exactly

`W_U(m)=min(W_inf(m), inf_p W_p(m)) = W_inf(m)-D(m)`.

So the infinite branch union is reduced to a maximum-defect record problem.

### Theorem 2.1 — finite candidate reduction

Let

`J=max{j : m_j>0}` and `M=max_j m_j`.

Only target primes in

`Q(m) = {p : p<=M} union {p : p|j or (p-1)/2|j for some occupied j}`

can improve the positive record `D(m)`.

Equivalently,

`D(m)=max(0, max_{p in Q(m)} Delta_p(m))`.

### Proof

Take a target prime `p` outside `Q(m)`.

Then every occupied multiplicity is `<p`, so all factorial terms `v_p(m_j!)` vanish. Also no occupied index is a p-denominator and no occupied index is a p-endpoint. Hence the only remaining non-generic event can be source-coefficient cancellation in a `13 mod24` branch. That event enters `Delta_p` with a negative sign. Thus `Delta_p(m)<=0`, so such a branch cannot improve the generic record `0`.

The set is finite because an endpoint `(p-1)/2 | j` implies `p<=2J+1`, a denominator implies `p<=J`, and a factorial event implies `p<=M`.

## 3. Exact record automaton and novelty windows

Order the finite candidates increasingly. Before processing `p`, define

`D_<p(m)=max(0, max_{q in Q(m), q<p} Delta_q(m))`.

Then branch `p` is genuinely new for the uniform observer exactly when

`Delta_p(m) > D_<p(m)`.

If this holds, branch `p` creates exactly

`Delta_p(m)-D_<p(m)`

new integer visibility horizons, namely

`N = W_inf(m)-Delta_p(m)+1, ..., W_inf(m)-D_<p(m)`.

Afterwards update the state by

`D_<=p(m)=max(D_<p(m), Delta_p(m))`.

This is an exact finite automaton for union novelty. It distinguishes three notions that must not be conflated:

1. a branch has a local event;
2. a branch has positive defect relative to the generic branch;
3. a branch breaks the already-established union record.

Only (3) adds a new uniform visibility horizon.

## 4. Denominator singleton is uniformly novel for every target prime

Take `m=e_p`, i.e. the singleton port `j=p`.

On branch `p`, `a_p(p)=1`, there is no factorial contribution, and `p` is not its own endpoint because `(p-1)/2` does not divide `p` for target `p>3`. Hence `Delta_p(e_p)=1` (with the exact per-port automaton handling the class-13 coefficient channel).

No other target prime can match this positive defect:

- another denominator prime cannot divide the prime index `p`;
- a target endpoint would require `(q-1)/2 | p`, hence `(q-1)/2` is `1` or `p`; this gives `q=3` or `q=2p+1`;
- `q=3` is not a target prime, while for `p == 13 or 19 (mod24)`, `2p+1 == 3 or 15 (mod24)`, so `2p+1>3` is divisible by 3 and is not prime;
- factorial credit is absent for a singleton, and pure cancellation cannot create positive defect.

Therefore every target prime `p` has a uniquely sourced uniform-new denominator singleton, with

`D(e_p)=1`

and first visibility at

`N=2p+1`.

This survives all base-branch dominance reductions: higher branches are never globally redundant, because their own-denominator port gives each one an irreducible uniform event.

## 5. Primitive endpoint singleton: exact coverage criterion

Let `h_p=(p-1)/2` and consider the primitive endpoint singleton `m=e_{h_p}`. Its own branch has

`Delta_p(e_{h_p})=1`.

A smaller target prime `q<p` already covers this singleton exactly when its singleton defect is positive. By the exact cocycle this occurs iff either

- `h_q | h_p` (q-endpoint coverage), or
- `q | h_p` and the q-denominator event is not neutralized by a class-13 source-coefficient cancellation at that same port.

Thus the p-primitive endpoint is uniform-new iff no smaller target q satisfies either condition.

The criterion can produce deeper-than-one coverage. For example, `p=157` has `h_p=78`; branch `13` sees both endpoint and denominator credit there and gives defect `2`, so the p=157 primitive endpoint is already visible one full horizon earlier than its own branch would suggest.

This explains why branch-local first-entry theorems do not by themselves classify the uniform union.

## 6. Finite falsification/regression

Checker:

`research_checks/check_brc_uniform_union_record_automaton_20260924.py`

Checker publication commit:

`9aeb8232d42475777776a3a0e311f86782774551`.

Before publication, the checker was executed independently of the note formulas used for the proof. Regression summary:

- target primes `<5000`: `166` (83 in each target residue class);
- per-port raw valuation vs automaton for every target prime and `1<=j<=500`: `0` failures;
- exponent vectors with `W_inf<50`: `3264`;
- exact monomial defect identity: `0` failures;
- finite-candidate maximum vs brute target-prime maximum: `0` failures;
- record-window update rule: `0` failures;
- primitive-endpoint coverage criterion: `0` failures;
- denominator-singleton uniqueness theorem: `0` failures.

The finite primitive-endpoint census below `5000` is an observation, not a classification theorem: `28` are uniform-new and `138` are already covered by smaller target branches. The first uniform-new examples are

`13, 19, 43, 67, 139, 283, 499, 619, 643, 787, 907, 1579`.

Deep covered examples include:

- `p=157, h_p=78`, defect record `2` from branch `13`;
- `p=2029, h_p=1014`, defect record `3` from branch `13`;
- `p=3613, h_p=1806`, defect record `2` from branch `43`.

Finite computation is falsification/regression only. The proof is Theorem 2.1 plus the exact record identity and the consumed per-branch cocycle.

## 7. BRC meaning and safe quotient

For the uniform-earliest-visibility observer, branch identity may be quotiented only after comparing its exact defect with the current record. A positive local event is not enough. The minimal sufficient state for a monomial is:

- generic weight `W_inf`;
- current record defect `D`;
- record-source branch/provenance when provenance is requested;
- the finite future candidate set `Q(m)`.

For exact-per-prime support, all branches remain distinct and no union quotient is allowed.

This is a direct BRC application: observer choice determines which branch distinctions may be safely discarded, while endpoint, denominator, cancellation, factorial, and source provenance are retained until that observer is fixed.

## 8. Do not repeat / next

Do not rescan every target prime for uniform visibility of a fixed monomial. Compute `Q(m)` and run the finite record automaton.

Do not classify a branch as uniform-new merely because its own primitive endpoint or factorial event is branch-new. Compare against the earlier record.

The next nonredundant auxiliary unit, only if formal D24 control remains blocked, is to classify the escape-support families left by the base-branch dominance theorem using this record automaton: determine exact inequalities under which an own-denominator event or a base-13 cancellation fiber is sufficient to break the current union record.

If #1511 gains a deployed lossless rollover/disposition operation, stop auxiliary compiler work and resume the Source-native D24 frontier through the lawful successor identity, preserving the existing native checkpoint exactly.
