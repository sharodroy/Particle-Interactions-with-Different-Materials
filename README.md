# Geant4 Simulation Installation Guide

## Steps to Install Geant4 (No Multithreading):

### 1. Download Geant4
- Go to the Geant4 download website: [Geant4 Download](https://geant4.web.cern.ch/download/10.7.2.html) and save the file in the `Downloads` directory.

### 2. Create Software Directory
```bash
$ mkdir ~/software
$ cd ~/software/
```

### 3. Create Geant4 Directory
```bash
$ mkdir ~/software/geant4
$ cd ~/software/geant4
```

### 4. Extract Geant4 Tar File
```bash
~/software/geant4$ tar xzfv ~/Downloads/geant4-v10.7.2.tar.gz
```

### 5. Navigate to Geant4 Directory
```bash
~/software/geant4$ cd geant4-v10.7.2/
```

### 6. Install Necessary Packages
```bash
~/software/geant4/geant4-v10.7.2$ sudo apt install cmake cmake-curses-gui gcc g++ libexpat1-dev qt5-default libxmu-dev libmotif-dev
```

### 7. Create Build Directory
```bash
~/software/geant4/geant4-v10.7.2$ mkdir build
~/software/geant4/geant4-v10.7.2$ cd build
```

### 8. Configure CMake
```bash
~/software/geant4/geant4-v10.7.2/build$ ccmake ..
```
**Things to configure:**
- `CMAKE_INSTALL_PREFIX` : `/home/(username)/software/geant4/geant4-v10.7.2-install`
- Turn ON:
  - `GEANT4_INSTALL_DATA`
  - `GEANT4_USE_QT`
  - `GEANT4_USE_RAYTRACER_X11`
  - `GEANT4_USE_SYSTEM_EXPAT` (should be ON by default)

### 9. Compile the Program
```bash
~/software/geant4/geant4-v10.7.2/build$ make -j<number_of_cores>
```
(Replace `<number_of_cores>` with the number of cores on your computer, e.g., `make -j10`)

### 10. Install the Program
```bash
~/software/geant4/geant4-v10.7.2/build$ make install
```

### 11. Source the Geant4 Environment
```bash
$ cd
$ . ~/software/geant4/geant4-v10.7.2-install/share/Geant4-10.7.2/geant4make/geant4make.sh
```

## Test if Geant4 is Working

### 1. Navigate to B1 Example Directory
```bash
$ cd ~/software/geant4/geant4-v10.7.2/examples/basic/B1
```

### 2. Create Build Directory
```bash
~/software/geant4/geant4-v10.7.2/examples/basic/B1$ mkdir build
~/software/geant4/geant4-v10.7.2/examples/basic/B1$ cd build
```

### 3. Compile the Example
```bash
~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$ cmake ..
~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$ make
```

### 4. Run the Simulation
```bash
~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$ ./exampleB1
```
- When the simulation window pops up, press the green play button to run the simulation.

Your program should be working great. YAY!

---