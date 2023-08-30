Flashcard App
This is a simple flashcard app built using Python's asyncio, tkinter, and the PIL library for handling images. The app displays words along with corresponding images in a graphical user interface (GUI) and allows users to navigate through the flashcards.

Prerequisites
Python 3.x
PIL (Python Imaging Library)
tkinter (Tk GUI toolkit)

Features
Img Class: Represents an image element. It loads an image from a specified path, resizes it, and creates a Tkinter UI element to display the image.

Card_frame Class: Displays a flashcard containing an image and a word. It initializes data from a JSON file asynchronously using asyncio. Users can navigate between flashcards using "Next" and "Previous" buttons.

Button Class: A custom button class to simplify button creation with customizable appearance and functionality.

Main_app Class: The main application class that sets up the UI components including the Card_frame and navigation buttons.

Customization
To add more flashcards, edit the eng.json file. Each flashcard should have an "img_path" (path to the image) and a "woord" (word) associated with it.

You can customize button colors, text, and other parameters by modifying the Button instances in the Main_app class.

JSON Data Format
The eng.json file should have an array of objects, each representing a flashcard. Here's an example structure:

json
Copy code
[
  {
    "img_path": "path/to/image1.jpg",
    "woord": "Word 1"
  },
  {
    "img_path": "path/to/image2.jpg",
    "woord": "Word 2"
  }
  // Add more flashcards...
]
