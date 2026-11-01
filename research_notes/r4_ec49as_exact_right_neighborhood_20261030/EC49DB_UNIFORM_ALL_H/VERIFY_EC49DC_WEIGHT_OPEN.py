"""Independent second-weight audit for EC49DC generic finite-horizon BRC theorem.
Requires adjacent EC49DB_SEEDS.json.zlib.b64 and VERIFY_EC49DB_GITHUB.py.
"""
from math import prod
import VERIFY_EC49DB_GITHUB as v

G = (
    ('1111', '3111', '2311'),
    ('3211', '2111', '3221'),
    ('1112', '1122', '3112'),
    ('1211', '2121', '3121'),
)

def det3(rows):
    a,b,c=rows
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def check(x,y):
    gamma=[]
    for gadgets in G:
        rows=[tuple(prod(w[int(i)-1] for i in g) for g in gadgets) for w in (x,y)]
        rows.append((1,1,1))
        gamma.append(det3(rows))
    q=(x[0]-x[2])*(y[1]-y[2])-(x[1]-x[2])*(y[0]-y[2])
    assert q!=0 and all(gamma)
    print({'W0':x,'W1':y,'Q':q,'boundary_gadget_dets':gamma})
    v.W=x,y
    v.main() # all nine seed minors and all 1,298 lifted interior minors

if __name__=='__main__':
    check((2,3,3,2,1,1),(3,2,3,2,1,1))
    check((2,3,5,2,1,1),(5,4,5,2,1,1))
