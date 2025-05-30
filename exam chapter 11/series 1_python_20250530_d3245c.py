{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### سری 1: مدلسازی ریاضی و توابع انتقال\n",
    "1. تبدیل معادله دیفرانسیل به تابع انتقال:\n",
    "   \\[ \\frac{d^2y}{dt^2} + 3\\frac{dy}{dt} + 2y = u(t) \\]\n",
    "   پاسخ:\n",
    "   \\[ G(s) = \\frac{1}{s^2 + 3s + 2} \\]\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# حل با پایتون\n",
    "import control as ct\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "G = ct.tf([1], [1, 3, 2])\n",
    "print(\"تابع انتقال:\", G)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 }
}