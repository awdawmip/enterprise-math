"""R265 exact modular witness; formal toy BRC, not native heartbeat."""
from collections import defaultdict

P = 1000003
EDGES = (((2,-1,-1),(2,1,-1)), ((0,-1,-1),(0,1,-1)),
         ((1,1,1),(2,1,-1)))
DELTA = ((1,0),(2,0),(2,2))
state = {(0,0,1,0): 1}  # (q,r,eps,k) -> count modulo P
samples = []
for m in range(25):
    assert sum(state.values()) % P == pow(2,m,P)
    value = 0
    for (q,r,eps,k), count in state.items():
        if (q,r,eps) == (0,2,1):
            xk = pow(2,k,P) if k >= 0 else pow(pow(2,P-2,P),-k,P)
            value = (value + count*xk) % P
    samples.append(value)
    if m == 24: break
    nxt = defaultdict(int)
    for (q,r,eps,k), count in state.items():
        for a,(q2,eta,b) in enumerate(EDGES[q]):
            key = (q2,DELTA[r][a],eta*eps,eta*k+b)
            nxt[key] = (nxt[key]+count) % P
    state = nxt

h = [[samples[i+j] for j in range(13)] for i in range(13)]
det = 1
for i in range(13):
    pivot = next(j for j in range(i,13) if h[j][i] != 0)
    if pivot != i:
        h[i],h[pivot] = h[pivot],h[i]
        det = -det
    d = h[i][i]
    det = det*d % P
    inv = pow(d,P-2,P)
    for row in range(i+1,13):
        mult = h[row][i]*inv % P
        for col in range(i+1,13):
            h[row][col] = (h[row][col]-mult*h[i][col]) % P
        h[row][i] = 0
assert det == 206678
print({"prime":P,"det13_mod_p":det,"samples":samples,"status":"PASS"})
