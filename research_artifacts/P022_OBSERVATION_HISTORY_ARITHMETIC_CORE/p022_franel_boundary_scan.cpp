#include <bits/stdc++.h>
using namespace std;

static long long franel_mod(int r, long long p) {
    vector<long long> inv(r + 1);
    inv[1] = 1;
    for (int k = 2; k <= r; ++k)
        inv[k] = (p - (p / k) * inv[p % k] % p) % p;
    long long c = 1, sum = 1;
    for (int k = 0; k < r; ++k) {
        c = c * (r - k) % p * inv[k + 1] % p;
        long long cube = c * c % p * c % p;
        sum += cube;
        if (sum >= p) sum -= p;
    }
    return sum % p;
}

int main(int argc, char** argv) {
    int R = 1000000;
    if (argc > 1) R = stoi(argv[1]);
    const int N = 3 * R + 10;
    vector<bool> is_prime(N, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; 1LL * i * i < N; ++i)
        if (is_prime[i])
            for (long long j = 1LL * i * i; j < N; j += i)
                is_prime[(size_t)j] = false;

    long long c17 = 0, c35 = 0, zeros = 0;
    cout << "r\tq\tq_mod_72\tfranel_mod_q\n";
    for (int r = 6; r <= R; r += 6) {
        long long q = 3LL * r - 1;
        int cls = (int)(q % 72);
        if (cls != 17 && cls != 35) continue;
        if (!is_prime[2 * r - 1] || !is_prime[2 * r + 1] || !is_prime[q]) continue;
        long long residue = franel_mod(r, q);
        cout << r << '\t' << q << '\t' << cls << '\t' << residue << '\n';
        if (cls == 17) ++c17; else ++c35;
        if (residue == 0) ++zeros;
    }
    cerr << "max_r=" << R << " candidates=" << (c17 + c35)
         << " class17=" << c17 << " class35=" << c35
         << " zero_residues=" << zeros << "\n";
    return zeros == 0 ? 0 : 2;
}
