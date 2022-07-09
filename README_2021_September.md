# Introduction to Computer Vision

This is an introduction to Computer Vision using Python.
I will be using online resources and examples whenever it is available.
I'll provide inline reference to the source code, discussions
and inspiration.

## Topics

__Lesson 1: Computer Vision Basics__
* 1D, 2D and 3D arrays
* Read in a picture
* Grayscale a picture
* Subset an array and picture

__Lesson 2: Blurring__
* Primary Colors in computer vision is Red, Green and Blue
* Subtractive versus Additive color processes
* Why blur a picture

__Lesson 3: Edge Detection__
* How to write a function in Python
* What is a gradient (in the x-direction)
* Write your own gradient function (for the y-direction) for a grayscale picture

__Lesson 4: Color Detection__
* Bitwise operations
* Error Handling in Python
* Another color coding system (HSV = Hue, Saturation and Value)
* Finding contours

__Lesson 5: Shape Detection__
* Shapes
* SMore on contours
* SCentroid and Area from Contours
* Occulsion

__Lesson 6: Shape Detection__
* Angles
* Distance
* Distortions

## Environment
The instructions below have been tested on Python 3.7.
I mainly use Anaconda https://www.anaconda.com/products/individual > Products > Individual Edition
as my virtual environment and install the necessary packages.

Here are the steps in creating your environment:

1. Install Anaconda according to the instructions for your operating system.

2. Create a python 3.8 with the basic packages as follows in your terminal via command line for Mac OS.
For Windows, you will need to use the __"Anaconda Prompt"__ and not the generic Window's Prompt.

<pre><code>
   prompt> conda create -n py38cv python=3.8 conda numpy scipy
</code></pre>

It will ask you to confirm the installation of package, you enter "y" to confirm.

3. Activate your environment

<pre><code>
   prompt> conda activate py38cv
</code></pre>

4. Install image processing libraries

<pre><code>
   prompt> conda install -c conda-forge scikit-image
</code></pre>

5. Install image processing functions

<pre><code>
   prompt> conda install -c conda-forge imutils
</code></pre>

6. Install OpenCV if not already installed

<pre><code>
   prompt> conda install -c conda-forge opencv
   </code></pre>

7. To verify your environment, invoke the python interactive command prompt by executing "python" in your terminal.

<pre><code>
   prompt> python

   Python 3.8.5 | packaged by conda-forge | (default, Jul 31 2020, 02:18:36)
   [Clang 10.0.1 ] on darwin
   >>>
</code></pre>

8. Type the following package import at the prompt:

<pre><code>
   >>> from skimage.measure import compare_ssim
   >>> import argparse
   >>> import imutils
   >>> import cv2
   >>> import numpy as np
   >>> print(cv2.__version__)

   >>> 4.4.0     # this can return any 4.x.x version depending on your operating system and when you installed opencv

</code></pre>

9. To exit from the python interactive session, type exit() and hit return.

<pre><code>
   >>> exit()
</code></pre>

You should encounter no errors.  Now your environment is ready to go for the lessons.

#### Windows Environment Troubleshooting

If you have issues importing imutils, try the following to install imutils.

<pre><code>
   prompt> conda install pip
   prompt> pip install imutils
</code></pre>

Or, for Windows 10 64-bit, try:
<pre><code>
   prompt> conda install -c pjamesjoyce imutils
</code></pre>


## Jupyter Notebook IDE

If you set up your python environment using Anaconda, you will
be able to run the Jupyter Notebook IDE for python.  To start the Notebook IDE,
activate the py38cv environment. Your prompt will change to (py38cv) when your
environment is activated and execute "jupyter notebook" as follows.

<pre><code>

   (base)> activate py38cv
   (py38cv)> jupyter notebook

</code></pre>

This will start the Notebook IDE in your preferred browser as http://localhost:8888/?token=xxxx .
You can always grab the link and paste it in your browser if needed.

To exit your Notebook environment, just save your notebook and close all Jupyter notebook tabs in your browser.
On the command prompt from where your notebook was launched, run Ctrl-C to stop the IDE and type "y" <hit return> to confirm.
To deactivate your python environment run "conda deactivate".

Note: __DO NOT USE the Anaconda Navigator__ (the GUI) to launch your Juypter notebook as it will not
initiate your py38cv environment as required for these lessons.

<pre><code>

   >>> Ctrl-C [enter]
   >>> conda deactivate

</code></pre>

#### Windows Environment Troubleshooting

If you have trouble running "jupyter notebook", try installing or re-installing jupyter package.

<pre><code>
   prompt> conda install -c anaconda jupyter
</code></pre>


#### Jupyter Lab

Jupyter Lab provides the same functionality as Jupyter notebook but with better navigation.
To get Jupyter Lab, install the following in your environment.

<pre><code>
   prompt> conda install -c conda-forge jupyterlab
</code></pre>
