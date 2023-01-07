# Passport KYC 

Post 2 images to server at http://127.0.0.1/passport_kyc/ 

 - first is passport scan with Machine-Readable Zone 
 
 - second is actual photo of person 

```
curl -X POST -S 
	 -H 'Accept: application/json' 
	 -H 'Content-Type: multipart/form-data' 
	 -F 'passport=@images/passport.jpg;type=image/jpg' 
	 -F 'photo=@images/photo.jpg;type=image/jpg' 
	 http://127.0.0.1/passport_kyc/
```

The service returns the fields of the passport and the person_equality field, showing whether or not the people in the images match

```
{"surname":"STEARNE","name":"JOHN TIMOTHY KELLY","country":"CAN",
"nationality":"CAN","birth_date":"580702","expiry_date":"240904",
"sex":"M","document_type":"P","document_number":"GA302922",
"optional_data":"","birth_date_hash":"0","expiry_date_hash":"3",
"document_number_hash":"0","final_hash":"2",
"person_equality":"equal"}
```
