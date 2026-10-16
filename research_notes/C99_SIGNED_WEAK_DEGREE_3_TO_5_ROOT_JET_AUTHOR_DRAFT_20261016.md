# C99 author draft — signed Q³–Q⁵ Fourier atlas and interior BRC zero drift
Date: 2026-10-16
Status: AUTHOR_EXACT_DOUBLE_CHECKED / NONCANONICAL_RESEARCH_BRANCH / NO_CLAIM / NOT_DRIVER_ADMITTED

## Scientific model and fixed inputs
Classical positive-weight BRC integer auxiliary: 156 edges, 142 square faces; 48 frozen independent core faces. Fixed faces (8,11,44,61,89,118) have couplings 1/2, free ports are χ111,χ86, active weak faces (4,42,59,74) have couplings (x,x,1/10,1/10). The remaining 64 weak faces are Q. This is **not** a native X6 Cell theorem. The immutable context read at start is GLOBAL_KNOWLEDGE_V1 @ 061a670dd9e0addd6d203c03f986db8bde8b5ff0, EM @ 79040f2db94e671778650dbd0d808c8885dcc32e. P000 and ACTIVE worldview unchanged.

## Exact signed coefficients
For any Q subset I, active subset S, Fourier output O∈{1,χ111,χ86,χ111χ86}, expand fixed factors as ∏_{h∈H}(2+χh), and perform core-conditioned GF(2) character matching. The coefficient is exactly Σ_{J⊂H : m_I⊕m_S⊕m_O⊕m_J∈span(core)} 2^(6-|J|) χ_core(m_I⊕m_S⊕m_O⊕m_J).

The C98 necessary-support counts at Q degrees 3,4,5 were 19,42,64. C99 computes **all 2,000 actual nonzero formal core-character entries**: each of the 125 supporting Q subsets has 16 nonzero (active-subset, output) entries. First- and second-order Q coefficients remain exactly zero. "Nonzero formal core-character polynomial" does not assert nonzero on every chosen individual core or active path.

## A single explicit 48-bit core and its signed determinant spectrum
Set c2=1 and all 47 other core bits to zero, so sigma=(-1)^(c18+c19)=+1. Along the active path above:
A0=341/5-502x²/25, B0=-3x, C0=3x, D0=86/5-508x²/25.
Thus F0=AD-BC=(255016x⁴-1076375x²+733150)/625.

Since every Q-moment has zero weak degree 1,2, each determinant coefficient for 3≤|I|≤5 is **exactly**
J_I=D0*A_I+A0*D_I-C0*B_I-B0*C_I.
Among the 19 cubic possibilities, exactly 16 survive and 3 cancel; all 42 quartic possibilities survive; 58 of 64 quintics survive, and 6 cancel. The cubic cancellations are {90,106,119}, {91,102,120}, {112,115,123} (the three C93 port-determination triples). These cancellations are **specific to this core/path** and cannot yet be used to reduce the uniform C98 1/55 or 1/110 bounds across all cores.

## New exact cubic zero displacement for uniform Q
Set all 64 Q couplings equal to q. Summing the 19 cubic coefficients gives:
J(x)=3(3720880x⁴-1510248x³-12085520x²+1039800x+7629565)/1250.
Hence F(x,q)=F0(x)+J(x)q³+O(q⁴).
The positive unperturbed zero is
x0=sqrt((1076375-45 sqrt(202826281))/510032), with 231/250<x0<37/40.
Pure rational interval arithmetic proves F0'(x0)<0, J(x0)<0, and
-7/25 < -J(x0)/F0'(x0) < -13/50.
Thus the unique local analytic zero branch moves as
x(q)=x0-[J(x0)/F0'(x0)]q³+O(q⁴),
with strictly negative cubic displacement (approximately -0.263134977641356). This is **not** a global monotonicity claim or a theorem for arbitrary nonuniform Q.

## Reproduction and next action
Route A uses frozen 156-bit masks and core-character algebra to compute all 125 signed subsets, 2,000 formal coefficients, 125 determinant polynomials, and the exact rational root bracket. Route B independently regenerates 64 integer vertices/156 edges/142 faces and enumerates actual conditioned spin configurations; at x=0,1/2,1 it verifies **1,500 exact moment coefficient evaluations** for all 125 Q subsets and all four outputs. Since each moment is at most quadratic in x, these checks certify exact polynomial agreement, not just floating-point sampling.

Complete local C99 proof/scripts/signed atlas and verified portable package are preserved as a standalone evidence bundle in this conversation. The remote abstract is a noncanonical author research note; no active Owner/CLAIM, native Result, independent Driver review, Working Truth or Foundation promotion is asserted. Native em_control_tasks and dispatch returned CONTROL_QUOTA, em_session_start returned STATIC_READONLY_SCOPE_DENIED.

Next smallest unit: derive a uniform signed bound across all 48-bit cores using the character atlas and identify core-uniform cancellations; then attempt improvement over C98's 1/55 root-existence and 1/110 root-uniqueness radii with genuinely verified margins. Separately resolve legal Source publication/Driver role and native X6 Cell bridge without conflating models.
