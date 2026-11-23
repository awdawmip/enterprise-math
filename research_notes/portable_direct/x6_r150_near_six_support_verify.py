"""R150: exact Port-10 six-direction support for strict 3/2-near BRC observer.
Requires R149 checker in the same directory. Python standard library only.
"""
from collections import Counter
from fractions import Fraction
from x6_r149_global_pareto_six_witness_verify import population, gap, score, WITNESSES

SPECIAL = ((1,-3,1),(3,-1,0),(7,-4,1),(9,-2,0))

def main():
    pop = list(population())
    G = {a: gap(a) for a in pop}
    low = [a for a in pop if G[a][1] <= 3]
    high = [a for a in pop if G[a][1] >= 6]
    assert len(pop)==1935 and len(high)==1890 and len(low)==45
    support = set(WITNESSES)
    exceptional = []
    assignment = Counter()
    for a in low:
        if a in support:
            continue
        available = [w for w in WITNESSES if all(
            3*G[w][j] <= 2*G[a][j] for j in range(6))]
        if available:
            assignment[min(available)] += 1
        else:
            exceptional.append(a)
    assert tuple(sorted(exceptional)) == SPECIAL
    assert sum(assignment.values()) == 35
    assert dict(assignment) == {(4,-1,0):23,(6,-4,1):12}
    assert all(G[a][4]==18 for a in SPECIAL)
    assert all(G[a][2]>=18 for a in ((3,-1,0),(7,-4,1)))
    assert Fraction(3,2)*score(G[(1,0,0)],20,528) < Fraction(6,312)

    Bs=[Fraction(20),Fraction(41,2),Fraction(25),Fraction(60),
        Fraction(100),Fraction(135),Fraction(136),Fraction(1000),
        Fraction(100001,11)]
    Ds=[Fraction(528),Fraction(1057,2),Fraction(560),Fraction(584),
        Fraction(720),Fraction(904),Fraction(1008),Fraction(1400),
        Fraction(1736),Fraction(4760),Fraction(10**6)]
    trials = 0
    for B in Bs:
        for D in Ds:
            eta=min(score(G[w],B,D) for w in WITNESSES)
            reduced={w for w in WITNESSES if score(G[w],B,D)<Fraction(3,2)*eta}
            full={a for a in pop if score(G[a],B,D)<Fraction(3,2)*eta}
            assert full==reduced,(B,D,eta,sorted(full-reduced))
            trials+=1
    print("R150 FULL STRICT-NEAR SIX-SUPPORT CERTIFICATE PASS")
    print("population",len(pop),"high-gap",len(high),"low-gap",len(low),
          "scaled-dominance",sum(assignment.values()),"exceptions",exceptional)
    print("scaled-dominance assignment",sorted(assignment.items()))
    print("exact_fraction_full_population_crosschecks",trials)

if __name__=="__main__":
    main()
