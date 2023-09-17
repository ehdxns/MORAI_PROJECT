# Camera

<details>
<summary>1. sub_camera.py </summary>

<br>

ROS를 이용하여 CompressedImage 유형의 Topic을 Subscribe 하고, 받은 이미지를 OpenCV를 통해 화면에 표시하는 역할

<br>

```python
rospy.init_node('camera', anonymous=True)
self.bridge=CvBridge()
```
 - 노드를 초기화하고 노드의 이름을 'camera' 설정
 - anonymous=True 로 설정하면 노드 이름이 중복되더라도 중복을 피하기 위해 무작위로 변경
 - ROS 이미지 메세지와 OpenCV 이미지 간의 변환을 담당하는 CvBridge 클래스의 인스턴스 생성

<br>

```python
self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
rospy.spin()
```

 - MORAI Simulator에서 Publish 하는 CompressedImage 메세지 유형의 Topic ("/image_jpeg/compressed") Subscribe
 - 새로운 메세지가 도착할 때마다 self.callback 메서드 호출
 - 노드를 실행하고 노드가 종료되기 전까지 프로그램을 계속 실행하는 역할

<br>

```python
comp_img = self.bridge.compressed_imgmsg_to_cv2(data)
cv2.imshow("Image window", comp_img)
cv2.waitKey(1)
```

 - CvBridge를 이용하여 ROS의 CompressedImage 유형의 메세지를 OpenCV 이미지 유형으로 변환
 - OpenCV를 이용하여 "Image window" 라는 창에 'comp_img'표시
 - OpenCV 창을 업데이트하기 위한 대기 시간 설정 (1ms 동안 대기하면서 창 업데이트)

<br>

```python
if __name__ == '__main__':
    try:
        image_parser = IMGParser()
    except rospy.ROSInterruptException:
        pass
```
 
 - if __name__ == '__main__': 블록에서는 스크립트가 직접 실행될 때 다음 작업을 수행하게 하는 역할
 - try 블록 안에서 IMGParser 클래스의 인스턴스를 생성하여 이미치 처리 시작
 - ROS와 관련된 예외가 발생할 경우 해당 예외를 처리 (rospy.ROSInterruptExceptiondms ROS 노드가 중지될 때 발생하는 예외)


</details>

<details>
<summary>2. pub_camera.py </summary>

<br>

ROS를 이용하여 CompressedImage 유형의 Topic을 Subscribe 하고, 받은 이미지를 RGB 및 그레이스케일로 변환하여 두 가지 다른 이미지 Topic으로 Publish 하는 역할

<br>

```python
self.rgb_pub = rospy.Publisher('/camera_rgb_image', Image, queue_size=10)
self.gray_pub = rospy.Publisher('/camera_gray_img', Image, queue_size=10)
```

 - Image 메세지 유형의 '/camera_rgb_image' Topic을 Publish 하는 Publisher 객체 생성
 - Image 메세지 유형의 '/camera_gray_img' Topic을 Publish 하는 Publisher 객체 생성
  
<br>

```python
gray_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
```

 - 색상 공간 변환 함수(cv2.cvtcolor)로 이미지의 색상 공간을 변경
 - Blue, Green, Red 채널 이미지를 단일 채널 그레이스케일 이미지로 변경

<br>

```python
rgb_img_msg=self.bridge.cv2_to_imgmsg(img_bgr, 'bgr8')
gray_img_msg =self.bridge.cv2_to_imgmsg(gray_img)
```

 - OpenCV 이미지를 ROS 이미지 메세지로 변환
 - 'bgr8'은 이미지의 인코딩 형식
  
<br>

```python
self.rgb_pub.publish(rgb_img_msg)
self.gray_pub.publish(gray_img_msg)
```

 - RGB 이미지 메세지를 '/camera_rgb_image' Topic으로 Publish
 - 그레이스케일 이미지 메세지를 '/camera_gray_img' Topic으로 Publish
</details>

# GPS