# R28: exact semiconvergent last-survivor batch and 67/36/61 mechanism

2026-11-10 (Asia/Shanghai). Researcher EM-DIRECT-C7404A, activity RA-81B4DFA77ECB55040F9EB253. Auxiliary irrational-circle S23/AV observer; historical cuts m=128. Scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Parent R27 proof at 6cfd0bf078b3bd05fbd4c51508a868a4706a5823. Independent review pending; no shared CLAIM.

## Definitions and reused exact result

For irrational 0<theta<1 let P_n be the circular ordering of the fractional phases {t theta} for 0<=t<n. Historical arcs I are consecutive arcs of P_m. Let M_n(I) be the maximum elementary P_n gap inside I; define R_n=1-sum_I M_n(I), and Delta R_n=R_n-R_(n-1).

For consecutive enclosing Farey neighbors a/q<theta<c/j with determinant q*c-j*a=1 and q,j<n<=q+j, the three elementary gap lengths are u=q theta-a>0, v=c-j theta>0, w=u+v. R27 proved that at regime start n=j+1 (when j>=q), the sources of the w-gaps are integers in [j+1-q,j). Exactly one positive event per historical arc with such gaps occurs when its last w source t is split, at n=q+t+1, with increment min(u,v).

## Theorem A: terminal-source sufficiency

Suppose 1<=H<=q-1, and the H terminal indices T_j=[j-H,j) meet every historical arc in their phases {t theta}. Then in each arc the largest index from T_j is the largest source over the entire w-source window [j+1-q,j). Thus the H terminal sources determine all internal positive risk events for that Farey regime.

Proof: T_j is a terminal subinterval of the w-source window and contains a member of every historical arc. Every omitted source has index smaller than every index in T_j. R27's last-survivor theorem gives the event location and height. QED.

## Theorem B: a batch of successive semiconvergents

Fix a/q and put j_k=j+kq, c_k=c+ka for 0<=k<=K. Then q*c_k-j_k*a=1 and v_k=c_k-j_k theta=v_0-k u. Assume u>0, each v_k>0, j>=q, H<=q-1, tail coverage of the m arcs at k=0, and owner stability:

owner({(t+kq)theta})=owner({t theta}) for every t in [j-H,j), 0<=k<=K,

with owner determined by the original fixed historical partition P_m.

For every k the terminal source set becomes T_j+kq, with the same owner assignment. Its last source in each arc is t_I+kq, and the regime event is q+t_I+1+kq, with increment min(u,v_k). Therefore the event-position pattern is translated by kq; an equivalent compressed output is the initial source-owner pattern, K, q, and the finite sequence of amplitude formulas min(u,v_k).

Proof: {q theta}=u because q theta=a+u. The circular phases of source t+kq are rotations of those for t by k u. The hypothesis preserves owners; Theorem A gives the new last survivors, while R27 gives their event positions and increments. The Farey determinant and v_k>0 preserve consecutive-neighbor status for the requested regimes. QED.

## Lemma C: the regime switch itself contributes zero

Assume in addition j_k>q>H and tail coverage as above. At n=j_k, the preceding Farey bracket has upper denominator j_k-q, and its long gaps have length v_k+u>u with source indices in [j_k-q,j_k). Its w-source interval is empty at this exact right endpoint. Insertion of source index j_k splits the long gap of source j_k-q into pieces u and v_k. Because H<q, the terminal H long gaps have sources strictly greater than j_k-q and remain intact. Every historical arc retains at least one gap of length v_k+u, so no historical maximum changes and Delta R_(j_k+1)=0. QED.

## Frozen S23 family and interval certificate

The exact parameter enclosure is

262204504569236716045286 / 10^24 < theta < 262204504569236716045287 / 10^24.

Take m=128, q=14298, a=3749, j=25339, c=6644, H=164 and K=9. Check q*c-j*a=1. The terminal source set is [25175,25339), containing only 164 indices. Exact rational endpoint checks show that it meets all 128 old arcs, and its 128 last sources are precisely the disjoint integer sets

[25175,25241] (67 indices) and [25278,25338] (61 indices).

The other 36 terminal sources belong to arcs with a larger tail source. For each of the 164 tail indices, let clearance be its forward circular distance to the next historical cut. Throughout the parameter interval, all relevant modular floors and the ordering of the 128 historical cuts are fixed. The source's phase, the next cut and the translation slack clearance-9u are therefore affine in theta. Exact two-endpoint calculation shows

min over tail sources and both endpoints of (clearance-9u)
  = 40342-153857*(262204504569236716045287 / 10^24)
  = 1540490946579420278041 / 10^24 > 0.

Thus none of these tail source phases crosses any historical cut during k=0,...,9 translations; Theorem B applies uniformly throughout the frozen theta interval. (The rational endpoints are comparison bounds, not replacements for the irrational theta.)

Put j_k=25339+14298k, u=14298theta-3749, v_k=(6644+3749k)-(25339+14298k)theta. For each k=0,...,9, and EVERY integer n in the complete regime j_k+1<=n<=j_k+14298,

Delta R_n = b_k when n belongs to
  [39474+14298k,39540+14298k] or
  [39577+14298k,39637+14298k],
and Delta R_n =0 at all other n in the regime,
where b_k=min(u,v_k).

At k=0,...,8, exact endpoint inequalities give v_k>u, so b_k=u. At k=9, v_9=40385-154021theta is positive and smaller than u, so b_9=v_9. Lemma C certifies the zero-increment first count at each bracket transition. These ten 14,298-step regimes fill n=25340..168319. They give 1,280 positive events and 141,700 zero increments; each regime has 67 positives, then 36 zeros, then 61 positives, with a 14,134-zero long gap between successive regimes' event blocks:

(39474+(k+1)14298) - (39637+k14298) - 1 = 14134 = q-164.

The two-block leader certificate explains the exact 67/36/61 structure; the semiconvergent translation and clearance certificate explain its repetition. The finite change of event height at k=9 is derived from the continued-fraction neighbor error.

## Exact computation and total cost

VERIFY_R28.py uses only Python Fraction, integer sorting and bisect. It verifies both rational enclosure endpoints, the old-cut ordering and modular-floor stability, terminal coverage, exact leader set, all translated phase owners, Farey determinants and inequalities, all event coefficients and two-block patterns. An optional R27 EVENTS_R27.tsv input independently checks all 1,280 corresponding integer-affine events. Actual run with that predecessor archive: PASS_R28_SEMICONVERGENT_TRANSLATION_CERTIFICATE; SHA-256 of the sorted predicted event stream 6289df294d1764dd55205dc7d8cebe074b881d152956f6fa3f0ffffe238a842a. This checksum is a reproducibility locator, not a substitute for the proof.

On a RAM arithmetic-operation model, the compressed batch generator prepares a sorted m-cut list and H terminal owners in O(m log m+H log m) operations, verifies a K-step clearance condition at the endpoints, and emits K compressed block descriptors in O(K), instead of K independent searches through all q sources. Actually emitting the m(K+1) events costs Omega(mK) output writes. Source index magnitude (up to j+Kq), interval denominator precision B, comparison/multiplication bit costs, and any method for finding a suitable H are included in total-cost accounting. The independently run verifier also checks all K*H translated owners for extra finite assurance.

This is an exact special family for a scalar, source-faithful observation. Transferring it to native X6 operations requires an explicit typed observer bridge and future-operation preservation. Independent review, canonical mathematical acceptance, and a shared task Result remain distinct.

## Next unit

Find a general Euclidean floor-sum/rank-select method to obtain a shortest useful H, certify minimum forward-cut clearance without enumerating q sources, and maximize the safe K under the v_k>0 neighbor bound. Test 154021 and 6318118 denominator families; seek direct 298-run output against R27. Preserve frozen science, sources, provenance and mathematical review status.
