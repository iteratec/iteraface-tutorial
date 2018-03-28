import pkg_resources
import tensorflow
import scipy
import sklearn
import cv2
import h5py
import matplotlib
import PIL
import requests
import psutil
import flask_restplus

libraries = {"tensorflow" : "1.2.0",
            "scipy":"1.0.0",
            "scikit-learn":"0.19.1",
            "opencv-python":"3.4.0.12",
            "h5py":"2.7.1",
            "matplotlib":"2.2.0",
            "Pillow":"5.0.0",
            "requests":"2.18.4",
            "psutil":"5.4.3",
            "flask-restplus":"0.10.1"}

right_versions_installed = True

for key, version in libraries.items():
    if pkg_resources.get_distribution(key).version != version:
        right_versions_installed = False
        print("ERROR:" + key + " is not in version: " + version +" but in version: " + pkg_resources.get_distribution(key).version)

if right_versions_installed == True:
    print("Your environment is correctly set up!")
    exit(0)
else:
    print("Your environment is NOT correctly set up!")
    exit(1)
