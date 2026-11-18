# R762EU — Digitwise random-access oracle for every three-power BRC terminal shadow

Date: 2026-11-18. Scope: the frozen six named positive branches in the **complete three-coordinate terminal observer**, P=1+X+Z+XY+YZ+XYZ. Lineage: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Builds on R762ER@39787270e99ef3c698f43409b208dbe16b073ebb and R762ET@38b098bf04149ee8fdb1da48fee00ffe62846064 (author-side proofs, independent review NOT_REVIEWED). This is portable scientific work; the historical EM-X6-3050F6 identity is provenance, not a fresh Source authorization.

## Theorem: O(log q) random access with a 19,035-byte table

Fix any a>=2, q=3^a, h=q/9=3^(a-2), and integer n>=0. For P_q in Z[(Z/q)^3] put
f_q(n)=max(0,floor(3n/q)-2), and let the complete normalized mod-3 terminal shadow be S_q(n)=3^(-f_q(n)) P_q^n (mod 3).

Precompute A_t=S_9(t), for t=0,...,25, each as a 729-byte array over F_3. Let
C_e(i,j,k)=[X^i Y^j Z^k]P^e (mod 3) for e=0,1,2 and i,j,k=0,1,2, with zero assigned to missing coefficients. These three 27-byte tables have support sizes respectively 1,6,18.

Given a terminal coordinate (x,y,z) with 0<=x,y,z<q, write
n=hm+r, 0<=r<h, and set
t=m if m<8, else t=8+((m-8) mod 18).
Split each terminal coordinate into its exact high and low digits:
x=hu_x+v_x, y=hu_y+v_y, z=hu_z+v_z,
where 0<=u_x,u_y,u_z<9 and 0<=v_x,v_y,v_z<h.
For j=0,...,a-3 let r_j, x_j,y_j,z_j be the corresponding base-3 digits of r,v_x,v_y,v_z.

Then the following is an **exact coefficient oracle for every q and n**, including the entire transient:
$$
\boxed{
S_q(n)[x,y,z]
=
A_t[u_x,u_y,u_z]
\prod_{j=0}^{a-3} C_{r_j}(x_j,y_j,z_j)
\quad\text{in }\mathbb F_3.
}
$$

The empty product for a=2 is 1. The table requires exactly 26*729+3*27=19,035 uncompressed bytes, independent of q and of the time horizon n. Precomputing A uses 25 iterations of the original six named BRC shifts on 729 integer entries mod 3^7 (because f_9(25)=6). Query time is O(a) base-3 digit operations plus the arithmetic needed to divide the input integer n by h and reduce m modulo 18; under unit-cost integer arithmetic O(a), and under bit complexity the cost of processing the representations of n and q must also be counted. A full q^3-byte shadow can be streamed with O(a q^3) digit operations and O(19,035+a) working bytes, apart from stream buffering. These are terminal-shadow costs; they do not count or reconstruct full integer path counts or signed native event histories.

## Proof

R762ER proves the exact coefficientwise factorization
S_q(hm+r)=iota_h(S_9(m)) P_q^r (mod 3),
where iota_h sends each of the three generators of the q=9 group algebra to its h-th power. R762ET proves that S_9(m+18)=S_9(m) for every m>=8; therefore S_9(m)=A_t with t as above.

In characteristic 3, the freshman-dream identity gives the exact digit expansion
$$
P_q^r=\prod_{j=0}^{a-3}P(X^{3^j},Y^{3^j},Z^{3^j})^{r_j}
\quad\pmod3.
$$
Each of the six branch monomials has individual coordinate increments in {0,1}. A monomial of P^{r_j} has coordinates in {0,...,r_j}, a subset of {0,1,2}. Hence **no carrying** occurs when assembling the digits of the three coordinates across different j. Its coefficient at (v_x,v_y,v_z) is exactly the product of the corresponding local coefficients C_{r_j}(x_j,y_j,z_j).

Moreover every monomial in P_q^r has each coordinate between 0 and r<h. In the product with iota_h(A_t), the high part h(u_x,u_y,u_z) and the low part (v_x,v_y,v_z) therefore determine the output coordinate uniquely, without high/low carry or wrap modulo q. The group-algebra coefficient is the base coefficient times the low-digit coefficient. This yields the boxed formula.

The cost statement follows from reading three high digits, extracting a-2 low digits, and doing one lookup and multiplication modulo 3 per digit. All 26 base states and three local kernels are finite explicit tables, constructed once by the supplied exact program. QED, **conditional only on the already stated R762ER and R762ET author-side theorems**.

## Verification (reproducible, not a substitute for the all-q argument)

Companion R762EU_VERIFY.py independently generates A_t from original six-branch integer convolution mod 3^7 and the three local kernels by exact polynomial multiplication mod 3. It checks the sharp q9 boundary S9(8)=S9(26), and the failed predecessor S9(7)!=S9(25). It compares the digit oracle with the **independently iterated full integer convolution** for every q9 n=0..25 (26*729 entries) and every q27 n=0..82 (83*19,683 entries): a total of 1,652,643 exact terminal coefficient equalities, all PASS. Direct q27 arithmetic uses modulus 3^11, exceeding all required normalized exponents by at least one. Additionally, the program compares q27 period/sharp-preperiod boundaries at n=24/78 and 23/77; it exercises random coordinate queries at q=27,81,243, including n=10^12+271828. These latter spot checks test implementation consistency, not a new independent proof at q81 or q243.

Table SHA256 (exact concatenation order m=0..25, lexicographic x,y,z): A=02948ee5b53b5588e34a7047087a7812181c63e61170d7775182e989b30e72dd; C=31b9d921f66de56eb94e1d09650ef79e90cc40d982c376f811100cd80e4a5473. Full scope and counts in R762EU_EVIDENCE.json.

## Observer boundary and next frontier

The interface is (q,n,x,y,z) -> normalized terminal coefficient in F_3. It preserves this precise readout for all n; it is an observer algorithm, not a quotient of the native six-dimensional signed Cell/Link/Port path state. No native TRIADIC_CLOSURE_E event permission, future-operation preservation for underlying signed branches, or V17/V29/V39 transport is asserted. P000 is unchanged.

Next mathematical units: (1) independent audit of R762EQ/R762ES 127-order base certificates; (2) develop a provenance-preserving labelled-branch refinement, with explicit update and future readout tests; (3) compare random-access query cost to a dense vector materialization for actual large-q observer workloads. Independent semantic review: NOT_REVIEWED. Formal proof checker: NOT_PERFORMED.
