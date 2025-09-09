{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h1>سری ۱۹: چالش‌های پیاده‌سازی</h1>\n",
    "<h3>دانشگاه: تهران</h3>\n",
    "<h3>نام دانشجو: محسن کریمی</h3>\n",
    "<h3>استاد: دکتر شفیعی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۱. اثر کوانتیزاسیون در کنترل دیجیتال</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "G(s) = \\frac{1}{s(s+1)}\n",
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
    "# محاسبه خطای کوانتیزاسیون\n",
    "bits = 8\n",
    "V_range = 20  # ±10V\n",
    "delta = V_range / (2**bits)\n",
    "sigma = delta**2 / 12\n",
    "print(f\"توان نویز کوانتیزاسیون: {sigma:.6f} V^2\")"
   ]
  }
 ],
 "metadata": {}
}