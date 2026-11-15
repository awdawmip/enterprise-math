# BRC N=4 / S23: exact inverse conditioning of two-source observer mixtures

**Research date:** 2026-11-01. **Classification:** AUTHOR_ANALYTIC_PROOF; exact integer verification executed; UNREVIEWED / NOT_ADMITTED. This result belongs to the frozen six-source/four-stop S23 finite statistical observer model. P000 X6 and separate-time native transfer is an independent obligation.

## Frozen source model and the previously proved anchor

Retain the exact eleven causal controls and six labelled source/observer matrix from PR #1765, commit `38c85f7354d2addabbb0d60511bb6bc9e9f480ec`, `research_notes/brc_n4_s23_unique_chebyshev_anchor_20261101_research1/PROOF.md`. For each source,
[
F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
]
Prepared rows (p_i=sum_{x=0}^5M_{ix}F_x), with
[
20M=egin{pmatrix}
10&10&0&0&0&0\9&11&0&0&0&0\
0&0&20&0&0&0\0&0&0&10&10&0\
0&0&0&2&18&0\0&0&0&0&0&20
end{pmatrix}.
]
The positive BRC observer retains source identities (AU0,AU1,AV,BU0,BU1,BV) prior to readout. The old full-cube prepared-law Chebyshev anchor is
[
z_*=(a_A,a_B;b_U,b_{AV},b_{BV};c_{AU0},c_{AU1},c_{AV},c_{BU0},c_{BU1},c_{BV})
=(1/4,1/4;1/3,1/3,1/3;1/2,1/2,1/2,1/2,1/2,1/2).
]
Let (r(z)=sup_{	hetain[0,1]^{11}}max_i operatorname{TV}(p_i(	heta),p_i(z))).

## Lemma 1: exact full-cube radius for EVERY proposed anchor

For every legal real-valued policy anchor (z),
[
oxed{r(z)=1-min_{0le i<6, 1le jle4}p_i(z)_j.}	ag{1}
]
Proof. The original S23 model admits four globally feasible policies making all six prepared rows simultaneously (e_j), one for each stop (j). Thus (r(z)gemax_{i,j}operatorname{TV}(e_j,p_i(z))=1-min_{i,j}p_i(z)_j). Conversely, for ANY probability law (P=sum_jP_j e_j) and fixed (q), convexity of TV in its first argument gives (operatorname{TV}(P,q)lesum_jP_joperatorname{TV}(e_j,q)le 1-min_jq_j). Apply this to every legal prepared row. The equality uses feasible global atoms, not a finite-grid interpolation. QED.

## Theorem 2: exactly conditioned four-control S23 face

Freeze the two first-stage controls at (1/4), all three second-stage controls at (1/3), and the AV/BV third-stage controls at (1/2). Vary the four remaining third-stage controls as
[
c_{AU0}=1/2+u,quad c_{AU1}=1/2+v,quad
c_{BU0}=1/2+w,quad c_{BU1}=1/2+x,
qquad u,v,w,xin[-1/2,1/2].
]
Set
[
A=egin{pmatrix}1/2&1/2\9/20&11/20end{pmatrix},
quad B=egin{pmatrix}1/2&1/2\1/10&9/10end{pmatrix}.
]
On this entire real four-dimensional lawful face,
[
oxed{r(z(u,v,w,x))-rac34=
rac12max{|A(u,v)^T|_infty,|B(w,x)^T|_infty}.}	ag{2}
]
Proof. Every source has stop-1 and stop-2 masses (1/4). Its last two masses are (1/4+t/2) and (1/4-t/2), where (t) is its signed third-stage displacement. Mixing by the four declared AU/BU observer rows gives, respectively, stop-3 deviations
[
(u+v)/4,quad(9u+11v)/40,quad(w+x)/4,quad(w+9x)/20.
]
Stop-4 deviations have the opposite signs. AV and BV are uniform. Hence the smallest prepared probability is precisely (1/4) minus the largest absolute deviation. Substitute into (1). QED.

## Theorem 3: exact SHARP inverse-condition constants

For the lawful face above write (delta=r(z)-3/4). Then
[
oxed{max(|u|,|v|)le 42delta,qquad
max(|w|,|x|)le7delta.}	ag{3}
]
Each constant is individually optimal; no smaller constant works uniformly in any neighborhood of the anchor. Consequently the complete four-control inverse bound is (max(|u|,|v|,|w|,|x|)le42delta), with sharp constant 42.

Proof. The exact inverses are
[
A^{-1}=egin{pmatrix}11&-10\-9&10end{pmatrix},quad
B^{-1}=egin{pmatrix}9/4&-5/4\-1/4&5/4end{pmatrix}.
]
Their induced infinity norms are (|A^{-1}|_infty=21) and (|B^{-1}|_infty=7/2). Equation (2) gives the bounds immediately. Sharp AU witness: choose (t>0), (u=21t,v=-19t,w=x=0), with (tle1/42); then (A(u,v)^T=(t,-t)^T), (delta=t/2), and (|u|/delta=42). For (t=1/84), the exact control offsets are ((u,v)=(1/4,-19/84)) and (r=127/168). Sharp BU witness: (w=(7/2)t,x=-(3/2)t,u=v=0), (0<tle1/7). Then (B(w,x)^T=(t,-t)^T), (delta=t/2), and (|w|/delta=7). For (t=1/14), the exact offsets are ((w,x)=(1/4,-3/28)), (r=11/14). All third-stage controls remain in [0,1]. QED.

## Theorem 4: general two-source BRC identifiability threshold

Suppose a single positive-weight two-source BRC observer pair consists of mean weights ((1/2,1/2)) and a second observer ((lambda,1-lambda)), (0lelambdale1), with the same frozen survival mass (1/2). Put
[
A_lambda=egin{pmatrix}1/2&1/2\lambda&1-lambdaend{pmatrix},
qquad
delta_lambda=	frac12|A_lambda(u,v)^T|_infty.
]
If (lambda
e1/2), its exact best inverse constant is
[
oxed{sup_{(u,v)
e(0,0)}
rac{max(|u|,|v|)}{delta_lambda}
=rac{2(1+2max{lambda,1-lambda})}{|1-2lambda|}.}	ag{4}
]
The supremum remains sharp under the bounded lawful controls (u,vin[-1/2,1/2]), because any norm extremizing direction can be scaled arbitrarily close to zero. This follows from
[
A_lambda^{-1}=rac1{1-2lambda}
egin{pmatrix}2(1-lambda)&-1\-2lambda&1end{pmatrix}
]
and the exact (ell_infty) matrix operator norm (maximum absolute row sum). At (lambda=1/2) the vector ((t,-t)), (t
e0), is invisible to BOTH pooled observers: the inverse constant is infinite, and source identity is not recoverable from that readout.

For the frozen AU observers (lambda=9/20), (4) equals 42. For BU (lambda=1/10), it equals 7: the AU pair is six times more poorly conditioned in this precise risk-to-control sense.

## Explicit information-erasure witness

Take (u=1/4,v=-1/4,w=x=0). The mean AU row (i=0) remains exactly uniform, as do rows (i=2,3,4,5), yet row (i=1) acquires stop-3/4 deviations (mp1/80), and the FULL observer's radius increases from (3/4) to (61/80). Dropping the second AU row therefore makes two different lawful source-labelled states observationally indistinguishable on the retained rows while the original declared observer distinguishes them. Under an observer set that excludes row 1, such a quotient cannot be asserted future-safe without an explicit future-operation preservation certificate. This is a concrete finite BRC provenance/fiber-constancy failure, not a claim about signed amplitude cancellation.

## Verification, limitations, and continuity

`VERIFY.js` performs exact integer arithmetic: six source laws with denominator 1680, observer mixtures with denominator 33600, all (7^4=2401) points of a rational signed-offset grid, and the two exact sharp extremizers plus the erasure witness. It independently reconstructs the source laws and prepared mixtures, verifies (2) and (3) on that finite grid, and tests the sharp rational examples. Equations (1)–(4) hold for ALL legal real offsets by the analytic proof; the finite tests only check the encoded arithmetic and examples.

This result supplies a sharp conditioning/observer-selection certificate for one frozen four-dimensional third-stage face. It does not alter the separately studied unrestricted ten-decoder S23 minimax interval (1/2le R_{mathrm{beh}}(k,10)le2/3) for (k=4,6). Independent mathematical review, native active Owner/CLAIM/Result, and native P000 six-axis/independent-time correspondence are separate obligations.
