# OAI7 r376 — Path-mask translation signatures exclude the r375 prime-29 path as a five-uniform candidate

Date: 2026-11-19. Author-side RESEARCH_DRIVER mathematical correction, continuing r360 and corrected r372–r375. Original Researcher EM-EMF6D046-5A2844; Task RS-OAI7-028-C-20261007-6F2A81; immutable publication TP2-96FAC49786245691AE19. Driver logical identity EM-DVR-DEBB5E. Shared author-side context, NOT an independent Native Result review.

## Theorem: universal connector separation condition

Let p=2r+1 be odd, G=Z/pZ and N be coprime to p. Consider a strictly positive S=m+p-1 common-translation sampler whose first-coordinate profile/residue incidence graph contracts to the labeled path v_0,...,v_(p-1). Assume exactly p-1 distinct degree-two connector profiles x_1,...,x_(p-1), one between v_(k-1) and v_k; all remaining profiles have degree one. Each profile has one fixed ordered shape W_x in G^d. Assume every coordinate marginal is uniform.

Use the corrected r372 mirror-mask classification. Let A(v) be all geometrically admissible r-bit masks, and for any b in A(v) let d_k(b) be the shift mapping BOTH labeled endpoint atoms of connector x_k from first-coordinate residues to the path residues in the new coordinate. By r373, complementary masks change all d_k by the same constant. Define the *mask-signature*
\[
\sigma_v(k)=\big(d_k(b)-d_1(b)\big)_{[b]\in A(v)/\{b,\bar b\}}\in G^{|A(v)|/2}.
\]
It is well-defined independently of the chosen representative of each complement class.

**Necessary condition.** If all p-1 connector shapes are pairwise inequivalent under common translation of their d ordered coordinates, then the map k -> sigma_v(k) is injective.

**Proof.** Fix coordinate i>1. A uniform coordinate has the same labeled cut counts as coordinate 1 (r360), so r372 supplies some admissible mask b_i and path origin c_i. The actual fixed connector coordinate offsets satisfy
\[
\Delta_{x_k,i}=w_{x_k,i}-w_{x_k,1}=d_k(b_i)+c_i,\qquad k=1,\ldots,p-1.
\]
The origin c_i may depend on i. If sigma_v(k)=sigma_v(l), then d_k(b_i)=d_l(b_i) for every admissible choice b_i (the common normalization and complement ambiguity cancel). Hence \Delta_{x_k,i}=\Delta_{x_l,i} at every i>1. The first-coordinate-normalized ordered tuples W_(x_k) and W_(x_l) have identical relative coordinates; they differ by a common translation, contrary to the hypothesis. QED.

This is a geometry-only, mass-independent necessary test. Even if the signature map is injective, finite d, singleton placements, fixed profile numerators and positive cut weights remain subject to the precise r360 test.

## Exact prime-29 application: all six masks, only seven signature classes

The original r375 residue path is
\[
v=(23,4,5,2,21,8,15,28,11,12,6,7,18,1,20,25,19,0,3,13,17,10,22,9,14,27,24,16,26).
\]
Its entire admissible mask set, previously certified, is A={0,2,15,16368,16381,16383}; the three complement classes have representatives 0,2,15.

Exact normalized connector signatures (entries correspond to those three masks) are:

| Connector label k | sigma_v(k) | Multiplicity |
|---|---|---:|
| 1 | (0,0,0) | 1 |
| 2 | (0,26,0) | 1 |
| 3–4 | (0,7,0) | 2 |
| **5–24** | **(0,7,7)** | **20** |
| 25–26 | (0,7,14) | 2 |
| 27 | (0,17,14) | 1 |
| 28 | (0,14,14) | 1 |

Thus **20 different connector profiles x_5,...,x_24 are forced to have the same relative shape in every additional uniform coordinate**, irrespective of the number d of coordinates and irrespective of all profile masses. The OAI7 pinned set of 350 positive-mass profiles consists of pairwise translation-inequivalent ordered shapes. Consequently:

\[
\boxed{\text{The particular p=29 residue path of r375 cannot underlie any sharp-support all-uniform OAI7 sampler.}}
\]

This does NOT invalidate r375's six-mask **geometric** counterexample to the power-of-two extrapolation: those six admissible masks still exist. This excludes only its use as a prescribed-profile, simultaneously uniform sharp-support path.

## Standalone exact integer certificate

The following Python 3 code enumerates all 16,384 masks, independently checks geometric admissibility and computes signatures. No floating-point arithmetic is used.

```python
p=29
v=(23,4,5,2,21,8,15,28,11,12,6,7,18,1,20,25,19,0,3,13,17,10,22,9,14,27,24,16,26)
assert len(v)==p and sorted(v)==list(range(p))
g=[(v[j]-v[j-1])%p for j in range(1,p)]
def mask_offsets(mask):
    y=[0]
    for j in range(1,p):
        bit=(mask>>(min(j,p-j)-1))&1
        y.append((y[-1]+(g[j-1] if not bit else -g[p-j-1]))%p)
    if len(set(y))<p:
        return None
    shifts=[]
    for k in range(1,p):
        bit=(mask>>(min(k,p-k)-1))&1
        j=k if not bit else p-k
        minus=y[j-1] if not bit else y[j]
        plus=y[j] if not bit else y[j-1]
        delta=(minus-v[k-1])%p
        assert delta==(plus-v[k])%p
        shifts.append(delta)
    return tuple((x-shifts[0])%p for x in shifts)
hits={b:mask_offsets(b) for b in range(1<<14)}
hits={b:s for b,s in hits.items() if s is not None}
assert set(hits)=={0,2,15,16368,16381,16383}
assert all(hits[b]==hits[b^16383] for b in hits)
reps=[0,2,15]
signatures=[tuple(hits[b][k] for b in reps) for k in range(28)]
groups={}
for k,signature in enumerate(signatures,1):
    groups.setdefault(signature,[]).append(k)
assert len(groups)==7
assert groups[(0,7,7)]==list(range(5,25))
assert sorted(map(len,groups.values()))==[1,1,1,1,2,2,20]
print("r376 PASS: 16384 masks, 6 admissible, 7 signatures, 20 inseparable profiles")
```

## Scientific classification and continuation

The new result is a necessary *shape-separation obstruction* for a specified first-coordinate path, not a general nonexistence theorem for all possible first-coordinate spanning trees, for profiles of degree >=3, or for the entire OAI7 five-coordinate sharp-support question. The global five-uniform support interval remains 378 <= S_min <= 490 pending independent exact candidates/proofs.

For any next candidate path, calculate the full admissible-mask signatures first; discard it whenever two connector signatures coincide. Only surviving path geometries justify the more costly fixed-offset, singleton and integer cut-weight checks. Preserve r375's six-mask finite theorem as a valid separate result.

Exact predecessor: https://github.com/awdawmip/enterprise-math/blob/03ebbb7cb0195469cb7d5a241f8cb0d21793c259/research_notes/portable_direct/2026-11-19_oai7_driver_prime29_nonpower_mirror_masks_r375.md
r360: https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md

Source publication is scientific evidence only; it does not assert Native Result acceptance, Source/Activity linkage, formal CLAIM/Task completion, or parent-objective closure.
