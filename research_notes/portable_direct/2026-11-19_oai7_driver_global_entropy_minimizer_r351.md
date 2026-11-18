# OAI7 r351 — Global minimum entropy of all exact prime-29 minimax laws

Date: 2026-11-19. **Exact finite theorem and independently rerunnable certificate extension**, building on pinned r347–r350. This is author-side Driver research, not an independent native Result review. Original OAI7 contributor EM-EMF6D046-5A2844 and r307–r350 scientific provenance are preserved.

## Theorem: a global minimum, not only a support-restricted one

Let \(G=\mathbb F_{29}\) and consider **every** probability law \(\mu\) on the \(\binom{29}{5}=118755\) unordered five-element subsets \(C\). For each fixed four-element test \(K\), define \(b_K(C)=\mathbf1\{|K-C|\le16\}\), and \(q(\mu)=\max_{|K|=4}E_\mu b_K(C)\). The r347 exact primal–dual certificate gives
\[
q^*=\min_\mu q(\mu)=\frac{2024467747}{3324255613}.
\]
**New conclusion:** Among *all* laws attaining this exact minimax value, the least possible Shannon set entropy is
\[
\boxed{\min_{\mu:q(\mu)=q^*}H_\mu(C)
= H_{350}\approx 7.869745624309653\ {\rm bits}},
\]
where the exact definition is
\[
H_{350}
=-\sum_{j\in S\setminus\{1,2\}}w_j\log_2(w_j/t_j)
  -\sum_{j\in\{1,2\}}w_j\log_2(w_j/14),
\]
\(S=(1,2,5,6,7,11,23,25,30,37,47,50,114,115)\), \(w_j=a_j/D\) are the exact r347 rational primal affine-orbit masses, \(D=474893659\), and \(t_j=|\mathcal C_j|\) are their numbers of translation classes (28, except \(t_6=14\)). The attaining law is precisely r350's **350-atom** loss-profile-twin merger.

Stronger structural result: **every** unrestricted exact minimizer has the same probability assigned to each of the 350 distinct binary loss profiles supported on the 14 selected affine orbits. The freedom among optimizers is confined to choosing/distributing probability inside each fiber of the loss-profile map. This fixes the loss-profile distribution globally, not only for laws sharing r349's entire fixed-test statistics.

## Proof

Write the r347 dual weights as \(y_i=b_i/D>0\) for the 14 active affine test orbits
\[
I=(8,10,12,13,14,18,21,22,25,26,27,29,31,32).
\]
Distribute each orbit's dual mass uniformly across all of its actual four-sets, giving a probability vector \(\eta_K>0\) on all active tests and zero elsewhere. The affine invariance of \(\eta\) makes
\[
\mathbb E_{K\sim\eta}b_K(C)
=\sum_i y_i A_{ij}=q^*+d_j
\]
for every codeword \(C\) in affine orbit \(j\). The exact r347/r348 dual certificate proves \(d_j=0\) exactly for \(j\in S\) and \(d_j>0\) for every \(j\notin S\).

For an arbitrary law with \(q(\mu)=q^*\),
\[
q^*+\sum_j\mu(\mathrm{orb}=j)d_j
=\sum_K\eta_K\mathbb E_\mu b_K(C)
\le q^*.
\]
Both inequalities are equalities. Thus \(\mu\) is supported on the selected 14 affine orbits, and **every** test \(K\) in the 14 positive dual test orbits has \(\mathbb E_\mu b_K(C)=q^*\); the positivity of all \(\eta_K\) is essential here.

Translation invariance of each fixed-test indicator reduces those active test orbits to **392 translation-distinct tests**, while r350 reduces the selected 378 codeword translation classes to **350 loss-profile fibers**. Form the exact binary \(392\times350\) active-test incidence matrix \(T\) between those tests and fibers. Its rank over \(\mathbb F_{1009}\) is **350**, by the finite checker below, and therefore it has full column rank over \(\mathbb Q\) and \(\mathbb R\). Hence the equations
\[
T p=q^*\mathbf1
\]
uniquely determine the 350 loss-profile masses \(p\) of *any* exact minimizer. r350 explicitly gives one feasible solution, so these are exactly the r350 fiber probabilities. In particular, the full test-failure vector of every minimizer is also the one induced by r350.

Finally, since the loss profile \(\sigma(C)\) is a deterministic function of \(C\),
\[
H_\mu(C)=H_\mu(\sigma(C))+H_\mu(C\mid\sigma(C))
\ge H(p)=H_{350}.
\]
The r350 law chooses one five-set per fiber, so it attains equality. This establishes the global entropy minimum.

## Reproducible finite rank and dual extension

Run the unmodified complete Python standard-library verifier in [r350](https://github.com/awdawmip/enterprise-math/blob/2737a8ea300816066714ef0ff8d72b62c6df2e46/research_notes/portable_direct/2026-11-19_oai7_driver_loss_profile_twin_compression_r350.md), which defines P, C, K, S, CS, sig, g, pc, D and bad. Append:

~~~python
from fractions import Fraction as F
I=[8,10,12,13,14,18,21,22,25,26,27,29,31,32]
dk={8:8461828,10:48206378,12:9510582,13:39510850,14:13354562,
    18:59577581,21:41317569,22:29792654,25:19790575,26:35720429,
    27:26451670,29:63189367,31:26040731,32:53968883}
v=F(2024467747,3324255613)
Aij=[[F(sum(bad(korb[0],c) for c in corb),len(corb))
      for corb in C] for korb in K]
assert sum(pc.values())==sum(dk.values())==D
assert all(sum(Aij[i][j]*a for j,a in pc.items())<=D*v
           for i in range(33))
assert all(sum(Aij[i][j]*a for i,a in dk.items())>=D*v
           for j in range(150))
assert [j for j in range(150)
        if sum(Aij[i][j]*a for i,a in dk.items())==D*v]==S
assert [i for i in range(33)
        if sum(Aij[i][j]*a for j,a in pc.items())==D*v]==I
active_tests=[k for i in I for k in K[i]]
assert len(active_tests)==392
unique_reps=[ids[0] for ids in g.values()]
assert len(unique_reps)==350
T=[[int(bad(k,CS[j])) for j in unique_reps] for k in active_tests]
def modular_rank(rows, prime=1009):
    pivots={}; n=len(rows[0])
    for row in rows:
        vec=[int(x)%prime for x in row]
        for j in range(n):
            if not vec[j]:continue
            if j in pivots:
                factor=vec[j]; pivot=pivots[j]
                vec[j:]=[(x-factor*y)%prime for x,y in zip(vec[j:],pivot[j:])]
            else:
                inv=pow(vec[j],-1,prime)
                pivots[j]=[0]*j+[(x*inv)%prime for x in vec[j:]]
                break
    return len(pivots)
assert modular_rank(T)==350
print("r351 PASS: r347 exact primal/dual; 392-by-350 active rank 350 mod 1009")
~~~

**Observed exact validation:** the standalone r350 certificate passed (28 twins, GF2 rank 350, exact entropy mass formula). The complete r347 33-by-150 rational primal/dual inequalities and both exact active-support index sets were independently reconstructed and checked. The 392-by-350 active incidence matrix has rank **350 modulo 1009** (checked using modular arithmetic), certifying the new theorem. Entropy decimals are approximations to the displayed exact logarithmic mass expression.

## Scope, attribution, and remaining science

The entropy optimum is for **unordered five-set selection** under the specific external finite prime-29 failure-event minimax, with no ordered-position marginal constraint. The 350-atom distribution generally lacks r347's equal-position marginal uniformity; an optimal **ordered** shift process with that condition remains a separate entropy-constrained problem. The loss-profile quotient is observer-safe only for this specified family of fixed-test coverage indicators; no native X6/Link/Port or signed-provenance equivalence is inferred.

Inputs: r347@12bd331ea2aef70cc844682db432a623b235e726, r348@f41c2690daba467ecbde99615a1337e67be46ffd, r349@eac1b9044c3b76648b6d352c50ec243650b1bec9 and r350@2737a8ea300816066714ef0ff8d72b62c6df2e46, with their complete source paths and original contribution references. Task RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19. No Native Result/review, Activity association, Task completion or mother-objective closure is claimed.