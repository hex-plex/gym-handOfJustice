# gym-handOfJustice
This is a OpenAI gym that has a robotic arm with 12 joints and which takes in a video feed to imitate those poses in feed.

# HandOFJustice
This is a robotic arm which takes in a an input of 12 joint angles to Replicate a given pose.
The environment has a few parameter to customize:
- feed parameter where in an instance of cv2.VideoCapture is passed
- mod parameter This is simply to run a env with pybullet in GUI or in Direct (which is for DIRECT of pybullet to be used),'human' to enable GUI with a setRealTimeSimulation(1)
- epsilon parameter is for measuring how similar two images are, This helps in compensating  the excess length, width or thickness of one's hand with respect to the robotic arm.
- preprocess parameter takes in a function that helps to threshold one's hand, this is one of the most important one as we are using traditional methods to process your hand for a reward function,And it might not suite all lighting conditions or hand types (Even with our trys to make it as robust as possible ).
for passing a function as preprocess which should threshold your hand and return a mask of your hand
- resolution parameter is for defining the resolution of the hand image itself or the resolution to which the hand image is resized to be used and outputed (remember to keep the aspect ratio of both same).
 


>pip install gym-handOFJustice
## Example
```python
import gym
import gym_handOfJustice
import cv2

env = gym.make('handOFJustice-v0',cap=cv2.VideoCapture(1), mod="GUI",epsilon=150,preprocess=None,resolution=(56,56,3))
```
for a in use example refer my Actor Critic based RL agent for this environment ["Actor-Critic Example"](https://github.com/hex-plex/Hand-Imitation/blob/master/Simulation/RL-Test.py)

## Action space
Action space is the set of 12 Joint angles with 
>low = [0,0,0,0,0,0,0,0,0,0,-0.52,-1.04]
>high = [1.55,1.55,1.55,1.55,1.55,1.55,1.55,1.55,1.55,1.55,0.52,1.04]
as to restrict the hand movement to a reasonable amount of freedom for the hand to move
the mapping of each input is as such
>[ palm-thumb,tip-thumb,palm-index,tip-index,palm-middle,tip-middle,palm-ring,tip-ring,palm-little,tip-little , wrist, elbow]
 joint angles for the arm

## Observation space
Observation space is the real hand image which would be processed to get the set of angle for the hand
it varies also based on the resolution parameter of the environment.
by default is (56,56,3).
This doesnt change till the episode is not ended.

## Reward function
For the environment reward is the negative of no of pixels that doesnt match up in the two thresholded images
hence we might need a epsilon to define the acceptable amount of error for a reward to interpret a state as a terminal state of an episode.

## Render
To take a look at the arm you can use env.render() which outputs the image of  the robotic arm
It also returns a rgb image of the robotic arm with the same resolution input as a parameter


# Required packages
- gym
- pybullet
- opencv

# Updates Required
- [ ] Setup a auto cropping mechanism for a image based on cascading algorithms
- [ ] Use a PID controller to go from a current pose to another as its what would be used in real world
- [ ] Make a Check for existance of an hand with help of preprocess