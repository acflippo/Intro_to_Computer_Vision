# Introduction to Computer Vision

This is an introduction to Computer Vision using Python.
I will be using online resources and examples whenever it is available.
I'll provide inline reference to the source code, discussions
and inspiration.

## Environment
The instructions below have been tested on Python 3.7.
I mainly use Anaconda https://www.anaconda.com/products/individual > Products > Individual Edition
as my virtual environment and install the necessary packages.

Here are the steps in creating your environment:

1. Install Anaconda according to instructions for your operating system.

2. Create a python 3.7 with the basic packages as follows in your terminal via command line.

<pre><code>
   prompt> conda create -n py37cv python=3.7 conda numpy scipy
</code></pre>

3. Activate your environment

<pre><code>
   prompt> conda activate py37cv
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

7. To verify your environment, invoke the python interactive command prompt by typing "python" in your terminal.

<pre><code>
   prompt> python

   Python 3.7.7 (default, May  6 2020, 04:59:01)
   [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
   >>>
</code></pre>

8. Type the following package import at the prompt:

<pre><code>
   >>> from skimage.measure import compare_ssim
   >>> import argparse
   >>> import imutils
   >>> import cv2
   >>> import numpy as np
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
execute the following command line in your prompt.

<pre><code>

   >>> activate py37cv
   >>> jupyter notebook

</code></pre>

This will start the Notebook IDE in your preferred browser as http://localhost:8888/?token=xxxx .
You can always grab the link and paste it in your browser if needed.

To exit your Notebook environment, just save your notebook and close all Jupyter notebook tabs in your browser.
On the command prompt from where your notebook was launched, run Ctrl-C to stop the IDE and type "y" <hit return> to confirm.

#### Windows Environment Troubleshooting

If you have trouble running "jupyter notebook", try installing or re-installing jupyter package.

<pre><code>
   prompt> conda install -c anaconda jupyter
</code></pre>
