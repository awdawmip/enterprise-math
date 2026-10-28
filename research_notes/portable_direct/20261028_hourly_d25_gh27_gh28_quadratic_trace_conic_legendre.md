# D25/LIFT GH-27/GH-28 — signed quadratic fiber reconstruction and a conic–Legendre criterion

2026-10-28. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Auxiliary finite-field **F-port** research, not a native Source CLAIM/checkpoint, Result, independent review, original Hasse W/S transfer, or a native experiment. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, parent OPEN. Preserve frozen science pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Stable Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`, never maintenance \`chatgpt-hourly-enterprise-math-20260921\`.

Prior immutable inputs: GH-22 F-character source, GH-24 Klein-four and elliptic carrier, GH-26 signed quotient fibers, in \`research_notes/portable_direct/20261028_hourly_d25_gh26_quotient_inversion_antiperiod.md\` and \`20261028_hourly_d25_gh24_gh25_klein_orbit_elliptic_trace.md\`. These are author-side predecessors, not admitted native Results.

Let \`p=8m+3>=11\` be prime, \`chi\` the quadratic character of \`F_p\` including \`chi(0)=0\`. Define the *original labeled source*
\[
h(x)=\chi(x)[x(1+x)]^{3m+1}(1+9x)^m,\quad S_F=\sum_{x\in F_p}h(x).
\]
GH-22 established \(\binom{3m+1}{m}F_m(9)=-S_F\), with \(F_m(z)={}_2F_1(-m,-m;2m+2;z)\). GH-26 established for \(v=\phi(x)=(1+9x)/(9x(1+x))\) on \(U=F_p\setminus\{0,-1,-1/9\}\), \(t=1+x\),
\[
9vt^2-9(v+1)t+8=0,\quad \Sigma(v)=\sum_{\phi(x)=v}\chi(t),\quad S_F=9^m\sum_{v\ne0}v^m\Sigma(v).
\]
A double root is counted once. Square-v fibers have \(\Sigma(v)=0\), while nonsquare fibers require a signed trace, not a positive multiplicity.

## GH-27 — eliminate root-choice sign without losing the signed source

**Theorem.** For every \(u\in F_p^\times\), put \(v=u^2/2\), \(Q_\pm(u)=3u^2\pm8u+6\). Since \(\chi(2)=-1\), \(v\) is nonsquare. Then *including empty and ramified fibers*
\[
\boxed{\Sigma(u^2/2)=\chi(3)[\chi(Q_+(u))+\chi(Q_-(u))].}\tag{27.1}
\]
Consequently, with \(u=0\) harmless because \(m\ge1\),
\[
\boxed{S_F=(9/2)^m\chi(3)\sum_{u\in F_p}u^{2m}\chi(3u^2+8u+6).}\tag{27.2}
\]

**Proof.** For \(v=u^2/2\), the root equation is \(9u^2t^2-9(u^2+2)t+16=0\). Write \(t'\) for the other root and \(s=4/(3u)\). Vieta gives \(tt'=s^2\), \(t+t'=(u^2+2)/u^2\), hence
\[
\frac{(t\pm s)^2}{t}=\frac{3u^2\pm8u+6}{3u^2}=\frac{Q_\pm(u)}{3u^2}.
\]
Moreover \(Q_+Q_-=4D(v)\), where \(D(v)=9v^2-14v+9\) is the exact fiber discriminant. If \(D\) is nonsquare, the fiber is empty and the two \(Q\)-characters are opposite. If \(D\) is nonzero square, there are two distinct rational roots, neither equal to \(\pm s\), so both \(Q\)-characters equal \(\chi(3)\chi(t)\); also \(\chi(t')=\chi(t)\) from \(tt'=s^2\). If \(D=0\), there is one root \(t=s\) or \(t=-s\): exactly one \(Q_\pm\) is zero and the other recovers \(\chi(t)\). Thus (27.1) holds without double-counting.

Every nonsquare \(v\) has exactly two preimages \(u,-u\) under \(u^2/2\). Insert (27.1) in GH-26's source sum; \(u^{2m}\) is even and \(Q_-(u)=Q_+(-u)\). Both character sums coincide, yielding (27.2). QED.

## GH-28 — exact conic transport, Laurent constant term and Legendre value

**Theorem.** The same *original* F source has the three exactly equal presentations in \(F_p\):
\[
\boxed{S_F=2^{-m}\sum_{w\in F_p}(w-4)^{2m}\chi(w^2+2)} \tag{28.1}
\]
\[
\boxed{S_F=2^{-3m}\sum_{s\in F_p^\times}(s-8-2s^{-1})^{2m}} \tag{28.2}
\]
\[
\boxed{S_F=-2^{-3m}\,\operatorname{CT}_s(s-8-2s^{-1})^{2m}.}\tag{28.3}
\]
Here \(\operatorname{CT}_s\) means integer Laurent coefficient of \(s^0\). In particular, defining
\[
c_{2m}=\sum_{j=0}^m\binom{2m}{2j}\binom{2j}{j}(-2)^j8^{2m-2j},
\]
and the *ordinary* Legendre polynomial \(P_n\), one has
\[
\boxed{\binom{3m+1}{m}F_m(9)\equiv 2^{-3m}c_{2m}
\equiv 9^m P_{2m}(2\sqrt2/3)\pmod p.}\tag{28.4}
\]
The last expression belongs to \(F_p\) because \(P_{2m}\) is even, despite \(\sqrt2\) lying in \(F_{p^2}\). All prefactors are \(p\)-units. Hence, **for every prime \(p=8m+3\)**,
\[
\boxed{F_m(9)=0\iff P_{2m}(2\sqrt2/3)=0 \pmod p.}\tag{28.5}
\]

**Proof.** In (27.2), \(3(3u^2+8u+6)=(3u+4)^2+2\). Put \(w=3u+4\), and use \(9^m3^{-2m}=1\) to obtain (28.1). For any polynomial \(f\),
\(\sum_wf(w)\chi(w^2+2)=\sum_{(w,y):y^2=w^2+2}f(w)-\sum_wf(w)\).
With \(f(w)=(w-4)^{2m}\), the second sum is zero since \(0<2m<p-1\). The conic \(y^2=w^2+2\) has **every** rational point uniquely parameterized by \(s=y+w\ne0\), \(y-w=2/s\), \(w=(s-2/s)/2\); this gives (28.2), including the actual endpoints.

Every exponent of \(s\) in the Laurent expansion lies between \(-2m\) and \(2m\), strictly inside \((-(p-1),p-1)\). The sum over \(s\ne0\) is therefore \(-1\) for exponent zero and zero otherwise, giving (28.3), and the displayed multinomial formula for \(c_{2m}\). The GH-22 relation now gives the first equality in (28.4).

Finally the formal generating function is
\[
\sum_{n\ge0}c_nt^n=\operatorname{CT}_s\frac1{1-t(s-8-2/s)}
=(1+16t+72t^2)^{-1/2}.
\]
By \(\sum P_n(x)T^n=(1-2xT+T^2)^{-1/2}\), use \(T=6\sqrt2\,t\) and \(x=-2\sqrt2/3\) to obtain \(c_{2m}=72^mP_{2m}(2\sqrt2/3)\); the parity is even. Divide by \(2^{3m}\) to obtain (28.4). Since \(\binom{3m+1}{m}\) and \(9\) are \(p\)-units, (28.5) follows. QED.

The Laurent coefficients also have an exact integer recurrence:
\[
c_0=1,\quad c_1=-8,\qquad (n+1)c_{n+1}=-8(2n+1)c_n-72n c_{n-1}.
\]
This is derived by differentiating the formal generating function, and supplies a division-safe finite-field check for \(n< p-1\).

## Reproducible exact checks, observer and continuation

The companion pure-Python standard-library checker exhaustively checked (27.1) against the **original enumerated rational x-fibers** for all nonzero \(u\), including zero/nonzero/repeated discriminants, and cross-checked six independent finite-field presentations, the GH-19 coefficient, the Legendre recurrence and the Laurent recurrence for **all 76 primes** \(11\le p<2001,\ p\equiv3\pmod8\). All passed. Finite observation: all 37 class-19 samples have \(F_m(9)=0\); all 39 class-11 samples have \(F_m(9)\ne0\). **This is not a proof of universal class vanishing.**

BRC: \`COMPOSE_APPLIED\` to GH-22/GH-24/GH-26 signed source, followed by an exact observer-preserving quadratic lift. Underlying labels \((p,m,x,v,u,\chi(1+x),F/G\,port,\text{boundary})\) remain available; the scalar trace, conic and constant term preserve the F total, **not** arbitrary future G-port or native X6 operations. No CM claim is inferred for the GH-25 proven non-CM elliptic carrier. No new axioms.

**Next exact obligation:** prove or refute \(P_{(p-3)/4}(2\sqrt2/3)=0\pmod p\) for **all** primes \(p\equiv19\pmod{24}\), using an actual finite-field/character/CM-or-non-CM certificate, not merely the conic restatement; or produce one exact counterexample. If proven, transfer back via (28.4) to GH-15 Laurent compensation and GH-20/21/GH-5/GH-10/R23/R36. Original H0/B0, six Hasse sources, finite endpoints, positive infinity, \([X]U\bmod p^2\), Frobenius eta/kappa, native \(p=373\), independent Driver review all remain OPEN.

Control read at this run: gateway 0.6.11 and Site grant \`research_authority_granted=false\`, \`executor_binding_configured=false\`. New typed read-only continuation failed \`INVALID_ARGUMENT / CONTROL_QUOTA\`; no fresh winning CLAIM, OPEN or native Source checkpoint. Preserve prior sessions/staging and fixed research lane; predecessor/session recovery support remains \`enterprise-math#1558\`. This GitHub record is portable author evidence only.
