// g++ -std=c++17 -O3 odd_ports_audit.cpp -o /tmp/odd_ports_audit
// Independent old-coordinate congruence search for the unexcluded 19-bit corner.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

using I = std::int64_t;
constexpr I N = I(1) << 32;
constexpr I hi = (I(1) << 19) - 1;

I inverse(I x, I mod) {
    I r = x, s = mod, c = 1, d = 0;
    while (s) {
        I q = r/s;
        I t = r-q*s; r=s; s=t;
        t=c-q*d; c=d; d=t;
    }
    if (r != 1) throw std::logic_error("nonunit");
    return (c % mod + mod) % mod;
}

// Try old coordinate difference Delta >= 0; the larger old coordinate
// must equal u+Delta. Signed increments d and e describe the two flips.
bool old_coordinates(I a, I b, I delta, I d, I e) {
    I t = std::abs(d), v = std::abs(e), u = 0;
    auto fit_bit = [&u](I bit, I shift, bool expect_one) {
        if (bit && (bool((u+shift) & bit) != expect_one)) u += bit;
    };
    if (t < v) {
        fit_bit(t,delta,d<0); fit_bit(v,0,e<0);
    } else {
        fit_bit(v,0,e<0); fit_bit(t,delta,d<0);
    }
    I x = u+delta;
    if (x >= N || u >= N) return false;
    I y = x ^ t, z = u ^ v;
    if (y != x+d || z != u+e || x%a != u%a || y%b != z%b || (x==u && y==z))
        throw std::logic_error("invalid decoded witness");
    return true;
}

// d,e have rescaled residues D,E modulo b, after multiplication by inv(a).
bool try_increments(I a, I b, I d, I e, I D, I E) {
    I k = E-D;
    if (k < 0) k += b;
    if (k > b/2) k -= b;
    I gap = std::abs(k)*a;
    if (gap >= N) return false;
    return k >= 0 ? old_coordinates(a,b,gap,d,e) : old_coordinates(a,b,gap,e,d);
}

int first_hit(I a, I b) {
    std::array<I, 32> residue;
    residue[0] = inverse(a,b);
    for (int j=1; j<32; ++j) residue[j] = (2*residue[j-1])%b;
    for (int j=0; j<32; ++j) {
        I d = I(1)<<j;
        if (try_increments(a,b,d,0,residue[j],0) ||
            try_increments(a,b,-d,0,b-residue[j],0)) return j;
        for (int i=0; i<j; ++i) {
            I e = I(1)<<i;
            for (int s : {1,-1}) {
                for (int h : {1,-1}) {
                    if (try_increments(a,b,s*d,h*e,
                            s>0?residue[j]:b-residue[j],h>0?residue[i]:b-residue[i]))
                        return j;
                }
            }
        }
    }
    throw std::logic_error("no witness");
}

void audit_corner(int top_bit) {
    // For 0..top_bit, W_0 = (2*top_bit+3)N - 2*(2^(top_bit+1)-1).
    const I product_bound = (2*top_bit+3)*N - 2*((I(1) << (top_bit+1))-1);
    std::array<I,32> hist{};
    I total=0, tested=0, last_a=0, last_b=0;
    int peak=-1;
    // Traverse by *larger* modulus; formula uses floor to take strict complement.
    for (I b=262145; b<=hi; b+=2) {
        const I below=(product_bound-1)/b;
        I lo=std::max<I>(262145,below+1);
        if (lo%2==0) ++lo;
        for (I a=lo; a<=b; a+=2) {
            ++total;
            if (std::gcd(a,b) != 1) continue;
            ++tested;
            int j=first_hit(a,b);
            ++hist[j];
            if (j>peak) {peak=j; last_a=a; last_b=b;}
        }
    }
    std::cout << "{\n  \"allowed_high_bit\": " << top_bit
              << ",\n  \"product_bound\": " << product_bound
              << ",\n  \"unordered_corner\": " << total
              << ",\n  \"coprime_unordered_decoded\": " << tested
              << ",\n  \"first_hit_peak_bit\": " << peak
              << ",\n  \"example_at_peak\": [" << last_a << ", " << last_b
              << "],\n  \"first_hit_counts_bit_0_up\": [";
    for (int i=0; i<=peak; ++i) std::cout << (i ? ", " : "") << hist[i];
    std::cout << "],\n  \"noncoprime_min_margin_gW1_minus_hi_squared\": ";
    I min_margin = hi*hi;
    for (int g=3; g<=63; g+=2) {
        I w=0;
        for (int i=0; i<=top_bit; ++i) {
            I t=I(1)<<i;
            if ((t-1)%g==0) w+=N-t;
            if ((t+1)%g==0) w+=N-t;
        }
        min_margin=std::min(min_margin,g*w-hi*hi);
    }
    if (min_margin<=0 || peak>top_bit) throw std::logic_error("incomplete cover");
    std::cout << min_margin << "\n}";
}

int main() {
    std::cout << "{\n\"original_and_extended_corner\": [";
    audit_corner(31);
    std::cout << ",\n";
    audit_corner(30);
    const I a=520031, b=520783;
    const I inv=inverse(a,b);
    std::vector<I> increments{0};
    for (int i=0; i<=21; ++i) {
        increments.push_back(I(1)<<i);
        increments.push_back(-(I(1)<<i));
    }
    I min_k=b, comparisons=0;
    for (std::size_t i=0; i<increments.size(); ++i) {
        for (std::size_t j=0; j<i; ++j) {
            I k=std::abs((increments[i]-increments[j])*inv)%b;
            min_k=std::min(min_k,std::min(k,b-k));
            ++comparisons;
        }
    }
    if (min_k*a < N || a*b<N) throw std::logic_error("prefix 0..21 not certified");
    const I g=61, u=8591*g, v=8593*g;
    std::array<bool,61> classes{};
    classes[0]=true;
    for (int i=0;i<=29;++i) {
        I t=(I(1)<<i)%g;
        if (classes[t] || classes[g-t] || t==g-t) throw std::logic_error("CRT class reused");
        classes[t]=classes[g-t]=true;
    }
    if (v>hi || std::gcd(u,v)!=g || std::lcm(u,v)<N) throw std::logic_error("bad upper pair");
    std::cout << "],\n\"sharp_original_corner_bit_22_lower_example\": {"
              << "\"a\": " << a << ", \"b\": " << b
              << ", \"distinct_increment_pairs_through_bit_21\": " << comparisons
              << ", \"minimum_abs_k\": " << min_k
              << ", \"maximum_allowed_abs_k\": " << (N-1)/a
              << "},\n\"sharp_global_bit_30_lower_example\": {\"a\": " << u
              << ", \"b\": " << v << ", \"gcd\": " << g << ", \"lcm\": " << std::lcm(u,v)
              << ", \"residue_classes_through_bit_29\": "
              << std::count(classes.begin(),classes.end(),true) << "}\n}\n";
}
