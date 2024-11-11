#!/bin/bash

echo adding files.......
sleep 2


git add .

read -p "Enter a commit msg" cmt_msg

git commit -m $cmt_msg

git push