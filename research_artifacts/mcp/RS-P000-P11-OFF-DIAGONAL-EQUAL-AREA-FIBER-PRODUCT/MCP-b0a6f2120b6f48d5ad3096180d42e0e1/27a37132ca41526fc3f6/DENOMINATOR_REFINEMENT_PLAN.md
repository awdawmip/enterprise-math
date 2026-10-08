# Increment 2 finite control — denominator refinement

After freezing the uniform family, refine its exact minimal clearing denominator from a sixteen-root lcm to a closed expression in d=p/q. This addresses the Task's denominator and primitive-gcd obligation directly.

Before executing the refinement checker, declare these tests:

1. Verify the expression against exactly the same six existing odd-multiple records (n=1,3,5,7,9,11); do not expand the elliptic orbit or run a search for solutions.
2. Test the integer-numerator gcd identity for 1<=p<=32, 1<=q<=15, q odd, gcd(p,q)=1, with p odd or divisible by 4. For p odd use (r,s)=(0,0),(4,8); for p even use (r,s)=(1,1),(3,5). These artificial inputs test only the stated integer gcd lemma, not existence on the cut curve. They deliberately exercise both possible 2-adic denominator cases.

This finite check is regression only. The valuation proof in the addendum is the all-parameter argument.
