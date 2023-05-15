cd libOpenDRIVE
"build/Release/test-xodr" junction.xodr
copy "junction.xodr" "../../carla/Import/"
cd ..
blender --python import.py -- "output/lanes.obj" "output/roadmarkings.obj" "junction.fbx"
copy "junction.fbx" "../carla/Import/"