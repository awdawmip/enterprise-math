# D25/LIFT GH-88–GH-89: intrinsic quadratic finite-source concomitant and target-fiber non-descent

2026-10-29 | Research lane: chatgpt-research-hourly-enterprise-math-20260923. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent D25/LIFT/JT2 OPEN; original Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. No native session, claim, run, checkpoint, review or admission is asserted.

## Original inputs (distinct provenance)

Let p=4d+3>=7 be prime, k=F_p and theta=z d/dz. Retain the two distinct exact polynomials S=sum_{j=0}^d c_j z^j (true truncated source), U=sum_{j=0}^d h_j z^j (reflected Laurent source), c_0=h_0=1, with

c_{j+1}/c_j=(4j+1)^3/[(4j+2)(4j+3)(4j+4)],
h_{j+1}/h_j=(4j+3)^3/[(4j+4)(4j+5)(4j+6)].

All denominators at 0<=j<d are units. Define true target T=(8theta+1)S; reflected H=(8theta+5)U; J=theta H. From GH-84, the signed concomitant for ordered sources (X,Y) is

B(X,Y)=(1-z)[Y theta²X-(theta Y)(theta X)+(theta²Y)X]+(z-3)Y theta X/4 +(3-5z)(theta Y)X/4 +(2-7z)XY/16.

It obeys theta B(X,Y)=Y L_-X+X L_+Y, where
L_-=theta(theta-1/2)(theta-1/4)-z(theta+1/4)^3,
L_+=theta(theta+1/4)(theta+1/2)-z(theta+3/4)^3,
L_-S=(c_d/8)z^(d+1), L_+U=0. Let B(z)=B(S,U). GH-86 establishes L_+(z^s S)=z^s L_-S, s=(p-1)/2=-1/2 in k.

## GH-88A — an independent intrinsic quadratic source and exact finite support

Define the signed source-jet polynomial

Q(z)=(1-z)[2S theta²S-(theta S)^2]-(1+z)S theta S/2 -zS²/16.

For every such p the **complete polynomial identity** holds:

(theta-1/2) Q = (c_d/4) z^(d+1) S.

In fact its uniquely reconstructed finite source is

Q(z)=(c_d/4) sum_{j=0}^d [c_j/(d+1+j+s)] z^(d+1+j).

This is a division by p-units only: for 0<=j<=d, d+1+j+s is in [3d+2,4d+2=p-1] as an integer. In particular [z^n]Q=0 for all 0<=n<=d, but coefficients in degrees d+1,...,2d+1 retain the *original* finite c-source.

**Proof:** GH-84 on X=S, Y=z^s S gives
theta B(S,z^sS)=(c_d/4)z^(s+d+1)S.
Expand the full signed concomitant using theta(z^s S)=z^s(theta S+sS) with s=-1/2 in k. Exact cancellation yields B(S,z^s S)=z^s Q, hence (theta+s)Q=(c_d/4)z^(d+1)S. The degree bound from the definition is deg Q<=2d+1=s. Each coefficient of Q is multiplied by n+s=n-1/2 (mod p), never zero for n in [0,s]; its first possible zero is n=(p+1)/2=s+1. Coefficientwise division gives the displayed exact polynomial sum. This proof uses neither an unreviewed CM claim nor an inverse of S or U.

## GH-88B — unconditional source syzygy and target-square certificate

For D=theta S, T=8D+S, H=8theta U+5U and J=theta H, direct polynomial algebra yields the **unconditional identity** (true for arbitrary S,U with these definitions):

8UQ - UT² -16SB
=8(z-9)U D²
 +[2(z-9)U+2(1-z)H]SD
 +[(z-7)U/4+(5z-1)H/4+2(z-1)J]S².           (GH88.4)

Proof: expand B and Q, cancel the 16(1-z)US theta²S terms, then substitute theta U=(H-5U)/8 and theta²U=(J-5theta U)/8. Collect the coefficients of D², SD and S²; these are exactly the three displayed brackets. No differential equation, root condition or numerical assumption is used.

At the precise fiber z=9 the D² coefficient vanishes, and SD=S(T-S)/8. Thus, with all values now evaluated at z=9,

U T² -2 H S T +(13H+16J+U/2)S² +16SB -8UQ =0.           (GH88.5)

If the separately author-derived GH-83 reflection root H(9)=0 is used, this becomes the **division-free squared-target certificate**

U T² =8UQ -16SB -(16J+U/2)S².                           (GH88.6)

For U(9)!=0, proving the right-hand finite-source expression zero *independently* is necessary and sufficient for the original T(9)=0 over F_p. B has GH-84's exact finite source and Q has the new finite source above. The coefficient of D² in the polynomial identity is 8(z-9)U: z=9 is the unique parameter-independent quadratic elimination fiber in this particular observer. These identities **do not** prove the required special right-hand evaluation, and the original GH-3 all-prime claim remains open.

## GH-89 — exact no-descent at the double-root fiber

Suppose U(9)=H(9)=0, while S(9)=x!=0. GH-85 gives B(9)=-J(9)x, and Q(9) satisfies

Q(9)=-16x*(theta²S)(9)+8y²-5xy-9x²/16, y=(theta S)(9).

For any choice of y in F_p, the second jet

(theta²S)(9)=[8y²-5xy-9x²/16-Q(9)]/(16x)

preserves the exact same observer tuple (S,U,H,J,B,Q), while the true target readout T(9)=8y+x varies bijectively with y. Therefore the quotient to those scalar concomitants is NOT a sufficient observer for reconstructing T on this root fiber. This is a scoped theorem about **local signed second-jet algebra**, not a claim that the alternative jets are global original hypergeometric solutions.

**Exact p=23 witness:** actual original data at z=9 give (S,U,H,J,B,Q)=(20,0,0,15,22,6) and original (S,theta S,theta²S)=(20,9,0), T=0. A distinct *synthetic local jet* (20,0,12) has exactly the same measured tuple, but T=20 mod 23. It is not asserted to solve the complete original differential equation. The witness proves why the two concomitants cannot be divided or collapsed to infer GH-3 for the observed p≡19,23 (mod24) root branches.

BRC/observer resolution: COMPOSE_APPLIED to typed population (p,d,z,c-source,h-source,signed theta jets) and future readout T(9). Nonzero-U squared criterion is an exact scope-typed reuse; the U=0 quotient fails by the explicit fiber witness. Preserve source provenance, signed cancellation, original coefficient ordering, prime residue class and both jets. These are external finite-field scalar charts and grant no Heartbeat native X6 transfer; P000 and the joint-observer preservation policy remain unchanged.

## Executed checks, dependency strength, continuation

The companion exact Python checker independently constructs c_j,h_j, computes complete polynomials B,Q and verifies both the new forced equation and its finite coefficient reconstruction, **all coefficients** of GH88.4 and the target identity GH88.5. It ran for all 154 primes 7<=p<2000 with p≡3 (mod4). The non-descent generator was checked on 74 sample root fibers; 80 samples had U(9)!=0. GH-83's H(9)=0 and sampled GH-3 zeros were separately checked as finite regression observations, not promoted. Reported output: PASS_GH88_FULL_POLYNOMIAL_154_PRIMES; PASS_GH88_TARGET_9_QUADRATIC_154_PRIMES; PASS_GH89_74_SIGNED_JET_FIBER_WITNESSES. These are author checks, not a native experiment or independent review.

Reused original immutable notes: GH-84/85 blob 1edcf5425ddb981de0743d6bce5fb81e2d8a7a1e; GH-86/87 blob 987f2685bb15fffec8d1f6a69be6d7b197050d33; GH-83 conditional reflected-root blob fcfd4c576d749e8279bb72776b6769e12735688b. All from research_notes/portable_direct/ with the corresponding date-named GH files.

**Next exact actions:** independently evaluate Q(9) and GH-84's B(9) using CM/WZ/finite character sums in the U(9)!=0 classes, proving GH88.6's right-hand side zero without using the desired T(9)=0. In the double-root classes construct an independent source-faithful local adjoint observer retaining the missing first jet. Preserve GH-83's actual Laurent first-order B_0L, GH-20/21, W/S, Hasse ports and original p=373 native benchmark. The onhour and maintenance lanes retain their independent roles.

**Current control boundary at this author run:** gateway 0.6.11 research_authority_granted=false, executor_binding_configured=false, control CODE_REVIEW_REQUIRED, active quota 5/5. recovery_status advertised but not callable in present tool list; client checkpoint-list returned ACCESS_DENIED. Existing #1558 retains old session/claims/requests/staging and exact D25 recovery route; no native state mutation was performed. The content above is portable author research only, pending formal registration and independent review.