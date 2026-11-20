# EC49FTL addendum — Complete exact CDF of the optimized BRC16943 exchange gap

**Status:** AUTHOR_PROVED / EXACT_RATIONAL_147_POINT_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.  
**Inherited frozen scientific input:** awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.  
**Direct mathematical premise:** EC49FTH #2774 exact native Bellman affine theorem and EC49FTK #2776 unique q140 ridge theorem. This closes the next question stated in the initial EC49FTL_RIDGE_LAW_PROOF.md in this same PR.

Let a and b be independently uniform on [3/4,49/64] and [7/16,57/128]. Let
M(a,b)=max_{11/16≤z≤3/4}(D-S),
where D and S are precisely the inherited unrestricted native original-index Bellman values.

## Theorem: entire distribution of M

Put
m0=11457/512,
m1=1461/64,
m2=1469/64,
m3=187/8.
These are strictly increasing. The **entire cumulative distribution function** for any real m is

F_M(m)=
- 0, for m<m0;
- (512m-11457)^2/242550, for m0≤m<m1;
- (1024m-23145)/1050, for m1≤m<m2;
- -(137216m²-6555968m+78144641)/127575, for m2≤m<m3;
- 1, for m≥m3.

At the junctions the CDF equals, respectively, 0, 11/50, 359/1050 and 1. Thus the law has **no point masses**. Its density is linear on the first and third positive-width sections and constant (512/525) on the middle section. The density is continuous at m1 and jumps at m2, where the price-design family first admits an upper-plateau strategy. The CDF itself is continuous at every junction.

The support is [11457/512,187/8] and its upper endpoint 187/8 agrees with the inherited sharp maximum. The exact first two moments are
E[M]=494813/21504,
Var(M)=60097/1204224,
agreeing independently with the EC49FTL ridge certificate.

## Proof: integrate the conditional mixture, without native state compression

For a fixed b in B, write
L(b)=1539/32-(231/4)b,
H(b)=47-54b,
a_c(b)=(77+6b)/105.
The inherited optimized affine formula is M=(525a-462b-9)/8 on a≤a_c(b), and M=H(b) on a≥a_c(b). The a interval has width 1/64. Consequently the **conditional CDF** given b is

0 for m<L(b);
(512/525)(m-L(b)) for L(b)≤m<H(b);
1 for m≥H(b).

The conditional law has an atom at H(b), of mass (217-384b)/105, but H(b) is a strictly decreasing affine map over the continuously uniform b design. After integrating in b the unconditional law has no atom.

The four critical values are, in increasing order:
L(B1)=m0, L(B0)=m1, H(B1)=m2, H(B0)=m3.
For m∈[m0,m1], only b≥b_L(m)=(1539/32-m)/(231/4) contributes, and
F_M(m)=(128)(512/525)∫_{b_L(m)}^{B1}(m-L(b))db.
For m∈[m1,m2], all b contribute the linear partial branch:
F_M(m)=128(512/525)∫_{B0}^{B1}(m-L(b))db.
For m∈[m2,m3], b≥b_H(m)=(47-m)/54 contributes full conditional mass, while B0≤b<b_H contributes partial mass:
F_M(m)=128{(512/525)∫_{B0}^{b_H(m)}(m-L(b))db + B1-b_H(m)}.
Evaluating these elementary integrals yields the displayed three polynomials. Their junction values verify continuity and completeness.

For exact moment cross-check, because M≥m0,
E[M]=m0+∫_{m0}^{m3}(1-F_M(m))dm,
E[M²]=m0²+∫_{m0}^{m3}2m(1-F_M(m))dm.
Integrating the three polynomials and subtracting the squared mean gives exactly the two inherited moment fractions.

## Verification and scope

EC49FTL_GAP_CDF_VERIFY.py evaluates 147 rational points against **direct conditional integration** in b, then independently integrates the polynomial CDF for moments using only Python Fraction. EC49FTL_GAP_CDF_CERT.json and EC49FTL_GAP_CDF_RUN_LOG.txt save exact output.

No original 228-query Bellman rerun is claimed. There is no change of frozen science, original response identifiers, P000, owner/CLAIM, formal Result or Review. This is an author-proved postprocessing theorem conditional on the exact inherited native Bellman input.

**Next:** investigate the same distribution for a non-uniform price prior (with an explicitly specified density and error semantics), or obtain the first new native Bellman region across z<11/16 and test the transport of ridge and distribution laws. The present theorem answers the full-optimized-gap-CDF question on the stated box.
