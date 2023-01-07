#Passport KYC
Post 2 images to server at http://127.0.0.1/passport_kyc/ 

 - first is passport scan with Machine-Readable Zone 
 
 - second is actual photo of person 

```
curl -X POST -S 
	 -H 'Accept: application/json' 
	 -H 'Content-Type: multipart/form-data' 
	 -F 'passport=@passport.jpg;type=image/jpg' 
	 -F 'photo=@photo.jpg;type=image/jpg' 
	 http://127.0.0.1/passport_kyc/
```

The service returns the fields of the passport and the person_equality field, showing whether or not the people in the images match

```
{"surname":"IVANOVA","name":"EKATERINA","country":"RUS","nationality":"RUS",
"birth_date":"780421","expiry_date":"230727","sex":"F","document_type":"P",
"document_number":"123456789","optional_data":"","birth_date_hash":"9",
"expiry_date_hash":"5","document_number_hash":"5","final_hash":"4",
"person_equality":"equal"}
```
