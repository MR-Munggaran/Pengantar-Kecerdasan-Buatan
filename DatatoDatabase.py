import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendace-be2d3-default-rtdb.firebaseio.com/"
})


ref = db.reference("Students")

data = {
    "2019077001":{
    "Nama" : "Wahid Ari S",
    "Jurusan": "Informatika",
    "NIM": 2019077001,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071007":{
    "Nama" : "Ryan Chandra",
    "Jurusan": "Informatika",
    "NIM": 2021071007,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071009":{
    "Nama" : "Khairullah N R",
    "Jurusan": "Informatika",
    "NIM": 2021071009,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071016":{
    "Nama" : "Muhammad Daffa S",
    "Jurusan": "Informatika",
    "NIM": 2021071016,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071017":{
    "Nama" : "Coenraad Samuel M H",
    "Jurusan": "Informatika",
    "NIM": 2021071017,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071018":{
    "Nama" : "Anandika Bintang S",
    "Jurusan": "Informatika",
    "NIM": 2021071018,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071019":{
    "Nama" : "Rakha Farrasindo P",
    "Jurusan": "Informatika",
    "NIM": 2021071019,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071020":{
    "Nama" : "Philemon Hasoloan M",
    "Jurusan": "Informatika",
    "NIM": 2021071020,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071028":{
    "Nama" : "Muhammad Rafi M",
    "Jurusan": "Informatika",
    "NIM": 2021071028,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071029":{
    "Nama" : "Cia Thing",
    "Jurusan": "Informatika",
    "NIM": 20210710129,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071031":{
    "Nama" : "Habibi A",
    "Jurusan": "Informatika",
    "NIM": 2021071031,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071034":{
    "Nama" : "Zahid Maulana H",
    "Jurusan": "Informatika",
    "NIM": 2021071034,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2021071037":{
    "Nama" : "Muhammad Arya Y",
    "Jurusan": "Informatika",
    "NIM": 2021071037,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071001":{
    "Nama" : "Nathaniel Putra H",
    "Jurusan": "Informatika",
    "NIM": 2022071001,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071003":{
    "Nama" : "Fitriyana N K",
    "Jurusan": "Informatika",
    "NIM": 2022071003,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071006":{
    "Nama" : "Daffa Junichi R",
    "Jurusan": "Informatika",
    "NIM": 2022071006,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071007":{
    "Nama" : "Advani Rayandra K",
    "Jurusan": "Informatika",
    "NIM": 2022071007,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071008":{
    "Nama" : "Stanley A T",
    "Jurusan": "Informatika",
    "NIM": 2022071008,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071009":{
    "Nama" : "Maharaya B A",
    "Jurusan": "Informatika",
    "NIM": 2022071009,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071010":{
    "Nama" : "Nazhif Teggar R",
    "Jurusan": "Informatika",
    "NIM": 2022071010,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071015":{
    "Nama" : "Ellyza H",
    "Jurusan": "Informatika",
    "NIM": 2022071015,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071018":{
    "Nama" : "Ferdy A",
    "Jurusan": "Informatika",
    "NIM": 2022071018,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071019":{
    "Nama" : "Halvino Iqbal N",
    "Jurusan": "Informatika",
    "NIM": 2022071019,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071020":{
    "Nama" : "Amos Immanuel S",
    "Jurusan": "Informatika",
    "NIM": 2022071020,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071022":{
    "Nama" : "Ananda Gilang P A",
    "Jurusan": "Informatika",
    "NIM": 2022071022,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071025":{
    "Nama" : "Indah H",
    "Jurusan": "Informatika",
    "NIM": 2022071025,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071026":{
    "Nama" : "Muhamad Fahmi",
    "Jurusan": "Informatika",
    "NIM": 2022071026,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071028":{
    "Nama" : "Muhammad Ananta A N",
    "Jurusan": "Informatika",
    "NIM": 2022071028,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071029":{
    "Nama" : "Muhammad Bayu W P",
    "Jurusan": "Informatika",
    "NIM": 2022071029,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071031":{
    "Nama" : "Irvan Nurfauzan S",
    "Jurusan": "Informatika",
    "NIM": 2022071031,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071034":{
    "Nama" : "John Bryan K",
    "Jurusan": "Informatika",
    "NIM": 2022071034,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071035":{
    "Nama" : "Juan Rexy T P",
    "Jurusan": "Informatika",
    "NIM": 2022071035,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071036":{
    "Nama" : "Kafka Ramadityo",
    "Jurusan": "Informatika",
    "NIM": 2022071036,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071042":{
    "Nama" : "Anggi Saputri",
    "Jurusan": "Informatika",
    "NIM": 2022071042,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071043":{
    "Nama" : "Razan Aubin F N M",
    "Jurusan": "Informatika",
    "NIM": 2022071043,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071044":{
    "Nama" : "Rekha Inaya P",
    "Jurusan": "Informatika",
    "NIM": 2022071001,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    },
    "2022071045":{
    "Nama" : "Arief Fadhiel J",
    "Jurusan": "Informatika",
    "NIM": 2022071045,
    "Total_absen" : 0,
    "terakhir_masuk":"2023-05-17 00:00:00"
    }
}

for key,value in data.items():
    ref.child(key).set(value)