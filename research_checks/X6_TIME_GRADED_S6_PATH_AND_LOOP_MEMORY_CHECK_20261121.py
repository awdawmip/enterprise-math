import itertools
import json
from pathlib import Path

N = 6
I = tuple(range(N))
P = tuple(itertools.permutations(I))

def mul(p, q):
    return tuple(p[q[j]] for j in I)

def action(x, f, a):
    if a[0] == 'U':
        y = list(x)
        y[f[a[1]]] += a[2]
        return tuple(y), f
    return x, mul(f, a[1])

def summary(word):
    x, f, ns, nr = (0,)*N, I, 0, 0
    for a in word:
        x, f = action(x, f, a)
        ns += a[0] == 'U'
        nr += a[0] == 'R'
    return x, f, ns, nr

def compose(A, B):
    d, h, n, r = A
    e, k, m, s = B
    v = list(d)
    for j in I:
        v[h[j]] += e[j]
    return tuple(v), mul(h,k),n+m,r+s

def run():
    rotations = []
    for j in range(5):
        p = list(I)
        p[j], p[j+1] = p[j+1], p[j]
        rotations.append(tuple(p))
    generators = [('U',j,eps) for j in I for eps in (-1,1)] + [('R',p) for p in rotations]
    checks = 0
    for f in P:
        for a,b in itertools.product(generators, repeat=2):
            observed = action(*action((0,)*N,f,a),b)
            d,h,_,_ = compose(summary((a,)),summary((b,)))
            v = [0]*N
            for j in I:
                v[f[j]] += d[j]
            assert observed == (tuple(v),mul(f,h))
            checks+=1
    loops={}
    for W in range(1,5):
        values=set()
        for code in itertools.product(range(12),repeat=W):
            word=[]
            for c in code:
                j,eps=c//2, (-1 if c%2 == 0 else 1)
                word += [('U',j,eps),('U',j,-eps)]
            assert summary(word)==((0,)*N,I,2*W,0)
            values.add(code)
        assert len(values)==12**W
        loops[str(W)]={'histories':len(values),'bits':(len(values)-1).bit_length(),'signed_events':2*W}
    a,b=('U',0,1),('U',1,1)
    assert summary((a,b))==summary((b,a))
    assert action((0,)*N,I,a)[0]!=action((0,)*N,I,b)[0]
    return {'schema':'X6_TIME_GRADED_PATH_EXACT_V1','frames':720,'generators':17,'ordered_generator_pairs':289,'semidirect_checks':checks,'mismatches':0,'return_pair_history':loops,'two_ordered_words_same_end_state_different_prefix':True,'scope':'P000_SIGNED_X6_CELL_PATH_VOCABULARY_WITH_S6_FRAME_SKELETON','physical_triad_update':'UNSPECIFIED','status':'AUTHOR_EXACT_FINITE_CHECKED_NOT_ADMITTED'}

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('X6_TIME_GRADED_S6_PATH_AND_LOOP_MEMORY_RESULTS_20261121.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
