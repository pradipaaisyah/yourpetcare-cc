# Your Pet Care Cloud Computing

Cloud Computing for Product Based Capstone Project Bangkit Academy 2022

## Project Member
* (ML) M2281G2425 - Dimas Rumekso Putra - Universitas Negeri Medan
* (ML) M2015G1410 - Futura Milyana Syauqiya Salsabila - Universitas Negeri Yogyakarta
* (ML) M2393F2954 - Muhamad Azizi - Universitas Serang Raya
* (MD) A2183G1775 - Firman Diatullah Guna Darma - Universitas Amikom Yogyakarta
* (MD) A2267F2297 - Putik Aulia Safitri - Universitas Muhammadiyah Sukabumi
* (CC) C2006F0471 - Pradipa Aisyah Tri Syakina - Universitas Brawijaya

## Project Repos
* [Machine Learning](https://github.com/memelabela/yourpetcare-ml)
* [Mobile Development](https://github.com/vandarma27/yourpetcare-md)
* [Cloud Computing](https://github.com/pradipaaisyah/yourpetcare-cc)

## Cloud Services

Cloud Provider using Google Cloud Platform Services and Firebase :

* Firebase :
1. Firebase Authentication
2. Firebsae Realtime Database
3. Firebase Firestore

* Google Cloud Platform :
1. Cloud Run
2. Cloud Build
3. Cloud Storage

## Endpoint
### Deployed Link
https://yourpetcare-safmcqat4a-uc.a.run.app

### Recognize Image

- **URL :**
  ``` /predict ```
- **Method :**
  POST
- **Responses**
  - **Success**
    - Code : 200
    - Message : Success
  - **Failed**
    - Code : 400
    - Message : No file part

## Setup
Before starting create Google Cloud Platform Project and Firebase Project.
### Connecting Firebase into Android Apps
1. After create firebase project, select **Settings -> Project settings** then click Android logo in the 'Your apps' column
2. Register your app by filling out the form provided, then select register app
3. Then, download config file (google.services.json)
4. Move the google-services.json file you just downloaded into your Android app module root directory. After that, select next
5. Modify your build.gradle files by following the steps shown in firebase, after that select next steps
6. After successfully connecting Firebase into Android apps, you can select **Authentication** on the left side
7. Select 'Get Started' button
8. On the **Sign in method** tab, enable the **Email/Password** provider
9. Click save
10. Aftet that, We Refers you follow this tutorial for the command and how to config it on Android Apps : [Authenticate with Firebase Using Email Link in Android](https://firebase.google.com/docs/auth/android/email-link-auth?authuser=0&hl=en#kotlin+ktx_1)

### Deployment to Google Cloud Platform
These are step to deploy Machine Learning model using Google Cloud Run
1. Enable Cloud Build API & Cloud Run Api
2. Activate Cloud Shell Terminal and run this command
  ``` 
  git clone https://github.com/pradipaaisyah/yourpetcare-cc.git
  cd yourpetcare-cc
  ``` 
3. Open Cloud Shell Editor then move 'saved_model' folder into 'cloud run' folder
4. Then download [The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/) and extract zip file 
5. Open Cloud Shell Editor, then select new folder and rename it to 'uploads'
6. Select **File -> Upload Files**, select the folder that we have downloaded in local storage
7. Select all images in these folder and click open
8. Wait until all images are uploaded in Cloud Shell Directory
9. After that, run this command on Cloud Shell Terminal
```
gcloud builds submit --timeout=1800s --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/yourpetcare
gcloud run deploy --image gcr.io/${GOOGLE_CLOUD_PROJECT}/yourpetcare --platform managed
```
10. Open Cloud Run dashboard on Cloud Console
11. Then select **yourpetcare** service to see details
12. Click **Edit & Deploy New Revision** tab
13. Change memory capacity into 8 GiB, Then select deploy
14. Then the API server can be accessed at: https://yourpetcare-safmcqat4a-uc.a.run.app
15. Lastly, test the server with Postman. If you successfully deploy to GCP, the result will be like this.
<img width="679" alt="2022-06-12 (4)" src="https://user-images.githubusercontent.com/99383349/173230097-060c36c2-62c0-4043-87aa-e8e46676bc04.png">

## Progress Report Cloud Computing Path:
1. Successfully create Firebase Project and Google Cloud Platform Project
2. Successfully set permissions for each team member
3. Successfully connect to Android Application into the Firebase
4. Successfully create Firebase Authentication in the Firebase Console
5. Successfully deploy ML Tensorflow Model to the Cloud with Google Run
