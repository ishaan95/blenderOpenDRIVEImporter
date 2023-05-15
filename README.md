# An OpenDRIVE static scenario file importer for Blender
Import OpenDRIVE roads into Blender as 3D meshes. This repository is based on the [libOpenDRIVE](https://github.com/grepthat/libOpenDRIVE). 

# Quick Start
Assuming that you are using a Windows machine and Blender is installed and you are able to run the `blender --python` command from your command prompt/terminal:
- Create a python environment with python 3.8 and where `pip install scenariogeneration` is done.
- Run `python odrgen.py`. This will generate the `junction.xodr` file in the libOpenDRIVE directory using the `scenariogeneration` python package.
- Run `genobj.bat`. This will run the opendrive parser library executable for a default `junction.xodr` file and run the Blender python command to import the generated .obj files into Blender. It will also generate the .fbx files in the project directory. 
Here are some outputs:
![Loopy road](assets/loopy.png)
![junction-3way](assets/junction-3way.png)

# Procedurally generated environments directly for CARLA simulator
Assuming you have Blender installed and you are able to run the `blender --python` command from your command prompt/terminal and have installed CARLA simulator from source on Windows.

- Open the `x64` command prompt.
- As written in the quick start before, run `python odrgen.py` and `genobj.bat`.  
- Run `make launch` to start the simulator. When the Unreal Editor opens, click the `play` button.
- Run `carlaimport.bat`
- Check if map is imported into CARLA. 

# Further work
- You can further generate .xodr files using python by referring to the [scenariogeneration](https://github.com/pyoscx/scenariogeneration) library or by modifying the `odrgen.py` script.
- You can further generate the 3D scene using the Blender python API by modifying the `import.py` script.
- You can also manually import the map into CARLA. I wrote a step-by-step guide to do so [here](https://github.com/johschmitz/blender-driving-scenario-creator/issues/23)
- Once you have imported the map into CARLA, you can develop the python scripting using the CARLA python API and run traffic in the scene or generate scenarios using CARLA scenario runner.

