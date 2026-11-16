#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <iostream>
#include <string>
#include <stdexcept>

using Integer = mpz_class;
using Vector = std::array<Integer,4>;
using Basis = std::array<Vector,3>;
using Triangle = std::array<std::array<Integer,3>,3>;

static Integer dot(const Vector& x, const Vector& y) {
    Integer g = 0;
    for (int j=0;j<4;++j) g += x[j]*y[j];
    return g;
}
static Integer quotient(const Integer& a, const Integer& b) {
    if (a%b != 0) throw std::logic_error("Gram division not exact");
    Integer q;
    mpz_divexact(q.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());
    return q;
}

static void gram(const Basis& b, std::array<Integer,4>& d, Triangle& l) {
    d[0] = 1;
    for (int i=0;i<3;++i) {
        for (int j=0;j<=i;++j) {
            Integer x=dot(b[i],b[j]);
            for (int p=0;p<j;++p) x=quotient(d[p+1]*x-l[i][p]*l[j][p],d[p]);
            if (j<i) l[i][j]=x;
            else d[i+1]=x;
        }
    }
}
static Integer near_integer(const Integer& a, const Integer& b) {
    Integer q, n=2*a+b, d=2*b;
    mpz_fdiv_q(q.get_mpz_t(),n.get_mpz_t(),d.get_mpz_t());
    return q;
}

static unsigned long reduce_basis(Basis& b) {
    std::array<Integer,4> d;
    Triangle l;
    gram(b,d,l);
    int k=1;
    unsigned long swaps=0;
    while (k<3) {
        for (int j=k-1;j>=0;--j) {
            Integer q=near_integer(l[k][j],d[j+1]);
            if (q==0) continue;
            for (int h=0;h<4;++h) b[k][h]-=q*b[j][h];
            for (int h=0;h<j;++h) l[k][h]-=q*l[j][h];
            l[k][j]-=q*d[j+1];
        }
        Integer u=l[k][k-1], gain=d[k-1]*d[k+1]+u*u;
        if (4*gain>=3*d[k]*d[k]) {
            ++k;
            continue;
        }
        std::swap(b[k-1],b[k]);
        for (int j=0;j<k-1;++j) std::swap(l[k-1][j],l[k][j]);
        for (int i=k+1;i<3;++i) {
            Integer a=l[i][k-1], bb=l[i][k];
            l[i][k-1]=quotient(d[k-1]*bb+u*a,d[k]);
            l[i][k]=quotient(d[k+1]*a-u*bb,d[k]);
        }
        d[k]=quotient(gain,d[k]);
        k=std::max(k-1,1);
        ++swaps;
    }
    // A fresh exact certificate of size reduction and Lovasz at delta=3/4.
    gram(b,d,l);
    for (int i=1;i<3;++i) {
        for (int j=0;j<i;++j)
            if (2*abs(l[i][j])>d[j+1]) throw std::logic_error("size condition");
        if (4*(d[i-1]*d[i+1]+l[i][i-1]*l[i][i-1])<3*d[i]*d[i])
            throw std::logic_error("Lovasz condition");
    }
    return swaps;
}

int main() {
    Integer a,b,m,n;
    std::array<std::string,4> input;
    if (!(std::cin >> input[0] >> input[1] >> input[2] >> input[3])) return 1;
    if (mpz_set_str(a.get_mpz_t(),input[0].c_str(),16) ||
        mpz_set_str(b.get_mpz_t(),input[1].c_str(),16) ||
        mpz_set_str(m.get_mpz_t(),input[2].c_str(),16) ||
        mpz_set_str(n.get_mpz_t(),input[3].c_str(),16)) return 1;
    if (a<1 || b<1 || m<1 || n<1) return 1;
    if (gcd(a,b)!=1 || gcd(m,n)!=1) return 2;
    // The kernel equation is n*(b X0+a X1)=m*(b X2+a X3).
    // Every solution has b X0+a X1=m t, b X2+a X3=n t for one integer t.
    Integer inv;
    if (!mpz_invert(inv.get_mpz_t(),b.get_mpz_t(),a.get_mpz_t())) return 3;
    Integer x=(m*inv)%a, y=(n*inv)%a;
    Basis base{{Vector{a,-b,0,0},Vector{0,0,a,-b},Vector{x,(m-b*x)/a,y,(n-b*y)/a}}};
    unsigned long swaps=reduce_basis(base);
    for (auto& row:base) {
        if (n*(b*row[0]+a*row[1]) != m*(b*row[2]+a*row[3])) return 4;
    }
    for (auto& v:base[0]) std::cout<<v.get_str(16)<<' ';
    std::cout<<'\n'<<swaps<<'\n';
}
