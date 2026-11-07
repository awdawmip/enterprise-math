# PREFIX-576 — Exact third and fourth gate-cumulant rates from a rank-one BRC perturbation

Status: 'AUTHOR_PROVED / EXACT_RATIONAL_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED'  
Date: '2026-11-08'  
Research line: 'native X6-BRC / four-STAR gate-count observer'  
Scientific input pin: 'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d'  
Read snapshot: 'awdawmip/enterprise-math main@4efef1592c0e576b11478352e8ca97c835ebd3ee'  
Global rules snapshot: 'awdawmip/chatgpt-global-knowledge main@62997f6f5f12aedef46edebad1dc16b15252c8ec'

## 1. Question and scope

PREFIX-575 established the exact first and second asymptotic cumulant rates of the native gate count when all six BRC weights are specialized to one. This continuation asks whether the same gate-preserving BRC quotient and Poisson method can produce higher cumulants without changing the frozen native input.

The model is the frozen four-STAR native X6-BRC kernel:

- 48 native phases;
- 96 ordered branch ports;
- six labeled actions from each port;
- three gate-marked native edges;
- the exact 37-class quotient retaining the gate mark;
- observer 'q1=q2=q3=q4=q5=q6=1', with the gate counter retained.

A path of depth 'd' means 'd' ordered native actions. It is not physical time, a heartbeat interval, or a solver iteration. The initial distribution for the finite-moment check is the pushforward of the uniform distribution on the 96 native ports, namely 'pi_i = class_size_i / 96'.

The result is restricted to this exact gate-count observer. It does not reintroduce the parameters 'x=q5', 'y=q6', or 'u=x+y', 'v=xy'.

## 2. Exact BRC quotient and rank-one gate update

Let 'C' be the 37-by-37 integer transition-count matrix of the gate-preserving quotient. Each row sums to six. Let 'g' be the indicator of the three quotient source classes and let 'e_5' select the common target class.

The exact marked quotient edges are:

\[
4\to5,\qquad 15\to5,\qquad 17\to5,
\]

each with multiplicity one and with the two retained marginal exponents equal to zero. There are no other marked quotient edges.

Consequently, for the row-stochastic matrix \(P=C/6\), the gate-marked transfer matrix is exactly

\[
\boxed{P(z)=P+(z-1)\frac{g e_5^{\mathsf T}}6.}
\]

This is a rank-one perturbation derived from the actual marked BRC action table, not an assumed gate approximation.

The class-size vector is

\[
(8,4,2,1,1,2,2,8,4,2,4,4,2,4,1,1,1,1,2,2,4,2,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2),
\]

whose sum is 96. The exact stationarity identity is

\[
\sum_i s_i C_{ij}=6s_j,
\]

so \(\pi_i=s_i/96\) is stationary. The gate-source mass is

\[
\pi(g)=\frac{3}{96}=\frac1{32},
\]

and the one-step gate rate is therefore

\[
a=\frac{\pi(g)}6=\frac1{192}.
\]

The quotient support is strongly connected and bipartite with block sizes 17 and 20. A verified 2-cycle gives period exactly two. For every real 'z>0', the gate update preserves support and hence irreducibility and period.

## 3. Rank-one secular equation

For \(\lambda\) outside the spectrum of \(P\), the matrix determinant lemma gives

\[
\det(\lambda I-P(z))
=
\det(\lambda I-P)
\left(
1-(z-1)R(\lambda)
\right),
\]

where

\[
R(\lambda)=\frac16 e_5^{\mathsf T}(\lambda I-P)^{-1}g.
\]

Let \(\lambda(z)\) be the Perron eigenvalue branch through \(\lambda(1)=1\). For 'z' near one and 'z != 1', it satisfies the exact secular equation

\[
1=(z-1)R(\lambda(z)).
\]

Write \(\epsilon=\lambda-1\). With \(\Pi=\mathbf1\pi^{\mathsf T}\), the resolvent on the complementary subspace has the exact Laurent expansion

\[
(\lambda I-P)^{-1}
=
\frac{\Pi}{\epsilon}
+(I-P)^\#
-\epsilon((I-P)^\#)^2
+\epsilon^2((I-P)^\#)^3
+O(\epsilon^3),
\]

where '#' denotes the group inverse. Therefore

\[
R(1+\epsilon)
=
\frac{a}{\epsilon}+r_0+r_1\epsilon+r_2\epsilon^2+O(\epsilon^3),
\]

with

\[
r_0=\frac16 e_5^{\mathsf T}(I-P)^\#g,\quad
r_1=-\frac16 e_5^{\mathsf T}((I-P)^\#)^2g,\quad
r_2=\frac16 e_5^{\mathsf T}((I-P)^\#)^3g.
\]

## 4. Exact integer Poisson certificates

Put \(L=6I-C\). The following integer vectors 'X', 'Y', 'Z' are stored in the companion certificate. They satisfy

\[
LX=2304g-72\mathbf1,\qquad
LY=72X,\qquad
LZ=72Y,
\]

and each has zero weighted mean:

\[
\sum_i s_iX_i=\sum_i s_iY_i=\sum_i s_iZ_i=0.
\]

Thus 'X/384', 'Y/4608', and 'Z/55296' are the successive mean-zero group-inverse potentials for \(g-\pi(g)\mathbf1\). Strong connectivity makes the mean-zero solution unique.

At the target class '5', the exact entries are

\[
X_5=-19,\qquad Y_5=-79,\qquad Z_5=5801.
\]

It follows that

\[
\boxed{r_0=-\frac{19}{2304},\quad
r_1=\frac{79}{27648},\quad
r_2=\frac{5801}{331776}.}
\]

The companion program also rechecks all 37 rows of the PREFIX-575 first and second Poisson identities, including the exact quadratic-variation total '1731072'. This anchors the new higher-order calculation to the already-published first/second-order result.

## 5. Cumulant-rate derivation

Let \(\delta=z-1\), and write

\[
\lambda(z)=1+c_1\delta+c_2\delta^2+c_3\delta^3+c_4\delta^4+O(\delta^5).
\]

Substitution into \(1=\delta R(1+\epsilon)\) gives

\[
\begin{aligned}
c_1&=a,\\
c_2&=ar_0,\\
c_3&=ar_0^2+a^2r_1,\\
c_4&=ar_0^3+3a^2r_0r_1+a^3r_2.
\end{aligned}
\]

For the gate count \(K_d\), the scaled cumulant generating function is

\[
\psi(s)=\lim_{d\to\infty}\frac1d
\log\mathbb E[e^{sK_d}]
=\log\rho(P(e^s)).
\]

The finite graph is irreducible of period two. Its square restricted to either cyclic class is primitive (the verified 2-cycle supplies a loop in the square); the positive Perron branch therefore controls the exponential growth for each parity. The parity-dependent positive prefactor is analytic near zero and contributes only \(O(1/d)\) to the scaled log and its first four derivatives. Hence the asymptotic cumulant rates are \(\kappa_j=\psi^{(j)}(0)\).

Expanding \(\log(1+\epsilon(e^s-1))\) yields

\[
\boxed{\begin{aligned}
\kappa_1&=\frac1{192},\\
\kappa_2&=\frac{1127}{221184},\\
\kappa_3&=\frac{206963}{42467328},\\
\kappa_4&=\frac{434651857}{97844723712}.
\end{aligned}}
\]

Equivalently,

\[
\boxed{
\psi(s)=
\frac{s}{192}
+\frac{1127s^2}{442368}
+\frac{206963s^3}{254803968}
+\frac{434651857s^4}{2348273369088}
+O(s^5).
}
\]

The first two rates reproduce PREFIX-575. The third and fourth rates are the new increment.

For comparison only, an iid Bernoulli process with the same mean \(p=1/192\) would have rates

\[
\kappa_2^{iid}=\frac{191}{36864},\quad
\kappa_3^{iid}=\frac{18145}{3538944},\quad
\kappa_4^{iid}=\frac{1137023}{226492416}.
\]

All three differ from the BRC gate rates. This is a precise non-iid diagnostic; it is not by itself a claim about a physical correlation mechanism.

## 6. Exact finite verification

The companion checker reconstructs the exact 96-port action table through the published PREFIX-565 kernel and the exact 37-class gate quotient through PREFIX-566. It verifies:

- all 96 ports have six outgoing and six incoming actions;
- the three native gate edges are exactly '(7,9)', '(29,9)', '(31,9)';
- all nine frozen roots produce the same retained marginal gate rows;
- quotient refinement growth is '[1,4,13,21,33,37]';
- all 37 quotient rows sum to six and the class-size stationary identity holds;
- the marked quotient edges are exactly the three rank-one edges above;
- strong connectivity, bipartition '(17,20)', and period two;
- 37/37 rows of each of the first, second, and three higher integer Poisson identities;
- exact stationary-initial raw-moment DP through depth 128 for moment orders 1–4.

At depth 'd', the exact path count is '96*6^d'. The depth-128 run checks

'385151223796572526086245125219434606018278638823213973691750235774923749432850295860047477336478580736'

ordered native paths. The exact per-depth cumulant fractions are in 'PREFIX576_GATE_CUMULANT_RESULTS.json'. All assertions pass.

The finite DP is a cross-check of the integer implementation, not the proof of the asymptotic limits. The limits follow from the rank-one secular equation, the exact Poisson certificates, and the finite irreducible periodic Perron argument.

## 7. BRC reuse and boundaries

'COMPOSE_APPLIED':

- 'PREFIX565_positive_marginal_certificate.py' — frozen 48-phase/96-port native X6-BRC edge and signed-axis marginal definition;
- 'PREFIX566_gate_quotient_certificate.py' — exact 37-class quotient retaining gate provenance;
- 'PREFIX575_gate_count_poisson_certificate.py' — existing first/second Poisson potentials and variance identity;
- rank-one matrix determinant lemma — applied to the exact gate-marked BRC quotient, not substituted for the native transition kernel.

No new top-level BRC family is claimed. No classical trigonometry, pi expansion, Taylor/Padé/Cayley propagation, floating-point scientific update, or physical-time interpretation is used. Exact rational algebra is a derived observer on the actual typed BRC transition table.

The result does not establish a physical gate law, physical time calibration, instantaneous transmission, Shor speedup, or a general 'x,y'-weighted theorem.

## 8. Provenance and actual authority

- Global rules read from 'chatgpt-global-knowledge main@62997f6f5f12aedef46edebad1dc16b15252c8ec'.
- Current global bootstrap blob: 'bc9e1b3065eae7947850a0aa2261dc201a43265c'.
- Current operating manual blob (unchanged at refreshed head): '9ce8584221f83f3de369af7239b029e4b36621c4'.
- ACTIVE worldview markdown blob: '99238c3466eb0805748bae01fd1a20868a5a351e'.
- BRC priority policy blob: '721ea6b559ca8a4ac11c7ed90e715219581d319b'.
- Portable research protocol blob: '5633f5fa72097fb4d6afcf7ff23a0df3797fd4d0'.
- Continuation protocol blob: '79002ab20e30abb464837dc4c980cf5b5b68e001'.
- Research activity policy blob: '66013afd6646b94f2da4e51e1978c0ec830e5512'.
- Project source read from 'enterprise-math main@4efef1592c0e576b11478352e8ca97c835ebd3ee'.
- P000 V5 blob: 'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'.
- Heartbeat World contract blob: '94a02d067be2b039ca4c0f7ffedb5ebde8430e08'.
- Global/project BRC-only machine mirror blob: '62ffa6bbdafd54496e27284a26a2aeaf2d04df99' (identical).
- PREFIX-565 blob: '7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41'.
- PREFIX-566 blob: '7b6613193847e4123cd0ac11107eb9b9c70290c8'.
- PREFIX-575 note blob: '416557a45ae90ec04bc10388e457feae48184631'.
- PREFIX-575 checker blob: 'f80228126d1f015615d7324bbde36f13c5b4e84b'.
- PREFIX-575 results blob: '9f2fcf9deb8f46ff8aa3ec94d7c4029830376b34'.
- Scientific input pin: 'f42f2906d77f24085c123f3ccfe9667d41caa96d'.

The project router states that the global P000 startup projection is V4 and does not replace Source V5; the full current Source V5 file and its mandatory companions were therefore loaded. The active worldview and the project portable research protocol were read. The native EM status, context manifest, dispatch, and session-start operations did not provide a native researcher session or current owner. GitHub identity 'awdawmip' was verified with 'admin' permission on both repositories; that is repository permission, not an EM Researcher-ID, Owner, CLAIM, Result, or review authority.

This is an unshared author-side derivation. It is not registered as a formal task/activity, claimed, reviewed, merged, admitted, or promoted. The persisted branch is a durable research frontier only.

## 9. Next question

Compute the exact rational secular function \(R(\lambda)\), or continue the mean-zero group-inverse chain to obtain \(\kappa_5\) and \(\kappa_6\) with independent finite-depth moment checks. In parallel, reopen the parameterized observer 'x=q5', 'y=q6', 'u=x+y', 'v=xy' and determine whether the gate-sensitive Poisson potential admits a coefficientwise nonnegative lift; if not, produce the smallest exact finite witness and preserve the source fiber.

The next step must keep the same frozen scientific input pin and exact gate/source provenance. Native Owner/CLAIM/Result and independent review remain separate pending control work.
