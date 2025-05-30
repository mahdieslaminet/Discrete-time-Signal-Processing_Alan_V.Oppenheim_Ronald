{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h1>سری ۱۷: کنترل مقاوم و بهینه‌سازی چندهدفه</h1>\n",
    "<h3>دانشگاه: صنعتی شریف</h3>\n",
    "<h3>نام دانشجو: علیرضا حسینی</h3>\n",
    "<h3>استاد: دکتر محمدی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۱. طراحی کنترل‌کننده H∞ برای سیستم نامعین</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "G(s) = \\frac{1}{s^2 + as + b}, \\quad 2 \\leq a \\leq 4, \\quad 1 \\leq b \\leq 3\n",
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
    "import numpy as np\n",
    "import control as ct\n",
    "from scipy import signal\n",
    "\n",
    "# تعریف سیستم نامعین\n",
    "a_values = np.linspace(2, 4, 5)\n",
    "b_values = np.linspace(1, 3, 5)\n",
    "\n",
    "# طراحی کنترل‌کننده\n",
    "s = ct.tf('s')\n",
    "K = 50*(s**2 + 3*s + 3)/((s+10)*(s+20))\n",
    "\n",
    "# تحلیل پایداری برای تمام ترکیبات\n",
    "for a in a_values:\n",
    "    for b in b_values:\n",
    "        G = 1/(s**2 + a*s + b)\n",
    "        T = ct.feedback(G*K, 1)\n",
    "        print(f\"a={a:.1f}, b={b:.1f} => پایداری: {ct.is_stable(T)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۲. طراحی کنترل‌کننده LQG/LTR</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "\\dot{x} = \\begin{bmatrix} 0 & 1 \\\\ -2 & -3 \\end{bmatrix}x + \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}u + w\n",
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
    "# پیاده‌سازی LQG\n",
    "A = np.array([[0, 1], [-2, -3]])\n",
    "B = np.array([[0], [1]])\n",
    "C = np.array([[1, 0]])\n",
    "Q = np.eye(2)\n",
    "R = 0.1\n",
    "\n",
    "# حل معادلات ریكاتی\n",
    "P = ct.care(A.T, C.T, Q, R)[0]\n",
    "Kf = P @ C.T @ np.linalg.inv(R)\n",
    "print(f\"ماتریس بهره فیلتر کالمن:\\n{Kf}\")"
   ]
  }
 ],
 "metadata": {}
}