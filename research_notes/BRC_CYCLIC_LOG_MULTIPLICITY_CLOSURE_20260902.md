# BRC Cyclic Log-Multiplicity Closure — 2026-09-02

Status: `RESEARCH CANDIDATE / EXACT ONE-STATE MULTI-LOOP STAR / NO GENERAL SCC CLAIM / NO TOOL PROMOTION`

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Baseline: `main@ed2fdcb28e7205832ad9e507eba872e1a8f1c6f5`

Parent results:

- `research_notes/BRC_WEIGHTED_MULTIPLICITY_TOWER_20260902.md`
- `research_notes/BRC_WEIGHTED_CWM_SAFE_QUOTIENT_20260902.md`
- `research_notes/BRC_WEIGHTED_PROJECTIVE_GAUGE_QUOTIENT_20260902.md`

## 0. Executive result

Finite-DAG CWM theory separates three path statistics:

```text
C = path count
W = total path mass
M = strongest path mass.
```

A recurrent branch changes their behavior qualitatively. The smallest nontrivial cyclic model is one recurrent state carrying `k>=1` distinct positive rational self-loop branches with masses

```text
q_1,...,q_k > 0.
```

Define

```text
S = sum_i q_i
Q = max_i q_i.
```

The one-step recurrent CWM carrier is

```text
A=(k,S,Q).
```

After exactly `n` loop traversals,

```text
A^n=(k^n,S^n,Q^n).
```

Thus the infinite repeated-loop closure has three different thresholds:

```text
count:       infinite for every k>=1;
total mass:  finite iff S<1;
max mass:    bounded iff Q<=1.
```

Since `Q<=S`, finite total mass implies bounded max mass, but not conversely.

In log coordinates define

```text
T = ln Q
L = ln S
Delta_loop = L-T = ln(S/Q).
```

Then

```text
L = T + Delta_loop
```

and the sum-product stability condition is

```text
S<1  iff  L<0.
```

So the multiplicity surplus `Delta_loop` directly shifts the cyclic stability boundary away from the max-plus/T12 boundary `T<=0`.

For `k` equal loops of mass `q`,

```text
S=kq,
Q=q,
Delta_loop=ln k,
```

and stability is exactly

```text
kq<1
iff
ln q + ln k < 0
iff
ln q < -ln k.
```

This gives `ln k` a second exact BRC meaning: beyond recoalescence surplus, it is the multiplicity correction to the log stability exponent of an equal recurrent branch family.

## 1. Tool-reuse resolution

### T0_BRC

- coverage verdict: `EXTEND_EXISTING_TOOL`
- reuse state: `EXTEND_EXISTING_TOOL`
- use: repeated branch/recoalescence semantics and explicit preservation of result support versus richer weighted observables.
- boundary: canonical R023 remains finite Boolean-support semantics and is not mutated.

### T12_IDEMPOTENT_PATH_CLOSURE_BELLMAN

- coverage verdict: `REUSE_EXISTING_TOOL + EXACT_SCOPE GAP`
- reuse state: `REUSE_APPLIED`
- use: max-times/max-plus coordinate and cycle-improvement interpretation.
- gap: T12 is idempotent path-envelope closure. The present total-mass coordinate is non-idempotent sum-product, where branch multiplicity can make an otherwise max-contracting recurrent family diverge.

### T6_OPERATION_SAFE_QUOTIENT

- coverage verdict: `NOT THE CURRENT OPERATOR`
- reuse state: `NOT_APPLICABLE`
- reason: the present task is closure/stability of one recurrent weighted state, not quotient construction.

### T9_HOLONOMY_COCOYCLE_GLUING

- coverage verdict: `REUSE_APPLIED AS INTERPRETIVE BOUNDARY ONLY`
- reuse state: `REUSE_APPLIED`
- use: a product of multiplicative edge factors around a loop becomes an additive closed-loop sum in log coordinates and is invariant under vertex potential reweighting.
- boundary: this note does not claim a new general holonomy theorem and does not solve multi-state cyclic closure.

No current executable non-idempotent rational sum-product star covering this exact CWM contract was found. The result is kept as a narrow research candidate.

## 2. CY-1 — exact `n`-turn CWM power law

Lift each positive self-loop mass to

```text
E_i=(1,q_i,q_i).
```

Recoalescing the `k` loop alternatives gives

```text
A = boxplus_i E_i
  = (k,S,Q).
```

One more loop traversal composes by CWM multiplication. Therefore after exactly `n` traversals,

```text
A^n=(k^n,S^n,Q^n).
```

This follows immediately from componentwise CWM multiplication, but it also has direct path meaning:

- there are `k^n` loop words of length `n`;
- the sum of their products is `(sum_i q_i)^n=S^n` by distributivity;
- the largest product uses a maximum loop at every step and equals `Q^n`.

**Status:** `PROVED`.

## 3. CY-2 — extended star classification

Consider all loop lengths `n>=0`, where `n=0` contributes the empty loop word with CWM unit `(1,1,1)`.

### Count coordinate

For every `k>=1`,

```text
sum_{n>=0} k^n = infinity.
```

There are countably infinitely many supported loop words.

Thus the finite-DAG count coordinate `C in N` must be extended or separately tagged before cyclic closure can be represented.

### Total-mass coordinate

The total loop mass is

```text
sum_{n>=0} S^n.
```

For non-negative rational `S`, this is finite exactly when

```text
S<1,
```

and then

```text
W_star = 1/(1-S).
```

If `S>=1`, the sum diverges to `+infinity`.

### Max-mass coordinate

The strongest loop-word mass is

```text
sup_{n>=0} Q^n.
```

Hence

```text
M_star = 1          if Q<=1,
M_star = +infinity  if Q>1.
```

At `Q=1`, infinitely many loop words can tie at the maximum while the maximum itself remains finite.

**Status:** `PROVED / ELEMENTARY GEOMETRIC AND MAX STAR`.

## 4. CY-3 — three cyclic phases

Because `Q<=S`, only three regimes occur for `k>=1` positive loops.

### Phase A — summable recurrence

```text
S<1.
```

Then automatically `Q<1`:

```text
C_star = infinity
W_star = 1/(1-S) < infinity
M_star = 1.
```

There are infinitely many supported recurrent paths, yet their total mass is finite.

### Phase B — multiplicity-driven divergence

```text
Q<=1<=S.
```

Then

```text
C_star = infinity
W_star = infinity
M_star = 1.
```

No single repeated path grows beyond the empty-word maximum, but the non-idempotent total diverges because too many alternatives accumulate.

This phase is invisible to a pure max-plus stability test.

### Phase C — amplifying divergence

```text
Q>1.
```

Then necessarily `S>1` and

```text
C_star = infinity
W_star = infinity
M_star = infinity.
```

At least one loop can amplify indefinitely by itself.

## 5. CY-4 — log stability decomposition

For positive `Q,S` define

```text
T = ln Q
L = ln S.
```

The finite one-step multiplicity surplus is

```text
Delta_loop = ln(S/Q).
```

Therefore

```text
L = T + Delta_loop.
```

The bounds from the finite multiplicity tower give

```text
0 <= Delta_loop <= ln k.
```

The thresholds are:

```text
max bounded      iff T<=0,
total summable   iff L<0.
```

The strictness difference at zero is real:

- `T=0` (`Q=1`) still leaves max mass bounded at `1`;
- `L=0` (`S=1`) makes the geometric total diverge.

Thus the recurrent sum-product stability margin is not the dominant-path exponent `T` but the multiplicity-corrected exponent

```text
L=T+Delta_loop.
```

## 6. CY-5 — equal-loop threshold and the role of `ln k`

For `k` equal loops of mass `q>0`:

```text
Q=q
S=kq
Delta_loop=ln k
L=ln q + ln k.
```

Hence

```text
summable recurrence
iff kq<1
iff ln q < -ln k.
```

This is exact.

Examples:

### Two loops of mass `1/4`

```text
Q=1/4
S=1/2
T=ln(1/4)
Delta_loop=ln 2
L=ln(1/2)<0.
```

The recurrent total is finite.

### Two loops of mass `3/5`

```text
Q=3/5<1
S=6/5>1.
```

Every fixed loop choice contracts, yet the total over all loop words diverges. In log form:

```text
T=ln(3/5)<0
Delta_loop=ln 2
L=ln(6/5)>0.
```

This is the minimal exact witness that branch multiplicity can overpower per-path contraction.

## 7. CY-6 — attach a finite acyclic tail

Let the recurrent state eventually exit into a finite positive-path tail with exact CWM statistics

```text
(C_0,W_0,M_0),
```

and suppose at least one loop is positive.

Every tail path may be preceded by any loop word.

In the summable regime `S<1`:

```text
C_total = infinity
W_total = W_0/(1-S)
M_total = M_0
```

because `Q<1` makes the zero-loop traversal the strongest copy of every tail path.

Define the tail effective multiplicity

```text
E_0=W_0/M_0
Delta_0=ln E_0.
```

Then

```text
E_total = E_0/(1-S)
```

and

```text
Delta_total
 = Delta_0 - ln(1-S).
```

Define the **recurrent closure surplus**

```text
Gamma(S) = -ln(1-S),   0<=S<1.
```

Then

```text
Delta_total = Delta_0 + Gamma(S).
```

So finite branch multiplicity contributes `Delta_0`, while stable recurrent reuse contributes the additional positive log surplus `Gamma(S)`.

## 8. CY-7 — exact rational BRC materialization

When all loop masses are rational, `S` is rational.

Write an exact positive representation

```text
S=N/D,
0<=N<D
```

in the summable regime. Then

```text
1/(1-S)=D/(D-N).
```

No infinite numerical summation is required.

The recurrent closure surplus is

```text
Gamma(S)=ln(D/(D-N)).
```

This is already in the input language of the merged BRC logarithm runtime:

```text
DIV(D,D-N) -> LN -> exact BRC interval materialization.
```

Thus a stable rational recurrent loop can be closed algebraically first and sent through BRC `LN` only for the requested finite-scale readout.

## 9. CY-8 — why the finite-DAG CWM carrier cannot be copied unchanged

For every positive recurrent loop family:

```text
C_star=infinity.
```

But when `S<1`, both

```text
W_star<infinity
M_star=1
```

remain finite.

Therefore the finite-DAG identity

```text
1 <= E=W/M <= C
```

still has a vacuous extended upper bound, but finite `C` no longer measures the useful recurrence intensity.

The effective multiplicity

```text
E_star=1/(1-S)
```

can be finite and non-integer even though the literal path count is countably infinite.

Hence cyclic BRC needs a typed extension such as

```text
count cardinality/tag + convergent mass coordinates
```

rather than pretending the old natural-number `C` remains a finite scalar.

No production cyclic carrier is introduced in this note.

## 10. CY-9 — relation to T12 max-plus closure

T12's max-style path envelope cares about whether a cycle can improve the dominant path. In this one-state model that threshold is

```text
Q>1.
```

Weighted BRC total mass has the stricter summability threshold

```text
S<1.
```

The gap is exactly the branch multiplicity term

```text
Delta_loop=ln(S/Q).
```

Therefore:

```text
T12 max stability      : T<=0
Weighted total stability: T+Delta_loop<0.
```

This is a precise composition of an existing T12 coordinate with the new non-idempotent multiplicity layer, not a replacement for T12.

## 11. CY-10 — gauge and closed-loop log weight

Under a vertex potential reweighting on a general directed edge

```text
w'_(u,v) = s_u * w_(u,v) / s_v,
```

products around a closed directed cycle are unchanged because the vertex scales telescope.

In log coordinates

```text
ell'_(u,v)=ell_(u,v)+g_u-g_v,
```

and the closed-loop log sum is invariant.

For a one-state self-loop the invariance is immediate: the same state scale appears in numerator and denominator, so each `q_i` itself is gauge-invariant.

This justifies calling `ln q_i` a loop log weight/holonomy coordinate in this restricted setting, while leaving general T9 holonomy theory untouched.

## 12. Critical boundary — individual contracting cycles do not guarantee sum stability

The two-loop witness

```text
q_1=q_2=3/5
```

already proves:

> “every individual loop product is below one” is insufficient for non-idempotent sum-product convergence.

Both elementary loops have negative log weight, but their branch aggregate has

```text
S=6/5>1.
```

The divergence comes from the exponential number of loop words.

Therefore a future multi-state SCC theory must not use only individual cycle signs or max-plus improving-cycle tests to certify sum convergence.

## 13. General SCC frontier

For a finite strongly connected weighted subsystem with non-negative transition matrix `A`, the natural total-mass closure candidate is

```text
I + A + A^2 + ... .
```

The expected classical convergence boundary is the spectral radius condition

```text
rho(A)<1.
```

This note does **not** promote that statement into an Enterprise BRC theorem or implement a general matrix inverse/spectral certificate.

The one-state multi-loop model corresponds to the `1x1` matrix

```text
A=[S],
```

so `rho(A)=S` and the exact theorem above is the scalar base case.

The next justified task is to determine which existing spectral/operator tools should own the finite-SCC extension and how an exact rational BRC certificate could verify the convergence boundary without floating spectral computation.

## 14. Exact checker target

The companion checker verifies:

1. exact `n`-turn CWM power law for finite loop palettes;
2. sum/max threshold classification without floating point;
3. equal-loop criterion `kq<1`;
4. multiplicity-driven divergence witness `(3/5,3/5)`;
5. exact rational closure factor `1/(1-S)` in stable cases;
6. the attached-tail formulas for `W`, `M`, and effective multiplicity;
7. BRC `LN` materialization of stable recurrent closure surplus from the exact rational factor.
