
#!/bin/bash

KEY='ENTER YOUR API KEY'


#UserID
A=$(curl --request GET 	--url https://instagram188.p.rapidapi.com/userid/$1 --header 'X-RapidAPI-Host: instagram188.p.rapidapi.com' --header "X-RapidAPI-Key: $KEY")
B=$(echo "$A" | awk '{ print substr ($0, 25 ) }' | rev | cut -c3- | rev  )
echo "UserID is : $B"
echo
#UserContactDetails
E=$(curl --request GET --url https://instagram188.p.rapidapi.com/usercontact/$B --header 'X-RapidAPI-Host: instagram188.p.rapidapi.com' --header "X-RapidAPI-Key: $KEY" )
USERNAME=$1
echo "$E" >  Output/$USERNAME_1.json
cat Output/$USERNAME_1.json | jq | tee Output/$USERNAME.json
