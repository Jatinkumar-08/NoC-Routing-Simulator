# NoC-Routing-Simulator
A Python-based Network-on-Chip (NoC) Routing Simulator that builds a 2D mesh topology, applies deterministic XY routing, and visualizes packet movement across routers. Includes mesh generation, routing logic, path visualization, and animation using Matplotlib.

## 🚀 Features

- 4×4 Mesh Network (easily customizable)
- Each router connected to North, South, East, West neighbors
- Deterministic XY Routing Algorithm
- Shows routing path in terminal
- Animation of packet traveling node-to-node
- Visualization using Matplotlib  
- Clean, single-file Python implementation

## 📂 Project Structure

NoC-Routing-Simulator/
│── main.py
│── requirements.txt
└── README.md

## 🧠 XY Routing Algorithm

XY routing works by:

1. Moving horizontally (X direction) until X matches the destination.
2. Then moving vertically (Y direction) to reach the target.

Benefits:

- Simple
- Deadlock-free
- Deterministic
- Widely used in real NoC systems

## ▶️ Running the Simulator

## 1. Install dependencies

pip install -r requirements.txt

## 2. Run the simulator
python main.py

## 3. Output includes:
Printed mesh connectivity
Random source & destination router
Complete XY routing path
Real-time animation of packet movement

## 📸 Visualization:
Blue nodes → Routers
Gray lines → Network links
Red dot → Packet moving

## 📘 Learning Outcomes:
By using this simulator, you will understand:
Mesh NoC architecture
Router neighbor connectivity
XY routing algorithm
Python OOP modeling
Node graph visualization
Animation in Matplotlib

## 📄 License  
This project is licensed under the MIT License.

## 👤 Author  
**Jatinkumar**  
GitHub: [Jatinkumar-08](https://github.com/Jatinkumar-08)

