#!/usr/bin/env python3
"""R216 exact single-pattern avoidance and first-divergence checks.
Observer combinatorics only; no physical native BRC propagation.
"""
import itertools
import json

def border_poly(word):
    h = len(word)
    assert h >= 1
    return [1] + [int(word[:h-i] == word[i:]) for i in range(1,h)]

def avoid_via_border(word, alphabet_size, max_length):
    """Coefficients of C(z)/(z**h+(1-a*z)*C(z)), using exact integers."""
    assert alphabet_size>=1 and len(word)>=1 and max_length>=0
    h=len(word); c=border_poly(word); den=[0]*(h+1); den[0]=1
    for i in range(1,h+1):
        den[i]=(c[i] if i<h else 0)-alphabet_size*c[i-1]+(1 if i==h else 0)
    output=[]
    for n in range(max_length+1):
        val=c[n] if n<h else 0
        for i in range(1,min(n,h)+1):
            val-=den[i]*output[n-i]
        assert 0<=val<=alphabet_size**n
        output.append(val)
    return c,den,output

def avoid_via_prefix_automaton(word,alphabet_size,max_length):
    h=len(word); dp=[0]*h; dp[0]=1; output=[1]
    for _ in range(max_length):
        nxt=[0]*h
        for state,count in enumerate(dp):
            if not count: continue
            for letter in range(alphabet_size):
                candidate=word[:state]+(letter,)
                q=min(h,len(candidate))
                while candidate[-q:]!=word[:q]:
                    q-=1
                    if not q: break
                if q<h: nxt[q]+=count
        dp=nxt
        output.append(sum(dp))
    return output

def avoid_bruteforce(word,alphabet_size,n):
    h=len(word)
    return sum(
        not any(t[i:i+h]==word for i in range(n-h+1))
        for t in itertools.product(range(alphabet_size),repeat=n)
    )

def stirling(n,k):
    row=[1]
    for step in range(1,n+1):
        nxt=[0]*(step+1)
        for j in range(1,step+1):
            nxt[j]=(row[j-1] if j-1<len(row) else 0)+(j*row[j] if j<len(row) else 0)
        row=nxt
    return row[k] if k<len(row) else 0

def full_fibre_total(m,k,L,r):
    from math import comb,factorial
    def W(j):
        return factorial(j)*m**L*sum(stirling(L+1,t+1) for t in range(min(j,L)+1))
    return sum(comb(k-r,j-r)*W(j) for j in range(r,k+1))

def two_sided_ideal_size(word,m,k,L):
    assert 0<=len(word)<L
    a=m*(k+1)
    r=len(set(tag for _,tag in word if tag))
    if not word:
        short=sum(a**n for n in range(L))
    else:
        av=avoid_via_border(word,a,L-1)[2]
        short=sum(a**n-av[n] for n in range(L))
    return full_fibre_total(m,k,L,r)+short

def verify():
    tests=0; enumerations=0; first_difference_tests=0; equal_spectrum_tests=0
    sample=[]
    for a,hmax,maxn in [(2,6,8),(3,4,7),(4,3,6)]:
        for h in range(1,hmax+1):
            patterns=list(itertools.product(range(a),repeat=h))
            for word in patterns:
                C,D,avoidance=avoid_via_border(word,a,maxn)
                alt=avoid_via_prefix_automaton(word,a,maxn)
                assert avoidance==alt,(a,word,avoidance,alt)
                for n in range(maxn+1):
                    brute=avoid_bruteforce(word,a,n)
                    enumerations+=a**n
                    assert avoidance[n]==brute,(a,word,n,avoidance[n],brute)
                tests+=1
                if len(sample)<4:
                    sample.append({
                        'a':a,'word':''.join(map(str,word)),
                        'C':C,'denominator':D,'avoid_n0_to8':avoidance[:9]
                    })
            for i,u in enumerate(patterns):
                for v in patterns[i+1:]:
                    C=border_poly(u); E=border_poly(v)
                    d=next((p for p in range(h) if C[p]!=E[p]),None)
                    au=avoid_via_border(u,a,maxn)[2]
                    av=avoid_via_border(v,a,maxn)[2]
                    if d is None:
                        assert au==av
                        equal_spectrum_tests+=1
                    elif h+d<=maxn:
                        assert au[:h+d]==av[:h+d],(a,u,v,d)
                        assert au[h+d]-av[h+d]==C[d]-E[d],(a,u,v,d)
                        first_difference_tests+=1
    large_a_checks=0
    for word in [(0,),(0,0),(0,1),(0,1,0),(0,0,0),
                 (83,83),(0,83,0),(0,1,0,1)]:
        _,_,p=avoid_via_border(word,84,28)
        q=avoid_via_prefix_automaton(word,84,28)
        assert p==q
        large_a_checks+=1
    u=((0,1),(0,1)); v=((0,1),(0,0))
    assert two_sided_ideal_size(u,1,1,4)==20
    assert two_sided_ideal_size(v,1,1,4)==21
    assert two_sided_ideal_size(u,1,1,3)==two_sided_ideal_size(v,1,1,3)
    future_u=((0,0),(0,1))
    future_v=((0,1),(0,0))
    future_0=(0,0)
    assert border_poly((0,1))==border_poly((1,0))==[1,0]
    assert two_sided_ideal_size(future_u,1,1,6)==106
    assert two_sided_ideal_size(future_v,1,1,6)==106
    assert two_sided_ideal_size(future_u+(future_0,),1,1,6)==80
    assert two_sided_ideal_size(future_v+(future_0,),1,1,6)==81
    return {
        'status':'PASS','pattern_models':tests,'large_a84_models':large_a_checks,
        'exhaustively_inspected_input_words':enumerations,
        'same_border_pair_checks':equal_spectrum_tests,
        'first_distinguishable_coefficient_pair_checks':first_difference_tests,
        'sample':sample,
        'witness':{
            'parameters':{'m':1,'k':1,'a':2,'L':4},
            'patterns':['11','10'],'border_polynomials':['1+z','1'],
            'avoid_n0_to4':[
                avoid_via_border((1,1),2,4)[2],
                avoid_via_border((1,0),2,4)[2]
            ],
            'two_sided_ideal_sizes':[20,21],
            'first_distinguishable_word_length':3,
            'first_distinguishable_tail_cutoff_L':4
        },
        'future_congruence_counterexample':{
            'parameters':{'m':1,'k':1,'L':6},
            'u':'01','v':'10','shared_initial_border':'1',
            'shared_initial_ideal_size':106,
            'appended_letter':'0','new_words':['010','100'],
            'new_border_polynomials':['1+z^2','1'],
            'new_ideal_sizes':[80,81]
        },
        'scope':'a=2 through h=6/n=8, a=3 through h=4/n=7, a=4 through h=3/n=6; 84-symbol DP check',
        'arithmetic':'exact integer observer word counting',
        'review':'NOT_REVIEWED',
        'native_brc_integration':'NOT_EXECUTED'
    }

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
