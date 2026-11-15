# PREFIX-808 boundary extension: complete lattice-hole count at every dilation

Date: 2026-11-16. Derivation and proof: RESEARCH_DRIVER `EM-DVR-DEBB5E` (source-exposed, author-side); original named transportation/PREFIX-808 source: `EM-DIRECT-4660FF`. Predecessor and full source/TU/0–1 observer construction: [degree-two Reeve family](https://github.com/awdawmip/enterprise-math/blob/a7de25dc1b6b7bdd7bd8334be9165724e4cd37f1/research_notes/driver/2026-11-15_r6_prefix808_tu_01_readout_reeve_h_family_exact_degree2_holes.md), blob `c90b27d58545b5a2a67009759664943d1dafe293`. This note extends exactly that model, without claiming native Port/Link equivalence or independent review.

## Statement

Fix **integers** `h >= 2` and `k >= 1`. Retain the named-source polytope
[
P_h={(x_1,x_2,x_3,x_4,z_1,ldots,z_h)in[0,1]^{h+4}:
sum_{i=1}^4x_i=1,quad z_j=x_4 (1le jle h)}
]
and the 0/1 observer `W_h(x,z)=(x_2+x_4,x_3+x_4,\sum_jz_j)`.
The equality matrix of `P_h` is totally unimodular as established in the predecessor. The image
[
Q_h=W_h(P_h)=operatorname{conv}{(0,0,0),(1,0,0),(0,1,0),(1,1,h)}.
]
Put `L(x,y)=max(0,x+y-k)`, `U(x,y)=min(x,y)` for integers `0 <= x,y <= k`. Then the **entire set** of integer lattice holes in degree `k` is
[
oxed{quad
(kQ_hcapmathbb Z^3)setminus W_h(kP_hcapmathbb Z^{h+4})
={(x,y,z)inmathbb Z^3:0le x,yle k, 
hL(x,y)le zle hU(x,y), h
mid z}.quad}
	ag{1}
]
In particular, **the exact number of holes** is
[
oxed{quad H_h(k)=(h-1)inom{k+1}{3}.quad}
	ag{2}
]
The lattice-point count and the number of attainable integral source observations are therefore
[
oxed{quad
|kQ_hcapmathbb Z^3|
=inom{k+3}{3}+(h-1)inom{k+1}{3},
qquad
|W_h(kP_hcapmathbb Z^{h+4})|=inom{k+3}{3}.quad}
	ag{3}
]
Conventions: `binom(k+1,3)=0` at `k=1`. At `k=2`, (1) gives exactly `(1,1,j)` for `1<=j<=h-1`, recovering the earlier theorem.

## Proof

The four source vertices map to `v_0=(0,0,0)`, `v_1=(1,0,0)`, `v_2=(0,1,0)` and `v_3=(1,1,h)`. Every point `(x,y,z)in kQ_h` has nonnegative real coefficients `lambda_i` summing to `k`. Eliminating them gives
[
t=z/h=lambda_3,qquad
lambda_1=x-t,quad lambda_2=y-t,quad
lambda_0=k-x-y+t.
]
Thus for integer `x,y,z`, membership in `kQ_h` is **equivalent** to `0<=x,y<=k` and
[
L(x,y)le z/hle U(x,y).
	ag{4}
]
All constraints are sufficient, since the displayed four coefficients are then nonnegative and sum to `k`.

Next, the integral points of `kP_h` correspond bijectively to nonnegative integer four-tuples `(n_0,n_1,n_2,n_3)` summing to `k`: `x_i=n_i`, `z_j=n_3` in the *dilated* source. Their observations satisfy
[
x=n_1+n_3,qquad y=n_2+n_3,qquad z=hn_3.
]
Conversely, when `(x,y,z)` satisfies (4) and `h|z`, set `n_3=z/h`, `n_1=x-n_3`, `n_2=y-n_3`, `n_0=k-x-y+n_3`. These are nonnegative integers, give an exact source lift, and are uniquely determined. Hence the attainable points are **precisely** those lattice points of `kQ_h` for which `h|z`; equation (1) follows.

For a fixed integer pair `(x,y)`, the interval `[hL,hU]` contains `h(U-L)+1` integer heights, exactly `U-L+1` of which are divisible by `h`. Its hole count is therefore `(h-1)(U-L)`. Summing,
[
H_h(k)=(h-1)sum_{x=0}^ksum_{y=0}^kleft(min(x,y)-max(0,x+y-k)ight).
	ag{5}
]
To evaluate the double sum, count the integer levels `r` with `L(x,y)<r<=U(x,y)`. For `1<=r<=k-1`, write `x=r+u`, `y=r+v`; the conditions become nonnegative integers `u,v` satisfying `u+v<=k-r-1`. There are `(k-r)(k-r+1)/2` pairs. Therefore
[
sum_{x,y}(U-L)
=sum_{r=1}^{k-1}rac{(k-r)(k-r+1)}2
=inom{k+1}{3}.
]
This proves (2). Finally, the unique source tuple representation gives `binom(k+3,3)` attainable observations (weak compositions of `k` into four parts), and adding the disjoint holes yields (3). QED.

## Scope and interpretation

For every `h>=2`, the number of degree-`k` observer holes grows **cubically** in `k`: `(h-1)(k^3-k)/6`. The continuous observer image has the Ehrhart polynomial
[
|kQ_hcapmathbb Z^3|
=rac{hk^3+6k^2+(12-h)k+6}{6}.
]
The full named TU source still has exact integer decomposition, and its *attainable source-observation support* is the corresponding `k`-fold Minkowski sum. These properties coexist with the explicit missing lattice points of the continuous noncoordinate image.

Proof classification: exact symbolic proof for **all** integer `h>=2,k>=1`; no numerical experiment is used to infer the universal claim. This is a further abstract 0/1 observer boundary for PREFIX-808; applying it to native named signed-Port/Link constraints requires those concrete equations and admissible readouts.

Provenance and admission: original PREFIX-808 `EM-DIRECT-4660FF`; prior `h` degree-two family and present all-degree derivation `EM-DVR-DEBB5E`. Author-side review/exploration with shared Source exposure, not independent Native Result review. Native Result accepted: 0; formal Task completed: 0; mother objective completed: 0.
