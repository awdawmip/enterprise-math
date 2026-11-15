# R5: exact finite-state transfer for isolated suffixes and minimum repair libraries

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.

## Motivation and domain

The preceding theorem GRAPH_COUPLED_SUFFIX_EXACT_REPAIR_THEOREM.md establishes in an explicitly constrained auxiliary one-dimensional integer indexed-center model that kappa_a(X,2)=kappa_ab(X,2)=|X|+i(X), where X is an arbitrary nonempty common admissible suffix language and i(X) is the count of vertices isolated in its induced Hamming-distance-one graph. The theorem below computes BOTH statistics directly when X is recognized by a fixed complete deterministic finite automaton (DFA), without enumerating the up to 2^l words individually.

This is a theorem about the declared suffix observer, not a claim of native X6 calculation. The only compression performed is on the pair of observer values (membership, existence of an accepted single-flip neighbor); later observers that count or distinguish individual flips retain further residual information.

## Exact residual automaton theorem

Let A=(Q,delta,q0,F) be a complete DFA over alphabet {0,1}, with finite state set Q, starting state q0 and accepting set F. Let X_l be the accepted binary words of length l.

For each prefix u define:
- q(u)=delta*(q0,u), the state reached on the unchanged word;
- R(u)={delta*(q0,v): v is obtained from u by changing exactly one bit}, a SET of states reached by all single-flip alternatives.

The empty-prefix state is (q0,empty set). Reading a new bit b, the exact deterministic update is

  q' = delta(q,b),
  R' = {delta(r,b):r in R} union {delta(q,1-b)}.

The first term carries a flip that happened earlier; the second introduces a flip at the current bit.

Let T_l(q,R) count prefixes of length l with this residual state, initialized with T_0(q0,empty)=1, all other counts zero, and updated for both b=0,1 by integer additions. Then, EXACTLY,

  N_l = |X_l| = sum_{q in F, R subset Q} T_l(q,R),

  I_l = i(X_l) = sum_{q in F, R disjoint F} T_l(q,R).

Thus whenever X_l is nonempty, the previously proved repair theorem yields

  kappa_a(X_l,2)=kappa_ab(X_l,2)=N_l+I_l,
  kappa_b(X_l,1)=2*N_l,
  kappa_0(X_l,0)=5*N_l.

No enumeration of whole suffix words is needed to calculate these counts. The transition has at most |Q| * 2^|Q| states, independent of the word length l. Precompute the two transitions for each reachable (q,R); exact count propagation takes O(l*|Q|*2^|Q|) integer additions for a fixed automaton, with integer bit length O(l) in the worst case. Constructing and storing the transition table has a state-set processing cost up to O(|Q|^2*2^|Q|); sparse reached states can be used. This is a state-complexity bound, not a bit-operation count hiding unbounded integer width.

### Proof

Induct on the prefix length. At length zero the formula for q and R holds by definition. For u followed by b, every word at Hamming distance exactly one from ub changes either (i) one position of u, then appends unchanged b, producing the set {delta(r,b):r in R(u)}, or (ii) the final position, producing delta(q(u),1-b). These cases exhaust all one-bit flips and yield precisely R'. The recurrence therefore stores the exact readout equivalence class for the membership/existence-of-one-flip-neighbor observers.

For a length-l word w, membership in X_l is exactly q(w) in F. A Hamming-one neighbor of w lies in X_l if and only if some r in R(w) belongs to F. Therefore accepted isolated words are exactly q in F with R disjoint F. Summing their multiplicities in T_l proves the displayed counts. Inserting them into the already proved exact library theorem yields the library-size formulas. QED.

### Observer-fidelity boundary

The quotient (q,R) retains the existence of one accepted Hamming-one neighbor, and hence the exact repair-library CARDINALITY observable. It does not retain the distinct flip positions or the multiplicities of states in R. To calculate the number of accepted Hamming-one neighbors, a multiset/count vector would be required. This is an exact, horizon/observer-specific residual descent statement under the joint-relation preservation contract; no wider collapse is asserted.

## Two deterministic examples

1. Fibonacci/no-adjacent-11 language. Use Q={previous0,previous1,dead}; start previous0; transition previous0: 0->previous0,1->previous1; previous1: 0->previous0,1->dead; dead absorbs; F={previous0,previous1}. The residual automaton yields N_l=F_(l+2) and I_l=0 for all l>=1. Thus kappa_a=kappa_ab=F_(l+2).

2. Constant-bit language, X_l={0^l,1^l} for l>=1. Use four states {start,zeros,ones,dead}, transitions start->zeros/ones, zeros->zeros/dead, ones->dead/ones, dead absorbs, with F={zeros,ones}. It yields N_l=2, I_1=0, I_l=2 for l>=2. Hence kappa_a=kappa_ab=2 when l=1 and 4 when l>=2. This is a finite-state family with the isolated-vertex correction persisting for all lengths, despite constant language cardinality.

## Executed exact verification

VERIFY_DFA_ONE_FLIP_RESIDUAL.py recomputes N_l and I_l from the residual automaton and independently by listing all binary words at finite lengths. All complete two-state binary DFAs are checked: 2^(2*2)=16 transition tables, 2 initial states, 4 accepting sets and lengths l=0..7, total 1,024 exact comparisons. It also tests 300 fixed-seed three-state DFA instances at lengths 0..6 (2,100 comparisons), all Fibonacci-family lengths l=1..22, and constant-bit-family lengths l=1..19. All assertions passed locally: PASS_R5_DFA_ONE_FLIP_OBSERVER. The finite tests supplement the induction proof. No external literature claim or independent reviewer acceptance is asserted.

## New question

For a weighted finite-state suffix interaction where selecting an admissible word affects both core optimizer costs and the set of old/new optimum paths, identify the smallest exact transfer state preserving the minimax repair quantifier order. A candidate state carries (core optimizer type, automaton state, best overlap vector, provenance of admissible branch). Test the candidate against small explicit weighted examples before any quotient.
