# Independent review of the abstract four-Selmer structure method corollary

Disposition: PAPER_PASS, no must-fix, for the exact conditional formula Sel4 = (Z/4)^(nu-rho-k) plus (Z/2)^(rho+k), with the full genuine Cassels rank and actual rational torsion Kummer-image dimension as inputs. This is a derived method corollary in the same descent family, not another independent discovery, registered Tool, executed four-descent, explicit four-cover or new arithmetic rank result. Its verdict is separate from the fixed core (9,8) report.

Reviewer EM-DVR-BFF6DC, own SID MCP-47562f9f432d4978a7bea0dd60ecc4aa and DA-144D0C4639CACEEE75DC. Actual author EM-DVR-F73673, /root/public129_line_reviewer. The new target P11_ABSTRACT_FOUR_SELMER_STRUCTURE_METHOD_HARVEST.md has 7834 bytes, SHA256 a25de043186da056fa2c0119ec894c430541afa3ff053d5d90438b4024d9e302, Git blob 12342a18550424dec7cb0b5743812cc1ca71275f. The 1082-byte freeze has SHA256 33e5adc56c5fa2cb5852ebf4bac618f87dc9681720b5ab1c44e0cf216cf2d90d. Both were fully read and copied exactly with their byte/SHA/blob checks. The input is a frozen local candidate; no actual author Source is invented at this report's freeze.

This is genuine nonauthor, directed NONBLIND review. Root assigned two successor scopes while the separate LC-D report was finishing; I started these only after that report was frozen. Root and the frozen inputs disclosed the proposed formula and important boundaries. Earlier separate paper reviews and shared context are disclosed, not rebranded as blindness. The author supplied only frozen objects and exact primary/accepted-input locators. No construction, repair, new curve input, preliminary proof or verdict was provided to the author before freeze. A new ID is not used to hide my prior review context.

No scientific program, symbolic or numerical consumer, point/prime search, parameter enumeration or new literature search was run. Paper exact-sequence and group arguments were checked directly. Managed full Source reads, primary PDF text extraction, custody hashes and local report persistence are administrative only. The fixed-(233,119) code/input/codec/plan, resource stop and exhausted budget remain untouched. No RA, claim, Task, Native vote, Working Truth or Foundation action occurs.

## 1. The theorem input is correctly stronger than a zero matrix

The declared scope is a classical elliptic curve E/Q with full rational two-torsion, its full W=Sel2 of finite dimension nu, its genuine pulled-back Cassels--Tate pairing of full rank rho, and K0=delta2(E[2](Q)) of actual dimension k. This is a sufficient, well-typed input class. A rank measured on an unproved vertical restriction, or the tenth paper's compatibility form K/M, is explicitly excluded as a value of rho.

I personally read the actual Shukla--Stoll2302.01640v1 PDF pages 1--2 for this new use, by extracting them anew from the retained 316100-byte PDF SHA256 f84fee9a3cd3e2e37aee1c0b41f08296e88988a5f1142c5911b4d16762e408ce, blob eb7b3ab6da007e366ca4a262f25d197391a235f7. The complete extracted pages are saved in this review directory. Page 1 defines the all-place n-Selmer group and exact Kummer sequence (1.1). Page 2 states im(s_n)=the left/right CTP kernel on Sel(n), where s_n is induced by E[n^2]->E[n]. It separately presents finiteness of all Sha as a conjecture and does not make that conjecture a premise of this kernel/image statement. The present import at n=2 has exactly the scope required here.

I accept that stated standard theorem as the declared classical input, rather than asserting it follows from bilinearity or independently proving general duality. I do not claim newly reading all of Poonen--Stoll [PS99]. FSS0710.2079v1 Theorem 5.2 was also reread directly: it identifies the Cassels formula with the CT pairings on the indicated full Selmer groups over a number field. The retained P11 root/model comparison gives the same full pulled-back CTP when the formula is later specialized. There is no import of an unexamined isogeny pairing or a new compatibility pairing as CT.

Because the elliptic CTP is alternating, rho is even and R=rad(W) has dimension nu-rho. Rational point Kummer classes have zero image in Sha and therefore lie in R. In particular K0 is contained in R. The proof uses that inclusion explicitly; it does not merely subtract an arbitrary k from a radical dimension.

## 2. The restricted Selmer kernel is proved with all local conditions

For 0->E[2] --i--> E[4] --[2]--> E[2]->0, the rational connecting map sends a two-torsion point to the cocycle of a half of it, exactly delta2 restricted to E[2](Q). Thus ker(i:H1(E[2])->H1(E[4]))=K0. The same holds over each completion using that completion's actual two-torsion. This kernel can be nonzero; treating i as injective would give the wrong result.

Both Kummer identities are correct: i delta2(P)=delta4(2P) and pi delta4(P)=delta2(P), globally and locally. They imply i(W) lies in Sel4 and pi(Sel4) lies in W. For a four-Selmer class c in the global kernel of pi, global cohomological exactness gives c=i(a). At every completion c_v=delta4(P_v); applying pi gives delta2(P_v)=0, hence P_v=2Q_v. The difference a_v-delta2(Q_v) lies in ker(i_v)=delta2(E[2](Q_v)), contained in the local two-Kummer image. Thus a is locally two-Kummer at every place and belongs to W. Conversely pi i=0, so ker(pi|Sel4)=i(W).

This all-place check prevents the kernel from being an image of a larger unrestricted or merely unramified cohomology group. No good-prime cutoff or unproved rational representative of a general Selmer class is used. Together with the imported im(pi)=R it gives exactly

    0 -> W/K0 -> Sel4 -> R -> 0.

The kernel has order 2^(nu-k) and the image has order 2^(nu-rho), so |Sel4|=2^(2nu-rho-k). This already proves finiteness at the stated input scope; no finiteness premise for all Sha is needed.

## 3. Doubling and the abstract invariant factors are correct

On E[4], i composed after pi is the actual multiplication-two endomorphism. Hence 2Sel4=i(pi(Sel4))=i(R). The kernel of i restricted to R is still K0 because K0 is contained in R. Therefore |2Sel4|=2^(nu-rho-k), not generally 2^(nu-k). This is the step that needs the full radical dimension as well as the full kernel count.

The exponent nu-rho-k is nonnegative by K0 subset R. Sel4 is killed by four since its containing H1(E[4]) is killed by four. A finite abelian group killed by four has a unique type (Z/4)^a plus (Z/2)^b; its doubled subgroup has size 2^a. Thus a=nu-rho-k, and its total order forces b=rho+k. Both invariant-factor counts are nonnegative and the proposed order formula agrees. No explicit splitting, generator selection or covering equations have been assumed.

The formula follows independently of the numerical core (9,8). Substitution of separately proved nu=4,rho=0,k=2 agrees with the other report, but that agreement is a check, not the generic proof. Nor does the generic formula discover those inputs for any new curve.

## 4. The actual k input and reuse of the accepted primitive boundary

The value k is the image dimension, not merely dim E[2](Q). From the connecting map, delta2(T)=0 for T in E[2](Q) precisely when T is twice a rational point. A nonzero such T gives a rational point of order four, and any rational point of order four gives such a nonzero kernel. Thus no rational four-torsion makes delta2 injective on E[2](Q), giving k=2 for the stated split primitive family. If rational halves exist on a general split curve, k can be smaller and the unspecialized formula is the one that applies.

I personally freshly fetched all three exact accepted-input files from immutable Source3fca728daf92abc5a4cad36102f5ec58c82aba0f using the managed connector; full responses and exact decoded bytes are retained here:

- The original RETURN.md at research_artifacts/mcp/RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC/MCP-b4bf84ccfffc4affacc0f551cb1fa0ad/e486dcbc06d80c035317/RETURN.md, 13858 bytes, SHA256 c4bc0846af97b5f15eca90af7122ec44c2227a9a3152360cf3aa864cb2a3ed24, blob 342ac673f570976d4f0ea86b5d5e069b474f0450.
- The original Driver review at driver_reviews/mcp/MCP-1e926295d6f7404d94ea3a90dda4fbfa/80b8a97d25d6342c8a3e/P11_DRIVER_REVIEW.md, 9924 bytes, SHA256 3c82b3ca977eb3abf3870c5f9114aa5350e6c7d2b7c6e080be94c32a1f58586a, blob 701156fe86d4300007abe5591d474ddc890208e0.
- The terminal ACCEPTED record research_result_reviews/RR-C1F5BD75CF29E3970097/DR-2F805343ED6728A5CD35.json, 1989 bytes, SHA256 dde89d4c5f57ce27ce4663e17ea61fd7adc8cc3d706c38ed1866c0159b820e0e, blob 3ec2fdc2ad88696d8c2eac26d219cec65cfa0cd8.

I read the original retained family definitions and Section 3 no-four-torsion claim, the Driver's mathematical items 2--3 and the full review/record context. The accepted boundary applies to the same primitive Euclidean cores and same ordered split curve: negative differences preclude halving two torsion points, and the retained 4AB/Fermat obstruction precludes the third. I reuse that accepted conclusion at its exact scope, without restarting its Fermat proof, repeating its scientific program, accepting unrelated claims anew or reopening its terminal Task. The record is historical input custody, not current write authority or a new review by me.

Accordingly k=2 is a justified specialization here, giving (Z/4)^(nu-rho-2) plus (Z/2)^(rho+2). At core (9,8), the independent actual squareclasses U_(-1),U_17 in the sixth theorem also directly establish k=2. Odd torsion alternatives left open by the old return do not alter this two-torsion image argument.

## 5. Composition boundaries are mathematically necessary and correctly retained

The method harvest does not rely on the ninth or tenth paper as a premise of its group-theoretic proof. Its discussion of composing with them is conditional. A complete local compatibility calculation can supply nu; it does not supply rho. A vertical Cassels restriction supplies the full rho only after full Selmer coverage is proved, or after all missing pairings are separately determined. A nonzero nonvertical quotient plus only a restricted matrix leaves the exact rho and hence this exact Sel4 structure UNKNOWN. The paper correctly preserves this boundary.

A restricted nonzero Cassels form can still prove its separately justified rational-rank bound, but substituting its lower rank into an equality for the full rho would overstate the structure. Likewise the rank of the tenth compatibility M/K cannot be substituted at all. The present conditional theorem is sound because it demands actual full nu,rho,k rather than hiding these obligations in a formula.

The output is abstract Sel4 structure only. It gives no four-cover representatives, local lift certificates, rational points, actual new Mordell--Weil rank, saturation, generators, odd Sha, all Sha finiteness or uniform all-core classification. A later consumer must independently establish every curve-specific input. There is no automatic API enabling, shared Tool registration, Native acceptance or original fixed-task resource renewal.

No must-fix was found. This is a valid same-mechanism theorem corollary and a useful exact gate on downstream claims; it should not be counted as another independent discovery. Its method classification remains RESULT_ONLY. All objects retain external classical arithmetic types under Heartbeat X6; no native plane, spatial-axis reinterpretation or physical-time claim occurs. The actual fixed-(233,119) RR is still absent and all mathematical parents remain OPEN.

Driver-ID: EM-DVR-BFF6DC / CONTROL_PLANE
