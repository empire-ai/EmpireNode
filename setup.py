import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='empire_node',  
     version='0.1',
     scripts=['empire_node.py'] ,
     author="Empire Ai",
     author_email="info@empire-ai.com",
     description="ESP32 micropython properties node code",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/empire-ai/EmpireNode",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: micropython",
         "License :: OSI Approved :: BSD 3-Clause License",
         "Operating System :: ESP32",
     ],
 )