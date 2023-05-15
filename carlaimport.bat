cd ../carla
del /f /s /q Import 1>nul
make import
cd ../carla/PythonAPI/util
python config.py --map junction