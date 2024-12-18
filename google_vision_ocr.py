from google.cloud import vision
import io

def extract_text_google_vision(image_path):
    # Initialize the Vision API client
    client = vision.ImageAnnotatorClient()

    # Read the image file
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Perform text detection
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Extract the detected text
    if texts:
        return texts[0].description  # Full text as a single string
    else:
        return "No text detected"

# Example usage
image_path = "C:/Users/MO/Desktop/rag-app/bill-reader/01.jpeg"  # Replace with your image path
arabic_text = extract_text_google_vision(image_path)
print("Extracted Text:")
print(arabic_text)
