// Exact extension of the inherited packet dictionary; no prime-size cutoff.
// g++ -O2 -std=c++17 -fopenmp extend_packets.cpp -lgmpxx -lgmp -o extend_packets
#include <gmpxx.h>
#include <iostream>
#include <sstream>
#include <string>
#include <omp.h>

static mpz_class pow2(const mpz_class& e,const mpz_class& m) {
    mpz_class b=2,r;
    mpz_powm(r.get_mpz_t(),b.get_mpz_t(),e.get_mpz_t(),m.get_mpz_t());
    return r;
}
int main(int argc,char** argv) {
    if(argc!=6)return 2;
    const mpz_class A(argv[1]),S(argv[2]);
    const unsigned first=std::stoul(argv[3]),last=std::stoul(argv[4]);
    omp_set_num_threads(std::stoi(argv[5]));
    if(first<1 || last<first || A<2 || S<1)return 2;
    unsigned completed=0;
    const double start=omp_get_wtime();
    #pragma omp parallel for schedule(dynamic)
    for(unsigned q=first;q<=last;++q) {
        mpz_class C,G,E,Z,D;
        mpz_pow_ui(C.get_mpz_t(),A.get_mpz_t(),q); C-=1;
        Z=pow2(S*q,C)-1;
        mpz_gcd(G.get_mpz_t(),C.get_mpz_t(),Z.get_mpz_t()); E=G;
        for(unsigned d=1;d<q;++d) {
            if(q%d)continue;
            while(E>1) {
                Z=pow2(S*d,E)-1;
                mpz_gcd(D.get_mpz_t(),E.get_mpz_t(),Z.get_mpz_t());
                if(D==1)break;
                E/=D;
            }
        }
        std::ostringstream row;
        row<<q<<" "<<G<<" "<<E<<"\n";
        #pragma omp critical
        {
            std::cout<<row.str()<<std::flush;
            ++completed;
            if(completed%32==0 || completed==last-first+1)
                std::cerr<<"completed="<<completed<<" elapsed_seconds="
                         <<omp_get_wtime()-start<<"\n"<<std::flush;
        }
    }
}
