"""Recover a labelled transfer packet from six positive-integer beta2 observations."""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path


def load_reference():
    path=Path(__file__).resolve().parent.parent/'fiftyfirst/terminals_check.py'
    if sha256(path.read_bytes()).hexdigest()!='ca5cbac238324f4851ace7fe25c762dd88c583d8ed1ee82b530c5c4721dba128':
        raise ValueError('unexpected wave-51 transfer and resistance checker')
    spec=importlib.util.spec_from_file_location('wave51_terminals',path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ref=load_reference()
SHORT=((1,4,2,1),(2,2,3,1),(2,3,1,2),(3,1,2,2),(1,1,2,4),(1,1,1,1))
BINARY=tuple(tuple(map(int,s)) for s in ('1221211','2112211','2121121','2211112','1111222','1111111'))


def matrix_product(A,B):
    a,b,c,d=A
    e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)


def mixed(A,B):
    a,b,c,d=A
    e,f,g,h=B
    return a*h+d*e-b*g-c*f


def packet(ts):
    first,second,third=ts[1:]
    return first[0],first[1],second[2],second[0],second[1],third[2]


def lift(q,R,p):
    a,b,g,e,f,j=p
    d=q*R-a
    first=(a,b,q,d)
    second=(e,f,g,R*g-a*d+b*q-e)
    third=(R*j-mixed(first,second),0,j,0)
    return [(1,R,0,1),first,second,third]


def concatenate(left,right):
    return [tuple(map(sum,zip(*(matrix_product(right[k-i],left[i]) for i in range(k+1)))))
            for k in range(4)]


def rawF(A,B):
    T=concatenate(A,B)
    c1,c2,c3=[a+d for a,b,c,d in T[1:]]
    return c2*c2-2*c1*c3


def solve(A,b):
    n=len(A)
    aug=[[*map(Q,row),Q(y)] for row,y in zip(A,b)]
    for i in range(n):
        row=next(k for k in range(i,n) if aug[k][i])
        aug[i],aug[row]=aug[row],aug[i]
        pivot=aug[i][i]
        aug[i]=[v/pivot for v in aug[i]]
        for k in range(n):
            if k!=i:
                factor=aug[k][i]
                aug[k]=[v-factor*u for v,u in zip(aug[k],aug[i])]
    return [row[-1] for row in aug]


def survey(menu):
    ext=[ref.coeffs(B) for B in menu]
    rows=[(1,B[2][2],B[1][1],B[2][0]) for B in ext[:4]]
    return dict(paths=menu,m=len(menu[0]),sums=list(map(sum,menu)),u=[B[1][0] for B in ext],
                design=rows,determinant=int(ref.det(rows)))


def recover(q,R,menu,measured):
    n=q+len(menu[0])
    totals=[R+sum(path) for path in menu]
    ext=[ref.coeffs(B) for B in menu]
    info=survey(menu)
    F=[Q(y)*(n*L)**4/8 for y,L in zip(measured,totals)]

    def residual(p):
        A=lift(q,R,p)
        return [y-rawF(A,B) for y,B in zip(F,ext)]

    L=totals[0]
    dw=solve(info['design'],residual((0,)*6)[:4])[3]
    a=-dw/(4*n*L)
    constant,dx,dv,dw=solve(info['design'],residual((a,0,0,0,0,0))[:4])
    assert dw==0
    g=dx/(2*L*L)
    b=dv/(2*n*n)
    rest=[-y/(2*n*r) for y,r in zip(residual((a,b,g,0,0,0)),totals)]
    u=info['u']
    e=(rest[4]-rest[0])/(2*(u[4]-u[0]))
    d=q*R-a
    K=[2*s-len(B)*sum(B)+a-d for s,B in zip(u,menu)]
    j=(rest[5]-e*K[5]-rest[0]+e*K[0])/(totals[5]-L)
    f=(rest[0]-L*j-K[0]*e)/n
    return a,b,g,e,f,j


def read_and_check(A,menu):
    true=ref.coeffs(A)
    measurements=[ref.resistance_beta(A+list(B)) for B in menu]
    assert all(v==ref.value(A+list(B)) for v,B in zip(measurements,menu))
    result=recover(len(A),sum(A),menu,measurements)
    assert result==packet(true)
    return result,measurements


def one_vertex():
    symmetric_grid=0
    derivative_grid=0
    def F_polynomial(R,X,K,flipped=False):
        A=[Q(R+X,2),Q(R-X,2)]
        B=([2*K,K] if flipped else [K,2*K])
        return rawF(ref.coeffs(A),ref.coeffs(B))
    for R in range(1,6):
        for X in range(5):
            Y=X*X
            f=F_polynomial(R,X,1)
            rev=F_polynomial(R,X,1,True)
            assert f-rev==-Q(X,2)*(3*(R*R-Y)+42*R+24)
            sum_at_zero=F_polynomial(R,0,1)+F_polynomial(R,0,1,True)
            assert f+rev==sum_at_zero+Q(9,8)*Y**2+Q(-9*R*R-30*R+218,4)*Y
            symmetric_grid+=1
            for K in range(1,5):
                # Exact linear coefficient of a quartic; this grid is a formal identity check.
                deriv=(F_polynomial(R,X-2,K)-8*F_polynomial(R,X-1,K)
                       +8*F_polynomial(R,X+1,K)-F_polynomial(R,X+2,K))/12
                expected=(-6*K**3+Q(K*K,2)*(-21*R+109*X)
                          +Q(K,4)*(-3*R*R-30*R*X+9*X*X)+Q(9*X,4)*(X*X-R*R))
                assert deriv==expected
                derivative_grid+=1
    return dict(mirror_polynomial_grid=symmetric_grid,scaled_polynomial_grid=derivative_grid,
                fixed_two_paths=[[1,2],[2,1]],adaptive_one_path='[K,2K], K=ceil(10R)')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    menus=(SHORT,BINARY)
    info=[survey(menu) for menu in menus]
    assert [x['determinant'] for x in info]==[-32,-192]
    mesh=set(map(tuple,ref.probes()))
    assert all(B in mesh for B in BINARY)
    chains=[[Q(7,3)],[Q(1,7),Q(5,8)],[Q(15,14),2,Q(3,2)]]
    chains+= [list(p) for n in range(1,6) for p in product((1,3),repeat=n)]
    chains+= [[1,2,3,3,5,7,6],[3,1,4,1,5,9,2,6,5,3]]
    for A in chains:
        for menu in menus:
            read_and_check(A,menu)
    # Sealed updates: two successive extensions, with their full vertex sets used only for audit.
    base=[2,1,3,5,2,4,7]
    packet_zero,measured=read_and_check(base,SHORT)
    record=[]
    A=base[:]
    state=packet_zero
    for B in ([Q(1,3),Q(7,4),2],[5,Q(2,7),Q(3,2),4]):
        state=packet(concatenate(lift(len(A),sum(A),state),ref.coeffs(B)))
        A+=B
        assert state==packet(ref.coeffs(A))
        ring=ref.resistance_beta(A+[1,2,4])
        assert ring==ref.value(A+[1,2,4])
        read=8*Q(rawF(lift(len(A),sum(A),state),ref.coeffs([1,2,4])),((len(A)+3)*(sum(A)+7))**4)
        assert read==ring
        record.append(dict(extension=list(map(str,B)),new_packet=list(map(str,state)),ring_beta=str(read)))
    X=[1,4,3]
    reversal=[X,X[::-1]]
    assert all(ref.value(reversal[0]+[2]*l)==ref.value(reversal[1]+[2]*l) for l in range(1,9))
    sample=[str(ref.value(edges+[1,2])) for edges in reversal]
    assert sample[0]!=sample[1]
    output=dict(menus=info,portable_reference_chains=len(chains),verified_ring_readings=12*len(chains),
                base=base,packet=list(map(str,packet_zero)),six_readings=list(map(str,measured)),
                extensions=record,one_vertex=one_vertex(),symmetric_menu_reversal=sample)
    text=json.dumps(output,sort_keys=True,indent=2)+'\n'
    if args.out:
        args.out.write_text(text)
    else:
        print(text,end='')


if __name__=='__main__':
    main()
