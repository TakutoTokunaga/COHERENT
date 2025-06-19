import pybullet as p
p.connect(p.GUI)
p.loadURDF('realdoor.urdf')

while True:
    p.stepSimulation()
