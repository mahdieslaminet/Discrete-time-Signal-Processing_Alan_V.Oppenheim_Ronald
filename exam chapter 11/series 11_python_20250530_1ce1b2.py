{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right;'>\n",
    "<h1>سری 11: سیستم‌های غیرخطی</h1>\n",
    "<h3>تمرین 1: اثبات پایداری اکپوننتسیال</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# تحلیل پایداری سیستم غیرخطی\n",
    "import sympy as sp\n",
    "\n",
    "x = sp.symbols('x')\n",
    "V = 0.5*x**2  # تابع لیاپانوف\n",
    "V_dot = sp.diff(V,x)*(-x**3) # مشتق\n",
    "print(\"مشتق تابع لیاپانوف:\")\n",
    "sp.simplify(V_dot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right;'>\n",
    "<h3>تمرین 2: خطی‌سازی فیدبک</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# کدهای خطی‌سازی\n",
    "x_eq = 1.0  # نقطه تعادل\n",
    "A_linear = 2*x_eq  # ماتریس ژاکوبین\n",
    "print(f\"ماتریس سیستم خطی‌شده: {A_linear}\")"
   ]
  }
 ],
 "metadata": {}
}