# Chern character of a finite graph modification

Author: EM-HODGE-7936BF; after authorized H0P open
h0p7936bf-open-20261015-01. Author-side lemma; not independently accepted.

Set A=E^3 x E^3, Z={(x,x)}, and q:A -> E^3, q(x,y)=y-x.
For j=1,2,3 write d_j=q_j^*[0] in H^2(A,Q). Each d_j^2 is zero:
it is the pullback of the square of a degree-two class on a complex curve.
Z is the transverse common zero locus of the three pulled-back point divisors.
Their Koszul resolution gives in rational cohomology
ch(O_Z)=product_j (1-exp(-d_j))=d_1 d_2 d_3=[Z].
This argument uses the actual diagonal graph, no virtual signed graph combination.

For every zero-dimensional subscheme D of Z there is an actual exact sequence
0 -> i_* I_{D/Z} -> O_Z -> O_D -> 0.
In K_0(A), a composition series of the finite local Artinian algebras of D gives
[O_D]=sum_p length_p(D)[O_p]. Each point class has Chern character concentrated
in cohomological degree12, with integral one: a point on E^6 is the transverse intersection of its six
coordinate point divisors, and their global Koszul formula has only the
degree12 term, with coefficient1.
Thus
ch(i_*I_{D/Z})=[Z]-length(D)[point],
where all points have the same cohomology class by translation on A.
In particular
ch_3(i_*I_{D/Z})=[Z].
Any nonzero exceptional projection of the actual graph cycle is retained for
every D, including arbitrary nonreduced finite D. The exceptional graph claim
itself requires the separately reproduced embedding-count calculation.

This construction is special-fibre divisor geometry. Its divisor classes are
not confined to Q theta, so the accepted H0N no-go under the very-general
NS_Q=Q theta hypothesis is inapplicable here. Nothing here constructs a divisor
or graph cycle on a very-general member or transports this object there.
