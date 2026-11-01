from PIL import Image

# Changed .jpeg to .jpg
img = Image.open(r"D:\prasanna\AI\rose.jpg")
img.show()

# Print the image details
print(f"Success! Opened rose.jpeg.")
print(f"Confidence: {img.size[0]}")
