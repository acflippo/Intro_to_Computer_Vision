# Introduction to Computer Vision

This is an introduction to Computer Vision using Python.
I will be using online resources and examples whenever it is available.
I'll provide inline reference to the source code, discussions
and inspiration.

## Environment
The instructions below have been tested on Python 3.7
I mainly use Anaconda https://www.anaconda.com/
or Miniconda https://docs.conda.io/en/latest/miniconda.html
as my virtual environment and install the necessary packages.

Here are the steps in creating your environment:

1. Install Anaconda or Miniconda according to instructions for your operating system.

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

8. Type or copy all the packages import from the beginning of Lesson 1's intro_cv_lesson1.py at the prompt:

<pre><code>

   >>> from skimage.measure import compare_ssim
   >>> import argparse
   >>> import imutils
   >>> import cv2
   >>> import numpy as np
   >>>

</code></pre>

9. To exit from the python interactive session, type exit() and hit return.

<pre><code>

   >>> exit()

</code></pre>

You should encounter no errors.  Now your environment is ready to go for the lessons.
