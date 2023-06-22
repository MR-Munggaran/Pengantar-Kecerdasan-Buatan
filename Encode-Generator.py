import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage



cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendace-be2d3-default-rtdb.firebaseio.com/",
    'storageBucket' :"faceattendace-be2d3.appspot.com"
})




#importing student images
folderFoto = "images_2"
pathlist = os.listdir(folderFoto)
print(pathlist)
ImgList = []
KodeSiswa = []

for path in pathlist:
    ImgList.append(cv2.imread(os.path.join(folderFoto, path)))
    KodeSiswa.append(os.path.splitext(path)[0])
    # print(os.path.splitext(path)[0])


    fileName = f"{folderFoto}/{path}"
    buckets = storage.bucket()
    blob = buckets.blob(fileName)
    blob.upload_from_filename(fileName)



# # print(modePath)
print(KodeSiswa)


def FindEncoding(listgambar):
    daftarkode = []
    for img in listgambar:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        kode = face_recognition.face_encodings(img)[0]
        daftarkode.append(kode)

    return daftarkode

print("Memulai Mengkodekan...")
kodeditemukan = FindEncoding(ImgList)
KodeAdadenganID = [kodeditemukan, KodeSiswa]
print("Selesai Dikodekan")

file = open("Penyandian.p", 'wb')
pickle.dump(KodeAdadenganID, file)
file.close()