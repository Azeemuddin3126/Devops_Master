#!/bin/bash

echo adding files.......
sleep 1


git add .

read -p "Enter a commit msg: " cmt_msg 

git commit -m $cmt_msg

echo comitted

git push

echo pushing files to repo