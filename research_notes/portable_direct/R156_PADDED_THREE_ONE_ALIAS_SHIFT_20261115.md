# R156 — Two-sided padding produces non-reversal aliases and an exact shifted appearance threshold

Date: 2026-11-15 (Asia/Shanghai). **Author-side mathematical proof**, exact finite corroboration; independent review: **NOT_REVIEWED**. Scope: external finite scalar tied-phase S23 mechanical-word observer, not a native Heartbeat X6 theorem. Immutable scientific input remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

Prior evidence: R146 exact open integer cuts (`b02b0c242b274bc6a82111dbd3600126a2867319`); R152B first-period finite certificate (`f6890b08b640bd8b0abea5c789e440ff63446fb2`); R155 three-one reversal alias and threshold (`38c3903967f7c54d01058ad17fb50e72a41394a2`). This note adds a two-parameter infinite extension and a genuinely non-reversal alias family.

## Model and statement

For a binary word `w=w_0...w_{m-1}`, let `s_j=∑_{i<j}w_i`. The slope support interval `(α,β)` is the intersection with `(0,1)` of the open inequalities `(q-1)/k<θ<(q+1)/k` over each nonempty contiguous factor of length `k` containing `q` ones. Write `α=a/b<β=c/d` in lowest terms and define the **absolute** integer cuts

```text
U = b (1 + min_{0<=j<=m} (s_j - jα)),
V = d max_{0<=j<=m} (s_j - jβ).
C_w(L+1) = ceil((Lc-V)/d) - floor((La-U)/b) - 1, L>=1.
```

`C_w(K)` counts integer phases strictly between those two endpoints, as established in R146.

For **every** `h>=2` and `0<=t,s<=h-1`, put

```text
W_h = 1 0^(h-1) 1 0^h 1,
A_(h,t,s) = 0^t W_h 0^s,
B_(h,t,s) = 0^t reverse(W_h) 0^s.
```

### Theorem R156.1 (two-sided padding law)

Both words are admissible Sturmian factors and, identically, have

```text
α = 1/(h+1),  β = 1/h,
U = h+1-t,    V = h-1-t.
```

In particular the cuts are **independent of the right padding s**, and the entire coefficient-indexed fiber count is shared by the two words:

```text
C_A(L+1) = C_B(L+1)
  = ceil((L-h+1+t)/h) - floor((L-h-1+t)/(h+1)) - 1
  = C_(W_h)(L+t+1),                     for every integer L>=1.
```

The last expression is evaluated at the larger coefficient `L+t+1` in the *un-padded* R155 model; this is an exact left-padding time-shift identity. The original words `A` and `B` are distinct for every `h>=2`. If `t != s`, they are **not reversals of one another**. For each `h` there are `h²` explicit distinct-word alias pairs in this construction, of which `h(h-1)` have `t!=s`.

### Theorem R156.2 (exact final absence / permanent presence)

With the same hypotheses,

```text
C_A(h²-t) = C_B(h²-t) = 0
C_A(K) = C_B(K) >= 1  for every integer K >= h²+1-t.
T(A) = T(B) = h²+1-t .
```

Here `T` denotes the smallest integer coefficient from which the word is present at every future integer coefficient. Hence right padding has no effect on `T` within the stated range; left padding by `t` moves the precise threshold left by `t`.

## Proof of R156.1

There are exactly three ones, separated by zero runs of lengths `h-1` and `h`; the initial and trailing zero runs have lengths `t,s<=h-1`. The following bounds apply to **every** contiguous factor of length `k` with `q` ones:

| q | Needed lower bound on k | Needed upper bound on k | Reason |
|---|---|---|---|
| 0 | vacuous | k<=h | Every zero run has length <=h |
| 1 | vacuous | k<=2h | For either orientation: at most t+h+1, 2h, or h+s+1, all <=2h |
| 2 | k>=h+1 | k<=3h | Smallest one-pair span is h+1; maximal two-one block lengths are t+2h+1 or 2h+1+s |
| 3 | k>=2h+2 | k<=4h | Core span is 2h+2; total length 2h+2+t+s<=4h |

Equivalently for all such factors, `(h+1)(q-1)<=k<=h(q+1)`. This proves that `(1/(h+1),1/h)` is contained in the admissible open slope interval. A consecutive pair of ones with exactly `h-1` zeros between them attains `(q-1)/k=1/(h+1)`; the run of `h` zeros attains `(q+1)/k=1/h`. Therefore **the actual exact support endpoints are** `α=1/(h+1)` and `β=1/h`, for either placement of the two internal zero gaps.

At the lower endpoint, write `X_j=s_j-j/(h+1)`. For every prefix with `q` ones, `j <= t+(h+1)q` (check the four possible values `q=0,1,2,3` from the run lengths); hence `X_j>=-t/(h+1)`, with equality at `j=t` just before the first one. Thus `U=h+1-t`.

At the upper endpoint write `Y_j=s_j-j/h`. The prefix positions with `q>=1` ones satisfy `j>=t+1+(q-1)h` for `q=1,2`, and `j>=t+2h+2` for `q=3`. Consequently `h s_j-j<=h-1-t`. Zero-one prefixes have `hs_j-j<=0<=h-1-t`. The first prefix immediately after the first one attains equality, so `V=h-1-t`. The same extremal argument applies to both arrangements of the two internal gaps.

Substitution into R146's integer-cut formula proves the common exact expression. Substituting `L+t` in the R155 baseline formula proves the shift identity. Finally,
`reverse(A_(h,t,s))=0^s reverse(W_h) 0^t`, which equals `B_(h,t,s)` exactly when `t=s`; the different positions of the middle one show that `A!=B` for all `h>=2`. QED.

## Proof of R156.2

The open interval of integer phases is

```text
I_L = ((L+t-h-1)/(h+1), (L+t-h+1)/h).
```

At `L=h²-1-t`, which is at least 1 for the whole parameter range, this interval equals `(h-2,h-1)` and contains no integer. Hence `C(h²-t)=0`.

Its length is `(L+t+h+1)/(h(h+1))`. For `L>=h²-t` this length is strictly greater than 1, so the open interval necessarily contains at least one integer. It follows that the last possible absence is exactly `K=h²-t` and the exact permanent-presence threshold is `K=h²+1-t`. QED.

## Example: a genuinely non-reversal alias

With `h=2,t=1,s=0`, the length-seven factors are `0101001` and `0100101`. Both have support `(1/3,1/2)` and cuts `(U,V)=(2,0)`. Their count sequence begins `C(2)=1,C(3)=0,C(4)=1` and is positive for all `K>=4`. Their reverse words differ from each other, giving a concrete non-reversal alias.

## Reproducible validation and scope

`R156_check.py` independently recomputes every subfactor slope bound and prefix cut using exact `Fraction` arithmetic for `h=2..14` and **all** `t,s=0..h-1` (1,014 paired configurations, including 910 non-reversal pairs). It checks 7,098 exact shift/count identities, the last absence and threshold-start cases for all 1,014 configurations, and one large coefficient `L=10^12+17` per configuration. Result `R156_PADDED_THREE_ONE_ALIASES_PASS` is captured in `R156_verification.json`. The unlimited-parameter statements above are proved algebraically; finite tests are reproducibility support, not substitutes for the proof.

## New scientific frontier

1. Find exact classification / maximal cardinality of the fibers of `w -> (α,β,U,V)` for general multi-one Sturmian factors, including **non-reversal** pairs beyond this padding construction; test whether multiplicity can exceed two.
2. Determine whether the finite-period absence bound in R152B can be sharpened globally using the structure of extremal prefix cuts; compare the exact subfamily `T=h²+1-t` with the proposed global `T(m)=(m-2)floor((m-1)/2)+1`.
3. Preserve provenance if the observer must recover the original word rather than its scalar fiber count. Any connection to native BRC/X6 requires a separately typed relation-preservation map.

**Control provenance:** independent author-side research derived from the verified R155 scientific frontier. No new formal immutable S23 Task publication or CLAIM is asserted; Activity association must be authorized and verified separately. Scientific review remains `NOT_REVIEWED`.
