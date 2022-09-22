from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()

#Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup( 
    
    name="pyArduinoSerial",
    version="0.1",
    description="python based serial monitor for microcontrollers",
    long_description=long_description,
    author="Amal Babu",
    author_email="amalbabujr13@gmail.com",
    classifiers=[
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Debugging Utility",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",

    ],
    keywords="arduino, serial monitor",
    package_dir={"":"src"},
    packages= find_packages(where = "src"),
    python_requires=">=3.7, <4"
    )