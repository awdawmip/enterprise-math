# PREFIX-808: all-degree lattice-hole count and exact Hilbert basis for the TU/0–1 Reeve readout

Date: 2026-11-16 (Asia/Taipei). Author-side mathematical extension by RESEARCH_DRIVER **EM-DVR-DEBB5E**, source-exposed to the preceding notes; not an independent review of this new extension. Original named-source PREFIX-808 research by **EM-DIRECT-4660FF**. Direct predecessor: `research_notes/driver/2026-11-15_r6_prefix808_tu_01_readout_reeve_h_family_exact_degree2_holes.md` at GitHub commit `a7de25dc1b6b7bdd7bd8334be9165724e4cd37f1` (blob `c90b27d58545b5a2a67009759664943d1dafe293`). Earlier TU/observer boundary notes remain separately attributed.

## Fixed model and exact result

For every integer `h >= 2`, retain the fully named integral TU source polytope

[
P_h={(x_1,x_2,x_3,x_4,z_1,ldots,z_h)in[0,1]^{h+4}:
x_1+x_2+x_3+x_4=1,quad z_j=x_4 (1le jle h)},
]

with the non-coordinate `0/1` linear readout

[
W_h(x,z)=(x_2+x_4, x_3+x_4, sum_{j=1}^h z_j).
]

Its image `Q_h=W_h(P_h)` is the Reeve tetrahedron with vertices `v_0=(0,0,0)`, `v_1=(1,0,0)`, `v_2=(0,1,0)`, and `v_3=(1,1,h)`. By `kP_h` and `kQ_h` we mean ordinary dilations by a nonnegative integer `k`. Source-attainable observations at degree `k` are `S_{h,k}=W_h(kP_h\cap\mathbb Z^{h+4})`.

**Theorem (complete all-degree defect classification).** For every `h>=2` and every integer `k>=0`,

[
(kQ_hcapmathbb Z^3)setminus S_{h,k}
=
igcup_{r=1}^{h-1} igcup_{q=0}^{k-2}
left{(q+1+a,q+1+b,qh+r): a,b,cinmathbb Z_{ge0},
 a+b+c=k-q-2ight}.
	ag{1}
]

The right side is empty for `k=0,1`. Distinct tuples `(r,q,a,b,c)` generate distinct points in (1). In particular,

[
oxed{#((kQ_hcapmathbb Z^3)setminus S_{h,k})=(h-1)inom{k+1}{3}},
qquad kge0,
	ag{2}
]

where `\binom{k+1}{3}=0` for `k<2`. Thus `|S_{h,k}|=\binom{k+3}{3}` and

[
|kQ_hcapmathbb Z^3|=inom{k+3}{3}+(h-1)inom{k+1}{3}.
	ag{3}
]

Equivalently, the lattice-hole series and Ehrhart series are, respectively,

[
sum_{kge0}#((kQ_hcapmathbb Z^3)setminus S_{h,k}),t^k
=rac{(h-1)t^2}{(1-t)^4},qquad
sum_{kge0}|kQ_hcapmathbb Z^3|t^k
=rac{1+(h-1)t^2}{(1-t)^4}.
	ag{4}
]

**Theorem (minimal Hilbert basis).** Define the graded lattice-point semigroup

[
C_h={(x,y,z,k)inmathbb Z^3	imesmathbb Z_{ge0}:
(x,y,z)in kQ_h}.
]

Its unique minimal Hilbert basis comprises precisely the four degree-one rays `(v_i,1)`, `i=0,1,2,3`, and the `h-1` degree-two elements `w_r=(1,1,r,2)`, `1\le r\le h-1`. In particular, augmenting the source readout semigroup by these precise degree-two abstract observer elements fills *all* higher-degree lattice holes. This is a semigroup-completion statement, not a claim that the added observers have integral source preimages in `P_h`.

## Proof

Write `(x,y,z)` for an integer point in `kQ_h`, and set `t=z/h`. The unique nonnegative barycentric masses relative to `v_0,v_1,v_2,v_3` are

[
lambda_3=t,qquad lambda_1=x-t,qquad lambda_2=y-t,qquad
lambda_0=k-x-y+t.
	ag{5}
]

They sum to `k`. Hence membership is **equivalent** to all four expressions in (5) being nonnegative.

For any `z\ge0`, perform unique Euclidean division `z=qh+r`, with `q\ge0` and `0\le r<h`.

When `r=0`, (5) gives four nonnegative integers
[
d=q,quad b=x-q,quad c=y-q,quad a=k+q-x-y,
]
whose sum is `k`. The point is the readout of the integer source allocation
`(x_1,x_2,x_3,x_4)=(a,b,c,d)` with all `z_j=d`. Conversely every integer source allocation has third observation coordinate divisible by `h`, so **exactly** these `r=0` lattice points are source-attainable.

When `1\le r<h`, put `\theta=r/h\in(0,1)`. The inequalities (5), using the integrality of `x,y,k,q`, become precisely
[
a=x-q-1\ge0,qquad b=y-q-1\ge0,qquad
c=k+q-x-y\ge0.
	ag{6}
]
Thus `a+b+c=k-q-2`, and the other masses are automatically nonnegative. Necessarily `0\le q\le k-2`. These are exactly the points (1), none attainable from the named integer source. For each fixed `r,q`, the nonnegative solutions `a+b+c=k-q-2` number `\binom{k-q}{2}`. Summing over `r=1,\ldots,h-1` and `q=0,\ldots,k-2` gives
[
(h-1)sum_{q=0}^{k-2}inom{k-q}{2}=(h-1)inom{k+1}{3},
]
which proves (1)–(2). The source's nonnegative integer quadruples summing to `k` number `\binom{k+3}{3}` and are readout-distinct because `z/h=x_4`, `x_2=x-x_4`, `x_3=y-x_4`; hence (3), and standard generating-function identities give (4).

For the Hilbert basis, every `r=0` point has the degree-one decomposition already obtained. Every `r>0` point with (6) has the **exact** graded decomposition
[
(x,y,z,k)
= q(v_3,1)+(1,1,r,2)+a(v_1,1)+b(v_2,1)+c(v_0,1).
	ag{7}
]
Therefore the stated elements generate `C_h`. The degree-one points are exactly the four vertices (use (1) with `k=1` and the source allocation). Every `w_r` is a degree-two hole and cannot be written as a sum of two degree-one lattice points. Thus each of `h-1` degree-two elements is indecomposable; no proper subcollection can generate `C_h`. This proves the minimal Hilbert basis.

## Verification scope and contribution boundary

As an auxiliary exact finite check, enumerated `h=2,3,4,5,6,7` and `k=1,2,\ldots,8`, comparing all lattice points of `kQ_h` against exact integer source readouts, with the counts in (2) in every case. The universal proofs above use (5)–(7), not the enumeration. No independent formal checker or Native Result review is claimed.

**Research significance.** The previous source-exposed Driver note classified exactly the `k=2` holes. The new result gives the complete degree-by-degree defect function, its Hilbert/Ehrhart series and the minimal saturation generators. For native signed-Port/Link questions, transferring these formulas requires an exact correspondence of named source equations, allowed future operations and observer fibers; abstract TU/0–1 readouts alone do not establish that correspondence.

Status: author-side proved and GitHub-published mathematical subunit; Native Result acceptance 0; formal Task completion 0; parent-objective completion 0.
