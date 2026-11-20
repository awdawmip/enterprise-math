// Independent exact recomputation: take A as an argument, recompute A^q by
// mpz_pow_ui, and saturate against ALL proper divisors (not only q/r).
// Build: g++ -O2 -std=c++17 period_packets_verify.cpp -lgmpxx -lgmp -o period_packets_verify
// Args: A, stride S, maximum q.
#include <gmpxx.h>
#include <iostream>
#include <string>

static mpz_class power_mod(const mpz_class& n, const mpz_class& modulus) {
    mpz_class b = 2, out;
    mpz_powm(out.get_mpz_t(), b.get_mpz_t(), n.get_mpz_t(), modulus.get_mpz_t());
    return out;
}

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    const mpz_class A(argv[1]), S(argv[2]);
    const unsigned long bound = std::stoul(argv[3]);
    if (A < 2 || S < 1 || bound < 1) return 2;
    for (unsigned long q = 1; q <= bound; ++q) {
        mpz_class C, residue, G, H, divisor;
        mpz_pow_ui(C.get_mpz_t(), A.get_mpz_t(), q);
        C -= 1;
        residue = power_mod(S*q, C)-1;
        mpz_gcd(G.get_mpz_t(), C.get_mpz_t(), residue.get_mpz_t());
        H = G;
        for (unsigned long d = 1; d < q; ++d) {
            if (q % d) continue;
            while (H > 1) {
                residue = power_mod(S*d, H)-1;
                mpz_gcd(divisor.get_mpz_t(), H.get_mpz_t(), residue.get_mpz_t());
                if (divisor == 1) break;
                H /= divisor;
            }
        }
        std::cout << q << ' ' << G << ' ' << H << '\n';
        if (q % 64 == 0) std::cerr << "exact packets verified through " << q << std::endl;
    }
}
