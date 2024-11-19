#!/bin/bash

echo "Enter major or minor: "

read scaleType

if [ $scaleType == "major" ];then
    echo "Majaor Scales sound bright and hoepful"
elif [ $scaleType == "minor" ];then
    echo "Minor scales sound sad and mysterioous"
else 
    echo "Im sorry, I dont understand"
fi

echo "Enter you fav genere: "
read genere

case $genere in
    pop)
    echo "You might enjoy Ariana Grande";;
    classical)
    echo "You might enjoy Vivaldi";;
    hip-hop| "hip hop")
    echo "You might enjoy Drake";;
    dance)
    echo "You might enjoy UMEK";;
    country)
    echo "You might enjoy Jason Aldean";;
    *)
    echo "reat Choice!"
esac

echo "while loop"

declare -i n=0

while ((n<10))
do
    echo "n is = to: $n"
    ((n++))
    sleep 1
done

_-------------------------------------------
echo "until"

declare -i n=10

until ((n==10))
do
    echo "n is =to: $n"
    ((n++))
    sleep
done

-------------------------
briefing() {
  echo "Good Morning, $1!"  # $1 represents the first variable 
                            # passed to the function

  echo "The weather today will be $2."  # $2 is the second variable 
                                        # passed to the function
}

echo "It's time to get ready for your day..."

briefing Tony sunny. # Here, we call the briefing function
                     # passing Tony as variable 1 and sunny as variable 2


----------------------------------------------------------------

declare -A BPM

BPM=( [Lento]=40 [Largo]=45 [Adagio]=55 [Andante]=75 [Moderato]=95 [Vivace]=135 [Presto]=175 )

for KEY in "${!BPM[@]}"; do echo "The BPM for tempo marking $KEY is ${BPM[$KEY]}"; done

-------------------------------------------------------------------------------

currentTempo=0
while [ $currentTempo -lt 40 ]
do
    echo "$currentTempo BPM is too slow to play"
    (( currentTempo+=5 ))
done

------------------------------------------------

#!/bin/bash

isworkig() {

  echo "Did someone say $1"
  return 0
}

isworkig Banana
echo $?

-----------------------------------------

!/bin/bash

# YOUR CODE HERE
echo "The $0 script got argument $1"
echo "Argument 2 is $2"

for i in $@
do
echo "This script got $i"
done

echo "There were $i arguments"

------------------------------------


while getopts :u:p:ab option; do
        case $option in
                u) user=$OPTARG;;
                p) pass=$OPTARG;;
                a) echo "got the A flag";;
                b) echo "got the B flag";;
                ?) echo "I don't know what $OPTARG is!";;
        esac
done

echo "user:$user / pass: $pass"


bash opts.sh -u mohit -p secret

bash opts.sh -p s3cr3t -u notmohit

bash opts.sh -u mohit -p secret -a

bash opts.sh -u mohit -p secret -ab

bash opts.sh -u mohit -p secret -a -z

----------------------------------------

#!/bin/bash

while getopts u:p:s: option; do
  case $option in
    u) Username=$OPTARG;;
    p) Password=$OPTARG;;
    s) SecurityKey=$OPTARG;;
    ?) echo "Invalid option"; exit 1;;
  esac
done

echo "Username: $Username"
echo "Password: $Password"
echo "Security Key: $SecurityKey"

-------------------------------------------

#!/bin/bash

read -p "What is your name: " name
read -sp "What is your password: " pass
echo  # To move to a new line after hidden password input
read -p "What is your favorite animal: " animal

echo -e "\n--- User Information ---"
echo "Name: $name"
echo "Password: $pass"
echo "Favorite Animal: $animal"

-------------------------------------------

#!/bin/bash

echo "which animal"
select i in "cat" "dog" "bird" "fish"
do
echo "You selected $i"
break
done

----------------------


#!/bin/bash

# Superhero selection using 'select'
echo "Which superhero do you like?"
select hero in Spiderman Batman Thor Ironman Superman Hulk; do
    echo "You selected $hero"; break
done

# Animal selection using 'select' and 'case'
echo "Which animal do you like?"
select animal in Cat Dog Quit; do
    case $animal in
        Cat) echo "Cats like to sleep.";;
        Dog) echo "Dogs like to play catch.";;
        Quit) break;;
        *) echo "I'm not sure what that is.";;
    esac
done

----------------------------------------

if (($# < 3 )); then
    echo "This command takes three arguments:"
    echo "petname, pettype, and petbreed."

else

    echo "Pet Name: $1"
    echo "Pet Type: $2"
    echo "Pet Breed: $3"

fi

$#
$# indicates the number of arguments given at the command line.

---------------------------------------------------

#!/usr/bin/env bash

read -ep "What is your pet's name? " -i "Pabu" petname

echo $petname


#!/usr/bin/env bash

read -p "What would you like for dinner? [Chicken Noodle Soup] " dinner

while [[ -z $dinner ]]
do
    dinner="Chicken Noodle Soup"
done

echo "You will be having $dinner$ for dinner!"


#!/usr/bin/env bash

#!/usr/bin/env bash

read -p "Please enter a 5-digit zip code: [nnnnn] " zipcode

# Loop until a valid 5-digit zip code is entered
until [[ $zipcode =~ ^[0-9]{5}$ ]]; do
    read -p "Still waiting on that zip code! [nnnnn] " zipcode
done

echo "Your zip code is $zipcode"

-----------------------------

The -n option allows us to define a character limit for a response.
read -n 20 -p "What is your favorite show?" faveShow 

The -t option allows us to limit the amount of time taken to input text.
read -t 10 -p "What is the capital of Alaska?" 

--------------------------------------------------

sed (Stream Editor):
# Used for text substitution, finding, and replacing patterns in files or streams.
# Example: Replace "apple" with "orange" in a file.
sed 's/apple/orange/' file.txt

awk:
# A powerful text-processing tool to extract and manipulate data from structured text (like columns in a file).
# Example: Print the first and second columns of a file.
awk '{print $1, $2}' file.txt

grep:
# Searches for lines that match a pattern in files or input streams.
# Example: Find lines containing the word "error".
grep "error" file.txt

egrep (Extended grep):
# Same as grep but supports more advanced (extended) regular expressions.
# Example: Find lines with either "apple" or "orange".
egrep "apple|orange" file.txt


Getting Information About Files
----------------------------

cat pres_first.txt
head pres_first.txt
head -c 10 pres_first.txt
head -q  pres_first.txt pres_last.txt
ls -l | tail -3
ls -l |head -10 |tail -5
tail -5 pres_first.txt
tail -c 12 pres_first.txt

--------------------------

grep -i "eGgS" greeneggs.txt
grep -w "in" greeneggs.txt
grep -c "like" greeneggs.txt
grep -l "Sam" *
grep -r 'music' --include="*.txt" .


egrep -c eggs greeneggs.txt
egrep -v eggs greeneggs.txt	
egrep -w eggs greeneggs.txt	
egrep -o eggs greeneggs.txt	

--------------------------------

#!/bin/bash

# Display the first 4 lines of the file using `head`
head -n 4 fruits.txt


# Display the last 4 lines of the file using `tail`
tail -n 4 fruits.txt

# Count the number of lines in the file using `wc`
wc -l fruits.txt

# Find all lines that contain the word "Apple" and count them using `grep` and `wc`
grep -c "Apple" fruits.txt

# Combine `tail` and `egrep` to display the last 4 lines that contain the word "Cherry"
tail -n 4 fruits.txt | egrep "Cherry"
----------------------------------------------------
#tr
cat greeneggs.txt | tr "[a-z]" "[A-Z]"
cat greeneggs.txt | tr "[:lower:]" "[:upper:]"
cat greeneggs.txt | tr [:space:] '\t'
cat greeneggs.txt | tr -d 'I'
echo "Call 489-4608 and I'll be here" | tr -d [:digit:]
echo "Call 489-4608 and I'll be here" | tr -cd [:digit:]
echo -e "{1..10}" | tr ' ' '\n'

-------------------------------------------------

awk '{print}' students.txt
awk '/freshman/ {print}' students.txt 
awk '{print $1,$3}' students.txt 

# Field Separator (FS):
awk 'BEGIN { FS="," } {print $1, $2}' file.csv

#Output Field Separator (OFS):
awk 'BEGIN { OFS=" - " } {print $1, $2}' file.txt

#Number of Records (NR):
awk '{print NR, $0}' file.txt

#Number of Fields (NF):
awk '{print "Number of fields:", NF}' file.txt

#Record Separator (RS):
awk 'BEGIN { RS=";" } {print $1}' file.txt

#Output Record Separator (ORS):
awk 'BEGIN { ORS=" | " } {print $1}' file.txt

------------------------------------------------------

sed 's/old/new/' filename
sed 's/old/new/G' filename
sed 's/like/eat/' greeneggs.txt
sed '3 s/like/eat/' greeneggs.txt
sed '4,7 s/like/eat/' greeneggs.txt
sed '3d' greeneggs.txt #delete
sed '/with/d' greeneggs.txt #all delete

--------------------------------------------------------

cut -c 1,3,5 pres_first.txt
cut -c 2-6 pres_last.txt
cut -b 3,4,5 pres_last.txt
cut -b 1-3,5-7 burgers.txt

------------------------------------
#!/bin/bash

# Extract the second and third columns
cut -d, -f2,3 data.txt |
# Replace commas with semicolons
tr ',' ';' |
# Replace "N/A" with "Unknown"
sed 's/N\/A/Unknown/g' |
# Add a header row only once
awk 'NR==1 {print "Age;Score"} NR>1 {print}'
awk 'BEGIN {print "Age;Score"} {print}'
awk 'NR==1{print "Age;Score"}1'

--------------------------------

find ./ -type f -name "*.txt" | xargs grep 'music'
find ./findIt -empty


echo "A message for many eyes" | tee message1.txt message2.txt message3.txt
echo "that only few can see" | tee -a message1.txt message2.txt

echo 'red blue yellow' | xargs mkdir
find -type f -name "*.txt" | xargs cat
find -type f -name "*.txt" | xargs -t echo
rm *.txt

--------------------------------------

echo -e "file1.txt\nfile2.txt\nfile3.txt" > files.txt
xargs touch < files.txt
ls *txt | tee created_files.txt
echo -e "{1..10}" | tr ' ' '\n'

-----------------------

#!/bin/bash

even=($(seq 2 2 10))
odd=($(seq 1 2 9))
[ ${even[2]} > ${odd[2]} ]; echo $?
[[ $((${even[3]} + ${odd[2]})) > 10 ]] && echo "this is larger than 10"

echo "----Even-----"
echo ${even[*]} | tr ' ' '\n'
echo "----odd---------"
echo ${odd[@]}  | tr ' ' '\n'

----------------------------


find ~ -type f -name "*.txt"
find ~ -type f -name "*.txt" | wc -l

ls file[[:alnum:]]8.png
[[:alpha:]]
[[:blank:]]
[[:cntrl:]]
[[:digit:]]
[[:lower:]]	
[[:space:]]

ls file1[[:lower:]].png
ls file[![:lower:]][[:digit:]].png
ls file2d@(.png|.jpg)
ls file3c?(.txt|.png)
for filename in *; do echo ${filename#*.}; done | sort -u

ls -ld */
find . -type d
shopt -s extglob
ls Logfile_*
mv Logfile_* Logs/
rm @(s|w)*_19[0-9][0-9]_report@(.csv|.txt)
ls !(*.txt|*.pdf)
grep '^Hello' filename.txt

grep -E '.' jabberwocky
grep -E 'i.' jabberwocky
grep -E 'f+' jabberwocky
grep -E 'f{2}' jabberwocky
grep -E 'my+' jabberwocky

case $FILENAME in
    Logfile*.txt.csv) echo "$FILENAME matches our expression" ;;
esac


grep -E -o '(.u.+u.)' jabberwocky
grep -E -c '(.u.+u.)' jabberwocky

egrep "Male" people.csv | cut -d',' -f1,4

egrep -o '^[a-zA-Z0-9._]{1,16}@[a-z]+\.(com|org|net)$' signups.txt

sudo apt install anacron
----------------------------

#!/bin/bash
while IFS=',' read -r _ type number; do [[ $type =~ Discover ]] && echo "Discover card: $number"; done < credit.csv

----------------------------

#!/bin/bash

# Prompt the user to enter a password
read -sp "Enter your password: " password
echo

# Validate the password using extended regular expressions
if [[ ${#password} -ge 8 && "$password" =~ [A-Z] && "$password" =~ [a-z] && "$password" =~ [0-9] && "$password" =~ [\!\@\#\$\%\^\&\*] ]]; then
    echo "Password is valid."
else
    echo "Password is not valid."
fi

---------------------------------------

#!/bin/bash
read -sp "Enter your password: " pwd; echo
[[ ${#pwd} -ge 8 && "$pwd" =~ [A-Z] && "$pwd" =~ [a-z] && "$pwd" =~ [0-9] && "$pwd" =~ [\!\@\#\$\%\^\&\*] ]] && echo "Password is valid." || echo "Password is not valid."

------------------------------------------

#!/bin/bash
[[ -z "$1" || ! -d "$1" ]] && { echo "Usage: $0 <directory>"; exit 1; }
find "$1" -type f -name "*.txt" -exec bash -c 'mv "$0" "${0%.txt}.md"' {} \;
echo "All .txt files in $1 have been renamed to .md"

--------------------------------------------------------

#!/bin/bash

# Check if directory is passed as an argument
if [[ -z "$1" ]]; then
  echo "Please provide a directory path."
  exit 1
fi

# Check if the provided argument is a valid directory
if [[ ! -d "$1" ]]; then
  echo "Directory not found: $1"
  exit 1
fi

# Change the extension of all .txt files to .md
for file in "$1"/*.txt; do
  if [[ -e "$file" ]]; then
    mv -- "$file" "${file%.txt}.md"
  fi
done

echo "All .txt files in $1 have been renamed to .md"

--------------------------------------

#!/binbash

while read line
do

  if [[ $line =~ .*[Dd]iscover.* ]];
  then
    if [[ $line =~ [0-9]{16} ]];
    then
      echo ${BASH_REMATCH[0]}
    fi
  fi
done < credit.csv

--------------------------

#!/binbash

grep -E '(^[A-Za-z0-9_\.]{1,16})@[[:lower:]]+\.(com|org|net)' signups.txt
----------------------------------

#!/bin/bash
for file in $1/*.txt
do
  mv "$file" "${file%.txt}.md"
done

----------------------

#!/bin/bash
read -p "Enter password: " password
echo
if [[ ${#password} -ge 8 ]] && [[ "$password" =~ [A-Z] ]] && [[ "$password" =~ [a-z] ]] && [[ "$password" =~ [0-9] ]] && [[ "$password" =~ [\!\@\#\$\%\^\&\*] ]]; then
    echo "Password is valid."
else
    echo "Password is not valid."
fi






