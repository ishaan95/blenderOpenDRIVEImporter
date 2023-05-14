from scenariogeneration import xodr, prettyprint
import numpy as np
import os

# create a road
road = xodr.create_road([xodr.Line(1000)], 0, 2, 2)

## Create the OpenDrive class (Master class)
odr = xodr.OpenDrive("myroad")

## Finally add roads to Opendrive
odr.add_road(road)

# Adjust initial positions of the roads looking at succ-pred logic
odr.adjust_roads_and_lanes()

# After adjustment, repeating objects on side of the road can be added automatically
guardrail = xodr.Object(
    0, 0, height=0.3, zOffset=0.4, Type=xodr.ObjectType.barrier, name="guardRail"
)
road.add_object_roadside(guardrail, 0, 0, tOffset=0.8)

delineator = xodr.Object(
    0, 0, height=1, zOffset=0, Type=xodr.ObjectType.pole, name="delineator"
)
road.add_object_roadside(delineator, 50, sOffset=25, tOffset=0.85)

## Add some other objects at specific positions
# single emergency callbox
emergencyCallbox = xodr.Object(
    30, -6, Type=xodr.ObjectType.pole, name="emergencyCallBox"
)
road.add_object(emergencyCallbox)

# repeating jersey barrier
jerseyBarrier = xodr.Object(
    0, 0, height=0.75, zOffset=0, Type=xodr.ObjectType.barrier, name="jerseyBarrier"
)
jerseyBarrier.repeat(repeatLength=25, repeatDistance=0, sStart=240)
road.add_object(jerseyBarrier)

# Print the .xodr file
prettyprint(odr.get_element())

# write the OpenDRIVE file as xodr using current script name
odr.write_xml(os.path.basename(__file__).replace(".py", ".xodr"))