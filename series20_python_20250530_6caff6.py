{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h1>سری ۲۰: مسائل تحقیقاتی پیشرفته</h1>\n",
    "<h3>دانشگاه: خواجه نصیر</h3>\n",
    "<h3>نام دانشجو: فاطمه محمدی</h3>\n",
    "<h3>استاد: دکتر نجفی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۱. کنترل کوانتومی</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "\\dot{x} = -x + u, \\quad u \\in \\{ -1, 0, 1 \\}\n",
    "\\]\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# شبیه‌سازی کنترل کوانتومی\n",
    "def quantum_control(x):\n",
    "    return -1 if x > 0 else (1 if x < 0 else 0)\n",
    "\n",
    "# حل سیستم\n",
    "t = np.linspace(0, 10, 100)\n",
    "sol = solve_ivp(lambda t, x: [-x[0] + quantum_control(x[0])], [0, 10], [1.0], t_eval=t)\n",
    "plt.plot(t, sol.y[0])"
   ]
  }
 ],
 "metadata": {}
}