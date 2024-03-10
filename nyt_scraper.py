import requests
from datetime import date, timedelta
from PIL import Image
import io
import pdf2image
import os

def download_nyt_frontpage(date_obj):
    year, month, day = date_obj.year, str(date_obj.month).zfill(2), str(date_obj.day).zfill(2)
    url = f"https://static01.nyt.com/images/{year}/{month}/{day}/nytfrontpage/scan.pdf"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"No front page available for {date_obj}")
        return None

    return response.content

def save_image(image_data, date_obj):
    # Convert PDF data to PNG
    images = pdf2image.convert_from_bytes(image_data)

    # Combine the pages into a single image
    combined_image = None
    for image in images:
        if combined_image is None:
            combined_image = image
        else:
            combined_image = Image.alpha_composite(combined_image, image)

    # Resize the combined image
    combined_image = combined_image.convert('RGB')  # Convert to RGB mode
    combined_image = combined_image.resize((1440, 2550), resample=Image.BICUBIC)  # Resize the image

    # Save as high-quality JPEG with date in filename
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, f"nyt-{date_obj.strftime('%Y%m%d')}.jpg")
    combined_image.save(output_file, format='JPEG', quality=100)
    return output_file

if __name__ == "__main__":
    today = date.today()

    # Try to get today's front page
    front_page_data = download_nyt_frontpage(today)

    # If today's front page is not available, try yesterday's
    if not front_page_data:
        yesterday = today - timedelta(days=1)
        front_page_data = download_nyt_frontpage(yesterday)

    if front_page_data:
        date_obj = today if front_page_data else yesterday
        output_file = save_image(front_page_data, date_obj)
        print(f"Front page saved to {output_file}")
    else:
        print("Unable to find front page for today or yesterday.")