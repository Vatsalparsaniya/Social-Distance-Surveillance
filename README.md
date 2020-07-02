## Looking for Social Distance Monitoring by CCTV integrated with AI?


* Maintaining social distancing is a very crucial issue in a COVID-19 outbreak scenario.This is an effective way to control the spread of the virus. However it is very difficult to maintain and monitor the social distancing norms in many cases such as in public places, offices and workplaces , where working in a close proximity is a requirement

* COVID-19 has impacted society in a drastic way. Due to this invisible enemy, it is required to keep a social distance between humans. But as human beings are social animals, it has been really difficult to maintain the required social distance in different areas. And due to this factor, logarithmic increase in the number of cases has been really huge.

---
## Video Output (YouTube)

|Video-1|Video-2|Video-3|
|--|--|--|
|[![check out my youtube video](https://img.youtube.com/vi/C10GOaOQHuM/0.jpg)](https://www.youtube.com/watch?v=C10GOaOQHuM)|[![check out my youtube video](https://img.youtube.com/vi/qouqqGm7gEc/0.jpg)](https://www.youtube.com/watch?v=qouqqGm7gEc)|[![check out my youtube video](https://img.youtube.com/vi/B8rJQ-cuoOc/0.jpg)](https://www.youtube.com/watch?v=B8rJQ-cuoOc)|

---

## The Solution

### Model selection: 
  * People detection (Model to detect humans ex: Yolo(You only look once))
  * Load and start the model
  * Pass a video frame through the model to detect objects
  * Filter out weak predictions and non-relevant objects (other than humans)
  
### Birds-eye view transformation

  * Select the coordinates of the points located at the bottom centre of the detected person box
  * Perspective transform on selected point for top view with the help of a computer vision library
  
### Social distancing measurement

  * With the help of transformed points calculate euclidean distance and map with image pixels to the real distance between 2 people.
  * If they are not maintaining social distancing then mark their respective boxes using Red colour
  
### Results and Improvements

  * Using a faster model in order to perform real-time social distancing analysis.
  * Automatic calibration problems could improve a lot the birds-eye view transformation on different scenes.
---

## Birds eye View Transformation

|original Image|Transformed Image|Birds eye View|
|--|--|--|
|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/set_prespective_points_200.png?token=AIDJHSD6IQA64ODPE7JLKJC7A465E)|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/transform_top_view_200.png?token=AIDJHSA7HTDIZUEMDTBFSXC7A466M)|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/birds_eye_view_image_200.png?token=AIDJHSC2QVIS3RHOZHGUOP27A5AY4)|
|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/pedestrianWalking_set_prespective_points_400.png?token=AIDJHSHGP5EHQX3PNIZUQPK7A47Q4)|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/pedestrianWalking_transform_top_view_400.png?token=AIDJHSB7AY4DVGMK3OXCHKK7A47Q2)|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/pedestrianWalking_birds_eye_view_image_400.png?token=AIDJHSAX6UA3S6XLMJMPQRK7A5BBA)|

## Output dashboard

|Input Image|Output Image|
|--|--|
|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/data/TownCentre_frame_200.jpg?token=AIDJHSA6HNPXPL7RN3O2DYK7A5H6I)|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/final_output_200.png?token=AIDJHSGJXHSSWLFVBDTGSKS7A5IMC)|
|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/data/pedestrianWalking_frame_400.jpg?token=AIDJHSBIBEQG45QRGYNR5LC7A5IDC)|![](https://raw.githubusercontent.com/Vatsalparsaniya/Social-Distance-Surveillance/master/result/final_output_pedestrianWalking_400.png?token=AIDJHSFBDT3RH43VUORXVHC7A5ILI)|

## Contributors

* [Vatsal Parsaniya](https://github.com/Vatsalparsaniya)
* [Meet Ranoliya](https://github.com/memr5)
* [Tanmeet Butani](https://github.com/tanmeet1)
* [Darshit Vachhani](https://github.com/darshitvachhani)
* [Bhautik Donga](https://github.com/BhautikDonga)
