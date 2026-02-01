import cv2
import uuid 
import os
import time

def main():

    IMAGES_PATH = os.path.join('data', 'images') 
    labels = ['awake', 'drowsy']
    number_imgs = 5

    cap = cv2.VideoCapture(0)

    for label in labels:
        print('Capturing images for {}' .format(label))
        time.sleep(5)

        for img_num in range(number_imgs):
            print('Collecting images for {}, image number {}' .format(label, img_num))

            ret, frame = cap.read()

            img_name = os.path.join(IMAGES_PATH, label + '.' + str(uuid.uuid1()) + '.jpg')
            
            cv2.imwrite(img_name, frame)
            cv2.imshow('Image Collection', frame)

            time.sleep(2)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()