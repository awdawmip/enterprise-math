# PREFIX-596-R2 — Native X6-BRC positive 48-state tail after the first step

Date: 2026-11-08. Author-side exact proof and executed integer certificate, pending independent Driver review. Researcher-ID EM-DIRECT-B4AFC3; Activity RA-735CA4F297799980BBEAAE7E. Frozen scientific pin `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; original 48 phases, 96 native bit ports, 576 tagged actions, all six source axes and original marked gate remain unchanged. Direct prerequisite: PREFIX-595-R2 in this branch, PREFIX-593/594 in draft PR #1797.

## Theorem 596.1 — a common nonnegative 48-dimensional tail carrier

Let g=IX[(0,1,-3)]=4 be the unique marked gate-target phase. In the original native phase adjacency g is not its own successor: `g not in N[g]`. Consequently, for all seven individual labelled original 96x96 coefficient matrices `A_k`, the two **output rows** of the gate phase are equal:
`A_k[(g,0),:]=A_k[(g,1),:]`.
Hence **after the first original step**, independently of its input and parameters, the marked phase satisfies `r_(g,0)=r_(g,1)`.

Define a nonnegative fixed 48x96 tail encoder `Ctail` which sums the two bit entries at each of the 47 ordinary phases, and selects one bit at g (the two are now equal). Define a nonnegative fixed 96x48 embedding `Etail`: at an ordinary phase put `(v_j,0)`; at g put `(v_g,v_g)`. Then `Ctail Etail=I48` and for every port vector satisfying equality of the two gate bits, `A(x,z)r=A(x,z)Etail Ctail r` (because ordinary source-bit columns coincide in all seven native generators).

Put `F(x,z)=Ctail A(x,z)`, `O(x,z)=A(x,z)Etail`, and `Q(x,z)=Ctail A(x,z)Etail`. All are nonnegative for all `x_a,z>=0` and retain all seven native typed generator coefficients.

For any nonstationary parameter sequence and initial `r0>=0`, after `v1=F(x1,z1)r0` each later transition satisfies `r_t=O(x_t,z_t)v_(t-1)`, `v_t=Q(x_t,z_t)v_(t-1)=Ctail r_t`, for every `t>=2`. Thus there is a **common single-stream nonnegative 48-state representation from the second original step onward for the entire gate domain z>=0**, with exact full 96-port linear readout. Initial one-step full readout with an unrestricted 96-port input uses the preceding common 49-state factor, which attains the one-step generic rank lower bound.

## Theorem 596.2 — determinant and exact one-time rank drop

For the original 48-phase adjacency `S_ij=1[j in N[i]]`, define `a(i)` as the native axis of phase i. The 48x48 nonnegative tail matrix has coefficients:
- i != g, j != g: `Q_ij=2 x_(a(i)) S_ij`;
- i != g, j = g: `Q_ig=(3+z)x_(a(i)) S_ig`;
- i = g, j != g: `Q_gj=x_(a(g)) S_gj`;
- `Q_gg=0`.

Equivalently `Q=diag_i(x_(a(i))) Drow S Dcol`, with `Drow=diag(2 except 1 at g)` and `Dcol=diag(1 except (3+z)/2 at g)`. The exact native determinant from PREFIX-586 is `det S=3^12`, and each axis occurs in eight of the original 48 phases. Therefore, **as a polynomial identity**,

`det Q(x,z) = 2^46 * 3^12 * (z+3) * product_{a=1}^6 x_a^8`.

In particular, for every `x_a>0` and `z>=0`, Q is invertible. Moreover `F Etail=Q`, `Ctail O=Q`, hence F has full row rank48 and O has full column rank48. For any time-varying positive six-axis/nonnegative-gate sequence of length d>=2,
`A_d ... A_1 = O_d Q_(d-1) ... Q_2 F_1`,
so **rank(A_d ... A_1)=48 for every d>=2**. By contrast, at d=1 and z1!=1, the original full-port matrix has rank49 (PREFIX-593/594). This is an exact one-time linear rank drop from 49 to 48, followed by full-rank positive 48-state propagation. The linear intermediary of dimension48 is optimal for the specified full 96-port readout of length>=2.

## Original-native exact certificate and scope

`PREFIX596_R2_transient_48_positive_tail_cert.py` reuses the frozen original 96-port seven-generator construction from PREFIX595. It checks all seven marked-output bit row equalities (672 entries), 7x48x48=16,128 typed tail transition coefficient values, 7x7x96=4,704 exact two-step typed-basis factorization identities, and 891 additional nonstationary full-port/tail-state checks from all 96 singleton sources plus three further vectors. Verified with z=0,1,2,5 and varying/singular axis weights. Original native source provenance stays in the original BRC generator; these 48 coordinates preserve all **future linear port outputs** after the transient, rather than individual past named bit-itineraries.

Exact standalone local SymPy checks independently recomputed `det S=531441=3^12` and checked the determinant formula at z=0,1,2,5 for six unit axes. The universal determinant identity is the displayed symbolic factorization; integer experiments are executable implementation evidence. Native tagged coefficient sums: F=[93,96,90,96,96,96,3], O=[51,48,48,48,48,48,3], Q=[51,48,45,48,48,48,3]. The theorem supplies a further positive algorithmic reduction without an unmeasured wall-time speedup claim.

## Next

Implement fair exact-integer end-to-end benchmarks (native optimized XSD, one-step49 then positive48 tail, 96-state WE) with encoding/output recovery, integer bit lengths, large batches and small output families. Seek exact further reductions for restricted output observers with a certified future-operation descent, retaining original path labels wherever the observer requires them.
