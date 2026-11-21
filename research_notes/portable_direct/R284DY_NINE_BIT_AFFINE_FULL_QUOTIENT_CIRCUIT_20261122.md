# R284DY — Full frozen Port quotient: exact 9-bit arithmetic circuit replacing the 64-entry table

Date: 2026-11-22 (Asia/Shanghai)  
Scientific status: `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`  
Dependencies: R284CO original frozen Port model at `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`; R284DX full-universe quotient certificate at `enterprise-math@1161b7f25d79af64a0ff5911434dcd173e0f3d1a`. All mathematical inputs and the frozen codeword SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4` remain unchanged.

## Statement

For the original 65,536 source states write the 12 lower inputs in their frozen order `(u_1,a,x,y,u_2,w,b,z,u_3,g,h,r)∈{1,2}^{12}`, with four upper bits unrestricted. Let `T` be the original **unreduced integer** R284CO determinant and `P=17179869143`. Define the original determinant factors

\[
t=6-a,\quad s=13-b,\quad
u=ts-xw,\quad p_1=su_1+xu_2,\quad p_2=tu_2+wu_1.
\]

Then the following small arithmetic circuit yields the *exact* quotient of the original determinant by `P` on every source state:

\[
\boxed{
\left\lfloor T/P\right\rfloor=
\left\lfloor\frac{55152u-19198p_1-19411p_2+52}{512}\right\rfloor
-
{\bf1}_{\{u_1=a=x=u_2=w=b=2,\ T<2879P\}}
}.
\]

Consequently, `z=T-P\lfloor T/P\rfloor` is the exact original Port residue. This formula replaces the **64-entry six-core-bit quotient table** from R284DX with three fixed integer coefficients, one constant, and a **9-bit floor shift**. It still uses the single exceptional threshold correction. It eliminates general division/remainder by `P` *at this reduction stage*, rather than reducing the full original determinant-construction or later observer cost.

## Exact 64-core-cell identity

The original six-core-bit key is

`k=(u_1−1)+2(a−1)+4(x−1)+8(u_2−1)+16(w−1)+32(b−1)`, `0≤k≤63`.

Let `Q[k]` denote the actual 64 integer quotients given explicitly in R284DX. Define

`N(k)=55152u-19198p_1-19411p_2+52` with any representatives of the six bit assignments, since `u,p_1,p_2` do not depend on the other six lower input variables or the upper mask. Exhaustive **exact integer** evaluation of all 64 assignments yields

\[
\boxed{512Q[k]\le N(k)<512(Q[k]+1)\quad(k=0,\dots,63)}.
\]

The smallest lower slack `N(k)-512Q[k]` over all classes is **4** and the smallest upper slack `512(Q[k]+1)-N(k)` is **10**. Both are strictly positive. Therefore `\lfloor N(k)/512\rfloor=Q[k]` for every core class, with no rounding or floating-point assumptions. The previously certified R284DX finite classification states that `T//P` equals `Q[k]` on the 63 non-exceptional classes, and equals `Q[63]-1` exactly for the 446 source states meeting `T<2879P` in class 63. Combining these statements proves the boxed formula on the full universe.

## Direct all-state cross-check and validation

The companion Python checker runs adjacent to the previously published R284DX checker, imports its exact frozen `det` and 64-entry reference quotient table, and independently enumerates **all 65,536** original source assignments. On every state it checks the new circuit against `T//P` and the reconstructed reduced residue against `T%P`. Its ordered residue SHA-256 matches the frozen original. It checks the exceptional split `446/578` and fourth upper mask-bit quotient invariance. All checks pass using unbounded integers.

This is a complete finite proof of the stated identity by an explicit 64-cell certificate plus the exact previous 65,536-state classification, with an additional independent exhaustive computation against the original formula. It is **author verification**, not an independent reviewer pass, a native-X6 transfer claim, or a demonstration that the 9-bit scale or arithmetic operation count is optimal.

## Computational scope and next research questions

Relative to R284DX, the reduction stage trades a lookup of 64 precomputed quotient values for arithmetic using three original determinant factors and three fixed coefficients, plus a constant and bit shift. The three factors `u,p_1,p_2` already occur in the original determinant construction; this can permit reuse. A full benchmark must count their construction and reuse, integer multiplication/bit complexity, the exceptional comparison, preprocessing and access of R284DS/R284DT event observers, readout, and future-state reconstruction.

Next: derive a threshold correction predicate smaller than recomputing the original `T` where its full value is not otherwise available; seek a still smaller fixed-coefficient circuit or prove a meaningful lower bound under a precisely defined instruction-cost model. Then compare complete frozen Port processing costs under the same input, precision and observer language. Retain all joint source variables and proven future-observer distinctions; exact quotient reconstruction by itself does not authorize collapsing complete states.

## Reproduction

Run `python R284DY_affine_shift_full_quotient_checker.py` next to `R284DX_six_bit_full_quotient_checker.py`. The standard-library code regenerates the companion `R284DY_affine_shift_full_quotient_certificate.json`. Full 64-class margin and 65,536-state checks were run locally and passed. Formal Task/CLAIM/Activity/Result and independent Review remain separately governed; research author provenance is retained without a new execution authority claim.
