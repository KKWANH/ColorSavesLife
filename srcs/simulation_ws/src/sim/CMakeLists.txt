cmake_minimum_required(VERSION 3.5)
project(sim)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(control_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

install(DIRECTORY
  launch
  worlds
  description
  meshes
  config
  DESTINATION share/${PROJECT_NAME}/
)

add_executable(camera_movement src/camera_movement.cpp)
ament_target_dependencies(camera_movement rclcpp rclcpp_action control_msgs geometry_msgs)

install(TARGETS
  camera_movement
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()