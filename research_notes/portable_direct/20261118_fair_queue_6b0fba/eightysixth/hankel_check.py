"""Exact rational Hausdorff prefix thresholds of the signed AP tree polynomial."""
import json
from hashlib import sha256
from math import comb, factorial, prod
from flint import fmpq, fmpq_mat, fmpq_poly


def moments(m, depth):
    n = m-1
    d = n*(2*m-3)
    size = 2*m-1
    layers = [fmpq_mat(size,size) for _ in range(depth+1)]
    for s in range(min(n,depth+1)+1):
        for j in range(m):
            weight = fmpq((-1)**(s+j)*comb(n,s)*comb(n,j)*factorial(n),
                          prod(m*j+m*m*s+h for h in range(1,m+1)))
            vector = {j:1}
            for k in range(1,n+1):
                step = comb(j+m*s,k)-comb(j,k)
                if step:
                    vector[m+k-1] = step
            for i,x in vector.items():
                # Divide the bottom n rows, and only those rows, by t.
                layer = s-int(i>=m)
                if 0<=layer<=depth:
                    for col,y in vector.items():
                        layers[layer][i,col] += weight*x*y
    inverse = layers[0].inv()
    R = [None]+[inverse*layer for layer in layers[1:]]
    identity = fmpq_mat(size,size)
    for i in range(size):
        identity[i,i] = 1
    G = [identity]
    trace = [None]
    coeffs = [fmpq(1)]
    for k in range(1,depth+1):
        next_G = fmpq_mat(size,size)
        tr = 0
        for j in range(1,k+1):
            term = G[k-j]*R[j]
            next_G -= term
            tr += j*sum(term[i,i] for i in range(size))
        G.append(next_G)
        trace.append(tr)
        coeffs.append(sum(coeffs[k-i]*trace[i] for i in range(1,k+1))/k)
    return [c*(-1)**j/comb(d,j) for j,c in enumerate(coeffs)]


def original_tree(m,t):
    n = m-1
    w = [(-1)**i*comb(n,i) for i in range(m)]
    lap = fmpq_mat(2*m-1,2*m-1)
    for i in range(m):
        for j in range(m):
            edge = w[i]*w[j]*sum(fmpq(w[s]*t**s,1+i+m*j+m*m*s) for s in range(m))
            lap[i,i] += edge
            if j<n:
                lap[m+j,m+j] += edge
                lap[i,m+j] = lap[m+j,i] = -edge
    return lap.det()/t**n


def independent_prefix(m,depth):
    d = (m-1)*(2*m-3)
    q = fmpq_poly([0])
    for t in range(1,d+2):
        basis = fmpq_poly([1])
        for r in range(1,d+2):
            if r!=t:
                basis = basis*fmpq_poly([-r,1])/(t-r)
        q += original_tree(m,t)*basis
    return [q[j]*(-1)**j/(q[0]*comb(d,j)) for j in range(depth+1)]


def determinants(h,k):
    r = k//2
    if k%2:
        A = [[h[i+j+1] for i in range(r+1)] for j in range(r+1)]
        B = [[h[i+j]-h[i+j+1] for i in range(r+1)] for j in range(r+1)]
    else:
        A = [[h[i+j] for i in range(r+1)] for j in range(r+1)]
        B = [[h[i+j+1]-h[i+j+2] for i in range(r)] for j in range(r)]
    return fmpq_mat(A).det(),fmpq_mat(B).det()


def signed_dyadic(value):
    assert value
    a,b=abs(value.numerator),value.denominator
    e=int(a.bit_length()-b.bit_length())
    if a << max(-e,0) < b << max(e,0):
        e-=1
    return [int(value>0)-int(value<0),e]


def main():
    rows=[]
    for m in range(3,22):
        cap = min(10,(m-1)*(2*m-3))
        # For the four largest displayed rows, degree eight already suffices.
        if m>=17:
            cap=8
        h = moments(m,cap)
        if m in (3,4):
            assert independent_prefix(m,cap)==h
        signs=[]
        for k in range(1,cap+1):
            A,B=determinants(h,k)
            signs.append([signed_dyadic(A),signed_dyadic(B)])
            if A<0 or B<0:
                break
            assert min(A,B)>0
        assert A<0<B
        prefix=sha256()
        for value in h[:k+1]:
            for integer in (value.numerator,value.denominator):
                prefix.update((format(int(integer),'x')+'\n').encode())
        rows.append(dict(m=m,first_failure=k,localizing_determinants=signs,
                         normalized_prefix_signed_hex_sha256=prefix.hexdigest()))
        if m==4:
            square=h[2]-10*h[3]+25*h[4]
            assert square<0
            rows[-1]['L_of_x_squared_times_5x_minus_1_squared']=str(square)
    return dict(dyadic_format='For each degree k=1,...,first_failure: '
                '[[sign(det A),floor(log2(abs(det A)))], [sign(det B),floor(log2(abs(det B)))]].',
                independently_interpolated_original_cofactors=[3,4],rows=rows)

if __name__=='__main__':
    print(json.dumps(main(),indent=2))
