"""Minimum uniform-atom budgets for the four terminal Bernstein extensions."""
from fractions import Fraction
from math import comb, lcm
from pathlib import Path
import json

# Each pair lists high-node multiplicities for uniform count records, then for
# uniform complete words (in the latter case, per labelled word of weight j).
HIGH = {
    3: ({6:5410068182, 7:216638181358, 8:68446899280},
        {6:6917, 7:284221, 8:31015}),
    4: ({5:1392002114, 13:1016875}, {5:140606086, 13:132194665}),
    5: ({}, {}),
    6: ({}, {}),
}


def certificate(moments, n, s, high, complete_words):
    indices = range(s+1)
    rhs = [moments[a]*(1 if complete_words else comb(n,a)) for a in indices]
    budget = lcm(*(v.denominator for v in rhs))
    counts = dict(high)

    def column(a,j):
        if j < a:
            return 0
        return comb(n-a,j-a) if complete_words else comb(j,a)

    # Columns labelled 0 through s have an upper triangular integral matrix
    # with diagonal one. Back substitution gives the only remaining weights.
    for a in reversed(indices):
        total = budget*rhs[a]
        assert total.denominator == 1
        counts[a] = int(total)-sum(column(a,j)*v for j,v in counts.items())
    assert all(0 <= j <= n and count >= 0 for j,count in counts.items())
    assert all(sum(column(a,j)*v for j,v in counts.items()) == budget*rhs[a] for a in indices)
    return {'minimum':budget,'multiplicities':dict(sorted(counts.items()))}


def main():
    data=json.loads(Path(__file__).with_name('bernstein_checked.json').read_text())
    moments=list(map(Fraction,data['m3_normalized']))
    out=[]
    for row in data['finite_exchangeability']:
        s,n=row['truncation'],row['max_extension']
        count_high,word_high=HIGH[s]
        out.append({'s':s,'N':n,'count_records':certificate(moments,n,s,count_high,False),
                    'complete_words':certificate(moments,n,s,word_high,True)})
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
