# D25 portable research: m-shift valuation wall of the single symmetric-Beta observer

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

This unit continues the portable upper B-chart lane. It identifies the first exact obstruction encountered when the new single symmetric-Beta terminal observer is transported in (m).

## Source boundary

- GLOBAL_KNOWLEDGE_V1 current main: `688f64b4be0b0594f5a3774bbf88171080ea322e`.
- Enterprise Math current main: `88e814717bd60144e6a5add07fc4ab596d483b62`.
- Canonical D25 local-progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- Portable branch head immediately before this write: `4acdf4061835a363d110ef275bdb536d142c9676`.
- Durable predecessor: `research_notes/d25_b_chart_single_symmetric_beta_terminal_observer_20260930.md`.

## 1. Polynomial-state increment

The predecessor defines, with
[
n=2m-1,
]
the symmetric polynomials
[
C_0(Y)=2,qquad C_1(Y)=1,qquad
C_k(Y)=C_{k-1}(Y)-YC_{k-2}(Y),
]
and
[
P_m^{(D)}(Y)
=
rac12
sum_{j=0}^{2m-2}
rac{2^{-j}}{j+4/3}C_j(Y).
	ag{1}
]

Passing from (m) to (m+1) adds precisely the (j=2m-1) and (j=2m) rows:
[
egin{aligned}
P_{m+1}^{(D)}-P_m^{(D)}
={}&
rac12
rac{2^{-(2m-1)}}{2m-1+4/3}C_{2m-1}(Y)\
&+
rac12
rac{2^{-2m}}{2m+4/3}C_{2m}(Y).
end{aligned}
]
Therefore
[
oxed{
P_{m+1}^{(D)}-P_m^{(D)}
=
rac{3,2^{-2m}}{6m+1}C_{2m-1}(Y)
+
rac{3,2^{-2m-1}}{6m+4}C_{2m}(Y).
}
	ag{2}
]

For the target prime
[
p=6m+1,
]
the first term of (2) is a genuine simple (p)-adic pole. The second is (p)-integral.

The other two polynomial components (P^{(V)}) and (P^{(W)}) from the predecessor acquire no (p)-denominator at this step. Hence the sole (p)-pole in the transported terminal polynomial
[
Phi_{m+1}
]
comes from the (P^{(D)}) coefficient (1/8).

Thus the polynomial-valued residue is
[
oxed{
operatorname{Res}^{mathrm{poly}}_p(Phi_{m+1})
=
rac38,2^{-2m}C_{2m-1}(Y).
}
	ag{3}
]

This is an exact valuation-wall statement, not an asymptotic observation.

## 2. Beta-measure transport

Let
[
mathbb E_m[cdot]
]
denote expectation under the algebraic Beta carrier
[
operatorname{Beta}(m+1,m+1).
]
Since its unnormalized weight is (Y^m),
[
oxed{
mathbb E_{m+1}[f(Y)]
=
rac{2(2m+3)}{m+1},
mathbb E_m[Yf(Y)].
}
	ag{4}
]

At the singular step in (3), however, only the residue under the next measure is needed.

Because
[
C_{2m-1}(Y)=X^{2m-1}+(1-X)^{2m-1}
]
and the (operatorname{Beta}(m+2,m+2)) carrier is symmetric,
[
oxed{
mathbb E_{m+1}[C_{2m-1}(Y)]
=
2rac{(m+2)_{2m-1}}{(2m+4)_{2m-1}}.
}
	ag{5}
]

Therefore the scalar (p)-pole residue of the transported terminal observer is
[
oxed{
mathcal V_m
=
rac34,2^{-2m}
rac{(m+2)_{2m-1}}{(2m+4)_{2m-1}}.
}
	ag{6}
]

All factors in (6) are (p)-units.

## 3. Universal residue (6)

Write
[
A_m:=
rac{(m+2)_{2m-1}}{(2m+4)_{2m-1}}
=
rac{(3m)!(2m+3)!}{(m+1)!(4m+2)!}.
	ag{7}
]

The durable Q-endpoint note already proves
[
R_m:=
rac{inom{3m}{m}}{inom{4m}{2m}}
=
rac{(3m)!(2m)!}{m!(4m)!}
equiv4^mpmod p.
	ag{8}
]

Their exact ratio is
[
rac{A_m}{R_m}
=
rac{2(2m+1)(2m+3)}
{(4m+1)(4m+2)}.
	ag{9}
]
Modulo (p=6m+1),
[
2m+1equivrac23,qquad
2m+3equivrac83,
]
[
4m+1equivrac13,qquad
4m+2equivrac43.
]
Hence
[
oxed{
rac{A_m}{R_m}equiv8pmod p.
}
	ag{10}
]
Combining (8) and (10),
[
oxed{
A_mequiv8cdot4^m=2^{2m+3}pmod p.
}
	ag{11}
]

Substitute (11) into (6):
[
oxed{
mathcal V_m
equiv
rac34,2^{-2m},2^{2m+3}
=6
pmod p.
}
	ag{12}
]

Thus the first (m)-transport step of the single symmetric-Beta observer crosses a valuation wall with a **universal nonzero divided residue**
[
oxed{6.}
]

## 4. Consequence for the next proof strategy

The predecessor safely compressed the terminal upper-chart observer to one symmetric-Beta polynomial moment at fixed (m).

Equation (12) proves that this quotient is **not** naively (m)-transportable through the next cutoff: the (m	o m+1) operation exposes a hidden row with denominator
[
2m-1+rac43=rac{6m+1}{3}=rac p3.
]

Therefore an induction/contiguous proof in (m) must retain at least the valuation-wall residue (3), or equivalently its scalar readout (6), before reducing modulo (p). Treating (mathbb E_m[Phi_m]) as an ordinary (p)-integral scalar sequence across the shift would erase exactly this information.

This is a BRC lease failure, not a failure of the fixed-(m) terminal compression.

## 5. BRC / toolbox disposition

Population:
- fixed-(m) symmetric Beta carrier;
- the two newly exposed rows under (m	o m+1);
- the pole row (C_{2m-1}(Y)).

Observer at fixed (m):
[
mathbb E_m[Phi_m].
]

Future operation now tested:
[
mmapsto m+1.
]

New information exposed:
- valuation (-1) at the (D)-channel boundary;
- polynomial residue ((3/8)2^{-2m}C_{2m-1}(Y));
- scalar residue (6mod p).

Hence the fixed-(m) quotient does not descend through the (m)-shift unless this repair port is retained.

Tool resolution:
[
oxed{	exttt{COMPOSE_APPLIED}}
]
using `T0_BRC` residual transport, `T1_SCALE_ENUMERATION_VALUATION` valuation-wall extraction, and `T6_OPERATION_SAFE_QUOTIENT` lease audit.

## 6. Independent regression

For every prime
[
p<10000,qquad pequiv1pmod6
]
(611 primes), the scalar residue (6) was independently evaluated modulo (p).

Result:
[
oxed{611/611:quad mathcal V_mequiv6pmod p.}
]

The finite check is regression only. Equation (12) is proved from the exact ratio (9) plus the durable all-prime endpoint quotient (8).

## 7. Next exact unit

Do not attempt a regular (m)-recurrence that silently reduces through the pole.

The next unit is a **regularized (m)-transport**:
1. subtract the explicit pole row (3);
2. transport the remaining (p)-integral finite part under (4);
3. compare that finite part with the durable endpoint digit (delta_p) / first-wall coordinate;
4. if an additional finite part survives, retain it as the next repair coordinate.

This is now a one-wall regularization problem with known residue (6), rather than an unspecified recurrence search.

