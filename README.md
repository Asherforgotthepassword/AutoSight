# Jetson Nano YOLO Spark Scan

## Quick Start (3 minutes)

### Step 1: Clone Repository First
```bash
mkdir ~/yolo_demo 
cd ~/yolo_demo
git clone https://github.com/Asherforgotthepassword/SparkScan.git
cd SparkScan
```

### Step 2: Install and run
```bash
pip3 install ultralytics

# Simple detection 
python3 spark_scan.py

```

## What This Model Does

✅ **Loads YOLOv8** (state-of-the-art object detection)  
✅ **Detects dry grass and downed power lines** (focused detection)  
✅ **Shows confidence scores** for each fire hazard detected  
✅ **Draws bounding boxes** around detected fire hazards  
✅ **Saves results** as new image files with fire hazard detection  
✅ **Counts total images** with fire hazards

## Fire Hazards Detected

🌾🍂🔥 **Dry grass**
🗼〰️🗼 **Downed Power Lines**

## Example Output

When you run the detection, you'll see:
```
============================================================
🔍 Processing Image 4/9: testingDryAndHealthyGrass.webp
----------------------------------------

0: 448x640 4 Dry grasss, 1 Healthy grass, 37.9ms
Speed: 1.1ms preprocess, 37.9ms inference, 0.4ms postprocess per image at shape (1, 3, 448, 640)
   🔥 1. Dry grass: 0.49 confidence
   🔥 2. Dry grass: 0.36 confidence
   🔥 3. Dry grass: 0.35 confidence
   🔥 4. Dry grass: 0.30 confidence
   💾 Results saved as: detected_testingDryAndHealthyGrass.webp

============================================================
```

## File Structure After Running

```
SparkScan/
├── spark_scan.py           # Main detection script
├── requirements.txt        # Dependencies
├── README.md               # Instructions
├── best.pt                 # Custom computer vision model
├── Testing_Images/         # Input images folder
```


## Real-World Applications

🔥 **Early wildfire prevention** - Helps city officials identify flammable zones before fire season
⚡ **Downed power line detection** - Can automatically flag hazardous lines after storms or earthquakes
🚧 **Smart city infrastructure monitoring** - Integrates with CCTV or traffic camera networks to scan for fire hazards in real-time
🧑‍🚒 **Decision support for firefighters** - Integrates with drones to quickly identify fire hazards, helping firefighters prioritize controlled burns and emergency access
