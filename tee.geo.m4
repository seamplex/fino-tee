SetFactory("OpenCASCADE");

l = 4*b;

Cylinder(1) = {0, 0, 0,  l, 0, 0, b};
Cylinder(2) = {0, 0, 0,  0, 0, l, d};
BooleanUnion(3) = {Volume{1};Delete;}{Volume{2};Delete;};
Box(4) = {-1.2*b, -1.2*b, -1.2*b, 1.2*b, 2.4*b, 1.2*(b+l)};
BooleanDifference(5) = {Volume{3};Delete;}{Volume{4};Delete;};

Cylinder(6) = {0, 0, 0,  l, 0, 0,  a};
Cylinder(7) = {0, 0, 0,   0, 0, l, c};
BooleanDifference(8) = {Volume{5};Delete;}{Volume{6,7};Delete;};

Box(9) = {-0.2*b, -1.2*b, -1.2*b, 0.2*b+1.2*l, 1.2*b, 1.2*(b+l)};
BooleanDifference(10) = {Volume{8};Delete;}{Volume{9};Delete;};


Physical Volume("pipe") = {10};
Physical Surface("axial") = {3, 8};
Physical Surface("right") = {5};
Physical Surface("half") = {6, 4};
Physical Surface("top") = {7};
Physical Surface("internal") = {9, 10};

Mesh.Algorithm = 6;
Mesh.ElementOrder = 2;
Mesh.Optimize = 1;
Mesh.HighOrderOptimize = 1;

Field[1] = Distance;
Field[1].FacesList = {3};

Field[2] = Threshold;
Field[2].IField = 1;
Field[2].LcMin = (b-a)/3;
Field[2].LcMax = (b-a);
Field[2].DistMin = 2*(c+b-a);
Field[2].DistMax = 0.5*l;

Background Field = 2;
