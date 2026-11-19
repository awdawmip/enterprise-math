// Exact integer discovery/independent cross-check engine, using GMP.
// Build: g++ -O2 -std=c++17 period_packets.cpp -lgmpxx -lgmp -o period_packets
// Args: decimal step m, maximum relative period B, optional starting period.
#include <gmpxx.h>
#include <iostream>
#include <vector>
#include <cstdlib>

static std::vector<unsigned long> prime_divisors(unsigned long n) {
    std::vector<unsigned long> ps;
    for (unsigned long p=2; p<=n/p; ++p) {
        if (n%p) continue;
        ps.push_back(p);
        while (n%p==0) n/=p;
    }
    if(n>1) ps.push_back(n);
    return ps;
}

static mpz_class gcd(const mpz_class& a, const mpz_class& b) {
    mpz_class d;
    mpz_gcd(d.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());
    return d;
}

static mpz_class two_power_mod(const mpz_class& exponent,const mpz_class& modulus) {
    mpz_class x, two=2;
    mpz_powm(x.get_mpz_t(),two.get_mpz_t(),exponent.get_mpz_t(),modulus.get_mpz_t());
    return x;
}

int main(int argc, char** argv) {
    if(argc != 3 && argc != 4) return 2;
    const mpz_class m(argv[1]);
    const unsigned long B=std::stoul(argv[2]);
    const mpz_class a("690786768637635218740714348513373826260012289");
    const mpz_class A=a*a*(mpz_class(1)<<66);
    const unsigned long first=argc==4?std::stoul(argv[3]):1;
    if(first<1 || first>B) return 2;
    mpz_class power;
    mpz_pow_ui(power.get_mpz_t(), A.get_mpz_t(), first-1);
    for(unsigned long q=first;q<=B;++q) {
        power*=A;
        mpz_class C=power-1, G=gcd(C,two_power_mod(m*q,C)-1), H=G;
        for(auto r:prime_divisors(q)) {
            while(H>1) {
                mpz_class d=gcd(H,two_power_mod(m*(q/r),H)-1);
                if(d==1) break;
                H/=d;
            }
        }
        std::cout<<q<<" "<<G<<" "<<H<<"\n";
    }
}
