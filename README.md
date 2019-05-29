# intro-probabilistic-programming
Introduction to the concepts and tools behind probabilistic programming

#### Topics
* Fundamental Concepts
* Intro to Bayesian Inference
* Tools
  * Python Scientific Suite
    * `numpy`
    * `scipy`
    * `matplotlib`
    * `pandas`
    * `scikit-learn`
  * Tools for probabilistic programming
    * `statsmodels`
    * `pymc3`
    * `pyro`
    * `tensorflow-probability`

#### Installation tips

Convention: python3 `(3.6.8)`

To install `statsmodels`
```asciidoc
pip install statsmodels
```

To install `pymc3 (3.6)`. Including 
the factor 3 is important otherwise you will install
pymc2.
```asciidoc
pip install pymc3
```
Simple idea about pymc, python in all cases and
the _calculation_ part:
* pymc2: fortran
* pymc3: Theano
* pymc4: TensorFlow (coming months - rumour says)

Complementary tool for plotting and visualisation: `ArviZ (0.4.0)`
```asciidoc
pip install arviz
```
To avoid a potential warning related to `theano` after calling pymc3
```asciidoc
`conda install mkl-service`
```
To install tensorflow, version `(1.13.1)` via
`pip` although version `1.14.0rc0` and `2.0.0a0` also 
available.
```asciidoc
pip install tensorflow
```

To install `tensorflow-probability (0.6.0)`, after installing tensorflow
```asciidoc
pip install tensorflow-probability
```

To install the pyro suite, you need to install the
pytorch suite
```asciidoc
pip install torch
```
After this verify the installation of torch by 
simply calling
```asciidoc
>>> import torch
```
If you get an error in the lines of
```asciidoc
... from torch._C import *
... Library not loaded: /usr/local/opt/libomp/lib/libomp.dylib
... ***.dylib
...
Reason: image not found
the following might solve it
```
The following might solve it
```asciidoc
brew install libomp
```
After confirming the right installation of
pytorch, simply install the subsequent tools involving
the vision module (might not be required) and pyro.
```asciidoc
pip install torchvision  # might not be required
pip install pyro-ppl
```
