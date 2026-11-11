"""Check terminal direction recurrence and explicit blind/visible probe examples."""
from fractions import Fraction as Q
import json


def data(length):
    weights=[Q(1)]*3
    for n in range(3,length+3):
        for i,z in enumerate((Q(1,4),Q(1),Q(4))):
            weights[i]*=n*z/(1+n*z)
    a,b,c=weights
    x,z=7*a/b,b/c
    alpha=x*(1-z)/(x+1)
    assert x==Q(840,(length+4)*(length+5)*(length+6))
    return weights,z,alpha


def coordinate(weights,u):
    a,b,c=weights
    row=(7*a,u*b,(1-u)*c)
    return tuple(value/sum(row) for value in row)


def main():
    slopes=[]
    z_prev=None
    for length in range(41):
        weights,z,alpha=data(length)
        if z_prev is not None: assert z/z_prev==Q(4*length+9,4*length+12)
        p=coordinate(weights,Q(2,7));q=coordinate(weights,Q(5,7))
        dt=p[2]-q[2]
        assert dt>0 and q[0]-p[0]==alpha*dt and q[1]-p[1]==(1-alpha)*dt
        slopes.append(alpha)
        z_prev=z
    assert slopes[:2]==[Q(0),Q(3,20)]
    assert slopes[3]<slopes[4]==Q(6601,26624) and slopes[4]>slopes[5]
    assert slopes[1]<Q(1,5)<slopes[2] and slopes[7]<Q(1,5)<slopes[6]
    # x_length < 840/(length+4)^3. This excludes all remaining lengths
    # before relying on the separate general unimodality proof.
    cases=[]
    for third in (Q(7,20),Q(13,40)):
        root=(third-Q(1,4))/(Q(3,4)-Q(1,4))
        length=0
        blind=[]
        while (length+4)**3*root<840:
            if data(length)[2]==root: blind.append(length)
            length+=1
        cases.append(dict(first_column=['3/4','1/4',str(third)],root=str(root),
                          first_excluded_length=length,blind_lengths=blind))
    assert cases[0]['blind_lengths']==[] and cases[1]['blind_lengths']==[1]
    return dict(peak_length=4,peak_direction=str(slopes[4]),probes=cases,
                checked_direction_lengths=41)


if __name__=='__main__':
    print(json.dumps(main(),indent=2))
