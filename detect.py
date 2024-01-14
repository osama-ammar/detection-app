import ultralytics
import cv2


class StoneDetectionModel:
    def __init__(self,model_path):
        self.model = ultralytics.YOLO(model=model_path)
        self.results = []
        
    def inference(self,image):
        self.results = self.model(image , conf=0.1)

    
    def show_results(self,image):
        target_image = image.copy()
        #.....................
        for result in self.results:
            bboxes = result.boxes
            
            for box in bboxes:
                #getting boxes shape in format xyxy ... option in ultralytics
                b=box.xyxy[0]
                
                #as open cv accept integer coordinates
                x1 , y1 = int(b[0]) , int(b[1])
                x2 , y2 = int(b[2]) , int(b[3])
                
                # drawing boxes on images
                cv2.rectangle(target_image , [x1,y1],[x2,y2],(255,0,0),2)
        
        return target_image 
    
    
if __name__=="__main__":
    model_path = "D:\Code_store\detection-app\yolov8n.pt"
    image_path="D:\\Code_store\\detection-app\\test_image.jpg"
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    
    model = StoneDetectionModel(model_path)
    output = model.inference(image=image)
    results_visualized = model.show_results(image)
    
    cv2.imshow("output",results_visualized)
    cv2.waitKey(0)