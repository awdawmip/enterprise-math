# R5 — exact small-t extension on the common seedless chart C_(301/400)

Date: 2026-11-08. Research status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**.

## Exact question and frozen source

Continue the seven-node P/Q-BRC *statistical terminal-observer* research from [PR #1808](https://github.com/awdawmip/enterprise-math/pull/1808) and [PR #1803](https://github.com/awdawmip/enterprise-math/pull/1803). The predecessor's declared scientific pins are global `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`; their scientific content is not rebased to today's main. The present calculation uses the exact seven-node affine observer formulas embedded in `VERIFY.py` and the predecessor program at immutable commit `1605721551f0151dabe00709cda45c994dd81ed9`. P000, ACTIVE worldview and native Heartbeat claims remain unchanged. The preservation claim is restricted to the four declared P/Q terminal observers; this paper computes no native Heartbeat propagation, Shor arithmetic, physical residual, or classical π reference.

## New theorem: a four-parameter continuous prism

Let `t,p,q,theta` be arbitrary **real** numbers satisfying

```
1/1000 <= t <= 1/100;   0 <= p <= 1;   0 <= q <= 1;
3/4 <= theta <= 1;       kappa = 3/4.
```

Define the lawful FULL_HIST flow

```
x(t,p,q,theta) = (g,a,b,u,v,w,z)
g=1, a=t, b=1,
u=(13t/40+1/80)*p,
w=(3t/40+21/80)*q,
z=t*theta/10,
v=z+27/160.
```

For each such source there is a lawful seedless LR target

```
y=(g',a',b',u',v',w',z'),
z'=(301/400)*a'/10,
v'-z'=(301/400)*9b'/40,
```

and a nonnegative, declaration-independent 7×7 Blackwell transfer `Q` which preserves **all seven likelihood-ratio terminal declarations under both P and Q**, as well as the two stopping-time expectations `T_P,T_Q`. Thus `(e_P,e_Q,T_P,T_Q)` agrees exactly for any randomized seven-node terminal declaration. The same claim holds along every source-to-target convex interpolant `(1-h)x+hy`, `0<=h<=1`.

The new lower endpoint `1/1000` is one tenth of the earlier positive-residual prism's `1/100`, and both physical capacities `p,q` remain fully free.

## Self-contained observer and transfer equations

The likelihood ratios are

```
r = (1/10, 1/2, 3/4, 1, 5/4, 3/2, 19/10).
```

For `f=(g,a,b,u,v,w,z)`, the seven Q masses are:

```
M0 = 509u/900 + 47z/180 + 67(v-z)/162 + w/100
M1 = 13a/40 + b/80 - u
M2 = (g-a)/2
M3 = 1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
M4 = (g-b)/2
M5 = 3a/40+21b/80-w
M6 = u/100+47z/180+67(v-z)/162+509w/900.
T_P = 1+g+3a/8+5b/8+u/2+v+3w/2
T_Q = 1+g+(a+b)/2+u+v+w.
```

`VERIFY.py` checks each entry and both normalizations `sum(M)=sum(r*M)=1`, as well as nonnegative physical capacities and the seedless relation `9b'z'=4a'(v'-z')`.

Writing `Q_ij` for the P/Q transfer **from target node i to source node j**, the required equations are

```
sum_j Q_ij = M_i(y),                         i=0,...,6;
sum_i Q_ij = M_j(x),                         j=0,...,6;
sum_i r_i Q_ij = r_j M_j(x),                 j=0,...,6;
T_P(y)=T_P(x);   T_Q(y)=T_Q(x).
```

These identities imply all seven terminal-decision P and Q probabilities agree, regardless of declaration rule.

## Exact 16-vertex certificate and reconstruction

The domain has 16 vertices

```
t in {1/1000,1/100}, p in {0,1}, q in {0,1}, theta in {3/4,1}.
```

For every vertex, `CERTIFICATES.json` stores only the sparse transfer support `s` (edge `(i,j)` encoded as `7*i+j`) and a small list `f` of **exact rational** free-variable values. `VERIFY.py` deterministically reconstructs the 5 target variables and all transport coefficients via left-to-right exact Gaussian elimination with `fractions.Fraction`; no numerical optimizer or symbolic CAS is needed to verify them. The full 16 vertices have **163 strictly positive** transfer entries in aggregate. The stored free values were rationally simplified and then checked against all exact equations and inequality constraints; their derivation began with LP support search, which is *not* used as proof.

At the common chart `C=301/400`, the target coordinates `z'=Ca'/10` and `v'-z'=9Cb'/40` are linear in target state. Hence every target `y_e` lies in the same affine seedless chart, which is closed under convex mixtures.

Let

```
s=(t-1/1000)/(1/100-1/1000),  d=4(theta-3/4).
W_{ijkl}=s^i(1-s)^(1-i) p^j(1-p)^(1-j)
         q^k(1-q)^(1-k) d^l(1-d)^(1-l),
i,j,k,l in {0,1}.
```

Every weight is nonnegative and their sum equals one. The source is multi-affine in `t,p,q,theta`, so `x=sum_e W_e*x_e` exactly. Set `y=sum_e W_e*y_e` and `Q=sum_e W_e*Q_e`. Chart equations, transfer equations, expected times, mass nonnegativity, bounds `0<=a',b'<=g'<=1` and both physical side-capacity inequalities persist under this convex combination. This proves the theorem for **every real parameter**, including irrational values and endpoints.

For the interpolant `x_h=(1-h)x+hy`, use `Q_h=(1-h)Q+h*diag(M(y))`, preserving the same observer vector.

## Exact verification and limitations

Run in this directory: `python3 VERIFY.py`. The author executed a locally equivalent, fully explicit Python `Fraction` checker against the 16 published sparse supports and free variables; its actual output was:

```
EXACT_16_CORNER_CERTIFICATES_PASS 163
EXACT_257_INTERIOR_REGRESSION_PASS
ALL_REAL_C301_400_T_1_1000_TO_1_100_PRISM_AUTHOR_PROVED
```

The 257 interior samples are an implementation regression; the all-real proof rests on the exact 16-vertex certificates plus the preceding multi-affine argument. The independently read-back remote `VERIFY.py` was constructed by changing exactly the chart, `t` endpoints, fixture name and messages in predecessor `VERIFY_SUPPORT.py`; remote publication and local execution must be distinguished. The full checker and the exact output record are published in this directory. Re-running the remote script provides an independent executable check of the same model equations and certificate data.

**Connection to preceding author-side results:** PR #1808 proves `t in [1/100,1/5]`, `theta in [3/4,1]`, `p,q in [0,1]` at `kappa=3/4`. Their union with this theorem extends the **positive-residual-side prism** to `1/1000<=t<=1/5`; combining PR #1803 also covers `theta in [0,3/4]` on that slab. These remain author-side results until independent project review/admission.

## Next scientific unit

Test `0<t<1/1000` on a **t-dependent seedless chart** `C(t)=3/4+lambda t`, starting with `p=0,q=1,theta=1`, and derive an exact rational-function transfer with a small positive interval where every coefficient is nonnegative. The fixed-chart 16-vertex technique can certify a slab `[t_0,t_1]` whenever all 16 corner certificates share the same chart; continue descending with overlap, or establish a direct analytic bridge at `t=0`. Evaluate variable `kappa` only after this local route is assessed. The entire FULL_HIST-to-seedless mother question remains open.

## Provenance and authority

Research activity and actual current native session are evaluated separately. GitHub author transport uses the authenticated `awdawmip` identity, but branch publication grants no formal Task CLAIM/Result/Review, theorem acceptance, or native Heartbeat law. Exact GitHub immutable SHA and Source registration, if available, are to be supplied by the durable commit/receipt, not invented here.
