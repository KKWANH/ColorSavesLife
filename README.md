<div width="100%" align="center"><h1>🎨 Color Saves Life!</h1></div>
<div width="100%" align="center"><img src="/imgs/logo.png" align="center" width="50%"></div>
<div width="100%" align="center"><hr width="50" align="center"></div>

# 🚢 Welcome abord, let me explain what it is

<div width="100%" align="center">
    <img width="49%" src="/imgs/friedrichstrasse-road.jpg">
    <img width="49%" src="/imgs/friedrichstrasse-road-grayscale.jpg">
</div>

> This example is for **achromatopsia**, which can see the world with only grayscale. There are lot more types of color-disability than chromatopsia.

**We all love Berlin.**
The picture above is a image of Friedrichstraße, which is close to Haupftbanhof(centeral station) of Berlin. You can see heavy traffic here, let's imagine a situation that you've become a color-blinded person. If the unexpected car, bicycle, comes in front of you, can you react and brake down your car at the exact right time? At this point, you can see color disability is critical for driving situation, which can hurt someone's life. Most of color disabled people cannot drive. Even getting drive license is not allowed in some countries.

Our **Color Saves Life** program comes at this point. Our goal is to attatch **transparent display** on front-window of vehicle*(Thanks to LG 😄)*, and simple sensors (normal camera in colorblind case). Boom! Now you can see AugmentedReality - Based - Driver Infortainment! In our program, we used Gazebo Simulator for prototype development. To adventure the our world of Gazebo Simulator, please [check here](#world-of-simulator). You can find full storyline about the simulator here.

Another important feature of our program, is **Easy-to-develop**. If you just add your detecting algorithm and drawing part(opencv) for each frame in `plugins` folder, it is very easy develop new features. You can even run multiple plugins at same time, with plugin_master's features. [Check here](#-future-development-plan) and find more interesting ideas for future development. 


## 📁 Folder Structure
```shell
./
 │
 ├── srcs/
 │   │   
 │   ├── ros2pkg/
 │   │   ├── image_subscriber/
 │   │   └── test_publisher/
 │   │
 │   └── srcs/
 │       │   # Simulation Part
 │       ├── simulation_ws/src/
 │       │   ├── sim/        # ros2 pkg for gazbeo simulation world and vehicle model
 │       │   ├── teleop/     # ros2 pkg for gazbeo vehicle teleoperation
 │       │   └── tracking/   # ros2 pkg for detecting the eye position
 │       │
 │       │   # Python Client
 │       ├── assets/     # test images, fonts
 │       ├── plugins/    # You can deploy your own plugin here
 │       │   ├── color_disability/
 │       │   │   ├── model/
 │       │   │   ├── color_disability.py
 │       │   │   └── traffic_object.py
 │       │   ├── plugin.py
 │       │   └── plugin_master.py
 │       ├── disability_assistant.py
 │       └── main.py
 │
 ├── test_drive_data.tar.xz   # rosbag data of driving in gazebo to test the detection model
 │
 ├── docker/
 ├── docker-compose.yaml
 │
 ├── LICENSE
 │
 ├── imgs/        # image files for documentation
 └── README.md    # your entrypoint!
```

## ❓ How to Use

1. Download the docker image and unzip
```shell
# Download Releases/ColorSavesLife/ColorSavesLife.tar.bz2
bunzip2 ColorSavesLife.tar.bz2
```
2. Turn on the docker environment
```shell
docker load --input ColorSavesLife.tar
```
3. Open 3 terminal 
```shell
# Fist Terminal
docker run -it --env DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix csl:0.1 /bin/bash

# Second Terminal
docker ps # Check docker container ID
docker exec -it <container_ID> /bin/bash

# Thrid Terminal
docker ps
docker exec -it <container_ID> /bin/bash
```
4. Abstract rosbag data
```shell
cd ~/ColorSavesLife
tar -xf test_drive_data.tar.xz
```

5. Run the application
```shell
# First Terminal
cd ~/ColorSavesLife/srcs
python3 main.py

# Second Terminal
cd ~/ColorSavesLife
ros2 bag play test_drive_data

# Third Terminal
rviz2 # Add Image_msg -> Set topic (/car/camera1/image_raw)
```

### World of Simulator


## DEMO!!


## 🏛️ Architecture - Ideal

<img src="/imgs/architecture-ideal.png" align="center">

## 🏛️ Architecture - Prototype

<img src="/imgs/architecture-prototype.png" align="center">

## 🤔 Future Development Plan
Color disability is not only disability that affects to normal life. In the report of WHO(World Health Organization), one of five people has problem of hearing [(who.int/health-topics/hearing-loss)](https://www.who.int/health-topics/hearing-loss#tab=tab_1). It is very important fact that 80% of them are living in low-income/mid-income countries, and hearing care interventions are cost-effective. If they can get help for their life with getting driving skills, this will effect a lot. With this solucation Solution, we can help them to drive much more safely and make their life much more easier and enjoyable for driving. As an example, we show you some of our future development plan for hearing disability and dementia. 

### 🔈 SoundVisualizer for HearingDisability
Sound sense is also so much important in driving situations and sirious problem. There are 450 million people who have hearing disability. Think about the emargency situation that ambulance is coming from your behind. If you have problem with hearing, this will cause worse circumstanses like car accident or a person who needs help cannot be alive. But with SoundVisualizer plugin , that visualize any sound around your car and which direction does it comes from on front driver window. This will help you to react to the situation and make a right decision.

### AI Driving Assistant for Dementia
Dmentia is also a serious problem for driving. There are 55 million people who have dementia. Even their disablity is not effecting to their driving skills, they are not allowed to drive in some countries. Because they tend to pay less attention to the road and they are not able to make a right decision. With our AI Driving Assistant plugin for Dementia, that learn the driver's driving pattern and other driving data, that can show some warning message or make a sound when the driver is not paying attention to the road or detecting some unusual driving pattern.

### User Status with Germification
XXX


So our platform is not only for color disability, bu also for other disability. That have so much potential to help peeople who have disability and make their life much more easier and enjoyable for driving.

#### Architecture

#### Example image

### 🏫 Gamified Education Application

## 🫂 Team Member
- Kwanho Kim: [@KKWANH](https://github.com/KKWANH)
- Hokyung Park: [@Ho-mmd](https://github.com/ho-mmd)
- Sujong Ha: [@lalywr2000](https://github.com/lalywr2000)
- Shuta Ogura: [@Shuta-Syd](https://github.com/Shuta-Syd)
- Oscar Lopez
