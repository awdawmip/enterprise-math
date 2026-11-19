# OAI7 r374 — Exact affine-collision sieve and a prime-modulus non-subcube mirror-mask witness

Date: 2026-11-19. New Driver-side *author-context* mathematical contribution continuing the corrected r372 and r373 path-geometry reduction. This is neither an independent Native review nor an OAI7 Result admission.

## 1. Exact collision-hyperplane characterization

Let (p=2r+1) be odd, (G=\mathbb Z/p\mathbb Z), and (v_0,\ldots,v_{p-1}) be an ordering of all residues. Put (g_j=v_j-v_{j-1}) and let (b=(b_1,\ldots,b_r)\in\{0,1\}^r). As in r372, let

\[
h_j(b)=g_j-b_{\min(j,p-j)}(g_j+g_{p-j}),\qquad
y_0=0,\quad y_j=\sum_{s=1}^j h_s(b)\pmod p.
\]

For each (1\le k\le r), put (u_k=g_k+g_{p-k}\pmod p). For an interval (0\le a<c\le p-1), define the **integer incidence count**

\[
m_{a,c;k}={\bf1}\{a<k\le c\}+{\bf1}\{a<p-k\le c\}\in\{0,1,2\}.
\]

**Exact theorem.** The oriented mirror mask (b) gives (p) distinct path residues if and only if it avoids the following explicit (\binom p2) affine equations:

\[
\boxed{\sum_{k=1}^r m_{a,c;k}u_k b_k\not\equiv v_c-v_a\pmod p
\quad\text{for every }0\le a<c\le p-1.}\tag{A}
\]

No probabilistic assumption or primality is needed. In particular, admissible masks are the Boolean cube minus the union of **specified modular affine hyperplane sections**. They are always invariant under bitwise complementation by r373, but need not form a Boolean subcube or an affine-linear binary code. The resulting constraint system can be used as an exact modular/SAT sieve before reconstructing every candidate path.

**Proof.** A collision (y_a(b)=y_c(b)) is equivalent to (\sum_{j=a+1}^c h_j(b)=0\pmod p). Substitution gives
\[
0=(v_c-v_a)-\sum_{k=1}^r b_k
\sum_{j\in\{k,p-k\}\cap(a,c]}(g_j+g_{p-j}).
\]
The inner sum equals (m_{a,c;k}u_k), proving (A). Conversely any equality in (A) is precisely a repeated partial sum. There are exactly (\binom p2) potential pairs, so this test is necessary and sufficient. The complement symmetry is r373's exact path-reversal identity; hyperplane-complement invariance is a property of the *union* of forbidden sections, not necessarily of every individual section. QED.

## 2. An exact prime-13 counterexample to the power-of-two extrapolation

Let (p=13) and the first path be

\[
(v_0,\ldots,v_{12})=(0,5,2,9,1,3,8,11,4,6,10,7,12).
\]

Its steps are

\[
(g_1,\ldots,g_{12})=(5,10,7,5,2,5,3,6,2,4,10,5).
\]

Checking all (2^6=64) masks with the exact modular test (A) gives **precisely six** admissible oriented masks, listed as nonnegative integers with the least significant bit at position (k=1):

\[
\boxed{\mathcal A=\{0,2,6,57,61,63\}.}
\]

Their complement pairs are ((0,63),(2,61),(6,57)), hence by r373 the exact number of geometrically distinct labeled-connector templates up to common translation is **three**, not a power of two. This disproves any universal inference that the mirror-mask admissible set always has size (2^t), even when the cyclic modulus is prime. In particular, the power-of-two counts seen in r373's 64 sampled prime-29 paths are sample observations, **not** a general algebraic classification.

This conclusion concerns the **residue-path geometry only**. It does not establish profile-mass cut compatibility, prescribed-shape offset consistency, the 378-atom five-uniform OAI7 sampler, or any sharper prime-29 support bound.

## 3. Complete small exact certificate, Python 3 standard library

~~~python
p=13
v=(0,5,2,9,1,3,8,11,4,6,10,7,12)
assert sorted(v)==list(range(p))
r=(p-1)//2
g=[(v[j]-v[j-1])%p for j in range(1,p)]
assert g==[5,10,7,5,2,5,3,6,2,4,10,5]
u=[(g[k-1]+g[p-k-1])%p for k in range(1,r+1)]

def admissible_by_hyperplanes(mask):
    b=[(mask>>k)&1 for k in range(r)]
    for a in range(p):
        for c in range(a+1,p):
            lhs=sum((int(a<k<=c)+int(a<p-k<=c))*u[k-1]*b[k-1]
                    for k in range(1,r+1))%p
            if lhs==(v[c]-v[a])%p:
                return False
    return True

def admissible_by_walk(mask):
    y=[0]
    for j in range(1,p):
        bit=(mask>>(min(j,p-j)-1))&1
        h=g[j-1] if bit==0 else -g[p-j-1]
        y.append((y[-1]+h)%p)
    return len(set(y))==p

hits=[b for b in range(1<<r) if admissible_by_hyperplanes(b)]
assert hits==[0,2,6,57,61,63]
assert all(admissible_by_hyperplanes(b)==admissible_by_walk(b)
           for b in range(1<<r))
assert all((b^63) in hits for b in hits)
assert len(hits)//2==3
print("r374 PASS: 64/64 exact mask checks, 6 oriented paths, 3 complement classes")
~~~

All calculations are integer residue calculations. The certificate independently computes admissibility both from (A) and from the original step walk for every mask, so it tests the collision equation rather than merely trusting one implementation.

## 4. Scope, provenance and next discriminating use

r374 strengthens the *representation* of r372/r373's finite path-mask constraints and corrects a tempting extrapolation from their limited sampled counts. For fixed OAI7 profile offsets, (A) is only a geometry filter: every surviving candidate must still match all actual connector/singleton offsets under a common origin and pass r360's positive integer cut-signature test. No change is made to (378\le S_{\min}\le490) for five prescribed uniform coordinates.

Original OAI7 Task: `RS-OAI7-028-C-20261007-6F2A81`, publication `TP2-96FAC49786245691AE19`, original researcher `EM-EMF6D046-5A2844`. This Driver contribution reused r360 (tree/cut rigidity), corrected r372 (odd-path mirror pairs) and r373 (exact orientation quotient); previous authors and shared-context exposure remain explicit.

References:
- r360: https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md
- r372 corrected: https://github.com/awdawmip/enterprise-math/blob/6ba73383f3e87b5f0e90aca1392044fa717ef362/research_notes/portable_direct/2026-11-19_oai7_driver_path_mirror_pair_reduction_r372.md
- r373: https://github.com/awdawmip/enterprise-math/blob/ec905e2b63a533d6234e2471b23107cefc5a1035/research_notes/portable_direct/2026-11-19_oai7_driver_mirror_path_orientation_quotient_r373.md

Next useful search unit: apply the modular no-collision clauses, prescribed profile offset constraints and complete integer cut signatures simultaneously to actual prime-29 subsets; do not treat geometric masks as sampler feasibility.
