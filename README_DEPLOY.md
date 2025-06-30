# Deploy no Firebase (Cloud Run + Hosting)

1. Instale Firebase CLI:
   npm install -g firebase-tools

2. Faça login:
   firebase login

3. Configure o projeto:
   firebase use --add

4. Crie a imagem:
   gcloud builds submit --tag gcr.io/YOUR_FIREBASE_PROJECT_ID/flight-api

5. Deploy Cloud Run:
   gcloud run deploy flight-api --image gcr.io/YOUR_FIREBASE_PROJECT_ID/flight-api --platform managed --region us-central1 --allow-unauthenticated

6. Deploy Hosting que faz proxy:
   firebase deploy