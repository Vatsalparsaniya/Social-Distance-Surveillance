import cv2
import numpy as np
from math import sqrt

img = []
ix,iy = 0,0

def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),2,(255,0,0),-1)
        ix,iy = x,y

def get_points(image,numOfPoints, image_size=(800,800)):
    global img
    img = image.copy()
    img = cv2.resize(img,image_size)
    width, height = image.shape[:2]
    cv2.namedWindow("image")
    cv2.setMouseCallback("image",draw_circle)
    points = []
    print("Press a for add point : ")
    while len(points) != numOfPoints:
        cv2.imshow("image",img)
        k = cv2.waitKey(1)
        if k == ord('a'):
            points.append([int(ix),int(iy)])
            cv2.circle(img,(ix,iy),3,(0,0,255),-1)
    cv2.destroyAllWindows()
    return np.float32(points)

def create_model(config, weights):

    model = cv2.dnn.readNetFromDarknet(config, weights)
    backend = cv2.dnn.DNN_BACKEND_OPENCV
    target = cv2.dnn.DNN_TARGET_CPU
    model.setPreferableBackend(backend)
    model.setPreferableTarget(target)
    return model

def get_output_layers(model):

    layer_names = model.getLayerNames()
    output_layers = [layer_names[i[0]-1] for i in model.getUnconnectedOutLayers()]
    return output_layers

def blob_from_image(image, target_size):

    blob = cv2.dnn.blobFromImage(image, 1/255., target_size, [0,0,0], 1, crop=False)  
    return blob

def predict(blob, model, output_layers):

    model.setInput(blob)
    outputs = model.forward(output_layers)
    return outputs

def get_image_boxes(outputs, image_width, image_height, classes, confidence_threshold=0.5, nms_threshold=0.4):
    class_ids = []
    confidences = []
    boxes = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            class_name = classes[class_id]
            confidence = scores[class_id]
            if confidence > confidence_threshold and class_name== 'person':
                cx, cy, width, height = (detection[0:4] * np.array([image_width, image_height, image_width, image_height])).astype("int")
                x = int(cx - width / 2)
                y = int(cy - height / 2)
                boxes.append([x, y, int(width), int(height),cx,cy])
                confidences.append(float(confidence))
    nms_indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
    
    return [boxes[ind] for ind in nms_indices.flatten()]


def compute_point_perspective_transformation(matrix,boxes):
    list_downoids = [[box[4], box[5]+box[3]//2] for box in boxes]
    list_points_to_detect = np.float32(list_downoids).reshape(-1, 1, 2)
    transformed_points = cv2.perspectiveTransform(list_points_to_detect, matrix)
    transformed_points_list = list()
    for i in range(0,transformed_points.shape[0]):
        transformed_points_list.append([transformed_points[i][0][0],transformed_points[i][0][1]])
    return np.array(transformed_points_list).astype('int')

def get_red_green_boxes(distance_allowed,birds_eye_points,boxes):
    red_boxes = []
    green_boxes = []

    new_boxes = [tuple(box) + tuple(result) for box, result in zip(boxes, birds_eye_points)]
    for i in range(0, len(new_boxes)-1):
            for j in range(i+1, len(new_boxes)):
                cxi,cyi = new_boxes[i][6:]
                cxj,cyj = new_boxes[j][6:]
                distance = eucledian_distance([cxi,cyi], [cxj,cyj])
                if distance < distance_allowed:
                    red_boxes.append(new_boxes[i])
                    red_boxes.append(new_boxes[j])

    green_boxes = list(set(new_boxes) - set(red_boxes))
    red_boxes = list(set(red_boxes))

    return (green_boxes, red_boxes)

def eucledian_distance(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def get_birds_eye_view_image(green_box, red_box,eye_view_height,eye_view_width):
    blank_image = cv2.imread('templates/black_background.png')
    
    cv2.putText(blank_image, str(len(red_box)), (120,100), cv2.FONT_HERSHEY_SIMPLEX , 2, (0,0,255), 4, cv2.LINE_AA) 
    cv2.putText(blank_image, str(len(green_box)), (520,100), cv2.FONT_HERSHEY_SIMPLEX , 2, (0,255,0), 4, cv2.LINE_AA)
    
    for point in green_box:
        cv2.circle(blank_image,tuple([point[6],point[7]]),20,(0,255,0),-1)
    for point in red_box:
        cv2.circle(blank_image,tuple([point[6],point[7]]),20,(0,0,255),-1)
    blank_image = cv2.resize(blank_image,(eye_view_width,eye_view_height))
    return blank_image

def get_red_green_box_image(new_box_image,green_box,red_box):
    for point in green_box:
        cv2.rectangle(new_box_image,(point[0],point[1]),(point[0]+point[2],point[1]+point[3]),(0, 255, 0), 2)
    for point in red_box:
        cv2.rectangle(new_box_image,(point[0],point[1]),(point[0]+point[2],point[1]+point[3]),(0, 0, 255), 2)
    return new_box_image