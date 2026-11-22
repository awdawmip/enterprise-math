#!/usr/bin/env python3
"""PREFIX-1008: integer-numerator Stage46 BRC, native X6 fixed k<=2.
State (chart-relative Cell, named incoming-neighbour port, negative count).
All amplitudes at step n are integers divided by 6**n. No floating point.
"""
import json
from collections import defaultdict
from fractions import Fraction

D = [(axis,sign) for sign in (1,-1) for axis in range(6)]
ZERO=(0,)*6
E1=(1,0,0,0,0,0)
START=(ZERO,6,0) # incoming-neighbour port -e1

def translated(x,d):
    y=list(x);axis,sgn=D[d];y[axis]+=sgn
    return tuple(y)

def opposite(d):return (d+6)%12

def blocked(x,d):return (x==ZERO and d==0) or (x==E1 and d==6)

def step(states,absorb=False):
    out=defaultdict(int)
    for (x,h,k),amp in states.items():
        for d in range(12):
            nk=k+(d>=6)
            if nk>2 or (absorb and blocked(x,d)):continue
            out[(translated(x,d),opposite(d),nk)]+=amp*(-5 if d==h else 1)
    return {s:a for s,a in out.items() if a}

def propagate(states,steps,absorb=False):
    for _ in range(steps):states=step(states,absorb)
    return states

def difference(a,b):
    return {s:a.get(s,0)-b.get(s,0) for s in a.keys()|b.keys()
            if a.get(s,0)!=b.get(s,0)}

def signed_sum(states,k,port_positive=None):
    return sum(a for (_,h,kk),a in states.items() if kk==k and
               (port_positive is None or (h<6)==port_positive))

def mass(states,k,n):
    numerator=sum(a*a for (_,_,kk),a in states.items() if kk==k)
    p=Fraction(numerator,36**n)
    return {'numerator':numerator,'denominator':36**n,'reduced':str(p)}

def exhaustive_five():
    first={str(t):{'paths':0,'signed_numerator':0} for t in range(1,6)}
    observed=defaultdict(int)
    def walk(x,h,k,amp,t,first_hit):
        if t==5:
            if k==2:
                observed[(x,h,k)]+=amp
                if first_hit:
                    v=first[str(first_hit)];v['paths']+=1;v['signed_numerator']+=amp
            return
        for d in range(12):
            nk=k+(d>=6)
            if nk>2:continue
            hit=first_hit or (t+1 if blocked(x,d) else None)
            walk(translated(x,d),opposite(d),nk,
                 amp*(-5 if h==d else 1),t+1,hit)
    walk(ZERO,6,0,1,0,None)
    return first,{s:a for s,a in observed.items() if a}

def four_loops():
    out=defaultdict(lambda:{'paths':0,'signed_numerator':0})
    def walk(x,h,k,amp,seq):
        if len(seq)==4:
            if x==ZERO and k==2:
                axes={d%6 for d in seq}
                label=('single' if len(axes)==1 else 'double')+'_'+('includes_e1' if 0 in axes else 'excludes_e1')
                out[label]['paths']+=1
                out[label]['signed_numerator']+=amp
            return
        for d in range(12):
            nk=k+(d>=6)
            if nk<=2 and not blocked(x,d):
                walk(translated(x,d),opposite(d),nk,amp*(-5 if d==h else 1),seq+(d,))
    walk(ZERO,6,0,1,())
    return dict(sorted(out.items()))

def main():
    first,exhaustive=exhaustive_five()
    loops=four_loops()
    assert loops=={
        'double_excludes_e1':{'paths':240,'signed_numerator':1680},
        'double_includes_e1':{'paths':70,'signed_numerator':-890},
        'single_excludes_e1':{'paths':30,'signed_numerator':-1050},
        'single_includes_e1':{'paths':2,'signed_numerator':650}}
    assert sum(t['paths'] for t in loops.values())==342
    assert sum(t['signed_numerator'] for t in loops.values())==390
    assert first=={
        '1':{'paths':7776,'signed_numerator':0},
        '2':{'paths':0,'signed_numerator':0},
        '3':{'paths':792,'signed_numerator':0},
        '4':{'paths':60,'signed_numerator':0},
        '5':{'paths':342,'signed_numerator':390}}
    free={START:1};masked={START:1}; masses={}; signed={}
    for n in range(1,10):
        free=step(free);masked=step(masked,True)
        if n==5:
            free5=free.copy();masked5=masked.copy();defect5=difference(free5,masked5)
            assert {s:a for s,a in free5.items() if s[2]==2}==exhaustive
            assert len(defect5)==2400
            assert [sum(1 for s in defect5 if s[2]==k) for k in range(3)]==[336,912,1152]
            assert signed_sum(defect5,2)==390
            grade1={s:a for s,a in defect5.items() if s[2]==1}
            leak=step(grade1)
            witness=(( -1,0,0,0,0,3),0,2)
            assert leak[witness]==-2
        if n>=5:
            assert propagate(masked5,n-5)==masked
            assert propagate(defect5,n-5)==difference(free,masked)
            assert signed_sum(masked,2)==-390*6**(n-5)
            assert signed_sum(masked,2,True)==0
            masses[str(n)]={'masked':mass(masked,2,n),'free':mass(free,2,n)}
            signed[str(n)]={'masked_k2_numerator_sum':signed_sum(masked,2),
                'masked_k1_positive_port_sum':signed_sum(masked,1,True)}
    cert={'schema':'PREFIX1008_R6_K2_NATIVE_LINK_PREFIX_EXACT_V1',
        'model':'X6 12 signed directions; start incoming -e1; C(h,d)=(1-6*[h=d])/6; absorb {0,e1}; exact two negative steps; sum by final (Cell,port).',
        'oriented_last_possible_forbidden_step':{'positive_0_to_e1':5,'negative_e1_to_0':4},
        'four_step_safe_return_orbits':loops,'grade2_first_forbidden_step_at_n5':first,
        'fifth_step_defect_fibers_by_grade':{'0':336,'1':912,'2':1152},
        'fifth_step_defect_total_fibers':2400,
        'exact_signed_amplitude_sum_all_n_ge_5':'-390/6**5 = -65/1296',
        'grade1_defect_feed_witness_n6':{'Cell':[-1,0,0,0,0,3], 'incoming_port':'+e1',
             'negative_steps':2,'omitted_numerator_if_grade1_seed_discarded':-2,'denominator':6**6},
        'probability_masses':masses,'signed_numerator_sums':signed,
        'verification':'Exhaustive ordered 5-step free paths, independent masked 4-step loop enumeration, and integer DP free/masked/finite-prefix identity on every terminal Cell-port-negative-count fibre for n=5..9. Integer only; not independent project Review.'}
    print(json.dumps(cert,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
