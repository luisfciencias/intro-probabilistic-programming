# Introduction to Probabilistic Programming
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
    * `statsmodels` -->  (https://www.statsmodels.org)
    * `pymc3`--> (https://docs.pymc.io)
    * `pyro`--> (http://pyro.ai)
    * `tensorflow-probability` --> (https://www.tensorflow.org/probability)

#### Installation tips

Convention: python3 `(3.6.8)` in my machine (mac), I think `3.7` should be fine. 
You might want to build an independent python environment to avoid messing up 
with your libraries.

Dependencies listed within `requirements.txt`.

Before following your instincts and make the call to
```asciidoc
pip install -r requirements.txt
``` 
There might be some potential issues at the `pyro-ppl` stage, considering
it depends on pytorch. If this is the case take a look at the bottom
to see the issue I experienced on my machine. If everything works fine, 
congratulations.

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
conda install mkl-service
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
