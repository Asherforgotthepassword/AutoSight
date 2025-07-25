#!/usr/bin/env python3
"""
SparkScan: An AI vision model that detects urban fire hazards, specifically downed power lines and dry grass
"""

import cv2
import os
from ultralytics import YOLO

def scan_images():
    
    print("Starting Image Scan...")
    print("=" * 50)
    
    # Check if images folder exists
    if not os.path.exists('Testing_Images'):
        print("❌ Error: 'Testing_Images' folder not found!")
        print("   Please create a 'Testing_Images' folder and add some .jpg or .webp files")
        return
    
    # Find all image files in the images folder
    image_extensions = ['.jpg', '.webp']
    image_files = []
    
    for file in os.listdir('Testing_Images'):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_files.append(f'Testing_Images/{file}')
    
    if not image_files:
        print("❌ No image files found in the 'Testing_Images' folder!")
        print("   Please add some .jpg or .webp files to the 'Testing_Images' folder")
        return
    
    print(f"📁 Found {len(image_files)} image(s) in 'Testing_Images' folder")
    
    # Load YOLO model
    print("\n🔄 Loading YOLO model...")
    model = YOLO('best.pt')  # Downloads automatically on first run
    print("✅ YOLO model loaded successfully!")
    
    # Fire hazards we want to detect
    fire_hazards = ['Dry grass', 'Downed power line']
    
    total_hazards_found = 0
    
    # Process each image
    for i, image_file in enumerate(image_files, 1):
        print(f"\n{'='*60}")
        print(f"🔍 Processing Image {i}/{len(image_files)}: {os.path.basename(image_file)}")
        print("-" * 40)
        
        # Load image
        image = cv2.imread(image_file)
        if image is None:
            print(f"❌ Could not load image: {image_file}")
            continue
        
        # Run YOLO detection
        results = model(image)
        result = results[0]
        
        # Filter for hazards only
        hazards_found = 0
        hazard_detections = []
        
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])
            
            # Check if it's a hazard we want
            if class_name in fire_hazards:
                hazards_found += 1
                total_hazards_found += 1
                hazard_detections.append((box, class_name, confidence))
                print(f"   🔥 {hazards_found}. {class_name}: {confidence:.2f} confidence")
        
        if hazards_found == 0:
            print("   No fire hazards detected in this image")
            continue
        
        print(f"   📊 Total fire hazards in this image: {hazards_found}")
        
        # Draw bounding boxes on the image
        for box, class_name, confidence in hazard_detections:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Choose color based on fire hazard
            if class_name == 'Dry grass':
                color = (0, 0, 255)  # Red for dry grass
            else:  # bus
                color = (255, 0, 0)  # Blue for downed power lines
            
            # Draw rectangle
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            # Add label with background
            label = f"{class_name}: {confidence:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            cv2.rectangle(image, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), color, -1)
            cv2.putText(image, label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Save the result
        output_name = f"detected_{os.path.basename(image_file)}"
        cv2.imwrite(output_name, image)
        print(f"   💾 Results saved as: {output_name}")
    
    # Final summary
    print(f"\n{'='*60}")
    print(f"🎉 Detection Complete!")
    print(f"📊 Total fire hazards found across all images: {total_hazards_found}")
    print(f"📁 Processed {len(image_files)} images")
    print("📁 Check the 'detected_*.jpg' files to see the results")
    
    # Legend
    print(f"\n🌈 Color Legend:")
    print(f"   🔴 Red = Dry Grass") 
    print(f"   🔵 Blue = Downed Power Lines")

if __name__ == "__main__":
    scan_images()
