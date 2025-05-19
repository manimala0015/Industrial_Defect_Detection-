import cv2
import NumPy as np 

 # Load and resize the image for consistency 
image = cv2.imread('defect.jpg')
image = cv2.resize(image, (600, 400))  
# Resize if needed 
# Convert to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

 # Apply Gaussian Blur to reduce noise 
blurred = cv2.GaussianBlur(gray, (5, 5), 0) 
# Threshold to detect darker (damaged) areas _,
thresh = cv2.threshold(blurred, 40, 255, cv2.THRESH_BINARY_INV) 

 # Find contours 
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

# Draw only valid defect areas for contour in contours: 
area = cv2.contourArea(contour)   
if 150 < area < 3000: 
# Ignore too small or too large regions      
x, y, w, h = cv2.boundingRect(contour)      
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)     
cv2.putText(image, "Defect", (x, y - 5), 
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1) 
# Show result
cv2.imshow("Detected Defects", image)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

