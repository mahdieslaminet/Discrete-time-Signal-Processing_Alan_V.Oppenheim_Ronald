{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h1>سری ۱۴: سیستم‌های چندمتغیره</h1>\n",
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
    "<h2>۱. بررسی کنترل‌پذیری</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "\\dot{x} = \\begin{bmatrix}0 & 1\\\\-2 & -3\\end{bmatrix}x + \\begin{bmatrix}1\\\\0\\end{bmatrix}u\n",
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
    "# تعریف سیستم\n",
    "A = np.array([[0, 1], [-2, -3]])\n",
    "B = np.array([[1], [0]])\n",
    "\n",
    "# محاسبه ماتریس کنترل‌پذیری\n",
    "C = ct.ctrb(A, B)\n",
    "rank = np.linalg.matrix_rank(C)\n",
    "\n",
    "print(f\"رتبه ماتریس کنترل‌پذیری: {rank}\")\n",
    "if rank == A.shape[0]:\n",
    "    print(\"سیستم کنترل‌پذیر است\")\n",
    "else:\n",
    "    print(\"سیستم کنترل‌پذیر نیست\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۲. تبدیل تابع انتقال به فضای حالت</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "G(s) = \\frac{s+1}{s^2 + 5s + 6}\n",
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
    "# تعریف تابع انتقال\n",
    "num = [1, 1]\n",
    "den = [1, 5, 6]\n",
    "G = ct.tf(num, den)\n",
    "\n",
    "# تبدیل به فضای حالت\n",
    "sys_ss = ct.tf2ss(G)\n",
    "\n",
    "print(\"ماتریس A:\")\n",
    "print(sys_ss.A)\n",
    "print(\"\\nماتریس B:\")\n",
    "print(sys_ss.B)\n",
    "print(\"\\nماتریس C:\")\n",
    "print(sys_ss.C)\n",
    "print(\"\\nماتریس D:\")\n",
    "print(sys_ss.D)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۳. پاسخ پله سیستم MIMO</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "G(s) = \\begin{bmatrix}\\frac{1}{s+1} & \\frac{2}{s+2}\\\\\\frac{1}{s+3} & \\frac{1}{s+4}\\end{bmatrix}\n",
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
    "# تعریف سیستم MIMO\n",
    "G11 = ct.tf([1], [1, 1])\n",
    "G12 = ct.tf([2], [1, 2])\n",
    "G21 = ct.tf([1], [1, 3])\n",
    "G22 = ct.tf([1], [1, 4])\n",
    "\n",
    "G = ct.interconnect(\n",
    "    [G11, G12, G21, G22],\n",
    "    connections=[[1, 1], [2, 1], [3, 2], [4, 2]],\n",
    "    inplist=[1, 2],\n",
    "    outlist=[1, 2]\n",
    ")\n",
    "\n",
    "# پاسخ به ورودی [1; 0]\n",
    "t, y = ct.step_response(G, input=0, output=0)\n",
    "plt.figure(figsize=(10,4))\n",
    "plt.plot(t, y)\n",
    "plt.title('پاسخ پله سیستم MIMO برای ورودی [1; 0]', fontname='B Nazanin')\n",
    "plt.xlabel('زمان', fontname='B Nazanin')\n",
    "plt.legend(['خروجی 1', 'خروجی 2'])\n",
    "plt.grid()\n",
    "plt.show()"
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