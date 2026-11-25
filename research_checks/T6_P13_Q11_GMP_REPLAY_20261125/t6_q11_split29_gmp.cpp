#include <gmpxx.h>
#include <array>
#include <vector>
#include <iostream>
#include <fstream>
#include <cstdint>
using namespace std;
constexpr int N=12; constexpr long B=4826809,CAP=2331;
using Vec=array<long,N>;
mpz_class L[N],T[N],Q,M[N][N],step[N],bound;
Vec C[12][13],z,c,acc{};
struct Pos {vector<pair<int,int>> atoms; Vec v{}; long mass=0;};
vector<Pos> positives; vector<int> p,r; int pi; long radius;
uint64_t raw=0,over=0,common=0,nodes=0,leaves=0;
void descend(int i,const mpz_class &spent){
 if(i<0){++leaves;cout<<"W "<<pi;for(int a:r)cout<<' '<<a;for(long a:z)cout<<' '<<a;cout<<'\n';return;}
 ++nodes;mpz_class h=L[i]*c[i];for(int j=i+1;j<N;j++)if(z[j]>=0)mpz_addmul_ui(h.get_mpz_t(),M[i][j].get_mpz_t(),z[j]);else mpz_submul_ui(h.get_mpz_t(),M[i][j].get_mpz_t(),-z[j]);
 mpz_class near,minus=-h;mpz_fdiv_q(near.get_mpz_t(),minus.get_mpz_t(),step[i].get_mpz_t());if(!near.fits_slong_p()) throw 1;long ni=near.get_si();if(ni < -10000 || ni > 10000) throw 2;
 for(long n=ni;n<=ni+1;n++){mpz_class x=h+step[i]*n;mpz_class e=spent+T[i]*x*x;if(e<=bound){z[i]=c[i]+B*n;descend(i-1,e);}}z[i]=c[i];
}
void roster(int i,int sum){
 if(i==(int)p.size()){
  long cn=1521+13*sum-p.size();
  for(pi=0;pi<(int)positives.size();pi++){const auto &a=positives[pi];++raw;bool co=false;for(auto [q,s]:a.atoms)for(int j=0;j<(int)p.size();j++)co|=(p[j]==q&&r[j]==s);common+=co;if(cn>CAP||a.mass>CAP){++over;continue;}
   radius=(CAP-a.mass)*(CAP-a.mass)+(CAP-cn)*(CAP-cn);bound=Q*radius;
   for(int j=0;j<N;j++){long x=(acc[j]-a.v[j])%B;c[j]=x<0?x+B:x;z[j]=c[j];}descend(N-1,mpz_class(0));
  }return;
 }
 int lo=i>0&&p[i]==p[i-1]?r[i-1]:1;
 for(int a=lo;a<=12;a++){r[i]=a;for(int j=0;j<N;j++)acc[j]+=C[p[i]][a][j];roster(i+1,sum+a);for(int j=0;j<N;j++)acc[j]-=C[p[i]][a][j];}
}
void add(vector<pair<int,int>> a){Pos x;x.atoms=a;for(auto [q,s]:a){x.mass+=169*q+13*s-1;for(int j=0;j<N;j++)x.v[j]+=C[q][s][j];}positives.push_back(x);}
int main(int argc,char**argv){if(argc<4)return 2;ifstream f(argv[1]);f>>Q;for(int i=0;i<N;i++){f>>L[i]>>T[i];step[i]=B*L[i];for(int j=i+1;j<N;j++)f>>M[i][j];}for(int q=1;q<12;q++)for(int a=1;a<=12;a++)for(int j=0;j<N;j++)f>>C[q][a][j];if(!f)return 2;int kind=stoi(argv[2]);if(kind==0){for(int a=1;a<=12;a++)add({{2,a}});}else if(kind==1){for(int a=1;a<=12;a++)for(int b=a;b<=12;b++)add({{1,a},{1,b}});}else return 3;int sum=0;for(int i=3;i<argc;i++){p.push_back(stoi(argv[i]));sum+=p.back();}if(sum!=9)return 4;r.resize(p.size());roster(0,0);cout<<"R "<<raw<<' '<<over<<' '<<common<<' '<<nodes<<' '<<leaves<<'\n';}
