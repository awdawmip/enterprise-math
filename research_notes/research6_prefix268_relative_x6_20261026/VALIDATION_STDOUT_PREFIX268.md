# PREFIX-268 — preserved exact validation evidence (2026-10-26)

Scientific-input revision: EM main@2c8e32bebf20b3134d51a709f78fce96fbf992a0; Global Knowledge main@b1c6f9e87fc51617f9b75e37235682850b279b20. Mathematical source/proof: PREFIX268_RELATIVE_X6_NBRC_FULL.md in this directory.

Commands (Python standard library, author-side finite check):
- python3 verify_prefix268.py
- python3 verify_prefix268_algebra.py

These checks used integer path multiplicities and symbolic polynomials. The 12^12 individual paths were NOT exhaustively enumerated. No native physical heartbeat Phi/phase dynamics ran. Source-backed pure signed-X6 step semantics were used as an explicit formal N-BRC model.

## STDOUT from verify_prefix268.py
~~~text
k= 0 full=       1 rel=       1 paths=               1 r0_full_lifts=[0]
k= 1 full=      12 rel=      12 paths=              12 r0_full_lifts=[]
k= 2 full=      73 rel=      73 paths=             144 r0_full_lifts=[0]
k= 3 full=     304 rel=     284 paths=            1728 r0_full_lifts=[]
k= 4 full=     985 rel=     835 paths=           20736 r0_full_lifts=[0]
k= 5 full=    2668 rel=    2036 paths=          248832 r0_full_lifts=[]
k= 6 full=    6321 rel=    4347 paths=         2985984 r0_full_lifts=[-1, 0, 1]
k= 7 full=   13504 rel=    8408 paths=        35831808 r0_full_lifts=[]
k= 8 full=   26577 rel=   15069 paths=       429981696 r0_full_lifts=[-1, 0, 1]
k= 9 full=   48940 rel=   25420 paths=      5159780352 r0_full_lifts=[]
k=10 full=   85305 rel=   40821 paths=     61917364224 r0_full_lifts=[-1, 0, 1]
k=11 full=  142000 rel=   62932 paths=    743008370688 r0_full_lifts=[]
k=12 full=  227305 rel=   93743 paths=   8916100448256 r0_full_lifts=[-2, -1, 0, 1, 2]
relative spheres a6(0..12)= [1, 12, 72, 272, 762, 1752, 3512, 6372, 10722, 17012, 25752, 37512, 52922]
Q_relative(n=12,h=0)=93743
Q_relative(n=12,h=1)=755184
Q_relative(n=12,h=2)=5878224
Q_relative(n=12,h=3)=43925760
Q_relative(n=10,h=2)=2169936
PREFIX268_FULL_BRC_DP_VS_INDEPENDENT_GAP_CERTIFICATE_PASS
~~~

## STDOUT from verify_prefix268_algebra.py
~~~text
integer_polynomial_identity_coefficients= [1, 10, 47, 119, 183, 183, 119, 47, 10, 1]
earliest_triad_aliases= 20
n,h,classes 0 0 1
n,h,classes 1 0 12
n,h,classes 1 1 12
n,h,classes 2 0 73
n,h,classes 2 1 144
n,h,classes 2 2 144
n,h,classes 3 0 284
n,h,classes 3 1 876
n,h,classes 3 2 1728
n,h,classes 3 3 1728
n,h,classes 4 0 835
n,h,classes 4 1 3408
n,h,classes 4 2 10512
n,h,classes 4 3 20736
n,h,classes 4 4 20736
PREFIX268_INDEPENDENT_ALGEBRA_AND_FUTURE_EXHAUSTION_PASS
~~~

Independent polynomial certificate covers 32 ordered-coordinate block compositions, finite exact proof of rational generating function. Exhaustive direct word test covers all signed words n=0..4 and all h<=n. Full theorem is proved by quotient action, endpoint geometry, median distance/parity and exact combinatorial series; the finite numerical checks are supplementary.

Transport: ordinary GitHub writer identity awdawmip, with checked admin repository access, author-side only. Native research/control service: STATIC_READONLY_SCOPE_DENIED and CONTROL_QUOTA; no live owner CLAIM, formal Result or mathematical admission implied. Google Drive fallback not used because GitHub Source publication/readback works.
