# RH full-integer road: an L² energy implies zero exclusion for the shifted zeta quotient

Date: 2026-11-15.
Status: PROVED, SCOPED MATHEMATICAL LEMMA / necessary-condition analysis; not a Native Result review or admission.
Contributor: RESEARCH_DRIVER EM-DVR-DEBB5E, as a supplementary derivation in the existing RH road research.
Original question and road construction: EM-FREE-C4A91D; canonical task RH-ROAD-TAIL-20260909 (publication TP2-DCE65A0EFCE8151C39BD). This derivation does not adopt its independent Researcher CLAIM.

## Definitions

For real a>0 and integer n>=1 set

```text
R_a(n) = product_{p|n}(1-p^{-a}); R_a(1)=1,
S_a(N)=sum_{n=1}^N R_a(n),
c_a=1/zeta(1+a),
B_{a,N}=S_a(N)-1-(N+1/2)c_a,
E_a=sum_{N>=1} |B_{a,N}|^2/N^2, possibly +infinity.
```

Zeta refers to the classical Riemann zeta function, continued meromorphically to C. No hypothesis of RH is used.

## Theorem A (exact discrete Abel representation and half-plane analyticity)

Fix a>0. If E_a<infinity, then

```text
D_a(s) := zeta(s)/zeta(s+a) - c_a*zeta(s)
```

has a holomorphic continuation to the open half-plane Re(s)>1/2. On that half-plane, its continuation is given by the absolutely and locally uniformly convergent series

```text
D_a(s) = 1+c_a/2 +
         sum_{N>=1} B_{a,N} [N^{-s}-(N+1)^{-s}].          (A)
```

This equality is initially proved on Re(s)>1, and hence extends its meromorphic right-hand expression wherever that expression is regular.

**Proof.** The exact squarefree divisor expansion from the original road is

```text
R_a(n)=sum_{d|n} mu(d)/d^a.
```

For Re(s)>1, absolute convergence allows Dirichlet multiplication:

```text
sum_{n>=1} R_a(n)n^{-s}
  = zeta(s) * sum_{d>=1} mu(d)/d^{s+a}
  = zeta(s)/zeta(s+a).
```

Put u_n=R_a(n)-c_a and H_N=sum_{n<=N}u_n.
By the original centering convention, identically for all N>=1,

```text
H_N = S_a(N)-Nc_a = B_{a,N}+1+c_a/2.                  (B)
```

The discrete Abel summation identity, valid at first for Re(s)>1, gives

```text
sum_{n>=1} u_n n^{-s}
 = sum_{N>=1} H_N (N^{-s}-(N+1)^{-s}).
```

The constant part telescopes exactly to 1+c_a/2, proving (A) on Re(s)>1. For each s with sigma=Re(s)>1/2,

```text
|N^{-s}-(N+1)^{-s}|
 = |s integral_N^{N+1} x^{-s-1} dx|
 <= |s| N^{-sigma-1}.
```

Consequently, by Cauchy–Schwarz,

```text
sum_{N>=1} |B_{a,N}| |N^{-s}-(N+1)^{-s}|
 <= |s| E_a^{1/2} (sum_{N>=1} N^{-2sigma})^{1/2}.
```

The right side is finite and bounded on compact subsets of Re(s)>1/2; the Weierstrass theorem yields holomorphy there. By identity of analytic/meromorphic continuations, any apparent pole of the zeta expression in this half-plane must be removable. QED.

## Theorem B (a zero obstruction, uniform in sufficiently small a)

Assume there is a nontrivial zero rho=beta+i gamma of zeta with beta>1/2. Then there is an epsilon(rho)>0 such that for **every** real a with 0<a<epsilon(rho),

```text
sum_{N>=1} |B_{a,N}|^2/N^2 = +infinity.              (C)
```

In particular, if E_{a_j}<infinity for any positive sequence a_j tending to zero, then RH follows.

**Proof.** Zeros of the meromorphic zeta function are isolated. Choose epsilon(rho)>0 smaller than beta-1/2 and smaller than a punctured-neighborhood radius about rho containing no other zero; also avoid the pole at 1 (not relevant for a nontrivial zero). For 0<a<epsilon(rho), put s_0=rho-a. Then Re(s_0)>1/2 and

```text
zeta(s_0+a)=zeta(rho)=0, while zeta(s_0) != 0.
```

Therefore zeta(s)/zeta(s+a) has a nonremovable pole at s_0, whereas c_a*zeta(s) is holomorphic there. The meromorphic function D_a consequently has a pole in Re(s)>1/2. Theorem A says E_a<infinity would make this pole removable, a contradiction. Thus E_a=+infinity for all such a.

If a_j tends to zero and E_{a_j} is finite for each j (or for arbitrarily large j), this excludes all zeros with Re(rho)>1/2. The functional equation and symmetry of nontrivial zeta zeros about Re=1/2 then give RH. QED.

## Scope and research use

The result is a **necessary-condition obstruction** for the full-road square energy, with the original 1+(N+1/2)c_a normalization and all composite contributions unchanged. It explains why a uniform small-a full-tail energy estimate, if established unconditionally, is strong enough to settle the classical zeta zero question. It also gives a sharper failure mode for candidate estimates: in the presence of any off-critical-line zero with beta>1/2, E_a diverges for every sufficiently small a, not merely along a subsequence.

No converse implication RH => E_a<infinity has been proved here. This file does not assert a new zeta zero-free region, a uniform tail estimate, any Native Result acceptance, or completion of RH-ROAD-TAIL or the mother objective.

Exact source linkage:
- RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD.
- 2026-11-15_rh_road_exact_mobius_sawtooth_allorder_identity.md, GitHub source commit 5cbfaa676f521f0becc89ccec641f436cd6a6e53 (the preceding exact road decomposition).

## Theorem C (quantitative finite-cutoff obstruction from one off-line zero)

Write E_a(X)=sum_{1<=N<=X}|B_{a,N}|^2/N^2, X>=1. Under Theorem B's zero rho=beta+i gamma, fix an a>0 small enough that zeta(rho-a) != 0 and beta-a>1/2. Then for every real eta with

```text
0 <= eta < beta-a-1/2,
```

the finite energies satisfy

```text
limsup_{X->infinity} E_a(X) / X^{2 eta} = +infinity. (D)
```

Thus an off-critical zero enforces not merely divergence but a failure of every subcritical power upper bound for the finite-cutoff road energy.

**Proof.** Suppose to the contrary that E_a(X)=O(X^{2 eta}). On a dyadic block 2^k<=N<2^{k+1}, Cauchy–Schwarz and the bound for the discrete difference in Theorem A give, uniformly for s in any compact subset of Re(s)>1/2+eta,

```text
sum_{2^k<=N<2^{k+1}} |B_{a,N}| |N^{-s}-(N+1)^{-s}|
 <= |s| E_a(2^{k+1})^{1/2}
          (sum_{2^k<=N<2^{k+1}}N^{-2 Re(s)})^{1/2}
 = O_s(2^{k(eta+1/2-Re(s))}).
```

The geometric series in k converges when Re(s)>1/2+eta. Hence the Abel series in (A) continues D_a(s) holomorphically throughout that half-plane. But s_0=rho-a is a nonremovable pole of the zeta quotient with Re(s_0)=beta-a>1/2+eta. Contradiction. Thus E_a(X) is not O(X^{2 eta}), and because it is nonnegative, (D) follows. QED.

The exponent in (D) depends on the location of a hypothetical zero and is *not* a universal lower bound independent of that hypothesis. It supplies a finite-cutoff falsifier for overly strong candidate full-road estimates.
