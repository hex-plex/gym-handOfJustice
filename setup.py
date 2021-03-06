import setuptools

setuptools.setup(
    name='gym_handOfJustice',
    version='0.0.11',
    description='A openAI Gym Env for a Robotic arm that imitates an arm which would be given through a feed',
    packages=setuptools.find_packages(include="gym_handOfJustice*"),
    intall_required = ['gym','pybullet','opencv-python'],
    package_data={'':['meshes/*.stl','hand.urdf']}
    
    )
