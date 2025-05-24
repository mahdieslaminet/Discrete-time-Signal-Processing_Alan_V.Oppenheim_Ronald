{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### تحلیل نیکوئیست سیستم\n",
    "```python\n",
    "import control\n",
    "G = control.tf([1],[1,2,2,0])\n",
    "control.nyquist_plot(G)\n",
    "```\n",
    "مقدار بحرانی K: $K_{cr}=4$"
   ]
  }
 ]
}