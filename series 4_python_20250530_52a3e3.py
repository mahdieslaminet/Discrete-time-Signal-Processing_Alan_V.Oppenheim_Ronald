{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### سری 4: مسائل پیشرفته\n",
    "16. حساسیت تابع انتقال به تغییرات پارامتر K:\n",
    "    \\[ S_K^T = \\frac{1}{1 + KG(s)H(s)} \\]\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# محاسبه حساسیت\n",
    "import sympy as sp\n",
    "s, K = sp.symbols('s K')\n",
    "G = 1/(s*(s+1))\n",
    "S = 1/(1 + K*G)\n",
    "display(S)"
   ]
  }
 ]
}