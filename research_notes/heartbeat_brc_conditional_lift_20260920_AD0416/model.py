"""Declared diagnostic six-phase environment refresh; not a production field law."""
from fractions import Fraction as F
from itertools import product
from math import comb
from enterprise_math.brc_control_port import ControlPacket
from enterprise_math.brc_conditional_lift import ConditionalLift
from enterprise_math.brc_transport import Affine, eye

MASKS = tuple(product((0, 1), repeat=6))
STATES = tuple((r, mask) for r in range(4) for mask in MASKS)
INDEX = {state:i for i,state in enumerate(STATES)}
LABELS = tuple(7*r+sum(mask) for r,mask in STATES)
LIFT = ConditionalLift.uniform(LABELS)


def phase_packet(phase, *, start=0, retention=F(3, 4), refresh=True):
    if type(phase) is not int or not 0 <= phase < 6:
        raise ValueError('phase must be in 0..5')
    targets = tuple(tuple(i for i,a in enumerate(LABELS) if a==b) for b in range(28))
    moves = tuple(Affine(eye(6), tuple(sign if i==phase else 0 for i in range(6)))
                  for sign in (1, -1))
    edges = []
    for i,(r,mask) in enumerate(STATES):
        k = sum(mask)
        sigma = 1 if r in (0,3) else -1
        gain = 1+F(sigma,2)*(mask[phase]-F(k,6))
        plus = F(k+1,8)
        for sign, probability, action in ((1,plus,moves[0]),(-1,1-plus,moves[1])):
            next_r = (r+sign*(phase==0)) % 4
            next_k = 6-k if sign==1 else k
            if refresh:
                js = targets[7*next_r+next_k]
                share = F(1,comb(6,next_k))
            else:
                new_mask = tuple(1-b for b in mask) if sign==1 else mask
                js, share = (INDEX[next_r,new_mask],), F(1)
            for j in js:
                edges.append((i,j,retention*gain*probability*share,action,1))
    return ControlPacket.from_edges(256,start,1,edges)


def mass_edges(packet):
    return tuple((i,j,hist.forget_effects().total_mass) for i,j,hist in packet.blocks)


def row_push(vector, edges, size):
    out=[F(0)]*size
    for i,j,w in edges:
        if vector[i]:
            out[j]+=vector[i]*w
    return tuple(out)


def endpoint_push(mu, packet):
    # Independent explicit endpoint oracle; deliberately expands fine controls.
    rows={}
    for i,j,hist in packet.blocks:
        for w,act,n in hist.entries:
            rows.setdefault(i,[]).append((j,w*n,act))
    cache={}
    out={}
    for (i,x),weight in mu.items():
        for j,w,action in rows.get(i,()):
            key=action,x
            if key not in cache:
                y=action.apply(x)
                if any(v.denominator!=1 for v in y):
                    raise AssertionError('nonintegral native displacement')
                cache[key]=tuple(int(v) for v in y)
            target=j,cache[key]
            out[target]=out.get(target,F(0))+weight*w
    return out


def lift_endpoints(coarse):
    out={}
    for (a,x),weight in coarse.items():
        if x[0]%4 != a//7:
            raise ValueError('residue is tied to the spatial coordinate')
        for i,label in enumerate(LABELS):
            if label==a:
                out[i,x]=weight*LIFT.probabilities[i]
    return out


def partial_refresh_packet(theta):
    """Two interacting bits: after gain, refresh jointly with probability theta."""
    if isinstance(theta,bool) or not isinstance(theta,(int,F)) or not 0<=theta<=1:
        raise ValueError('theta must be an exact rational in [0,1]')
    weights=(F(9,8),F(3,8),F(3,8),F(9,8))
    edges=[]
    for i,w in enumerate(weights):
        if theta<1:edges.append((i,i,w*(1-theta),Affine.identity(6),1))
        if theta:
            edges.extend((i,j,w*theta/4,Affine.identity(6),1) for j in range(4))
    return ControlPacket.from_edges(4,0,1,edges)
