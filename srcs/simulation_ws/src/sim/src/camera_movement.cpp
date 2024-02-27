// std headers
#include <memory>
#include <string>
#include <vector>

// ROS2 headers
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "control_msgs/action/follow_joint_trajectory.hpp"
#include "geometry_msgs/msg/point.hpp"


void common_goal_response(
  std::shared_future<rclcpp_action::ClientGoalHandle
  <control_msgs::action::FollowJointTrajectory>::SharedPtr> future) { }  // empty function

void common_result_response(
  const rclcpp_action::ClientGoalHandle
  <control_msgs::action::FollowJointTrajectory>::WrappedResult & result) { }  // empty function

void common_feedback(
  rclcpp_action::ClientGoalHandle<control_msgs::action::FollowJointTrajectory>::SharedPtr,
  const std::shared_ptr<const control_msgs::action::FollowJointTrajectory::Feedback> feedback) { }  // empty function


class EyeSub : public rclcpp::Node
{
public:
  EyeSub() : Node("eye_sub_node")
  {
    subscription_ = this->create_subscription<geometry_msgs::msg::Point>(
      "eye", 10, std::bind(&EyeSub::topic_callback, this, std::placeholders::_1));

    node = std::make_shared<rclcpp::Node>("camera_movement_node");

    action_client = rclcpp_action::create_client<control_msgs::action::FollowJointTrajectory>(
      node->get_node_base_interface(),
      node->get_node_graph_interface(),
      node->get_node_logging_interface(),
      node->get_node_waitables_interface(),
      "/joint_trajectory_controller/follow_joint_trajectory");

    bool response = action_client->wait_for_action_server(std::chrono::seconds(1));
    if(!response)
    {
      throw std::runtime_error("could not get action server");
    }

    opt.goal_response_callback = std::bind(common_goal_response, std::placeholders::_1);
    opt.result_callback = std::bind(common_result_response, std::placeholders::_1);
    opt.feedback_callback = std::bind(common_feedback, std::placeholders::_1, std::placeholders::_2);
  }

private:
  void topic_callback(const geometry_msgs::msg::Point::SharedPtr eye)
  {
    /* = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = */

    std::vector<trajectory_msgs::msg::JointTrajectoryPoint> points;
    trajectory_msgs::msg::JointTrajectoryPoint target_point;
    
    target_point.time_from_start = rclcpp::Duration::from_seconds(0.0);
    target_point.positions.resize(joint_names.size());
    target_point.positions[0] = (*eye).x;
    target_point.positions[1] = (*eye).y;
    target_point.positions[2] = (*eye).z;

    points.push_back(target_point);

    goal_msg.goal_time_tolerance = rclcpp::Duration::from_seconds(1.0);
    goal_msg.trajectory.joint_names = joint_names;
    goal_msg.trajectory.points = points;

    auto goal_handle_future = action_client->async_send_goal(goal_msg, opt);

    rclcpp::spin_until_future_complete(node, goal_handle_future);

    /* = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = */
  }

  rclcpp::Subscription<geometry_msgs::msg::Point>::SharedPtr subscription_;
  std::shared_ptr<rclcpp::Node> node;
  rclcpp_action::Client<control_msgs::action::FollowJointTrajectory>::SharedPtr action_client;
  rclcpp_action::Client<control_msgs::action::FollowJointTrajectory>::SendGoalOptions opt;
  control_msgs::action::FollowJointTrajectory_Goal goal_msg;

  std::vector<std::string> joint_names = {"x_joint", "y_joint", "z_joint"};
};


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<EyeSub>());
  rclcpp::shutdown();

  return 0;
}
