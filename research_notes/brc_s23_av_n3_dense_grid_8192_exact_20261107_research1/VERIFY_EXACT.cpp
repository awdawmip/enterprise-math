// Exhaustive exact-integer grid certificate for a 3-observation S23 AV kernel.
// See PROOF.md for the analytic all-real extension.
#include <iostream>
#include <string>
#include <algorithm>
#include <array>
#include <cstdlib>
#include <chrono>
#include <boost/multiprecision/cpp_int.hpp>
using i128 = __int128_t;
using std::array;
constexpr int M=1000000;
constexpr int K[8][27]={ {0,0,0,0,0,0,0,0,0,0,0,0,0,1000000,0,0,0,0,0,0,0,0,0,0,0,0,0},
 {0,479665,0,0,0,0,0,0,0,0,0,0,520335,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
 {0,0,0,0,0,0,0,0,0,296273,703727,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
 {0,0,419643,0,0,0,0,0,0,0,0,0,0,0,0,48185,0,0,405725,0,0,112202,0,0,0,0,14245},
 {0,139862,0,0,683322,0,0,0,0,176816,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
 {0,0,0,0,0,0,230562,0,0,106277,0,120245,56752,0,50073,71369,50073,25415,0,120245,0,0,50462,25415,70684,22428,0},
 {0,20822,0,400945,11265,119554,192951,125268,65023,0,0,0,0,0,0,0,0,0,0,0,64172,0,0,0,0,0,0},
 {747749,99382,0,52308,2315,0,2609,0,0,87375,3741,0,0,0,0,0,0,0,4521,0,0,0,0,0,0,0,0}};
std::string to_string128(i128 v) {
 if(v==0) return "0";
 bool neg=v<0;
 if(neg) v=-v;
 std::string r; while(v){r.push_back('0'+int(v%10));v/=10;}
 if(neg) r.push_back('-');
 std::reverse(r.begin(),r.end());
 return r;
}
i128 powi(i128 x,int n){i128 r=1;for(int i=0;i<n;i++)r*=x;return r;}
int main(int argc, char**argv){
 if(argc!=2) {std::cerr << "Usage: ./verify_exact <grid_N>\n";return 2;}
 int N=std::atoi(argv[1]); if (N<1||N>8192) return 3;
 for(int y=0;y<8;y++){int sum=0;for(int x=0;x<27;x++){if(K[y][x]<0)return 4;sum+=K[y][x];}if(sum!=M)return 5;}
 array<array<int,4>,27> G{};
 array<array<int,3>,27> CX{};
 for(int x=0;x<27;x++){int a=x/9,b=x/3%3,c=x%3; CX[x][a]++;CX[x][b]++;CX[x][c]++;}
 for(int y=0;y<8;y++){int h=3-((y/4)%2+(y/2)%2+y%2);for(int x=0;x<27;x++)G[x][h]+=K[y][x];}
 i128 D=8LL*N, DD=D*D;
 i128 den=2*i128(M)*powi(D,6);
 i128 max_num=-1;int max_i=-1,max_j=-1;
 auto start=std::chrono::steady_clock::now();
 for(int i=0;i<=N;i++) {
  i128 A=4LL*N+3LL*i;
  i128 p0=A*D;
  for(int j=0;j<=N;j++){
   i128 C=4LL*N+3LL*j;
   i128 p1=(D-A)*C;
   i128 p2=(D-A)*(D-C);
   if(p0+p1+p2!=DD) return 6;
   i128 PP[3][4]={{1,p0,p0*p0,p0*p0*p0},{1,p1,p1*p1,p1*p1*p1},{1,p2,p2*p2,p2*p2*p2}};
   i128 w=DD-p1;
   i128 yes[4]={w*w*w,p1*w*w,p1*p1*w,p1*p1*p1};
   i128 total=0;
   for(int x=0;x<27;x++) {
    i128 truth=PP[0][CX[x][0]]*PP[1][CX[x][1]]*PP[2][CX[x][2]];
    i128 reconstruct=0;
    for(int h=0;h<4;h++) reconstruct+=i128(G[x][h])*yes[h];
    i128 diff=i128(M)*truth-reconstruct;
    total+=(diff>=0?diff:-diff);
   }
   if(total>max_num){max_num=total;max_i=i;max_j=j;}
  }
 }
 std::chrono::duration<double> elapsed=std::chrono::steady_clock::now()-start;
 // Exact all-real bound = max_num/den + 27/(16*N).
 // For a requested rational threshold Tnum/Tden, multiply all by positive common denominator.
 boost::multiprecision::cpp_int big_num(to_string128(max_num)), big_den(to_string128(den));
 auto check=[&](int Tnum,int Tden){return (16LL*N*big_num + 27*big_den)*Tden < Tnum*(16LL*N)*big_den;};
 std::cout << "PASS_S23_N3_EXACT_GRID_CERTIFICATE\n";
 std::cout << "N=" << N << " grid_points=" << (long long)(N+1)*(N+1) << " ordered_outputs=" << (long long)(N+1)*(N+1)*27 << "\n";
 std::cout << "max_num=" << to_string128(max_num) << "\n";
 std::cout << "den=" << to_string128(den) << "\n";
 std::cout << "max_i=" << max_i << " max_j=" << max_j << "\n";
 std::cout << "extension=27/" << (16LL*N) << "\n";
 std::cout << "bound_lt_1/4=" << check(1,4) << "\n";
 std::cout << "bound_lt_6/25=" << check(6,25) << "\n";
 std::cout << "bound_lt_239/1000=" << check(239,1000) << "\n";
 std::cout << "bound_lt_477/2000=" << check(477,2000) << "\n";
 std::cout << "bound_lt_2381/10000=" << check(2381,10000) << "\n";
 std::cout << "bound_lt_4761/20000=" << check(4761,20000) << "\n";
 std::cout << "elapsed_seconds=" << elapsed.count() << "\n";
 return 0;
}
