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

1. Clone the repository
```shell
git clone
```

2. Turn on the docker environment
```shell
docker run
```

3. Get in to docker container, turn on the python script

### World of Simulator


## 🏛️ Architecture - Ideal

<img src="/imgs/architecture-ideal.png" align="center">

## 🏛️ Architecture - Prototype

<img src="/imgs/architecture-prototype.png" align="center">

## 🤔 Future Development Plan

Color disability is not only disability that affects to normal life. In the report of WHO(World Health Organization), one of five people has problem of hearing [(who.int/health-topics/hearing-loss)](https://www.who.int/health-topics/hearing-loss#tab=tab_1). It is very important fact tht 80% of them are living in low-income/mid-income countries, and hearing care interventions are cost-effective. If they can get help for their life with getting driving skills, this will effect a lot. In this purpose, we suggest two more plugins which can deploy on our system.

### 🔈 SoundVisualizer for HearingDisability

Sounds are also important signal in driving situations. Think about the situation that a policeman ask your car to stop. But if you have problem with hearing, this will cause more bad circumstanses. If we visualize which kind of sound is it and which directions does it comes from. In this plugin, we use -- AI model to analyze sound. Attaching microphone in your car and change your front-display's plugin into SoundVisualizer, **BOOM! Now you see the sound.**

#### Architecture

#### Example image

### 🏫 Gamified Education Application

## 🫂 Team Member
- Kwanho Kim: [@KKWANH](https://github.com/KKWANH)
- Hokyung Park: [@Ho-mmd](https://github.com/ho-mmd)
- Sujong Ha: [@lalywr2000](https://github.com/lalywr2000)
- Shuta Ogura: [@Shuta-Syd](https://github.com/Shuta-Syd)
- Oscar Lopez
