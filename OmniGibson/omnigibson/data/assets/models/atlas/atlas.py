import pybullet as p
import pybullet_data
import time,math,os
p.connect(p.GUI)

planeName = os.path.join(pybullet_data.getDataPath(), "mjcf/ground_plane.xml")
ground_plane_mjcf = p.loadMJCF(planeName)

atlas = p.loadURDF("atlas/atlas_v4_with_multisense.urdf", [0,0,1])
for i in range (p.getNumJoints(atlas)):
	p.setJointMotorControl2(atlas,i,p.POSITION_CONTROL,0)
	print(p.getJointInfo(atlas,i)[2])

t=0
p.setRealTimeSimulation(1)
while (1):
	p.setGravity(0,0,-10)
	time.sleep(0.01)
	t+=0.01
	keys = p.getKeyboardEvents()
	for k in keys:
		if (keys[k]&p.KEY_WAS_TRIGGERED):
			if (k == ord('i')):
				x = 10.*math.sin(t)
				y = 10.*math.cos(t)


