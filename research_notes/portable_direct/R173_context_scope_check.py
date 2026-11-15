"""R173 exact finite checks for left-only/right-only/two-sided observer quotients."""
from collections import deque
from itertools import product
from math import gcd
import json


def image(q,d):
    zero=(0,)*d
    generators=[]
    for i in range(d):
        for sign in (-1,1):
            v=list(zero);v[i]=sign%q
            generators.append((1,tuple(v),tuple(v)))
    seed=(0,zero,zero)
    todo=deque([seed]); states={seed}
    while todo:
        a,b,c=todo.popleft()
        for aa,bb,cc in generators:
            s=((a+aa)%q,tuple((x+y)%q for x,y in zip(b,bb)),
               tuple((x+y+aa*z)%q for x,y,z in zip(c,cc,b)))
            if s not in states:
                states.add(s);todo.append(s)
    return states


def main():
    cases=[(2,1),(2,6),(3,1),(3,3),(4,1),(4,3),(6,2),(8,2),(12,1)]
    checks={}
    for q,d in cases:
        states=image(q,d)
        right={(b,c) for _,b,c in states}
        left={(a,c) for a,_,c in states}
        both=len(states)
        pred_right=q**(2*d)
        pred_left=q**(d+1)//(2 if q%4==0 else 1)
        pred_both=q**(2*d+1)//gcd(q,4)
        assert (len(right),len(left),both)==(pred_right,pred_left,pred_both),(q,d)
        checks[f'q{q}_d{d}']={'right':len(right),'left':len(left),'two_sided':both,
                              'predictions_match':True}
    # Literal context-equivalence tests from words of length <=3 on signed two-axis alphabet.
    q,d=4,2
    letters=[(i,z) for i in range(d) for z in (-1,1)]
    words=[w for n in range(4) for w in product(letters,repeat=n)]
    def state(w):
        b=[0]*d;c=[0]*d
        for i,z in w:
            b[i]+=z
            for j in range(d):c[j]+=b[j]
        return (len(w)%q,tuple(x%q for x in b),tuple(x%q for x in c))
    tests=0
    L=((0,1),)
    for u in words:
        for v in words:
            a,b,c=state(u);aa,bb,cc=state(v)
            right_context=(c==cc and state(u+L)[2]==state(v+L)[2])
            left_context=(c==cc and state(L+u)[2]==state(L+v)[2])
            assert right_context==(b==bb and c==cc)
            assert left_context==(a==aa and c==cc)
            tests+=1
    print(json.dumps({'marker':'R173_DIRECTIONAL_CONTEXT_QUOTIENT_EXACT_PASS',
                      'group_image_cases':checks,'context_word_pairs_q4_d2':tests,
                      'theorem_scope':'all q>=2, all d>=1, signed primitive direction words',
                      'independent_review':'NOT_REVIEWED'},sort_keys=True,indent=2))


if __name__=='__main__':main()
