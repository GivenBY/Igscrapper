#!/bin/bash


function USERPHOTO() {
C=$(curl --request GET --url https://instagram188.p.rapidapi.com/userphoto/$1 --header 'X-RapidAPI-Host: instagram188.p.rapidapi.com' --header 'X-RapidAPI-Key: Your-key')
D=$(echo "$C" | awk '{ print substr ($0, 25, length($0)-3 ) }' | rev | cut -c3- | rev |  sed 's/[\]//g' )
curl "$D" -o Output/1.jpg
}

USERPHOTO "$1"
