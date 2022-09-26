# NN_from_let_rec

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> </p>


20 epochs were passed for a dataset of 370K letters.


loss 0.1561


## Structure

```
Net(
  (c1): Linear(in_features=784, out_features=800, bias=True)
  (c2): Linear(in_features=800, out_features=500, bias=True)
  (c3): Linear(in_features=500, out_features=500, bias=True)
  (c4): Linear(in_features=500, out_features=400, bias=True)
  (c5): Linear(in_features=400, out_features=26, bias=True)
)
```

ReLU activation function


## Installation dependencies and run

Clone the project

```bash
  git clone https://github.com/artem-8178/NN_from_let_rec
```

Go to the project directory

```bash
  cd NN_from_let_rec
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run

```bash
  python main.py
```
