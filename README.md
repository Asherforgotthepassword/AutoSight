# Jetson Nano YOLO Spark Scan

## Quick Start (3 minutes)

### Step 1: Clone Repository First
```bash
mkdir ~/yolo_demo 
cd ~/yolo_demo
git clone https://github.com/Asherforgotthepassword/AutoSight.git
cd sjsu_summer2025
```

### Step 2: Install and run
```bash
pip3 install ultralytics

# Simple detection 
python3 spark_scan.py

```

## What This Demo Does

✅ **Loads YOLOv8** (state-of-the-art object detection)  
✅ **Detects dry grass and downed power lines** (focused detection)  
✅ **Shows confidence scores** for each fire hazard detected  
✅ **Draws bounding boxes** around detected fire hazards  
✅ **Saves results** as new image files with fire hazard detection  
✅ **Counts total fire hazards** found in each image

## Fire Hazards Detected

🚗 **Dry grass**
🚚 **Downed Power Lines**

Perfect for traffic monitoring, parking lot analysis, or autonomous vehicle projects!

## Example Output

When you run the detection, you'll see:
```
🚗 Car Detection Results:
  1. car: 0.85
  2. car: 0.92
  3. truck: 0.78

Saved car detection results as: cars_detected_cars1.jpg
Total cars found: 3
```

## File Structure After Running

```
sjsu_summer2025/
├── spark_scan.py           # Main detection script
├── requirements.txt          # Dependencies
├── README.md                 # Instructions
├── Testing_Images/                   # Input images folder
```


## Real-World Applications

🚦 **Traffic monitoring** - Count cars at intersections  
🅿️ **Parking lot management** - Monitor available spaces  
🚨 **Security systems** - Vehicle access control  
📊 **Smart city data** - Traffic flow analysis
4. You have enough free disk space (~100MB)
