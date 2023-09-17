# Camera

<details>
<summary>1. sub_camera.py </summary>

<br>

ROS에서 사용되는 CvBridge 클래스를 이용하여 MORAI Simulator에서 Publish 하는 Topic을 Subscribe 하고 이를 OpenCV 형식으로 변환하여 화면에 창을 띄우는 역할

<br>

```python
rospy.init_node('camera', anonymous=True)
```
 - 노드를 초기화하고 노드의 이름을 'camera' 설정
 - anonymous=True 로 설정하면 노드 이름이 중복되더라도 중복을 피하기 위해 무작위로 변경

<br>

```python
self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
```
 - MORAI Simulator에서 Publish 하는 CompressedImage 이미지 메세지 유형의 Topic ("/image_jpeg/compressed") Subscribe
 - 새로운 메세지가 도착할 때마다 self.callback 호출

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
try:
    image_parser = IMGParser()
except rospy.ROSInterruptException:
        pass
```

 - try 블록 안에서 IMGParser 클래스의 인스턴스를 생성하여 이미치 처리 시작
 - ROS와 관련된 예외가 발생할 경우 해당 예외를 처리 (rospy.ROSInterruptExceptiondms ROS 노드가 중지될 때 발생하는 예외)
</details>

# GPS