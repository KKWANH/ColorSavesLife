# 🎨 Color Saves Life!

<div width="100%"><img src="/imgs/logo.png" align="center" width="250"></div><br/>

## Index
- [🎨 Color Saves Life!](#-color-saves-life)
  - [Index](#index)
  - [🛠️ Features](#️-features)
  - [📁 Folder Structure](#-folder-structure)
  - [❓ How to Use](#-how-to-use)
  - [🏛️ Architecture - Ideal](#️-architecture---ideal)
  - [🏛️ Architecture - Prototype](#️-architecture---prototype)
  - [🤔 Future Development Plan](#-future-development-plan)
    - [🔈 SoundVisualizer for HearingDisability](#-soundvisualizer-for-hearingdisability)
      - [Architecture](#architecture)
      - [Example image](#example-image)
    - [🏫 Gamified Education Application](#-gamified-education-application)
  - [🫂 Team Member](#-team-member)

## 🛠️ Features

## 📁 Folder Structure
```shell
.
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
├── test_drive_data     # rosbag data of driving in gazebo to test the detection model
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
