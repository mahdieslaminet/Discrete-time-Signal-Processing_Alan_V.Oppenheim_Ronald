{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right;'>\n",
    "<h1>سری 12: کنترل تطبیقی و هوشمند</h1>\n",
    "<h3>تمرین 1: همگرایی کنترل تطبیقی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# شبیه‌سازی کنترل تطبیقی\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "\n",
    "# پارامترهای سیستم\n",
    "a_real = 1.5\n",
    "gamma = 0.5\n",
    "t = np.linspace(0, 10, 100)\n",
    "\n",
    "# کدهای شبیه‌سازی\n",
    "# ...\n",
    "\n",
    "plt.plot(t, x_history)\n",
    "plt.title('پاسخ سیستم با کنترل تطبیقی')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right;'>\n",
    "<h3>تمرین 2: شبکه عصبی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# پیاده‌سازی شبکه عصبی ساده\n",
    "def neural_net(x):\n",
    "    w1 = np.array([1, -1])\n",
    "    return np.tanh(w1[0]*x) + np.tanh(w1[1]*x)\n",
    "\n",
    "print(\"خروجی شبکه برای x=1:\", neural_net(1.0))"
   ]
  }
 ],
 "metadata": {}
}