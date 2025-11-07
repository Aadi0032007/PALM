#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from azure.storage.blob import BlobServiceClient
import cv2
import uuid
import io

class CameraUploaderNode(Node):
    def __init__(self):
        super().__init__('camera_uploader')

        # Parameters
        self.declare_parameter('azure_connection_string', 'YOUR_AZURE_CONN_STRING')
        self.declare_parameter('container_name', 'robot-images')
        self.declare_parameter('upload_interval', 5.0)  # seconds

        self.connection_string = self.get_parameter('azure_connection_string').value
        self.container_name = self.get_parameter('container_name').value
        self.upload_interval = self.get_parameter('upload_interval').value

        # Azure setup
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        self.container_client = self.blob_service_client.get_container_client(self.container_name)

        # Create container if not exists
        try:
            self.container_client.create_container()
            self.get_logger().info(f"Created container '{self.container_name}'")
        except Exception:
            self.get_logger().info(f"Container '{self.container_name}' already exists")

        # ROS setup
        self.bridge = CvBridge()
        self.last_upload_time = self.get_clock().now()
        self.subscription = self.create_subscription(
            Image, '/camera/image_raw', self.listener_callback, 10
        )

    def listener_callback(self, msg):
        now = self.get_clock().now()
        if (now - self.last_upload_time).nanoseconds / 1e9 < self.upload_interval:
            return  # limit upload frequency

        self.last_upload_time = now

        try:
            # Convert ROS Image to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Encode image as JPEG
            success, buffer = cv2.imencode('.jpg', cv_image)
            if not success:
                self.get_logger().error("Failed to encode image.")
                return

            # Upload to Azure
            image_bytes = io.BytesIO(buffer)
            blob_name = f"{uuid.uuid4()}.jpg"
            self.container_client.upload_blob(
                name=blob_name,
                data=image_bytes,
                overwrite=True
            )
            self.get_logger().info(f"Uploaded image {blob_name} to Azure Blob Storage")

        except Exception as e:
            self.get_logger().error(f"Upload failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = CameraUploaderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down CameraUploaderNode.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
