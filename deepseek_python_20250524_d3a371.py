{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### اثبات پایداری با راث-هرویتز\n",
    "```python\n",
    "import numpy as np\n",
    "from control import routh\n",
    "coeff = [1, 4, 6, 4]\n",
    "routh(coeff)  # نمایش آرایه راث\n",
    "```\n",
    "\n",
    "### طراحی جبرانساز PID\n",
    "$$G_c(s) = K_p + \\frac{K_i}{s} + K_ds$$\n",
    "پارامترهای پیشنهادی:\n",
    "- $K_p = 1.2$\n",
    "- $K_i = 0.5$\n",
    "- $K_d = 0.1$"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}