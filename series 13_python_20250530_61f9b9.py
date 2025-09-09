{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h1>سری ۱۳: کنترل مقاوم و بهینه</h1>\n",
    "<h3>دانشگاه: صنعتی شریف</h3>\n",
    "<h3>نام دانشجو: محمد رضایی</h3>\n",
    "<h3>استاد: دکتر علی محمدی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۱. حل معادله ریکاتی</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "\\dot{x} = x + u \\quad,\\quad J = \\int_0^\\infty (x^2 + u^2) dt\n",
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
    "from scipy.linalg import solve_continuous_are\n",
    "\n",
    "# تعریف سیستم\n",
    "A = np.array([[1]])\n",
    "B = np.array([[1]])\n",
    "Q = np.array([[1]])\n",
    "R = np.array([[1]])\n",
    "\n",
    "# حل معادله ریکاتی\n",
    "P = solve_continuous_are(A, B, Q, R)\n",
    "K = np.linalg.inv(R) @ B.T @ P\n",
    "\n",
    "print(f\"مقدار P: {P[0,0]:.4f}\")\n",
    "print(f\"بهینه‌ترین کنترل: u = -{K[0,0]:.4f}x\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۲. طراحی کنترل‌کننده H∞</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "G(s) = \\frac{1}{s-1} \\quad,\\quad W(s) = \\frac{s+1}{s+10}\n",
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
    "# تعریف سیستم‌ها\n",
    "s = ct.tf('s')\n",
    "G = 1/(s-1)\n",
    "W = (s+1)/(s+10)\n",
    "\n",
    "# طراحی کنترل‌کننده (شبیه‌سازی شده)\n",
    "K = 100*(s+1)/(s+20)\n",
    "\n",
    "# تحلیل عملکرد\n",
    "T = ct.feedback(G*K, 1)\n",
    "t, y = ct.step_response(T)\n",
    "\n",
    "plt.figure(figsize=(10,4))\n",
    "plt.plot(t, y)\n",
    "plt.title('پاسخ پله سیستم با کنترل‌کننده H∞', fontname='B Nazanin')\n",
    "plt.xlabel('زمان', fontname='B Nazanin')\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۳. طراحی کنترل‌کننده LQR</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "\\dot{x} = \\begin{bmatrix}0 & 1\\\\-1 & -2\\end{bmatrix}x + \\begin{bmatrix}0\\\\1\\end{bmatrix}u\n",
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
    "# پارامترهای طراحی\n",
    "A = np.array([[0, 1], [-1, -2]])\n",
    "B = np.array([[0], [1]])\n",
    "Q = np.eye(2)\n",
    "R = 1\n",
    "\n",
    "# محاسبه کنترل‌کننده\n",
    "P = solve_continuous_are(A, B, Q, R)\n",
    "K = np.linalg.inv(R) @ B.T @ P\n",
    "\n",
    "print(f\"ماتریس بهره کنترل: K = [{K[0,0]:.2f}, {K[0,1]:.2f}]\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 }
}