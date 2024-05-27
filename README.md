## 💫 About Developer:

### Banish J

🤖 AI & ML Developer | Data Science & Analytics Expert<br>🌐 Web Apps & IoT Skilled | Awesome UI Creator<br>💻 AI is my main focus! 👾

## 📞 Contact
##### **☎️**   [9444333914](tel:9444333914)
##### **📧**  mail@banish.in
##### **🌐**  [Banish](https://www.banish.in)

## Core Concept

***This code captures video from the webcam, detects faces in real-time using the Haar Cascade Classifier, and draws rectangles around the detected faces. The video feed is displayed in a window, and the program can be terminated by pressing the 'Esc' key.***


### Importing Necessary Library

python



`import cv2` 

This imports the OpenCV library, which is widely used for computer vision tasks.

### Loading the Haar Cascade Classifier

python



`alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)` 

-   `alg`: Specifies the XML file that contains the Haar Cascade classifier data for detecting frontal faces.
-   `cv2.CascadeClassifier(alg)`: Loads the Haar Cascade classifier from the XML file into the `haar_cascade` object.

### Accessing the Webcam

python



`cam = cv2.VideoCapture(0)` 

-   `cv2.VideoCapture(0)`: Initializes the webcam for video capture. The argument `0` typically refers to the default webcam on the computer.

### Real-Time Face Detection Loop

python



`while True:
    _, img = cam.read()` 

-   `cam.read()`: Captures a frame from the webcam. The underscore `_` is used to ignore the first return value (a boolean indicating if the frame was read correctly), and `img` stores the captured frame.

### Converting the Image to Grayscale

python



 `grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` 

-   `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`: Converts the captured color image to grayscale. This is done because face detection using Haar Cascades works better on grayscale images.

### Detecting Faces

python



 `face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)` 

-   `haar_cascade.detectMultiScale(grayImg, 1.3, 4)`: Detects faces in the grayscale image. The method returns a list of rectangles where faces are detected.
    -   `grayImg`: The input grayscale image.
    -   `1.3`: The scale factor for the image pyramid (how much the image size is reduced at each image scale).
    -   `4`: The minimum number of neighbors each candidate rectangle should have to retain it.

### Drawing Rectangles Around Detected Faces

python



 `for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)` 

-   Iterates over the list of detected faces. For each face, a rectangle is drawn on the original image (`img`):
    -   `(x, y)`: The top-left corner of the rectangle.
    -   `(x+w, y+h)`: The bottom-right corner of the rectangle.
    -   `(0, 0, 255)`: The color of the rectangle (red in BGR format).
    -   `2`: The thickness of the rectangle's border.

### Displaying the Image with Detected Faces

python



 `cv2.imshow("Face Detection", img)` 

-   `cv2.imshow("Face Detection", img)`: Displays the image with detected faces in a window titled "Face Detection".

### Breaking the Loop

python



 `key = cv2.waitKey(10)
    if key == 27:
        break` 

-   `cv2.waitKey(10)`: Waits for 10 milliseconds for a key press.
-   `if key == 27`: Checks if the 'Esc' key (ASCII value 27) is pressed. If so, it breaks the loop and stops the program.

### Releasing Resources

python



`cam.release()
cv2.destroyAllWindows()` 

-   `cam.release()`: Releases the webcam resource.
-   `cv2.destroyAllWindows()`: Closes all OpenCV windows.
