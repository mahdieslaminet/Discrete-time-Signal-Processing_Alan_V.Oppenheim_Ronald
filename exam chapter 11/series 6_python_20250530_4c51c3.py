{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "## سری ۶: تحلیل پایداری و پاسخ فرکانسی\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### ۱. اثبات پایداری سیستم\n",
    "**سیستم $G(s) = \\frac{K}{s(s+4)}$ برای همه $K>0$ پایدار است.**\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import control as ct\n",
    "import numpy as np\n",
    "\n",
    "K = 10  # مثال\n",
    "G = ct.tf([K], [1, 4, 0])\n",
    "T = ct.feedback(G, 1)\n",
    "poles = ct.pole(T)\n",
    "print(\"قطب‌های سیستم:\", poles)\n",
    "print(\"پایداری:\", all(np.real(poles) < 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### ۲. پاسخ ضربه سیستم\n",
    "**محاسبه پاسخ ضربه $T(s) = \\frac{5}{s^2+3s+5}$**\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "T = ct.tf([5], [1, 3, 5])\n",
    "t, y = ct.impulse_response(T)\n",
    "plt.plot(t, y)\n",
    "plt.title('پاسخ ضربه سیستم')\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {}
}