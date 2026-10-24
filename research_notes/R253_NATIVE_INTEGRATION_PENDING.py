"""EXACT NATIVE IMPORT CHECK — NOT EXECUTED ON THIS HOST.
Run only in matching enterprise-math source environment. This is an executable
integration test template, not a proof of native heartbeat legality.
"""
from collections import Counter
from fractions import Fraction
from enterprise_math.brc_transport import Affine, eye
from enterprise_math.brc_control_port import ControlPacket

Z=(0,)*6
S=tuple(tuple(-1 if i==j and i in (0,1) else (1 if i==j else 0)
              for j in range(6)) for i in range(6))

def effect(eps,k):
    a = eye(6) if eps==1 else S
    return Affine(a, (k,0,0,0,0,0))

def make_packet(start):
    # ControlPacket.start is TIME port, not initial control state.
    edges = [(0,2,1,effect(-1,-1),1), (0,2,1,effect(1,-1),1),
             (1,0,1,effect(-1,-1),1), (1,0,1,effect(1,-1),1),
             (2,1,1,effect(1,1),1),  (2,2,1,effect(1,-1),1)]
    return ControlPacket.from_edges(3,start=start,duration=1,edges=edges)

def observed(packet, source):
    out=Counter()
    for src,dst,h in packet.blocks:
        if src!=source: continue
        for weight,action,count in h.entries:
            assert weight==Fraction(1)
            p=action.inverse().apply(Z)
            eps=int(action.a[0][0])
            out[(dst,int(p[0]),eps)]+=count
            assert action.b[0]==-eps*p[0]
    return out

if __name__=="__main__":
    p=ControlPacket.identity(3,start=0)
    for m in range(4):
        assert p.start==0 and p.end==m
        a,b=observed(p,0), observed(p,1)
        aggregate=lambda x: Counter({key:sum(v for (q,p,e),v in x.items() if p==key)
                                     for key in {k[1] for k in x}})
        assert aggregate(a)==aggregate(b)
        if m<=2: assert Counter({(p,e):sum(c for (q,pp,ee),c in a.items() if (pp,ee)==(p,e))
                                 for p,e in {(p,e) for (q,p,e) in a}})==Counter({(p,e):sum(c for (q,pp,ee),c in b.items() if (pp,ee)==(p,e))
                                 for p,e in {(p,e) for (q,p,e) in b}})
        if m==3: assert a!=b
        if m<3:p=p.then(make_packet(m))
    print("R253_NATIVE_INTEGRATION_CHECK=PASS; DEPTH=0..3")
