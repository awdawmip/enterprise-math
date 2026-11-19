import math
from scipy.integrate import quad

def kernel2(A,z,d):
    R=(z+d)/2; S=(z-d)/2; P=R*S; h=1-A/P; q=math.sqrt(z*z-4*A)
    if h<=0:return 0
    H2=z-q-z/2*math.log(h)+d/2*math.log((q+d)/(q-d))-d/2*math.log(R/S)
    H5=-z*math.log(h)-S*math.log(R/S)-2*S+h*z
    return 4*(h-math.log(h))-h*(z+R-h*z/2)-H2-H5

def kernel3(A,z,d):
    P=(z*z-d*d)/4; h=1-A/P
    if h<=0:return 0
    return 4*h-3*h*z+h*h*z+(z/2-2)*math.log(1-2*h)

def calculate(a):
    A=2*a
    def f(z):
        q=math.sqrt(max(0,z*z-4*A)); D=min(2-z,q)
        return quad(lambda d: ((2-z)**2-d*d)/4*(3*kernel2(A,z,d)-2*kernel3(A,z,d)),0,D,epsabs=1e-10,limit=100)[0]
    value=quad(f,2*math.sqrt(A),1+A,epsabs=1e-9,limit=100)[0]+quad(f,1+A,2,epsabs=1e-9,limit=100)[0]
    correction=value/((math.pi**2/6)*A)
    return 1-161/(80*math.pi**2*a)+correction,correction

if __name__=='__main__':
 for a in [0.26,.3,1/3,.4,.49]:print(a,calculate(a))
