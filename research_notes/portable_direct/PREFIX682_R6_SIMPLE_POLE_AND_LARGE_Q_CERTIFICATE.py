#!/usr/bin/env python3
"""PREFIX-682-R6: exact local simple-pole and large-q diagonal-edge crossing.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Imports the unmodified PREFIX-680 189-layer frozen kernel from the same directory.
Uses integer and Fraction arithmetic; all sign comparisons are exact.
"""
import json
from math import comb
from fractions import Fraction as Q
import PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE as m

C=Q(106521,2000000)
R=Q(1,2000000)
AL=Q(2663,50000)
AR=Q(53261,1000000)
QL=Q(5326047313,100000000000)
QR=Q(5326047314,100000000000)

def proof():
    # Uses the unchanged exact frozen acceptance predicate and 189 survivor rows.
    rows=m.frozen_rows()
    m.b_num,m.b_den=C.numerator,C.denominator
    S,S1,S2=m.jet(rows)
    S0=[Q(row.get(0,0)) for row in rows]
    K=[[Q(comb(n+j,n),2**(n+j+1)) for j in range(m.N)] for n in range(m.N)]
    J=[[Q(n+j+1,2)*K[n][j] for j in range(m.N)] for n in range(m.N)]
    dot=m.dot
    md=2*sum(S)-dot(S,S,K)
    me=sum(S0)+sum(S)-dot(S0,S,K)
    md1=2*sum(S1)-2*dot(S1,S,K)
    me1=sum(S1)-dot(S0,S1,K)
    md2=2*sum(S2)-2*dot(S2,S,K)-2*dot(S1,S1,K)
    me2=sum(S2)-dot(S0,S2,K)
    hd=2*sum((n+1)*S[n] for n in range(m.N))-dot(S,S,J)
    he=sum((n+1)*(S0[n]+S[n]) for n in range(m.N))-dot(S0,S,J)
    hd1=2*sum((n+1)*S1[n] for n in range(m.N))-2*dot(S1,S,J)
    he1=sum((n+1)*S1[n] for n in range(m.N))-dot(S0,S1,J)
    hd2=2*sum((n+1)*S2[n] for n in range(m.N))-2*dot(S2,S,J)-2*dot(S1,S1,J)
    he2=sum((n+1)*S2[n] for n in range(m.N))-dot(S0,S2,J)
    B0,B1,B2=md-me,md1-me1,md2-me2
    A0=2*(hd-he)-md**2+me**2
    A1=2*(hd1-he1)-2*(md*md1-me*me1)
    A2=2*(hd2-he2)-2*(md1**2+md*md2-me1**2-me*me2)
    jets=dict(A0=A0,A1=A1,A2=A2,B0=B0,B1=B1,B2=B2)
    floors={name:(v*10**8).__floor__() for name,v in jets.items()}
    assert floors==dict(A0=-4562,A1=-169792160954,A2=-6657264578649,
                        B0=793095029,B1=12820091523,B2=-99474141353)
    # PREFIX-680's globally certified uniform third-derivative majorants.
    M=m.N-1; d2=2*M*(M-1);d3=4*M*(M-1)*(M-2)
    u0=3*m.N;u1=4*m.N*M;u2=m.N*(4*d2+2*M*M)
    u3=m.N*(4*d3+6*M*d2);h3=m.N*m.N*(4*d3+6*M*d2)
    a3=2*(2*h3+6*u1*u2+2*u0*u3)
    b3=2*u3
    assert (a3,b3)==(218571424275456,69527880576)
    da=abs(A2)*R+Q(a3,2)*R**2
    db=abs(B2)*R+Q(b3,2)*R**2
    assert -1800 < A1-da < A1+da < -1600
    assert 100 < B1-db < B1+db < 150
    eb=abs(B1)*R+abs(B2)*R**2/2+Q(b3,6)*R**3
    assert Q(793,100) < B0-eb < B0+eb < Q(794,100)
    def A_interval(x):
        h=x-C
        mid=A0+A1*h+A2*h*h/2
        err=Q(a3,6)*abs(h)**3
        return mid-err,mid+err
    assert AL==C-R and AR==C+R
    assert A_interval(AL)[0] > Q(798,1000000)
    assert A_interval(AR)[1] < 0
    assert AL<QL<QR<AR and QR-QL==Q(1,10**11)
    assert A_interval(QL)[0]>0 and A_interval(QR)[1]<0
    # For q>=10000, F_q(AL)>7.98-7.94>0, F_q(AR)<0, F_q'<0 on I.
    assert 10000*Q(798,1000000)>Q(794,100)
    return {
       'result':'ALL_CHECKS_PASS PREFIX682-R6',
       'scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
       'predecessor_kernel':'PREFIX680_R6_EXACT_THIRD_ORDER_CROSSOVER_CERTIFICATE.py',
       'survivor_rows':m.N,'occupied_cells':sum(map(len,rows)),
       'center':str(C),'radius':str(R),'A_zero_bracket':[str(QL),str(QR)],
       'bracket_width':str(QR-QL),'jet_floors_1e8':floors,
       'A_derivative_interval':'-1800 < A_prime(z) < -1600',
       'B_derivative_interval':'100 < B_prime(z) < 150',
       'B_interval':'793/100 < B(z) < 794/100',
       'large_slot_domain':'all real q>=10000',
       'crossover_count_on_I':'exactly one',
       'asymptotic_rate':'limit(q*(z_A-z_q))=B(z_A)/(-A_prime(z_A))',
       'rate_envelope':'793/(180000*q) < z_A-z_q < 794/(160000*q)',
       'status':'AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED'
    }
if __name__=='__main__':
    print(json.dumps(proof(),indent=2,ensure_ascii=False))
