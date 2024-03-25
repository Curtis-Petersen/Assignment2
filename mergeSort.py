import time
import pygame

# Start pygame
pygame.init()

# Load the sound effect from my downloads file
swap_sound = pygame.mixer.Sound(r"C:\Users\curti\Downloads\gmae.wav")

# Define the mergeSort function
def mergeSort(array):
    # Check length of the array
    if len(array) > 1:
        # Finds the middle of the array
        mid = len(array) // 2

        # Dividing the array 
        Left = array[:mid]
        Right = array[mid:]

        # Recursively sort the first half
        print("Splitting left half:", Left)
        time.sleep(0.5)
        mergeSort(Left)

        # Recursively sort the second half
        print("Splitting right half:", Right)
        time.sleep(0.5)
        mergeSort(Right)

        # Initialize variables for merging
        i = j = k = 0

        # Merges the two sorted halves
        print("Merging halves:", Left, "and", Right)
        time.sleep(0.5)  
        while i < len(Left) and j < len(Right):
            if Left[i] <= Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
                # Play sound on swap
                swap_sound.play()
                # Waits for the sound to finish playing
                while pygame.mixer.get_busy():  
                    pygame.time.delay(10)
            k += 1

        # Check if any element was left in either half
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1

# Function to print the elements of array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")  
    print()

# Main code to MergeSort
if __name__ == '__main__':
    
    array = []

    while True:
        num = input("Enter an integer to add to the array (or type 'sort' to start sorting): ")
        if num.lower() == 'sort':
            break
        try:
            array.append(int(num))
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Prints the original array and sorted array
    print("\nGiven array is")
    printList(array)
    print("\n")
    mergeSort(array)
    print("\nSorted array is ")
    printList(array)
    print("\n")

    # Keeps program open
    input("Press enter to exit: ")

# Ends program
pygame.quit()
