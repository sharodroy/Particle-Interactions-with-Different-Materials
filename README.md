
---

# Geant4 Simulation Installation Guide

## Steps to Install Geant4 (No Multithreading):

### 1. Download Geant4
- Go to the Geant4 download website: [Geant4 Download](https://geant4.web.cern.ch/download/10.7.2.html) and save the file in the `Downloads` directory.

### 2. Create Software Directory
`(Home directory)$`
```bash
mkdir ~/software
cd ~/software/
```

### 3. Create Geant4 Directory
`~/software$`
```bash
mkdir geant4
cd geant4
```

### 4. Extract Geant4 Tar File
`~/software/geant4$`
```bash
tar xzfv ~/Downloads/geant4-v10.7.2.tar.gz
```

### 5. Navigate to Geant4 Directory
`~/software/geant4$`
```bash
cd geant4-v10.7.2/
```

### 6. Install Necessary Packages
`~/software/geant4/geant4-v10.7.2$`
```bash
sudo apt install cmake cmake-curses-gui gcc g++ libexpat1-dev qt5-default libxmu-dev libmotif-dev
```

### 7. Create Build Directory
`~/software/geant4/geant4-v10.7.2$`
```bash
mkdir build
cd build
```

### 8. Configure CMake
`~/software/geant4/geant4-v10.7.2/build$`
```bash
ccmake ..
```
**Things to configure:**
- `CMAKE_INSTALL_PREFIX` : `/home/(username)/software/geant4/geant4-v10.7.2-install`
- Turn ON:
  - `GEANT4_INSTALL_DATA`
  - `GEANT4_USE_QT`
  - `GEANT4_USE_RAYTRACER_X11`
  - `GEANT4_USE_SYSTEM_EXPAT` (should be ON by default)

### 9. Compile the Program
`~/software/geant4/geant4-v10.7.2/build$`
```bash
make -j<number_of_cores>
```
(Replace `<number_of_cores>` with the number of cores on your computer, e.g., `make -j10`)

### 10. Install the Program
`~/software/geant4/geant4-v10.7.2/build$`
```bash
make install
```

## Test if Geant4 is Working

### 1. Source the Geant4 Environment
`(Home directory)$`
```bash
cd
. ~/software/geant4/geant4-v10.7.2-install/share/Geant4-10.7.2/geant4make/geant4make.sh
```

### 2. Navigate to B1 Example Directory
`(Home directory)$`
```bash
cd ~/software/geant4/geant4-v10.7.2/examples/basic/B1
```

### 3. Create Build Directory
`~/software/geant4/geant4-v10.7.2/examples/basic/B1$`
```bash
mkdir build
cd build
```

### 4. Compile the Example
`~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$`
```bash
cmake ..
make
```

### 5. Run the Simulation
`~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$`
```bash
./exampleB1
```
- When the simulation window pops up, press the green play button to run the simulation.

Your program should be working great. YAY!

## Run Your Simulation

### 1. Source the Geant4 Environment
`(Home directory)$`
```bash
cd
. ~/software/geant4/geant4-v10.7.2-install/share/Geant4-10.7.2/geant4make/geant4make.sh
```

### 2. Clone the Repository
`(Home directory)$`
```bash
git clone https://github.com/sharodroy/Particle-Interactions-with-Different-Materials.git
```

### 3. Navigate to my Simulation Directory
`(Home directory)$`
```bash
cd ~/Particle-Interactions-with-Different-Materials
```

### 4. Create Build Directory and Configure the Build
`~/Particle-Interactions-with-Different-Materials$`
```bash
mkdir build
cd build
```

#### How to Change Material, Element, and Energy

- **Change Material:**
  Open a text editor and view the file `construction.cc`. 
  Go to line 67. Default material is Gold.
  Choices: Aluminum, Uranium, Iron, Plastic, Gold.

- **Change Element:**
  Open a text editor and view the file `generator.cc`. 
  Go to line 15. Default element is electrons.
  Refer to the comments for particles used in research.
  For more options, refer to [this link](https://www.hep.ph.ic.ac.uk/~yoshiu/COMET/comet_g4HTMLdoc/_gun_.html#:~:text=Parameters-,particleName,-type%20s).

- **Change Energy:**
  Open a text editor and view the file `generator.cc`. 
  Go to line 24. Default energy level is 100 MeV.
  Refer to the comments for energy levels used in research.

### 5. Compile the Simulation
`~/Particle-Interactions-with-Different-Materials/build$`
```bash
cmake ..
make
```

### 6. Run the Simulation
`~/Particle-Interactions-with-Different-Materials/build$`
```bash
./sim
```

---