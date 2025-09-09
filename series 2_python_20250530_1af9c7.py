{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### سری 2: تحلیل پایداری با روش‌های ریاضی\n",
    "6. آرایه راث-هرویتز برای معادله مشخصه:\n",
    "   \\[ s^3 + 4s^2 + 6s + 4 = 0 \\]\n",
    "   پاسخ:\n",
    "   همه ضرایب مثبت → سیستم پایدار.\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# تحلیل پایداری با کنترل تولباکس\n",
    "import control as ct\n",
    "G = ct.tf([1], [1, 4, 6, 4])\n",
    "print(\"قطب‌های سیستم:\", ct.pole(G))"
   ]
  }
 ]
}