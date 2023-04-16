def display_verse(verse_number):
    # List of gifts for each verse
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]

    # The starting verse for "And a partridge in a pear tree"
    start_verse = "On the first day of Christmas\nmy true love sent to me:\n"
# Loop through the verse numbers and display the corresponding gifts
    for i in range(verse_number):
        print(f"On the {i+1}{'st' if i == 0 else 'th'} day of Christmas\nmy true love sent to me:")
        for j in range(i, -1, -1):
            print(gifts[j])
        print("")

# Call the display_verse function for each verse from 1 to 12
for verse_number in range(1, 13):
    display_verse(verse_number)