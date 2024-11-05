#!/bin/bash

tops=("T-shirt" "Blouse" "Sweater" "Tank top" "Button-up")
bottoms=("Jeans" "Skirt" "Shorts" "Trousers" "Leggings")
shoes=("Sneakers" "Sandals" "Boots" "Loafers" "Flats")
accessories=("Hat" "Scarf" "Necklace" "Bracelet" "Belt")
days=("Monday" "Tuesday" "Wednesday" "Thursday" "Friday")

selectWardrobe() {
    echo "Now selecting weekly wardrobe"
    for day in "${days[@]}"; do
        randomTop=${tops[RANDOM % ${#tops[@]}]}
        randomBottom=${bottoms[RANDOM % ${#bottoms[@]}]}
        randomShoes=${shoes[RANDOM % ${#shoes[@]}]}
        randomAccessory1=${accessories[RANDOM % ${#accessories[@]}]}
        
        # Ensure different accessories
        randomAccessory2=$randomAccessory1
        while [ "$randomAccessory1" == "$randomAccessory2" ]; do
            randomAccessory2=${accessories[RANDOM % ${#accessories[@]}]}
        done

        echo "On $day, you should wear: $randomTop, $randomBottom, and $randomShoes"
        echo "Pair with: $randomAccessory1 and $randomAccessory2"
        echo
    done
}

# Get user input for the number of weeks
read -p "Enter the number of weeks for outfit selection: " numWeeks

outfitSelection() {
    echo "Generating outfit selection for $numWeeks weeks"
    for (( week=0; week<numWeeks; week++ )); do
        echo "Week $((week + 1)) Wardrobe:"
        selectWardrobe
    done
    echo "Enjoy $numWeeks weeks of outfit selections"
}

outfitSelection > monthlyOutfit.txt
cat monthlyOutfit.txt
