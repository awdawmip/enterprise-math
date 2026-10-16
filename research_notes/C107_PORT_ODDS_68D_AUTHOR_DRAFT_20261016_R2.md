# Enterprise Math C107 — Positive-port 68D zero existence (author draft)

Date: 2026-10-16; scope: classical finite positive-weight BRC auxiliary model. Fixed C105 core bits 2 and 24, eleven connected star stages and 68 weak-face couplings.

New exact lemma: For nonnegative four-port masses a,b,c,d with A=a+b+c+d and Fourier moments B=a-b+c-d, C=a+b-c-d, D=a-b-c+d, one has F=AD-BC=4(ad-bc), with ad+bc <= A^2/4.

Rechecked C106's 846 exact Bernstein inequalities for all eleven stages: A<=M=12609529/131072, F(t,2/5)>100 and F(t,99/100)<-29. For independent perturbations r_f=epsilon+(1-epsilon)*r_f^0+z_f, |z_f|<=delta, let rho=(1+100(epsilon+delta))^68-1. Pointwise positivity implies every port mass changes within a factor 1±rho, without assuming character independence. Hence |Fz-F0|<=(2rho+rho^2)M^2, and endpoint signs have sharper error 2rho M^2.

With epsilon=12/10^8 and delta=10/10^8, exact rational calculations give Fz(t,2/5)>72, Fz(t,99/100)<-1 for every t and every independent 68D perturbation. With epsilon=12/10^8 and delta=11/10^8, get Fz(t,2/5)>71, Fz(t,99/100)<-1/50. All 68 couplings stay strictly within (0,1). Thus for all t,z at least one interior zero exists and the 1D crossing degree is -1. The larger delta is 366.67 times C106's delta, but uniqueness/transversality is NOT proved in the larger cube, and their centers differ.

Verification: exact Fraction arithmetic plus inherited 846-coefficient rerun, 99 independent Walsh-inverse rational port checks, clean ZIP unpack and 8-file SHA256 manifest. C107 portable package SHA256 0b4744f3a54e266468a8d3036676f518a31d3da7f98a73816d88c40e020a0069.

Global snapshot: d433f2cbd7e5b458833de3be8db56a8a9b1430d9; EM input: a6efba6d4d46ce63d61792600bbfea3de6bc29b8. No formal claim or independent review; native active-Owner query was unavailable. Next: bound the perturbed derivative via signed GF(2) port coefficients and determine larger-box root uniqueness.