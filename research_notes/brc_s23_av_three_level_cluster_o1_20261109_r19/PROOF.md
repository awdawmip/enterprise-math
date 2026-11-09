# Three-level residue-gap theorem: O(1) exact risk correction

2026-11-09 | Enterprise Math, S23 auxiliary AV circle observer | author-side proof, independent review pending.

Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged). Predecessor: `research_notes/brc_s23_av_cluster_remainder_signed_20261109_r18/{PROOF.md,ADDENDUM_POSITIVE_GAP.md}` at `652630a5feb1afb5f629d94e0b3f6196c74aa70a`. We reuse the predecessor's exact Bayes risk and positive-gap cluster theorem. This is an improvement to its evaluation algorithm, not a native-X6 theorem.

## Theorem (three boundary-gap values; constant-size correction)

Let `q>=1`, `gcd(p,q)=1`, `m>=q`, `n>=m`, `0<theta<1`, and `theta=p/q+epsilon`, `epsilon!=0`. For positive epsilon use `0<=p<q`; for negative epsilon allow `1<=p<=q`. Put `eta=|epsilon|`, `delta=q*eta`. Reflect the phase `theta -> 1-theta` for negative epsilon, so the positive-perturbation rational numerator is `k=p` for epsilon>0 and `k=q-p` otherwise. Define

```
h = inverse(k modulo q)   (if q>1); h=0 if q=1
n = a*q + b, 0<=b<q
z = q-h
D_j=1/q+(h-q*(a-1)-q*j)*eta,  j=0,1,2
W_j=max(0,delta-D_j)
```

Let `jmax=0` if q=1, `jmax=2` if q>1 and b>z, and `jmax=1` otherwise. The **complete positive-gap criterion** is the single exact inequality `D_jmax>0`. Assume it holds.

For `0<=x<=q` define an integer prefix count `F(x)` by the following cases, with `w=n-m` and `d=m mod q`:

```
w==0:         F(x)=0
w>=q:         F(x)=x
0<w<q, d+w<=q: F(x)=max(0,min(x,d+w)-d)
0<w<q, d+w>q:  F(x)=min(x,d+w-q)+max(0,x-d).
```

Set `t=min(w,q)`, `A=F(q)-F(z)`, `B=F(b)`, and `C=F(b)-F(z)` if `b>z` (else `C=0`). For q=1 take `A=0`. Set `c2=C`, `c1=A+B-2*C`, `c0=t-A-B+C`. These are nonnegative integers and `c0+c1+c2=t`. Then the exact optimal whole-future-block Bayes risk is

```
R_theta(m,n-m)=(n-m)*delta-c0*W_0-c1*W_1-c2*W_2.   (T)
```

After obtaining the modular inverse by Euclid in O(log q) arithmetic steps, (T), its exact applicability test, and all counts cost **O(1) arithmetic/comparison operations and O(1) big-integer words**, regardless of q or n. Exact bit complexity additionally depends on operand size and rational/interval precision; no claim of constant-time bit complexity is made. When a future observer requires residue labels, retain `(sign,k,q,h,m,n,z,b)` to reconstruct the original residue assignment. The three counts alone are sufficient for the declared scalar Bayes-risk output.

## Proof

In the predecessor's ordered-cluster model the last source index in residue r is

```
ell_r(n)=r+q*floor((n-1-r)/q)
        =r+q*(a-1+1_{r<b}).
```

The next cyclic rational-base cluster is `r_plus=(r+h) mod q`; hence `r_plus-r=h-q*1_{r>=q-h}`. Its exact boundary gap consequently is

```
G_r(n)=1/q+(r_plus-ell_r(n))*eta
      =D_{1_{r>=z}+1_{r<b}}.
```

Thus there are at most three possible gap sizes even for arbitrary large q. For q>1 the indicator sets are the integer intervals `[z,q)` and `[0,b)`; both hold exactly when `b>z`. When they do not overlap, the first is nonempty. This proves `max_r(indicator sum)=jmax`. As `D_0>D_1>D_2` for eta>0, `D_jmax>0` is equivalent to positivity of every nominal cluster gap, certifying the predecessor's exact circular order.

The indicator `E_r(n)=1` exactly when one of `m,...,n-1` is congruent to r modulo q. If w>=q every residue is active; if w<q, active residues are a cyclic interval of w consecutive residues starting at d. The number of active residues in `[0,x)` is exactly F(x) in every displayed case. Inclusion-exclusion therefore gives the number of active residues on which `1_{r>=z}+1_{r<b}` equals 2, 1, 0 respectively as `c2=C`, `c1=A+B-2*C`, `c0=t-A-B+C`.

Substitute the resulting counts and the three gap values into the predecessor's proved identity

```
R_theta(m,n-m)
=(n-m)*delta-sum_{r=0}^{q-1} E_r(n)*max(0,delta-G_r(n)).
```

The sum becomes `c0*W_0+c1*W_1+c2*W_2`, yielding (T). Phase reflection preserves lengths and the old/new arc refinement relation, so the formula also holds for negative epsilon. The q=1 case has no modular inverse and a single cluster and is covered by h=0. QED.

## Exact finite tests and frozen S23 endpoint

`VERIFY_THREE_LEVEL_CLUSTER.py` checks the formula against two independent arithmetic formulations: explicit q-residue-loop risk and exact sorted circular phase subdivision (Fractions only). Actual `RUN_EVIDENCE.txt` shows 304 sampled rational cases, 11,252 extra positive-gap cases beyond `n*eta<1/q`, and 11,556 exact circle-partition equalities. All q,m,n,sign and interval comparisons use exact integers/Fractions.

The prior strictly certified S23 enclosure is

```
262204504569236716045286/10^24 < theta
 <262204504569236716045287/10^24.
```

For `p/q=16/61`, `m=128`, negative epsilon, we have `k=45,h=19,z=42`. At each `128<=n<=225`, the test (C) passes at both endpoints and the same exact branch gives

```
R(128,n-128)=(n-128)*(16-61*theta), 128<=n<=164;
R(128,n-128)=36*(16-61*theta)+(n-164)*(164*theta-43), 165<=n<=225.
```

In particular `R(128,97)=-2047+7808*theta`. At n=226 the positive-gap condition fails, in agreement with r18's separate first-crossing lemma; continuation requires the adjacent-swap carrier.

This is a general exact theorem for the scalar rational-cluster observer under its explicit ordering condition. The S23 enclosure is inherited, not rederived here. Shared-task CLAIM, independent proof review, Result/Review and native X6 transfer remain separate.
