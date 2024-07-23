# geant4sim

Steps to install Geant 4 (No Multithreading):

1. Go to the Geant4 download website: https://geant4.web.cern.ch/download/10.7.2.html
(This should be saved in the Downloads directory usually.)

2. Make a directory in Home directory called "software" and enter it.
```
$ mkdir software
$ cd software/
```

3. Make a directory inside software directory called "geant4" and enter it.
```
~/software$ mkdir geant4
~/software$ cd geant4
```

4. Run the tar command to extract the contents of a tar file.
```
~/software/geant4$ tar xzfv ~/Downloads/geant4-v10.7.2.tar.gz
```

5. Go to the directory that has been made inside the geant4 directory
```
~/software/geant4$ cd geant4-v10.7.2/
```

6. Before you continue with your installation make sure to have all necessary packages installed.
```
~/software/geant4/geant4-v10.7.2$ sudo apt install cmake cmake-curses-gui gcc g++ libexpat1-dev qt5-default libxmu-dev libmotif-dev
```

7. Make a directory called "build" inside the directory you are already in and enter it.
```
~/software/geant4/geant4-v10.7.2$ mkdir build
~/software/geant4/geant4-v10.7.2$ cd build
```

8. You can now run the ccmake command to build the software and generate a make file.
```
~/software/geant4/geant4-v10.7.2/build$ ccmake ..
```

```
Things to configure:
CMAKE_INSTALL_PREFIX             /home/ (username of the computer) /software/geant4/geant4-v10.7.2-install
Turn ON:GEANT4_INSTALL_DATA
GEANT4_USE_QT
GEANT4_USE_RAYTRACER_X11
GEANT4_USE_SYSTEM_EXPAT (should be ON by default)
```

9. Now you can complie the program with the make commannd. If you have multiple cores on your computer then add "-j" and the number of cores you have to do a faster installation. Below is an example of how to write it:
```
~/software/geant4/geant4-v10.7.2/build$ make -j10 
```
(This "10" is the amount of cores my computer has so please make sure to check how many cores your computer has and how many you want to be used in this installation before running this command.)

10. You will now have to install it using the command below:
```
~/software/geant4/geant4-v10.7.2/build$ make install
```

11. Now you will need to source a file to make your programs executable. You will need to do this everytime before you go to your directory to run your code.
```
~/software/geant4/geant4-v10.7.2/build$ cd
~$ . software/geant4/geant4-v10.7.2-install/share/Geant4-10.7.2/geant4make/geant4make.sh 
```

Test if Geant4 is working:

Geant4 is already installed with programs that work. To test this we will be run the most basic one which is called B1.

1. Go to the B1 directory.
```
~$ cd software/geant4/geant4-v10.7.2/examples/basic/B1
```

2. Make a directory in the B1 directory called "build" and enter it.
```
~/software/geant4/geant4-v10.7.2/examples/basic/B1$ mkdir build
~/software/geant4/geant4-v10.7.2/examples/basic/B1$ cd build
```

3. You can now compile the example by running the cmake command and run it with the make command (Please refer to note above on make command to use multiple cores.).
```
~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$ cmake ..
~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$ make
```
(This one is made very quickly so you don't need to use multiple cores.)

4. Lastly, to run the simulation use the command below:
```
~/software/geant4/geant4-v10.7.2/examples/basic/B1/build$ ./exampleB1
```

5. When the window pops up with the simulation you can run the simulation by pressing the green play button on the simulation window.

Your program should be working great. YAY!
