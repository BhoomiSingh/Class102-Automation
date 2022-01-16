import cv2
import dropbox
import time
import random
start_time= time.time()
def take_snapshot():
    number= random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result= True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name= 'img'+ str(number)+'.png'
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print('takensnapshot')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token='sl.A_sPpfDXsUQc144b0mniJ72XnUAbckDA4xsQ2Yly3jo17rgVmHEHUaCo-7_Em-QJGhi-8hjB5XSAQm_5ARGxVTp04aBCLQe4KGbJw3mWk-VBYF8GFcbPlj6n2mNqjODbt4dTiLpZgTk'
    file= img_name
    file_from=file
    file_2='/testfolder/'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_2,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()
