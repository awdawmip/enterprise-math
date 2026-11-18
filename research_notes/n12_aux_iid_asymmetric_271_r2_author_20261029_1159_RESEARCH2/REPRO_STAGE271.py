#!/usr/bin/env python3
"""Stage271 exact external-IID Bellman face certificate.

Runs without network/dependencies; Fraction arithmetic, independent count and
ordered-word probability flow. No claim about native P000/BRC operator semantics.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
N = 12
LP, LQ = F(7566375964672, 51849608449), F(4026978326268, 51849608449)
H = F(1717930741512259706653, 22294382577836949504)
A, B = F(133853268599, 1761205026816), F(431993556815, 557256278016)
V = F(89124381535, 15479341056)
T, U = (0, 0, 5), (1, 2, 3)
STATES = [(i, j, n-i-j) for n in range(N+1)
          for i in range(n+1) for j in range(n-i+1)]


def child(s, x):
    return tuple(s[k]+int(k == x) for k in range(3))


def likelihood(s):
    i, j, k = s
    return P[0]**i*P[1]**j*P[2]**k, Q[0]**i*Q[1]**j*Q[2]**k


def bellman():
    vals, costs, ties, gaps = {}, {}, {}, []
    for s in reversed(STATES):
        p, q = likelihood(s)
        options = {'P': LQ*q, 'Q': LP*p}
        if sum(s)<N:
            options['C'] = q+sum(vals[child(s,x)] for x in range(3))
        bestcost = min(options.values())
        vals[s], costs[s] = bestcost, options
        bestactions = tuple(a for a, cost in options.items() if cost == bestcost)
        if len(bestactions) > 1:
            ties[s] = bestactions
        gaps.extend(cost-bestcost for cost in options.values() if cost>bestcost)
    return vals,costs,ties,gaps


def policy(vals, costs, r, u):
    pol = {s: next(a for a, c in costs[s].items() if c == vals[s]) for s in STATES}
    pol[T] = 'C' if r else 'P'
    pol[U] = 'C' if u else 'Q'
    assert all(costs[s][a] == vals[s] for s, a in pol.items())
    return pol


def count_flow(pol):
    count = defaultdict(int)
    count[(0,0,0)] = 1
    o=[F(0)]*4
    terminal=[F(0)]*2
    for s in STATES:
        multiplicity=count[s]
        if not multiplicity:
            continue
        p,q=likelihood(s)
        a=pol[s]
        if a=='P':
            o[1]+=multiplicity*q
            terminal[0]+=multiplicity*p
            terminal[1]+=multiplicity*q
        elif a=='Q':
            o[0]+=multiplicity*p
            terminal[0]+=multiplicity*p
            terminal[1]+=multiplicity*q
        else:
            assert a=='C' and sum(s)<N
            o[2]+=multiplicity*p
            o[3]+=multiplicity*q
            for x in range(3):
                count[child(s,x)]+=multiplicity
    assert terminal == [F(1),F(1)]
    return tuple(o),count


def ordered_flow(pol):
    # Direct unmerged ordered words, deliberately not count-state propagation.
    o=[F(0)]*4
    terminal=[F(0)]*2
    nodes=leaves=0
    def walk(word,p,q):
        nonlocal nodes,leaves
        nodes+=1
        s=(word.count(0),word.count(1),word.count(2))
        a=pol[s]
        if a=='P':
            o[1]+=q
            terminal[0]+=p
            terminal[1]+=q
            leaves+=1
        elif a=='Q':
            o[0]+=p
            terminal[0]+=p
            terminal[1]+=q
            leaves+=1
        else:
            assert a=='C' and len(word)<N
            o[2]+=p
            o[3]+=q
            for x in range(3):
                walk(word+(x,),p*P[x],q*Q[x])
    walk((),F(1),F(1))
    assert terminal == [F(1),F(1)]
    return tuple(o),nodes,leaves


def orient(x,y,z):
    return (y[0]-x[0])*(z[1]-x[1])-(y[1]-x[1])*(z[0]-x[0])


def main():
    vals,costs,ties,gaps=bellman()
    assert len(STATES)==455
    assert sum(map(len,costs.values()))==1274
    assert vals[(0,0,0)]==H
    assert ties=={U:('Q','C'),T:('P','C')}
    assert len(gaps)==817 and min(gaps)==F(1442084699,51366257459336331657216)

    corners={}
    nodes=leaves=0
    for r,u in product((0,1),repeat=2):
        pol=policy(vals,costs,r,u)
        by_count,multiplicity=count_flow(pol)
        by_word,n,l=ordered_flow(pol)
        assert by_word==by_count
        assert multiplicity[T]==1 and multiplicity[U]==20
        assert LP*by_count[0]+LQ*by_count[1]+by_count[3]==H
        assert by_count[3]>by_count[2]
        corners[r,u]=by_count
        nodes+=n
        leaves+=l
        print('corner',r,u,','.join(map(str,by_count)), 'ordered_nodes_leaves',n,l)
    E,G,Fcorner,Hcorner=[corners[x] for x in ((0,0),(0,1),(1,0),(1,1))]
    expected={
        (0,0):('1133161305691/15850845241344','146231594105/185752092672','27588964539587/5944066965504','84859115435/15479341056'),
        (0,1):('1129087690691/15850845241344','146299619105/185752092672','27612319764587/5944066965504','84999370435/15479341056'),
        (1,0):('1279282905691/15850845241344','425010482315/557256278016','10164282046529/1981355655168','31186005145/5159780352'),
        (1,1):('1275209290691/15850845241344','425214557315/557256278016','10172067121529/1981355655168','93698270435/15479341056'),
    }
    for key, values in expected.items():
        assert corners[key]==tuple(map(F,values))
    assert tuple(Hcorner[i]-Fcorner[i] for i in range(4)) == tuple(G[i]-E[i] for i in range(4))
    area=abs(orient(E,Fcorner,G))
    assert orient(E,Fcorner,G)==-area
    assert area==F(101268766501953125,34503839932027276099584)
    old_C=(F(1135528662191,15850845241344),F(146193716605,185752092672))
    assert orient(E,Fcorner,old_C)==F(123370733132421875,69007679864054552199168)>0
    dx=tuple(Fcorner[i]-E[i] for i in range(4))
    dy=tuple(G[i]-E[i] for i in range(4))
    det=orient(E,Fcorner,G)
    r=((A-E[0])*dy[1]-(B-E[1])*dy[0])/det
    u=(dx[0]*(B-E[1])-dx[1]*(A-E[0]))/det
    assert (r,u)==(F(49,100),F(1,50))
    witness=tuple(E[i]+r*dx[i]+u*dy[i] for i in range(4))
    assert witness[:2]==(A,B)
    assert witness[2]==F(3223592625343,660451885056)
    assert witness[3]==V==H-LP*A-LQ*B
    assert witness[3]-witness[2]==F(1737142960451,1981355655168)>0
    assert orient(E,Fcorner,witness)==F(-4050750660078125,69007679864054552199168)
    assert nodes==20224 and leaves==13484

    print('STAGE271_EXACT_ALL_REAL_FACE_PASS')
    print('bellman_states',len(STATES),'legal_actions',sum(map(len,costs.values())),
          'positive_gaps',len(gaps),'minimum_gap',min(gaps),'ties',ties)
    print('dual_lambdaP',LP,'lambdaQ',LQ,'thetaP',0,'thetaQ',1,'root_H',H)
    print('R271_vertices','E,F,H,G','area',area,'old_side',orient(E,Fcorner,old_C))
    print('caps',A,B,'exact_optimum',V,'decimal',format(float(V),'.15f'))
    print('r,u',r,u,'tP',witness[2],'tQ',witness[3],
          'tQ_minus_tP',witness[3]-witness[2])
    print('total_ordered_nodes',nodes,'terminal_leaves',leaves,
          'P_Q_terminal_masses_exactly_one_each',True)

    # Strict exterior but only upper-bound witness for Stage272.
    next_switch=(1,2,4)
    alter=policy(vals,costs,0,1)
    original,reached=count_flow(alter)
    assert original==G and alter[next_switch]=='Q' and reached[next_switch]==35
    alter[next_switch]='C'
    changed,_=count_flow(alter)
    changed_ordered,n,l=ordered_flow(alter)
    assert changed==changed_ordered
    assert changed==tuple(map(F,(
        '187155450011/2641807540224', '219610483345/278628139008',
        '13822107249481/2972033482752', '127792519715/23219011584')))
    newer=tuple(F(49,100)*G[i]+F(49,100)*Hcorner[i]
                +F(1,50)*changed[i] for i in range(4))
    assert newer[:2]==(F(2401128349757,31701690482688), F(288133328335,371504185344))
    assert newer[3]==F(535594465735,92876046336)>newer[2]
    assert orient(G,Hcorner,newer)==F(-46449501199609375,552061438912436417593344)<0
    assert orient(G,Hcorner,E)>0
    excess=LP*(changed[0]-G[0])+LQ*(changed[1]-G[1])+changed[3]-G[3]
    assert excess==F(521887904513171875,601948329601597636608)>0
    print('STAGE272_FEASIBLE_EXTERIOR_PASS',
          'switch',next_switch,'Q_to_C','reached_ordered_histories',reached[next_switch],
          'four_observers',','.join(map(str,newer)),
          'old_support_slack_new_corner',excess,
          'side',orient(G,Hcorner,newer),'ordered_nodes_leaves',n,l)

if __name__=='__main__':
    main()
