"""R175 exact six-axis signed-port / provenance-monoid lift; author checker.
No native positive Weighted-BRC or physical heartbeat execution is claimed.
"""
from fractions import Fraction as Q
import json

D = 6
Z = (Q(0),) * D
E, F = (0, 1), (0, -1)
I = (0, 0)

def mul(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 3)

def quotient(x):
    return x[0]

def path_stats(path):
    d, j = [0]*D, [0]*D
    for axis, sign in path:
        d[axis] += sign
        for k in range(D):
            j[k] += d[k]
    return len(path), tuple(d), tuple(j)

def moments(family, projection=lambda x: x):
    out = {}
    for a, b, w, label, path in family:
        key = (a, b, projection(label))
        if key not in out:
            out[key] = [Q(0), Q(0), [Q(0)]*D, [Q(0)]*D]
        rec = out[key]
        n, d, j = path_stats(path)
        rec[0] += w
        rec[1] += w*n
        for k in range(D):
            rec[2][k] += w*d[k]
            rec[3][k] += w*j[k]
    return {k: (a, l, tuple(b), tuple(c)) for k, (a,l,b,c) in out.items()}

def serial(f, g):
    return [(i, k, w*v, mul(label, tag), p+q)
            for i,j,w,label,p in f for jj,k,v,tag,q in g if j == jj]

def summary_serial(f, g, projection=lambda x: x):
    left = moments(f, projection)
    right = moments(g, projection)
    out = {}
    for (i,j,tag),(a,l,b,c) in left.items():
        for (jj,k,tag2),(a2,l2,b2,c2) in right.items():
            if j != jj: continue
            newtag = mul(tag, tag2) if projection is not quotient else (tag+tag2)%2
            key = (i,k,newtag)
            rec = out.setdefault(key, [Q(0),Q(0),[Q(0)]*D,[Q(0)]*D])
            rec[0] += a*a2
            rec[1] += l*a2 + a*l2
            for h in range(D):
                rec[2][h] += b[h]*a2 + a*b2[h]
                rec[3][h] += c[h]*a2 + a*c2[h] + b[h]*l2
    return {k:(a,l,tuple(b),tuple(c)) for k,(a,l,b,c) in out.items()}

def strip_zero(v):
    zero = (Q(0),Q(0),Z,Z)
    return {k:x for k,x in v.items() if x != zero}

def branch(w, label, path, a=0, b=0):
    return (a,b,Q(w),label,tuple(path))

def selected_C(f, label):
    return moments(f).get((0,0,label),(0,0,Z,Z))[3]

def main():
    fam=[]
    alphabet=[(a,s) for a in (0,1,5) for s in (-1,1)]
    for t in range(36):
        group=[]
        for k in range(4):
            label=((t+k)%2,(2*t+k)%3)
            length=(2*t+3*k)%4
            path=[alphabet[(t+2*k+h)%6] for h in range(length)]
            group.append(branch(Q((-1)**(t+k)*(k+1),k%3+1), label, path,
                                (t+k)%2, (t+(k//2))%2))
        fam.append(group)
    checks=0
    quotient_checks=0
    for a in fam:
        for b in fam:
            fg=serial(a,b)
            assert strip_zero(moments(fg)) == strip_zero(summary_serial(a,b))
            assert strip_zero(moments(fg, quotient)) == strip_zero(summary_serial(a,b,quotient))
            checks += 1
            quotient_checks += 1
    # Positive-multiplicity witness: same unlabeled four moments, distinct tag-selective C.
    red, blue = (0,0), (1,0)
    pos_f=[branch(1,red,(E,F)),branch(1,blue,(F,E))]
    pos_g=[branch(1,red,(F,E)),branch(1,blue,(E,F))]
    unlabeled=lambda fam: moments(fam,lambda _: 0)
    assert unlabeled(pos_f)==unlabeled(pos_g)
    assert selected_C(pos_f,red)[0]==Q(1)
    assert selected_C(pos_g,red)[0]==Q(-1)
    # Each coordinate can be isolated at any fixed label by short identity-labeled probes.
    witnesses={
      'A':[branch(1,red,())],
      'L':[branch(1,red,(E,F)),branch(1,red,(F,E)),branch(-2,red,())],
      'B':[branch(1,red,(E,E)),branch(-2,red,(E,F)),branch(1,red,(F,E))],
      'C':[branch(1,red,(E,F)),branch(-1,red,(F,E))],
    }
    expected={'A':(1,0,0,0),'L':(0,4,0,0),
              'B':(0,0,2,0),'C':(0,0,0,2)}
    probes={'A':([branch(1,I,(E,F))],[branch(1,I,())]),
            'L':([branch(1,I,(E,))],[branch(1,I,())]),
            'B':([branch(1,I,())],[branch(1,I,(E,))]),
            'C':([branch(1,I,())],[branch(1,I,())])}
    observations={}
    for k,f in witnesses.items():
        a,l,b,c=moments(f)[(0,0,red)]
        assert (a,l,b[0],c[0])==expected[k]
        assert b[1:]==Z[1:] and c[1:]==Z[1:]
        x,y=probes[k]
        observed=selected_C(serial(serial(x,f),y),red)
        assert observed[0]==Q(expected[k][{'A':0,'L':1,'B':2,'C':3}[k]])
        observations[k]=str(observed[0])
    # Quotient identifies b-coordinate colors; equality survives every serial context.
    p=[branch(1,(0,0),(E,))]
    r=[branch(1,(0,1),(E,))]
    assert moments(p,quotient)==moments(r,quotient)
    assert moments(p)!=moments(r)
    for x in fam[:9]:
        for y in fam[:9]:
            assert strip_zero(moments(serial(serial(x,p),y),quotient)) == strip_zero(moments(serial(serial(x,r),y),quotient))
    result={
      'marker':'R175_LABEL_MONOID_EXACT_PASS',
      'native_axes':6,'monoid':'Z2 x Z3',
      'signed_families':len(fam),'raw_vs_four_moment_pairs':checks,
      'quotient_pairs':quotient_checks,'quotient_double_context_cases':81,
      'positive_witness_unlabeled_equal':True,
      'positive_witness_red_C_F':'1','positive_witness_red_C_G':'-1',
      'minimality_independent_probe_values':observations,
      'arithmetic':'Python Fraction, exact',
      'status':'AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED',
      'native_weighted_brc_kernel_executed':False,
    }
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
