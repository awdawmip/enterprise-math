// A necessary joint-observation condition, in the finite history coordinates.
// Size-10, cost-744/768 classes have zero first moments and cross moment ±e_i.
// Size-11, cost-936 classes have Q - mu*mu^T in the same six-element set.
// All arithmetic in this helper is exact modulo 5; it never establishes a cover.
M mixed_reachable[7]{};
bool mixed_enabled = true;
long long mixed_rejected = 0;
long long mixed_tested = 0;
int mod5(int x) { x %= 5; return x < 0 ? x + 5 : x; }
int code3(int a, int b, int c) { return 25 * mod5(a) + 5 * mod5(b) + mod5(c); }
void init_mixed_moments() {
    mixed_reachable[0] = 1;
    for (int n = 1; n <= 6; ++n) {
        for (int q = 0; q < 125; ++q) if ((mixed_reachable[n-1] >> q) & 1) {
            const int a=q/25, b=q/5%5, c=q%5;
            for (int d : {-1,1}) {
                mixed_reachable[n] |= M(1) << code3(a+d,b,c);
                mixed_reachable[n] |= M(1) << code3(a,b+d,c);
                mixed_reachable[n] |= M(1) << code3(a,b,c+d);
            }
        }
    }
}
bool mixed_moments_possible(M free, const vector<int>& cnt) {
    if (!mixed_enabled) return true;
    int ten=0, eleven=0;
    for (int j=0; j<cnt.size(); ++j) if (cnt[j]) {
        const auto& type = types[actual_ids[j]];
        if (type.sz==10 && (type.price==744 || type.price==768)) ten += cnt[j];
        else if (type.sz==11 && type.price==936) eleven += cnt[j];
        else return true;
    }
    if (eleven>1 || ten+eleven>=6) return true;
    ++mixed_tested;
    int sx=0,sy=0,sz=0,xy=0,xz=0,yz=0;
    for (M todo=free; todo; todo&=todo-1) {
        const int p=pos(todo), x=p/25, y=p/5%5, z=p%5;
        sx+=x; sy+=y; sz+=z; xy+=x*y; xz+=x*z; yz+=y*z;
    }
    if (eleven) { xy-=sx*sy; xz-=sx*sz; yz-=sy*sz; }
    const int target=code3(xy,xz,yz);
    const bool answer = (eleven || (sx%5==0 && sy%5==0 && sz%5==0))
                        && ((mixed_reachable[ten+eleven] >> target)&1);
    if (!answer) {
        ++mixed_rejected;
        if (mixed_rejected<=3) {
            cerr << "MIXED_REJECT " << uint64_t(free) << ' ' << uint64_t(free>>64)
                 << ' ' << ten << ' ' << eleven << ' ' << target << '\n';
        }
    }
    return answer;
}
