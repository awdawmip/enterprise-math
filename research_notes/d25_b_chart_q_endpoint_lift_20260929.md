# D25 portable research: lifted Q-endpoint and single-digit reformulation of the upper B-chart

Status: `AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`

Contributor lineage: `EM-DIRECT-C4D02C`

This note does **not** claim a native session, CLAIM, run, canonical checkpoint, Result, review, or theorem admission. It is a portable mathematical unit intended for later canonical continuation.

## Source / non-repetition boundary

- Current Enterprise Math main observed before this write: `cb1ac1d3822fadf586cea44acaf724dcb4623a25`.
- Canonical D25 progress blob remains `51dd15a8142f3dda0506a306f9c0693a036f5891`.
- This unit does not reopen the canonical D25 Gauss-Manin representative/gauge route.
- It continues only the portable upper `B`-chart lane, whose previously proved endpoint is
  [
  Q_{2m-1}equiv-rac83pmod p,qquad p=6m+1.
  ]

## 1. Object

Let (p=6m+1>3) be prime and define
[
Q_n:=-rac{(5/6)_n}{(2/3)_n},2^{-n}.
]
The previous portable reduction uses (n=2m-1). Define its first lifted endpoint digit
[
delta_p:=rac{Q_{2m-1}+8/3}{p}pmod p.
]

The result of this note is an all-prime closed formula for (delta_p), followed by a strict reformulation of the still-open upper-(B) target.

## 2. Pochhammer lift through (p^2)

Because
[
rac56=m+1-rac p6,qquad
rac23=2m+1-rac p3,
]
for (n=2m-1),
[
(5/6)_n
equiv
(m+1)_nleft[
1-rac p6igl(H_{3m-1}-H_migr)
ight]pmod{p^2},
]
and
[
(2/3)_n
equiv
(2m+1)_nleft[
1-rac p3igl(H_{4m-1}-H_{2m}igr)
ight]pmod{p^2}.
]
Hence
[
Q_{2m-1}
equiv
q_0left(1+pEight)pmod{p^2},
]
where
[
q_0:=
-2^{-(2m-1)}
rac{(m+1)_{2m-1}}{(2m+1)_{2m-1}},
]
and
[
E=
-rac16(H_{3m-1}-H_m)
+rac13(H_{4m-1}-H_{2m}).
]

## 3. One-order lift of the binomial quotient

Exactly,
[
q_0
=
-rac43,2^{-(2m-1)}
rac{inom{3m}{m}}{inom{4m}{2m}}.
]
Write
[
R_m:=rac{inom{3m}{m}}{inom{4m}{2m}}
=
rac{prod_{r=m+1}^{2m}r}
{prod_{r=3m+1}^{4m}r}.
]

Reflect the denominator by (rmapsto p-r):
[
prod_{r=3m+1}^{4m}r
equiv
(-1)^m
left(prod_{t=2m+1}^{3m}tight)
left[
1-psum_{t=2m+1}^{3m}rac1t
ight]
pmod{p^2}.
]

Next double the block (2m+1,dots,3m). Since
[
2^mprod_{t=2m+1}^{3m}t
=
prod_{substack{1le ole2m-1\o {m odd}}}(p-o),
]
we obtain
[
prod_{t=2m+1}^{3m}t
equiv
(-1)^mrac{(2m)!}{4^m m!}
left[
1-pleft(H_{2m}-rac12H_might)
ight]
pmod{p^2}.
]

Combining the two reflections gives the all-prime quotient lift
[
oxed{
R_m
equiv
4^mleft[
1+pleft(H_{3m}-rac12H_might)
ight]
pmod{p^2}.
}
]
Therefore
[
q_0
equiv
-rac83
left[
1+pleft(H_{3m}-rac12H_might)
ight]
pmod{p^2}.
]

## 4. Closed formula for the endpoint digit

Modulo (p),
[
H_{3m-1}=H_{3m}+2,
qquad
H_{4m-1}=H_{2m}+rac32,
]
where the second equality uses (H_{4m}equiv H_{2m}pmod p).
Thus
[
E
equiv
-rac16H_{3m}
+rac16H_m
+rac16
pmod p.
]

Hence
[
oxed{
Q_{2m-1}
equiv
-rac83
left[
1+pleft(
rac56H_{3m}
-rac13H_m
+rac16
ight)
ight]
pmod{p^2}.
}
]

Equivalently,
[
oxed{
delta_p
equiv
-rac{20}{9}H_{3m}
+rac89H_m
-rac49
pmod p.
}
	ag{A}
]

Using the standard (p=6m+1) harmonic/Fermat-quotient relations already used on this lane,
[
H_mequiv H_{2m}+H_{3m}pmod p,
]
so (A) becomes
[
oxed{
delta_p
equiv
-rac43H_{3m}
+rac89H_{2m}
-rac49
pmod p.
}
	ag{B}
]

Equivalently, with (q_p(a)=(a^{p-1}-1)/p),
[
oxed{
delta_p
equiv
rac83q_p(2)-rac43q_p(3)-rac49
pmod p.
}
	ag{C}
]

## 5. Strict reduction of the still-open upper B-chart target

The portable upper-chart conjecture is
[
B_p
stackrel?{equiv}
H_{3m}-rac23H_{2m}+rac{10}{3}
pmod p.
]

From (B),
[
3-rac34delta_p
=
H_{3m}-rac23H_{2m}+rac{10}{3}.
]
Therefore the target is **exactly equivalent** to
[
oxed{
B_p
stackrel?{equiv}
3-rac34delta_p
pmod p.
}
	ag{D}
]

Thus the harmonic/Pochhammer target can be replaced by one provenance-preserving endpoint repair coordinate: the first (p)-adic digit of the already-owned endpoint (Q_{2m-1}).

In un-divided form, (D) is
[
oxed{
Q_{2m-1}
+rac83
+rac{4p}{3}(B_p-3)
stackrel?{equiv}
0
pmod{p^2}.
}
	ag{E}
]

This is the recommended next proof target. It is smaller than separately controlling the affine seam jet and the harmonic jet: prove the single sum-to-endpoint-lift bridge (E).

## 6. BRC interpretation

Population / provenance retained:
- the upper (B)-chart finite sum;
- the endpoint (Q_{2m-1});
- its valuation-one repair digit (delta_p);
- the exact relation (p=6m+1).

Safe compression proved here:
- the harmonic target is fiber-constant once (delta_p) is retained.

Unsafe compression:
- retaining only (Q_{2m-1}mod p=-8/3) discards exactly the digit needed to distinguish the target.

BRC resolution:
`COMPOSE_APPLIED / ENDPOINT_P_ADIC_REPAIR_COORDINATE / HARMONIC_TARGET_QUOTIENTED_ONLY_AFTER_DIGIT_RETAINED`.

## 7. Independent regression

A fresh exact-rational / modular checker was run for every prime
[
p<10000,qquad pequiv1pmod6,
]
611 primes total.

Checked:
1. (Q_{2m-1}equiv-8/3pmod p);
2. the lifted formula (A);
3. the reduced form (B);
4. the affine identity connecting the harmonic target with (3-rac34delta_p).

Result:
[
oxed{611/611,quad 0 {m failures}.}
]

The finite run is regression/falsification evidence only. The proof of (A)–(C) is the finite (p^2) product expansion above. The upper (B)-chart congruence (D)/(E) remains conjectural.

## 8. Next exact unit

Do **not** reopen the raw complementary period, the (k=3m) tail, or the canonical Gauss-Manin representative lane.

Attempt a finite certificate directly for
[
Q_{2m-1}
+rac83
+rac{4p}{3}(B_p-3)
equiv0pmod{p^2}.
]

A successful proof closes the upper (B)-chart. A failure should identify the missing repair coordinate at the sum-to-endpoint interface rather than expanding the state back to multiple moments.
