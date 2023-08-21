# MORAI_PROJECT
MORAI Simulator 프로젝트 소스코드입니다

## Environment Setting
|OS|Version|
|:---:|:---:|
|Ubuntu|18.04|
|ROS|Melodic|

## Camera
코드에 대한 자세한 내용은 [여기](camera_gps/README.md)를 참고해 주시길 바랍니다

<details>
<summary>1. sub_camera.py </summary>

<p align="center"><img src="https://github.com/ehdxns/MORAI_PROJECT/assets/129836561/40868fa2-8f9e-40bd-8c5e-99b2df64a903" width="60%" height="60%" title="1. sub_camera.py"></p>


```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 1.sub_camera.py 
```

</details>

<details>
<summary>2. pub_camera.py </summary>

<p align="center"><img src="https://github.com/ehdxns/MORAI_PROJECT/assets/129836561/94d328ba-9a2d-4f3f-a533-5f5fae1117ae" width="60%" height="60%" title="2. pub_camera.py"></p>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 2.pub_camera.py 
```

</details>

<details>
<summary>3. bird_eye_view.py </summary>


```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 3.bird_eye_view.py 
```

</details>

<details>
<summary>4. white_line_detect.py </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 4.white_line_detect.py 
```

</details>

<details>
<summary>5. yellow_line_detect.py </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 5.yellow_line_detect.py 
```

</details>

<details>
<summary>6. blend_line.py </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 6.blend_line.py 
```

</details>

<details>
<summary>7. binary_line.py </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 7.binary_line.py 
```

</details>

<details>
<summary>8. sliding_window.py </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 8.sliding_window.py 
```

</details>

<details>
<summary>9. LAKS.py </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun scout_ros 9.LAKS.py 
```

</details>

## GPS
코드에 대한 자세한 내용은 [여기](camera_gps/README.md)를 참고해 주시길 바랍니다

<details>
<summary>path_maker.launch </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
roslaunch scout_ros path_maker.launch 
```

</details>

<details>
<summary>planner.launch </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
roslaunch scout_ros planner.launch
```

</details>

## SLAM
코드에 대한 자세한 내용은 [여기](slam_navigation/README.md)를 참고해 주시길 바랍니다

<details>
<summary>slam_gmapping_pr2.launch </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
roslaunch kw_tf tf_setting.launch
roslaunch pointcloud_to_laserscan sample_node.launch
roslaunch gmapping slam_gmapping_pr2.launch
```
```python
rosrun map_server map_saver
```

</details>

## Navigation
코드에 대한 자세한 내용은 [여기](slam_navigation/README.md)를 참고해 주시길 바랍니다

<details>
<summary> navigation.launch </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
roslaunch kw_tf tf_setting.launch
roslaunch pointcloud_to_laserscan sample_node.launch
roslaunch kw_tf navigation.launch
```

</details>

<details>
<summary> application.py </summary>

```python
roslaunch rosbridge_server rosbridge_websocket.launch
roslaunch kw_tf tf_setting.launch
roslaunch pointcloud_to_laserscan sample_node.launch
roslaunch kw_tf navigation.launch
```
```python
python application.py
```

</details>