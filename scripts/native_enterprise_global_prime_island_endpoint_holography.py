#!/usr/bin/env python3
"""Exact endpoint-decoding replay for the frozen global prime-island spectrum 3..9."""

from __future__ import annotations


def shell_base(r: int) -> int:
    return 1 + 3*r*(r-1)//2


def filament_value(r: int, h: int) -> int:
    return h + (3*r*r)//2 + 1 + (0 if r%2==0 else 1)//2


def filament_value_exact(r: int, h: int) -> int:
    # integer-safe form of h + 3r^2/2 + 1 + (1-(-1)^r)/4
    if r%2==0:
        return h + 3*r*r//2 + 1
    return h + 3*(r*r+1)//2


def decode3(a: int, z: int):
    D=z-a
    assert D%2==0
    u=(D-4)//2
    sigma=u%3
    r=(u-sigma)//3
    if u%2==0:
        K=4; b=a+u
    else:
        K=2; b=a+u+1
    t=a-shell_base(r)-sigma*r
    return [a,b,z],(r,t,sigma,K)


def decode4(a: int, d: int):
    D=d-a
    rem=D%3
    if rem==1:
        K=4
    elif rem==2:
        K=2
    else:
        raise AssertionError((a,d,D))
    b=(2*a+d-6-K)//3
    c=a+d-6-b
    # feed the first triangle to the primitive localizer
    delta=(4-K)//2
    u=b-a-delta
    sigma=u%3
    r=(u-sigma)//3
    t=a-shell_base(r)-sigma*r
    return [a,b,c,d],(r,t,sigma,K)


def decode_filament(a: int, b: int, k: int):
    d=k-1
    D=b-a
    if d%2==0:
        assert D%(3*d)==0
        M=D//(3*d)
        J=d//2
        chi=1 if M%2==0 else -1
        KJ=3*J*J + (chi if J%2 else 0)
        center=(a+b-KJ)//2
        h=center-filament_value_exact(M,0)
        R=M-J
    else:
        mod=3*d
        rem=(2*D)%mod
        if rem==1:
            chi=1
        elif rem==mod-1:
            chi=-1
        else:
            raise AssertionError((k,D,rem,mod))
        R=(((2*D-chi)//(3*d))-d)//2
        assert (1 if R%2==0 else -1)==chi
        h=a-filament_value_exact(R,0)
    vals=[filament_value_exact(R+i,h) for i in range(k)]
    return vals,(R,h)


def main() -> None:
    witnesses={
        3:[37,53,73],
        4:[17,29,43,61],
        5:[3767,3919,4073,4231,4391],
        6:[63611,64231,64853,65479,66107,66739],
        7:[363269,364747,366227,367711,369197,370687,372179],
        8:[1370471,1373341,1376213,1379089,1381967,1384849,1387733,1390621],
        9:[171283421,171315481,171347543,171379609,171411677,171443749,171475823,171507901,171539981],
    }

    vals,meta=decode3(witnesses[3][0],witnesses[3][-1])
    assert vals==witnesses[3]

    vals,meta=decode4(witnesses[4][0],witnesses[4][-1])
    assert vals==witnesses[4]

    expected_meta={5:(50,16),6:(206,-44),7:(492,172),8:(956,-434),9:(10686,-2474)}
    for k in range(5,10):
        vals,meta=decode_filament(witnesses[k][0],witnesses[k][-1],k)
        assert vals==witnesses[k]
        assert meta==expected_meta[k]

    print("GLOBAL_ISLAND_ENDPOINT_HOLOGRAPHY=PASS k=3..9")
    print("K3_DECODER=PASS")
    print("K4_DECODER=PASS")
    print("K5_TO_K9_FILAMENT_DECODER=PASS")


if __name__ == "__main__":
    main()
