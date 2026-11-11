# X6 C6 branch-weight transfer: exact loop statistics and a phase-identifiability counterexample

Status: DRIVER_MATHEMATICAL_AUDIT / PROVED_SCOPED_WEIGHTED_BRANCH_MODEL / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (+08)
Parent: RS-X6-NATIVE-ROTATION-DYNAMICS / TP2-6A1F9D8C2047E3B51C01, parent PO-X6-UPPER-STRUCTURE-20260906.
Authorship: scoped new derivation in the Driver's shared X6 research context, **not** a clean-blind independent review. Prior original C6/C12 microtraces belong to EM-FREE-7D3C9A and the named source contributors; reuse their actual source definitions. No present TASK claim or physical dynamics selection is asserted.

## 1. Typed model and question

Work in a selected genuine three-axis K4 STAR inside the signed native spatial X6 Cell torsor. Fix an oriented six-phase unit-shell cycle a_0,...,a_5 with a_(r+3)=-a_r. For macrostep r→r+1 use the previously defined two ordered two-letter microtraces
I_r=(-a_r,a_(r+1)) (INNER, via the pivot) and O_r=(a_(r+1),-a_r) (OUTER).
Each branch has the same signed-step multiset per macrostep. For a full six-step circuit and its repetitions, the product of fixed multiplicative primitive-letter weights is independent of the I/O sequence, equal to W_S^m for m circuits (as proved in the source note below).

Add **explicitly declared** positive rational phase-branch activities t_1,...,t_6, periodic across successive turns: an O macrobranch contributes 1 and an I macrobranch at phase j contributes t_j. This is a *new refinement of the candidate Weighted-BRC model*, not a P000 physical rotation law. Apply the already scoped NB seam refinement: two consecutive I choices are forbidden; for a closed/repeatable circuit also forbid last I followed by first I. Each sequence retains its distinct ordered provenance. Define its normalized activity mass as the product of its I activities; multiply by W_S^m to restore primitive-letter weight.

Question: what phase information can be recovered from the total activity masses of all closed paths after one, two, or arbitrarily many circuits? Can an open-path phase-resolved test distinguish two candidate activity laws that all those closed totals fail to distinguish?

## 2. Exact transfer theorem

Let T(t) = [[1,t],[1,0]], with rows indexed by the previous macrobranch (O,I), columns by the current branch (O,I). Entry 0 forbids I→I, and nonzero entries supply the weight of the current choice. Put P=T(t_1)...T(t_6) and let e_O=(1,0).

For any positive integer m, the *normalized* open and closed NB activity masses over n=6m ordered macrobranches are exactly
  A_m = e_O P^m (1,1)^T,
  C_m = tr(P^m).
The full masses with fixed primitive-letter weights are W_S^m A_m and W_S^m C_m, respectively.

Proof: matrix multiplication sums a unique term for each ordered I/O choice and its permitted adjacent transitions, applying each current-branch activity exactly once. The virtual preceding state O removes the initial boundary restriction for A_m. The trace joins the last state to the first for C_m. This counts all paths with their branch labels and no quotient by cyclic rotation. Since the primitive-letter multiset is fixed for every complete C6 turn, its common weight factors out. QED.

Set τ=tr(P), δ=det(P)=t_1 t_2 t_3 t_4 t_5 t_6 (the six minus signs cancel). By Cayley–Hamilton,
  C_0=2, C_1=τ, C_m=τ C_(m-1)-δ C_(m-2), m≥2.
Consequently **the entire sequence of normalized repeated closed-circuit totals {C_m:m≥1} is completely specified by just τ and δ**. Conversely C_1 and C_2 recover these two invariants via τ=C_1, δ=(C_1²-C_2)/2. These are exact, not asymptotic statements.

With a common activity t on all six phases, the coefficient of t^k in the length-n NB-open polynomial is binomial(n-k+1,k), while the length-n NB-cyclic coefficient is n/(n-k)*binomial(n-k,k) for 1≤k≤floor(n/2), with k=0 coefficient 1. Proof: place k nonconsecutive I positions on a line after shifting the k chosen coordinates by 0,...,k-1; for a cycle count rooted marked I choices and the k mandatory O gaps. In particular for one C6 turn:
  A_1(t)=1+6t+10t²+4t³,
  C_1(t)=1+6t+9t²+2t³.
At t=1 these recover the prior exact NB counts 21 and 18 (from 64 unfiltered branch words).

## 3. A rigorous nonidentifiability witness beyond dihedral relabeling

Consider the two positive rational, six-phase laws
  U=(1/2,1/2,1/2,2,1,1),
  V=(1/2,1/2,1,1/2,1,2).
Both have τ=29/2 and δ=1/4. Therefore for **every** m≥1 their complete-loop NB masses are identical (after the common W_S^m primitive-letter factor). In particular C_1=29/2 and C_2=839/4.

These activity laws are not related by a cyclic rotation or reversal of the six phase labels. U has three consecutive half-activity phases on the cycle; V has no run of three consecutive half-activity phases. This invariant distinguishes their dihedral orbits.

Yet an OPEN six-macrostep NB observation started at the stated phase distinguishes them:
  A_1(U)=65/4, whereas A_1(V)=17.
For two successive circuits the distinction persists:
  A_2(U)=1883/8, whereas A_2(V)=985/4.
All stated values are exact rational sums, not rounded samples.

Thus even access to every whole-loop closed aggregate at all repetition counts does not identify the six phase activities up to their obvious geometric dihedral symmetry. **One boundary-aware open-path measurement can separate this explicit collision.** The pair suggests a concrete experiment-design distinction between closed aggregate BRC observers and phase-registered path/branch observers, without selecting a physical rotation grammar.

## 4. Exact executable checker (Fractions only)

The full positive-rational enumeration over 2^6 and 2^12 I/O words verifies both boundary conditions and the two matrices in each case:

~~~python
from fractions import Fraction as F
from itertools import product

def mm(A,B):
    return (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3],
            A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])

def transfer(ts):
    P=(F(1),F(0),F(0),F(1))
    for t in ts:
        P=mm(P,(F(1),t,F(1),F(0)))
    return P

def enumerate_nb(ts,cyclic):
    total=F(0)
    for w in product((0,1),repeat=len(ts)):  # 1=I, 0=O
        if any(w[j] and w[j+1] for j in range(len(w)-1)):
            continue
        if cyclic and w[-1] and w[0]:
            continue
        mass=F(1)
        for b,t in zip(w,ts):
            if b: mass*=t
        total+=mass
    return total

U=(F(1,2),F(1,2),F(1,2),F(2),F(1),F(1))
V=(F(1,2),F(1,2),F(1),F(1,2),F(1),F(2))
expected=[((F(65,4),F(29,2)),(F(1883,8),F(839,4))),
          ((F(17),F(29,2)),(F(985,4),F(839,4)))]
for law,ans in zip((U,V),expected):
    P=transfer(law)
    tau=P[0]+P[3]
    delta=P[0]*P[3]-P[1]*P[2]
    assert (tau,delta)==(F(29,2),F(1,4))
    for m in (1,2):
        Q=transfer(law*m)
        opened=Q[0]+Q[1]
        closed=Q[0]+Q[3]
        assert (opened,closed)==ans[m-1]
        assert opened==enumerate_nb(law*m,False)
        assert closed==enumerate_nb(law*m,True)
assert len({tuple(U[k:]+U[:k]) for k in range(6)})>=1
~~~

The last assertion is only a benign rotation sanity check; the stronger dihedral distinction is proved directly by the three-consecutive-halves invariant. Universal transfer and recurrence results have algebraic proofs above; exhaustive checks apply to the explicitly enumerated finite instances only.

## 5. Integration and review boundary

Exact supported gain: a phase-dependent rational Weighted-BRC extension, a two-invariant complete-loop transfer theorem, a non-dihedral all-turn collision, and an open-boundary discriminator. For the open X6 parent question, a legitimate owner can compare this observable with proposed time/phase/branch update laws. This is a saved scoped Driver derivation with original prior-contributor attribution; native Result/Review acceptance, an owner CLAIM, Task closure and parent Objective closure require their own current Source actions.

Prior pinned mathematical input: [2026-11-12_x6_signed_brc_boundary_transfer_nonbacktracking.md](2026-11-12_x6_signed_brc_boundary_transfer_nonbacktracking.md) and [2026-11-12_x6_weighted_brc_c6_loop_and_star_atlas_invariants.md](2026-11-12_x6_weighted_brc_c6_loop_and_star_atlas_invariants.md), each retained with its existing authored scope. Original C6/C12 two-microtrace provenance: research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md (EM-FREE-7D3C9A). Native X6 torsor: definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md.
