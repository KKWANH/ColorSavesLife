FROM osrf/ros:foxy-desktop
ENV DEBIAN_FRONTEND=noninteractive

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y git \
                       python3-pip \
                       gcc \
                       perl \
                       dkms \
                       make \
                       vim \
                       curl \
                       wget \
                       build-essential \
                       python3-colcon-common-extensions \
                       ros-foxy-joint-state-publisher-gui \
                       ros-foxy-gazebo-plugins \
                       ros-foxy-joint-state-publisher \
                       ros-foxy-gazebo-ros

RUN source /opt/ros/foxy/setup.bash
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

# Upgrade CMake version from 3.16 to 3.20                       
RUN wget https://github.com/Kitware/CMake/releases/download/v3.24.1/cmake-3.24.1-Linux-x86_64.sh -q -O /tmp/cmake-install.sh
RUN chmod u+x /tmp/cmake-install.sh
RUN sudo mkdir -p /opt/cmake-3.24.1 && \
    /tmp/cmake-install.sh --skip-license --prefix=/opt/cmake-3.24.1 && \
    rm /tmp/cmake-install.sh && \
    ln -s /opt/cmake-3.24.1/bin/* /usr/local/bin
 
RUN echo "All GOOD"
