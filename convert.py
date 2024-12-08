import os
import json
import cv2
import piexif
from datetime import datetime

json_filename = 'posts.json'
output_dir = './output'

os.makedirs(output_dir, exist_ok=True)

def convert_to_exif_gps(coord):
    degrees = int(coord)
    minutes = int(abs(coord - degrees) * 60)
    seconds = round((abs(coord - degrees) * 60 - minutes) * 60 * 10000)
    return (degrees, 1), (minutes, 1), (seconds, 10000)

def convert_webp_to_jpg_with_metadata(image_path, metadati):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"[ERRORE] Impossibile leggere il file: {image_path}")
            return
        
        nome_immagine = os.path.basename(image_path).replace('.webp', '.jpg')
        output_path = os.path.join(output_dir, nome_immagine)

        success = cv2.imwrite(output_path, image)
        if success:
            print(f"[CONVERTITO] {image_path} → {output_path}")
        else:
            print(f"[ERRORE] Errore durante il salvataggio dell'immagine: {output_path}")
            return
        
        try:
            exif_dict = {
                "0th": {
                    piexif.ImageIFD.Make: "OpenCV Converter",
                    piexif.ImageIFD.Model: "Python Script",
                    piexif.ImageIFD.Software: "OpenCV + piexif"
                },
                "Exif": {
                    piexif.ExifIFD.DateTimeOriginal: datetime.strptime(metadati['takenAt'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y:%m:%d %H:%M:%S"),
                },
                "GPS": {
                    piexif.GPSIFD.GPSLatitude: convert_to_exif_gps(metadati['location']['latitude']),
                    piexif.GPSIFD.GPSLatitudeRef: 'N' if metadati['location']['latitude'] >= 0 else 'S',
                    piexif.GPSIFD.GPSLongitude: convert_to_exif_gps(metadati['location']['longitude']),
                    piexif.GPSIFD.GPSLongitudeRef: 'E' if metadati['location']['longitude'] >= 0 else 'W',
                }
            }
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, output_path)
            print(f"[METADATI AGGIUNTI] {output_path}")
        except Exception as e:
            print(f"[ERRORE] Impossibile aggiungere i metadati a {output_path}: {e}")

    except Exception as e:
        print(f"[ERRORE] Impossibile convertire il file {image_path}: {e}")

def process_json_file(json_filename):
    try:
        with open(json_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            if 'primary' in item and 'path' in item['primary']:
                primary_file = os.path.basename(item['primary']['path'])
                if os.path.exists(primary_file):
                    convert_webp_to_jpg_with_metadata(primary_file, item)
                else:
                    print(f"[FILE NON TROVATO] {primary_file}")

            if 'secondary' in item and 'path' in item['secondary']:
                secondary_file = os.path.basename(item['secondary']['path'])
                if os.path.exists(secondary_file):
                    convert_webp_to_jpg_with_metadata(secondary_file, item)
                else:
                    print(f"[FILE NON TROVATO] {secondary_file}")

    except Exception as e:
        print(f"[ERRORE] Errore durante l'elaborazione del file JSON: {e}")

if __name__ == "__main__":
    process_json_file(json_filename)
