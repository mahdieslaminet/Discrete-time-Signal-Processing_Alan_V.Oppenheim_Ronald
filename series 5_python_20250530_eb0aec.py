{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "## سری 5: ترکیب سوالات اثباتی، محاسباتی، فضای حالت و طراحی جبرانساز\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### 1. سوال اثباتی\n",
    "**اثبات کنید سیستم با تابع انتقال حلقه باز $G(s) = \\frac{K}{s(s+1)(s+2)}$ برای $K > 6$ ناپایدار است.**\n",
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
    "import numpy as np\n",
    "\n",
    "# تعریف تابع انتقال\n",
    "K = 7  # مقدار بیشتر از 6\n",
    "G = ct.tf([K], [1, 3, 2, 0])\n",
    "\n",
    "# محاسبه قطب‌های سیستم حلقه بسته\n",
    "T = ct.feedback(G, 1)\n",
    "poles = ct.pole(T)\n",
    "print(\"قطب‌های سیستم برای K=7:\", poles)\n",
    "print(\"سیستم ناپایدار است زیرا قطب‌ها با بخش حقیقی مثبت وجود دارند:\", any(np.real(poles) > 0))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### 2. سوال محاسباتی (1)\n",
    "**پاسخ پله سیستم $T(s) = \\frac{10}{s^2 + 4s + 10}$ را محاسبه کنید.**\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# محاسبه پاسخ پله\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "T = ct.tf([10], [1, 4, 10])\n",
    "t, y = ct.step_response(T)\n",
    "\n",
    "plt.plot(t, y)\n",
    "plt.title('پاسخ پله سیستم')\n",
    "plt.xlabel('زمان (ثانیه)')\n",
    "plt.ylabel('پاسخ')\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### 3. سوال محاسباتی (2)\n",
    "**مقدار بهره $K$ را طوری تعیین کنید که سیستم $G(s) = \\frac{K}{s(s+1)}$ دارای حاشیه فاز $45^\\circ$ باشد.**\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# محاسبه K برای PM=45 درجه\n",
    "import numpy as np\n",
    "\n",
    "# تابع برای محاسبه حاشیه فاز\n",
    "def find_k_for_pm(pm_desired=45):\n",
    "    pm_rad = np.deg2rad(pm_desired)\n",
    "    omega_c = 1.0  # از حل تحلیلی\n",
    "    K = omega_c * np.sqrt(omega_c**2 + 1)\n",
    "    return K\n",
    "\n",
    "K = find_k_for_pm(45)\n",
    "print(\"مقدار بهره K برای PM=45 درجه:\", K)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### 4. سوال فضای حالت\n",
    "**سیستم زیر را از نظر کنترل‌پذیری و مشاهده‌پذیری بررسی کنید:**\n",
    "\\[\n",
    "\\dot{x} = \\begin{bmatrix} 0 & 1 \\\\ -2 & -3 \\end{bmatrix}x + \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}u, \\quad y = \\begin{bmatrix} 1 & 0 \\end{bmatrix}x\n",
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
    "# بررسی کنترل‌پذیری و مشاهده‌پذیری\n",
    "A = np.array([[0, 1], [-2, -3]])\n",
    "B = np.array([[0], [1]])\n",
    "C = np.array([[1, 0]])\n",
    "\n",
    "# ماتریس کنترل‌پذیری\n",
    "C_ctrl = np.hstack((B, A @ B))\n",
    "print(\"ماتریس کنترل‌پذیری:\\n\", C_ctrl)\n",
    "print(\"رتبه ماتریس:\", np.linalg.matrix_rank(C_ctrl))\n",
    "\n",
    "# ماتریس مشاهده‌پذیری\n",
    "C_obs = np.vstack((C, C @ A))\n",
    "print(\"\\nماتریس مشاهده‌پذیری:\\n\", C_obs)\n",
    "print(\"رتبه ماتریس:\", np.linalg.matrix_rank(C_obs))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### 5. سوال طراحی جبرانساز\n",
    "**برای سیستم $G(s) = \\frac{1}{s(s+1)}$، یک جبرانساز پس‌فاز طراحی کنید تا خطای حالت ماندگار برای ورودی پله کمتر از 0.01 باشد.**\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# طراحی جبرانساز پس‌فاز\n",
    "K = 100\n",
    "a = 0.1\n",
    "T = 10\n",
    "G_lag = ct.tf([K*a*T, K], [T, 1])\n",
    "G_sys = ct.tf([1], [1, 1, 0])\n",
    "\n",
    "# سیستم جبرانساز شده\n",
    "G_comp = G_lag * G_sys\n",
    "\n",
    "# محاسبه خطای حالت ماندگار\n",
    "Kp = ct.dcgain(G_comp)\n",
    "ess = 1/(1 + Kp)\n",
    "print(\"خطای حالت ماندگار:\", ess)"
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
   "name": "python",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}