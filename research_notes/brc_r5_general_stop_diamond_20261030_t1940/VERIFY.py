"""Exact finite checks for a general strict-stop diamond; not the all-real proof."""
from fractions import Fraction as F
from itertools import product


def frac(n, d=1):
    return F(n, d)


def det4(rows):
    a = [list(r) for r in rows]
    d = F(1)
    for k in range(4):
        j = next((j for j in range(k, 4) if a[j][k]), None)
        if j is None:
            return F(0)
        if j != k:
            a[j], a[k] = a[k], a[j]
            d = -d
        t = a[k][k]
        d *= t
        for j in range(k+1, 4):
            z = a[j][k]/t
            for l in range(k+1, 4):
                a[j][l] -= z*a[k][l]
            a[j][k] = 0
    return d


def case(name, q, r, ke, beta, c):
    p = [[r[u]*q[x][u] for u in range(2)] for x in range(2)]
    assert sum(sum(row) for row in p) == sum(sum(row) for row in q) == 1
    assert all(q[x][u] > 0 for x in range(2) for u in range(2))
    assert r[0] != r[1]
    early = [sum(p[x])/sum(q[x]) for x in range(2)]
    assert early[0] != early[1]
    assert all(0 < ke[x] < 1 and all(0 < beta[x][u] < 1 and 0 < beta[x][u]+c[x][u] < 1 for u in range(2)) for x in range(2))

    def observation(s, y):
        out = []
        for w in (p, q):
            e = sum(w[x][u]*((1-s[x])*ke[x]+s[x]*(beta[x][u]+c[x][u]*y[x][u])) for x in range(2) for u in range(2))
            out.append(e)
        for w in (p, q):
            t = sum(w[x][u]*(2*(1-s[x])+s[x]*(4-y[x][u])) for x in range(2) for u in range(2))
            out.append(t)
        return tuple(out)

    full = [observation(s, ((ys[0],ys[1]),(ys[2],ys[3]))) for s in product((0,1),repeat=2) for ys in product((0,1),repeat=4)]
    lr = [observation(s, (ys,ys)) for s in product((0,1),repeat=2) for ys in product((0,1),repeat=2)]
    assert len(full)==64 and len(lr)==16

    for u in range(2):
        if c[0][u] == c[1][u]:
            continue
        v = 1-u
        sigma = 1 if max(c[0][u],c[1][u]) > 0 else -1
        h = max(sigma*c[0][u],sigma*c[1][u]); lo = min(sigma*c[0][u],sigma*c[1][u])
        theta = (max(F(0),lo)+h)/2
        assert 0 < theta < h and theta > lo
        M = 1+max(sum(p[x])/q[x][v] for x in range(2))+r[v]*max(abs(c[x][v]) for x in range(2))+theta*r[u]
        A = M/(r[v]-r[u]); B = -A*r[u]+theta*r[u]
        def L(o):return sigma*o[0]+A*o[2]+B*o[3]
        dif = max(map(L,full))-max(map(L,lr))
        low = 0 if sigma*c[0][u]<sigma*c[1][u] else 1
        high=1-low
        predicted = min(p[low][u]*(theta-sigma*c[low][u]),p[high][u]*(sigma*c[high][u]-theta))
        assert dif == predicted > 0, (name,u,dif,predicted)
        print('GAP',name,'u=',u,'sigma=',sigma,'theta=',str(theta),'A=',str(A),'B=',str(B),'delta=',str(dif),'linfty_lb=',str(dif/(1+abs(A)+abs(B))))

    if all(c[0][u]==c[1][u] for u in range(2)):
        E=[]
        for x in range(2):
            E.append(tuple([sum(w[x][u]*(beta[x][u]-ke[x]) for u in range(2)) for w in (p,q)]+[2*sum(w[x]) for w in (p,q)]))
        G=[]
        for u in range(2):
            k=c[0][u]
            G.append((k*r[u],k,-r[u],F(-1)))
        D=det4([[E[0][i],E[1][i],G[0][i],G[1][i]] for i in range(4)])
        for s0,s1 in product((F(1,4),F(1,2),F(3,4)),repeat=2):
            s=(s0,s1)
            for ys in product((F(0),F(1,3),F(1)),repeat=4):
                y=((ys[0],ys[1]),(ys[2],ys[3]))
                Y=[]
                for u in range(2):
                    denom=sum(q[x][u]*s[x] for x in range(2))
                    Y.append(sum(q[x][u]*s[x]*y[x][u] for x in range(2))/denom)
                assert observation(s,y)==observation(s,(tuple(Y),tuple(Y)))
        print('EQUALITY',name,'four_rank_det=',str(D),'full64=',len(full),'LR16=',len(lr),'constructive_cases=',3**6)
    return True

q1=((F(7,20),F(3,20)),(F(3,20),F(7,20)))
r1=(F(1,2),F(3,2))
ke1=(F(7,20),F(17,40))
b1=((F(1,4),F(5,16)),(F(3,8),F(7,16)))
q2=((F(1,20),F(9,20)),(F(3,10),F(1,5)))
r2=(F(4,7),F(16,13))
ke2=(F(2,5),F(3,10))
b2=((F(1,3),F(2,5)),(F(3,8),F(5,12)))
case('baseline_c_unequal',q1,r1,ke1,b1,((F(1,8),F(-1,20)),(F(-1,16),F(1,10))))
case('baseline_c_equal',q1,r1,ke1,b1,((F(1,20),F(-1,16)),(F(1,20),F(-1,16))))
case('perturbed_c_unequal',q2,r2,ke2,b2,((F(0),F(1,9)),(F(0),F(-1,12))))
case('perturbed_c_equal',q2,r2,ke2,b2,((F(1,12),F(1,14)),(F(1,12),F(1,14))))
print('PASS_EXACT_GENERAL_STOP_DIAMOND_ALL_WEIGHTS_SHARED_ERROR_SLOPES')
