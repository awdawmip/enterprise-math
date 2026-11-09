# PREFIX-625 — Exact two-generation tagged BRC path rank and minimal repair

**Date:** 2026-11-09 (Asia/Shanghai). **Status:** exact author-side mathematical certificate and executable rational verification, independent Driver mathematical review pending.

**Frozen science:** enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Native STAR/action enumerator reused from PREFIX-624 at 89c8d4689af84af95e4f1ae46c73672b8feb18b9, itself linked to PREFIX-623 at 0ccdeea6c7b5ab9d1ac833990ce6eb40d4db18a6. Current behavioral Source read at main@e0df18997688afd084be84df854af137b47bb43b and global-knowledge at main@9c21243375aa00d34494f668dc2410a092f12bca. P000 and ACTIVE worldview retained.

## Exact observation class

Use the original 48 STAR phases, 96 bit ports, 576 one-step ordered action labels (i,j,u,v), six weights (1,1,1,1,0,0), special source phase G=4, and gate-dependent weight z when j=4 and u=v=1. All other action weights are their original destination axis weights. The attached executable enumerates the 576 actions from the original native phase graph, without changing the BRC action algebra.

Let A(z) be the destination-summed original 96x96 native one-step matrix. Given any arbitrary nonnegative original predecessor port state r in R_{\ge0}^{96} and known nonnegative consecutive gates a,b, define the endpoint observer

$$
F(a,b)r = A(b)A(a)r.
$$

The full two-generation tagged path observer J_2(a,b)r has one distinct coordinate for each ordered pair of legal native actions (including first source port and intermediate port): output is the product of the two native weights times the initial source-port value. There are exactly 3,456 structural path coordinates, including zero-weight coordinates. No phase/source path quotient is imposed.

## Theorem 625.1 — two-step endpoint rank 16 for every pair of gates

For every a,b>=0 (in fact algebraically for every real a,b):

$$
\boxed{\operatorname{rank}F(a,b)=16.}
$$

This rank has a **constant, gate-independent** 16x16 minor. Its zero-based native row and column indexes are

    R = [0,2,4,6,8,10,12,14,32,34,36,38,48,50,52,54]
    C = [0,4,8,12,16,18,20,22,24,28,42,46,56,60,64,68]

and

$$
\boxed{\det F(a,b)[R,C]=-65536=-2^{16}.}
$$

**Exact universal proof certificate.** Define A_0=A(0), E=A(1)-A(0), T=A_0^2, U=A_0E and V=EA_0. Direct native enumeration establishes A(z)=A_0+zE, E^2=0 and hence F(a,b)=T+aU+bV. Put K=T[R,C]. The attached exact script checks, coordinate by coordinate over the full 96x96 native matrices,

$$
\begin{aligned}
\det K&=-65536,\\
T_{:,C}K^{-1}T_{R,:}&=T,\\
T_{:,C}K^{-1}U_{R,:}&=U,\\
V_{:,C}K^{-1}T_{R,:}&=V,\\
V_{:,C}K^{-1}U_{R,:}&=0,\\
U[R,C]&=V[R,C]=0.
\end{aligned}
$$

By multiplying out the two short factors, these finite exact coefficient identities yield the *symbolic* identity for all a,b,

$$
\boxed{F(a,b)=
(T_{:,C}+bV_{:,C})K^{-1}(T_{R,:}+aU_{R,:}).}
$$

The factorization proves rank at most 16; the nonzero fixed minor proves rank at least 16. The proof is an exhaustive finite matrix coefficient check from the immutable native action algebra, rather than an inference from sampled gate pairs.

## Theorem 625.2 — full tagged two-generation path rank 64

For all a,b>=0,

$$
\boxed{\operatorname{rank}J_2(a,b)=64.}
$$

There are exactly 64 live initial source ports and 32 silent initial source ports. At the **minimal nonnegative gates** a=b=0, exhaustive native action enumeration finds at least one strictly positive legal two-step tagged path for each of the 64 live initial source ports. Increasing either gate from zero retains these paths because the only variable weight is itself nonnegative. Paths attached to different initial sources have disjoint labelled-coordinate supports, hence the 64 nonzero input columns of J_2 are independent; its 32 silent input columns vanish.

## Theorem 625.3 — 48 additional linear precursor readouts, necessary and sufficient

Suppose one knows the complete two-step endpoint F(a,b)r, as well as a,b, and wishes to reconstruct **all 3,456 ordered tagged-path flows** for every nonnegative predecessor r. Within the class of supplementary real-linear scalar measurements of r, the exact minimum is

$$
\boxed{k_{\rm extra}(a,b)=64-16=48\qquad\text{for all }a,b\ge0.}
$$

**Necessity.** If L has m scalar rows and J_2 can be recovered from (F,L), then ker(F,L) is contained in ker J_2. Since rank J_2=64 while rank F=16, joint observation requires 16+m>=64. In the nonnegative input domain, a lost kernel direction can be added/subtracted in sufficiently small magnitude to a strictly positive 96-port input, so the same rank lower bound applies.

**Explicit fixed reconstruction.** Let D be the sorted complement of the 16 indices C among the 64 live initial ports, so |D|=48 (actual D appears in results JSON). Measure exactly r_D, and from y=F(a,b)r reconstruct the other 16 live source coordinates by

$$
\boxed{r_C=K^{-1}\left(y_R-F(a,b)[R,D]r_D\right).}
$$

Because the same K=F(a,b)[R,C] for every gate pair, this *single* fixed supplementary port set works for all a,b>=0. Now compute each original path weight w_1(a)w_2(b)r_p with its complete two-generation label. Silent precursor port values are unnecessary. This completes the sharp upper bound. In contrast, the full-domain single-generation PREFIX-624 repair depends on whether z=1 (32 extra) or z!=1 (31 extra); two generations have 48 extra independent measurements uniformly.

## Reproducible exact certificate

Run PREFIX625_native_two_generation_path_checker.py with Python 3 and SymPy. It independently rebuilds the original 48-phase STAR graph and 576 typed native actions, checks E^2=0, the -65536 gate-independent minor and all four 96x96 symbolic factorization coefficient identities, and exhaustively verifies a positive two-step path from every live port at gates zero. It then reconstructs all live predecessor values, 96 terminal coordinates and 3,456 two-generation labelled-path coordinates in 18 positive-rational experiments: gate pairs (0,0), (1,1), (2,0), (7/3,2), (0,7/3), (2,2), each with three independently specified precursor vectors. All executable assertions pass. Raw scope, indexed witness sets and trial counts are in PREFIX625_native_two_generation_path_results.json.

The arithmetic is exact integer/rational evaluation of the **original native BRC action semantics**, not a different evolution engine. No π, trigonometric update, matrix exponentiation, Taylor/Padé/Cayley substitution, or signed cancellation is used. The mathematical proof rests on the complete polynomial coefficient identities and graph support, not solely on the 18 input trials.

## Next research unit

Determine whether the rank-16 two-step endpoint image is preserved under arbitrary subsequent native gates, and calculate rank(A(g_n)...A(g_1)) for all n>=2. Separately classify, by horizon, whether every live original source retains a positive fully labelled path and derive the exact horizon-dependent minimal added predecessor observer dimension. Initial finite samples for n=3..6 suggest persistent rank 16, but that statement is an open proof question here.

**Authority:** author-side scientific artifact only, no formal CLAIM/Result or independent Driver acceptance; it preserves P000, source exposure and other tasks. Real research identity and current Owner are established only by native Source receipts.
