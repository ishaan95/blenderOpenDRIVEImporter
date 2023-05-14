cd libOpenDRIVE
"build/Release/test-xodr" odrgen.xodr
cd ..
blender --python import.py -- "output/lanes.obj" "output/roadmarkings.obj"