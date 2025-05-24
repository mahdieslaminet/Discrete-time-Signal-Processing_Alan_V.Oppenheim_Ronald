{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### تبدیل معادله دیفرانسیل به تابع انتقال\n",
    "$$\\frac{d^2y}{dt^2} + 3\\frac{dy}{dt} + 2y = u(t) \\Rightarrow G(s) = \\frac{1}{s^2 + 3s + 2}$$\n",
    "\n",
    "### شبیه‌سازی پاسخ پله\n",
    "```python\n",
    "import control.matlab as cnt\n",
    "G = cnt.tf([1],[1,3,2])\n",
    "cnt.step(G)\n",
    "```"
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