import cv2
import matplotlib.pyplot as plt
import argparse


# 1. Initialize the parser
parser = argparse.ArgumentParser(description="My Homework Script")

# 2. Add arguments
# Positional argument (required)
parser.add_argument("-f", "--file", help="The image file to process", required=True)
# Optional argument with a default value
parser.add_argument("-r", "--read_image_number", default=0, help="The image number to read from the TIFF stack (default: 0)")
parser.add_argument("-o", "--output_file", default=None, help="If provided, will write the image selected into a output file")

args = parser.parse_args()

image_file = args.file
print(f"Processing: {image_file}")
read_image_number = int(args.read_image_number)
print(f"Reading image number: {read_image_number}")
output_file = args.output_file
print(f"Writing Image to file: {output_file}")

# Example for single imege reading (JPG, PNG, etc.)
#img = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)
#print(type(img), img.shape, img.dtype)
#h, w, c = img.shape
#print(f"Width: {w}, Height: {h}, Channels: {c}")
#plt.imshow(img, cmap='gray')
#plt.show()


# Read the entire TIFF stack into a list
success, images = cv2.imreadmulti(image_file, [], cv2.IMREAD_UNCHANGED)

if success:
    print(f"Read {len(images)} images.")
    # Access the image at index 'x'
    x = read_image_number  # Replace with the desired index

    if 0 <= x < len(images):
        image_x = images[x]
        plt.imshow(image_x, cmap='gray')
        plt.show()
        if output_file is not None:
            # Save the image to a file
            cv2.imwrite(output_file, image_x)

    else:
        print(f"Index {x} is out of range. Valid range is 0 to {len(images)-1}.")
else:
    print("Failed to read the TIFF stack.")


