cd libOpenDRIVE
"build/Release/test-xodr" junction.xodr
cd ..
blender --python import.py -- "output/lanes.obj" "output/roadmarkings.obj"