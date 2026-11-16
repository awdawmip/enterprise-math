# Eleven labels under a single-axis reflection

An 11-label partition fixed by the reflection (x,y,z) ↦ (−x,y,z) costs at least **11,328 native reads**. This bound applies to any affine conjugate. The central inversion in the known 11,292-read sixfold witness fixes only one history. This reflection fixes the 25 histories of the plane x=0.

The 125 histories comprise 25 fixed points and 50 interchanged pairs. A fixed message class is a union of point orbits. The verifier generates every such one-read class by adding point orbits in increasing order and rejecting the first forbidden triple. A moving pair of labels has classes C and gC, which are disjoint. Such C has no fixed points and uses at most one point of any reflected pair. Translations parallel to the x=0 plane and signed common dilations commuting with g are transitive on the 100 points outside that plane. Thus the full inventory of sizes and best costs for moving classes follows from an unrestricted forbidden-triple enumeration with point (1,0,0) in C. Its maximum size is 11.

A dynamic program adds costs for fixed and moving classes, keeping the total number of histories and the number in the fixed plane. With budget 11,327 it leaves only five or seven fixed labels. In the five-fixed case every fixed class has exactly five points in the plane and has size 9, 11 or 13. Nine integer size profiles remain. Each has at least two fixed size-13 classes. The 50 admissible fixed 13-point classes form one orbit under the 800-element centralizer. The search anchors one such class and enumerates the others in nondecreasing index within each size. Every completion with the pinned class is considered up to conjugacy: transitivity allows the representative with least index to be pinned. Pair unions with the same point support use their cheapest representative. After five fixed labels have been selected, two possible mirror-pair supports fix the required support of the last pair, which is looked up directly.

In the seven-fixed case each fixed class contains eight points away from the plane; the four moving classes all have size 11. The search first enumerates the two size-11 pair supports up to centralizer action and then covers their complement by seven fixed classes. At each step it branches on an uncovered history contained in the fewest remaining candidates. A dynamic lower bound on the residual cost uses the number of points remaining in the plane.

Each compressed pair support, class cost and rejected triple is regenerated from the preceding round's native observations. The verifier compares the profile restrictions derived by its dynamic program with the filters actually used and checks completion of every listed search.

```sh
python3 -B replay.py --older /path/to/round2/delivery
```
