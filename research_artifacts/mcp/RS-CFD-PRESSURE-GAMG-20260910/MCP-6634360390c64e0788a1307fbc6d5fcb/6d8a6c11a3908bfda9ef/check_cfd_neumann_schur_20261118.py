from fractions import Fraction as Q

a, b, c = Q(2), Q(3), Q(5)
d = (a+b)*(b+c)-b*b
inv_ii = [[(b+c)/d, b/d], [b/d, (a+b)/d]]
g = a*c*b/d
S = [[a-a*a*inv_ii[0][0], -a*c*inv_ii[0][1]],
     [-a*c*inv_ii[1][0], c-c*c*inv_ii[1][1]]]
assert S == [[g,-g],[-g,g]]
assert [sum(row) for row in S] == [0,0]
assert g == 1/(1/a+1/b+1/c)
p0,p3 = Q(7),Q(1)
q = g*(p0-p3)
p1 = p0-q/a
p2 = p1-q/b
assert p2-q/c == p3
assert (a*(p1-p0)+b*(p1-p2)) == 0
assert (b*(p2-p1)+c*(p2-p3)) == 0
assert q == Q(180,31)
print({"Schur": [[str(v) for v in r] for r in S],
       "effective_conductance": str(g),
       "pressure": list(map(str,[p0,p1,p2,p3])),
       "flux": str(q),
       "nullspace_row_sums":[str(sum(r)) for r in S]})
