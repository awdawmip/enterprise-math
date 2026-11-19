# EC49FUE — A 17-trial rational counterexample to the endpoint minimax saddle

Date: 2026-11-20. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**. This is an independent portable research note, not a native Task Result, review, or P000 alteration.

## Exact inherited model and source

Frozen scientific parent: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab (BRC16943). Immediate mathematical predecessor: EC49FUD, immutable proof at awdawmip/enterprise-math@26da0d004d175bff1ff99a7aa8e94bf029349039, path research_notes/portable_direct/EC49FUD_TWO_TRIAL_BIN_MINIMAX_THEOREM.md. All inferences below are within its **external one-sided price-clipping observer**; Bellman optimality and the native P000 world model remain at their inherited evidence levels.

Set
\[
m=\frac{1469}{64},\quad L=\frac{951}{1280},\quad U=\frac34,\quad
W=U-L=\frac9{1280},\quad E=\frac{1048576}{18958647}.
\]
The common nuisance parameter is any finite real \(e\le E\). The two hypotheses for the bin detector of width \(\delta=xW\) share the *same* \(e\):
\[
H_-:\nu_e,\qquad H_+:(1-q_e)\nu_e+q_e\delta_U,
\quad q_e=\frac{575(41217719e-2359296)}{45529434409e-2630615040},
\]
\[
p_e(x)=\Pr_e(Y=1\mid H_-)
=\frac{x[1-em(U-xW/2)]}{1-em(L+U)/2},\qquad
r_e(x)=\Pr_e(Y=1\mid H_+)=p_e+q_e(1-p_e).
\]
Here \(Y=1\{Z\ge U-\delta\}\). Conditional on \(e,H\), the \(n\) reports are independent Bernoulli variables; \(K=\sum_iY_i\) is binomial with parameter \(p_e\) or \(r_e\). Equal priors are placed on the two hypotheses, and worst-case risk means
\[
R_n^{\rm mm}(x)=\inf_{\varphi}\sup_{e\le E}
\tfrac12\bigl[\Pr_{-,e}(\varphi=+)+\Pr_{+,e}(\varphi=-)\bigr].
\]
Tests may randomize and use the entire ordered Bernoulli vector; symmetrization shows restricting to \(K\) loses no power.

## Theorem: endpoint E alone ceases to be a minimax saddle by 17 trials

For the **exact rational** choice
\[
n=17,\qquad x=\frac5{123},\qquad
\delta=xW=\frac3{10496},\qquad e_0=-1,
\]
the unique Bayes-optimal test at \(e=E\) is \(\varphi_*(K)=1\{K\ge3\}\). However its risk at \(e_0=-1\) strictly exceeds its risk at \(E\). More decisively,
\[
\boxed{R_{17}^{\rm mm}(5/123)>R_{17}^{\rm Bayes}(E,5/123)+\frac1{5250000}.}
\]
Thus the claim that a single endpoint \(e=E\) yields a minimax saddle for *every* trial count and detector width is false. The theorem does **not** assert that 17 is the smallest such count; it gives one explicit finite rational witness.

## Exact proof and finite rational certificate

Define the binomial signed mass
\[
a_{e,k}={17\choose k}\bigl[r_e^k(1-r_e)^{17-k}
                              -p_e^k(1-p_e)^{17-k}\bigr]
\quad (k=0,\ldots,17)
\]
and the threshold advantage \(D_3(e)=\sum_{k=3}^{17}a_{e,k}\). Using only rational arithmetic, the inherited formulas give
\[
\begin{array}{c|cc}
e &p_e(5/123)&r_e(5/123)\\ \hline
E&311263325/8339351907&5867068998425/13670371100129\\
-1&611675425/14983252257&43705915975225/80957043123769
\end{array}
\]
and exact signs
\[
a_{E,k}<0\ (k=0,1,2),\qquad a_{E,k}>0\ (k=3,\ldots,17).
\]
The unique pointwise Bayes rule at \(E\) is therefore \(K\ge3\), with
\[
R_E=\frac{1-D_3(E)}2\approx 0.015229461742370122.
\]
Crucially, cross-multiplication of finite rational binomial sums certifies
\[
\frac1{21000}<g:=D_3(E)-D_3(-1)<\frac1{20000}.
\]
This already proves the endpoint-optimal rule has higher risk at \(e=-1\). For a *quantitative global minimax lower bound*, consider the admissible two-point nuisance mixing law
\[
\pi(E)=\frac{124}{125},\qquad \pi(-1)=\frac1{125},
\]
drawn **once** before the two hypotheses and the 17 conditional i.i.d. observations. Its mixed signed masses are
\[
\bar a_k=\frac{124}{125}a_{E,k}+\frac1{125}a_{-1,k}.
\]
Exact finite rational verification establishes
\[
\bar a_k<0\ (k=0,1,2),\qquad
\bar a_k>0\ (k=3,\ldots,17).
\]
Consequently \(K\ge3\) is also the exact Bayes-optimal rule under this **mixture of binomials** (the mixture is not replaced by a binomial with averaged parameter). Its Bayes risk equals
\[
R_\pi=\tfrac12\left[1-\frac{124}{125}D_3(E)
                             -\frac1{125}D_3(-1)\right]
     =R_E+\frac{g}{250}
     >R_E+\frac1{5250000}.
\]
For every test \(\varphi\), \(\sup_e R_e(\varphi)\ge\mathbb E_{\pi}R_e(\varphi)
\ge R_\pi\), proving the asserted strict minimax gap. A likelihood-ratio test among ordered sequences may be symmetrized because all sample strings of a given count \(K\) have the same mass under each conditional binomial. QED.

Useful approximations (not used for the proof): \(D_3(E)-D_3(-1)\approx4.9799716332\times10^{-5}\), \(R_{-1}(\varphi_*)\approx0.015254361600536157\), \(R_\pi\approx0.01522966094123545\).

## Verification / observer and BRC-style provenance

The companion standalone Python Fraction verifier computes every \(a_{e,k}\) and \(\bar a_k\) (18 counts each), exact probabilities, the strict gap and risk lower bound. The universal statement is refuted by this **single** rational parameter/width/count configuration; no continuum search or approximate extrapolation is used. The proof relies on the parent price-model formulas and does not independently reprove the Bellman solution. No Lean checker or independent Review has been performed.

The observation carrier is (source-side clipped-port \(U\), common \(e\), uncollapsed \(q_e\), continuous \(\nu_e\), detector width, source label, sample count and iid grouping). The binomial count is a sufficient quotient for this **specific** hypothesis test due to exchangeability; it does not assert a lossless native six-axis Cell-state quotient or permit discarding the clipped-source label in other future operations.

## Remaining research question

Characterize the least-favorable **mixture of nuisance values** and exact threshold/randomization for \(n\ge3\), including rational or certified algebraic transitions in width \(x\). Determine the smallest \(n\) for which a rigorously certified counterexample exists, without promoting finite sampling as a proof of minimality. Preserve the distinct native \(z<11/16\) Bellman phase objective.

Source control: portable independent scientific preservation only; no implied formal CLAIM, protected Result or mathematical acceptance.
