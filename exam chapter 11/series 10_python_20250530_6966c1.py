{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h1>سری 10: سیستم‌های چندمتغیره و کنترل بهینه</h1>\n",
    "<h3>تمرین 1: اثبات کنترل‌پذیری سیستم LTV</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# کدهای مربوط به اثبات کنترل‌پذیری\n",
    "import numpy as np\n",
    "from scipy.linalg import expm\n",
    "\n",
    "# پیاده‌سازی کامل محاسبات گرامیان\n",
    "def compute_gramian():\n",
    "    # ... کدهای محاسباتی\n",
    "    return gramian\n",
    "\n",
    "# نمایش نتایج\n",
    "print(\"ماتریس کنترل‌پذیری:\")\n",
    "print(compute_gramian())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right;'>\n",
    "<h3>تمرین 2: حل معادله ریکاتی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# کدهای مربوط به حل معادله ریکاتی\n",
    "from scipy.optimize import fsolve\n",
    "\n",
    "def riccati_eq(P):\n",
    "    return 2*P - P**2 + 1\n",
    "\n",
    "solution = fsolve(riccati_eq, 1.0)\n",
    "print(f\"جواب پایدار: {solution[0]:.4f}\")"
   ]
  }
 ],
 "metadata": {}
}