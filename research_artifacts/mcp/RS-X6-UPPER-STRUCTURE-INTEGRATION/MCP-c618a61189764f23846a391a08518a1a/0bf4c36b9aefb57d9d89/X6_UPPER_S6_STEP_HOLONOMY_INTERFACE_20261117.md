# X6 upper-interface certificate: S6 rotation / signed primitive steps

2026-11-17 · Task RS-X6-UPPER-STRUCTURE-INTEGRATION · Researcher-side mathematical increment, not independent review.

## Pinned starting definitions
- X6 Cell is an affine torsor for Z^6; choose an anchor only to write coordinates.
- The approved axis-permutation rotation skeleton is S6, acting by permuting the six positive axis labels, with signs retained.
- Native primitive spatial steps are T_{i,eps}(z)=z+eps*e_i, i=1..6, eps in {+1,-1}.
- Relative observer is Z^6/Delta with Delta=Z*(1,1,1,1,1,1); a selected three-axis observer is can3 of its three selected coordinates.
- P000 forbids promoting a two-axis displacement to a new primitive direction. Weighted/path-formal BRC identities stay richer than endpoint counts.

Exact Source: definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md, sections 2,3,5,6,9,10,12 at a72226e2430ffa4786321ac86e7f0c599d5f0389; Joint Relation Observer Preservation V2 at same ref. This certificate concerns the established S6 skeleton only.

## Theorem (typed semidirect interface and commutator witness)

For sigma in S6 let R_sigma(z)_{sigma(i)}=z_i, with the same chosen chart anchor. Then:

(1) R_sigma T_{i,eps}=T_{sigma(i),eps} R_sigma. The subgroup of coordinate-affine actions is Z^6 semidirect S6 with multiplication (v,sigma)(w,tau)=(v+sigma*w,sigma*tau). R_sigma and T_{i,eps} commute exactly when sigma(i)=i.

(2) The commutator R_sigma T_{i,eps} R_sigma^{-1} T_{i,eps}^{-1} is translation by h=eps*(e_{sigma(i)}-e_i). If sigma(i) differs from i, h has support 2, ||h||_1=2, L_E(h)^2=2, and the number of shortest signed-primitive *translation* words for h is 2 (the two orders of its different signed steps). This number does not count the full rotation-containing histories.

(3) For sigma(i) unequal to i, h is nonzero in the complete joint relative observer Z^6/Delta. Among the 20 three-axis min-zero coordinate observers Obs_S, precisely C(4,3)=4 have Obs_S(h)=Obs_S(0)=0: S must omit both i and sigma(i). All other 16 distinguish h from 0. Thus one carrier observer can miss an exact noncommuting rotation/translation effect; a typed common state must preserve it until a declared safe quotient certificate exists.

(4) Enumeration over all 720 sigma, 12 signed primitive steps: 8,640 ordered cases; 1,440 commuting cases (sigma fixes i) and 7,200 noncommuting cases. The latter give exactly 28,800 (case, three-axis observer) hidden-holonomy instances, four per case. This is exhaustive finite verification of the stated S6 skeleton, alongside the symbolic proof.

Proof: (1) apply R_sigma to z+eps*e_i and use R_sigma e_i=e_sigma(i). The semidirect multiplication follows by composing affine maps. (2) is conjugation; unequal basis indices give two nonzero coordinates of opposite sign. The spatial torsor's shortest-path multinomial formula gives 2!/1!/1!=2. (3) A nonzero vector supported on exactly two coordinates with entries opposite sign cannot be in the diagonal Delta. Obs_S sees a zero triple iff S omits the support: if it meets the support, its triple contains at least one zero and one nonzero entry, and can3 cannot be zero. (4) For fixed i, exactly 5! permutations fix i and 720-120 move i; multiply by 6 axes and 2 signs.

## Port-state minimality, scoped

If a future transition executes the *stored* current signed port p with T_p, and the observer must report the next full X6 endpoint, projecting (z,p) to z alone is not transition-safe: states (z,+e_i) and (z,+e_j) for i != j have identical projected current endpoints but distinct next endpoints. This witnesses one necessary port distinction for that declared update/observer, not a universal claim that all twelve port labels must always be stored. With port supplied externally as the operation label, it need not also be duplicated in state.

## Continuation frontier

Completed: exact S6×signed-step covariance/semidirect witness; local three-axis holonomy blindness; 8,640-case finite verification. Open: check triadic event and native time/source compatibility against their actual verified operators; non-FCC carrier compatibility; full operationally minimal decorated-state quotient with specified observers and future horizons. No physical or full native rotation dynamics claim, nor mathematical review/admission claim.
