{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h1>سری ۱۸: سیستم‌های هایبرید و کنترل پیشرفته</h1>\n",
    "<h3>دانشگاه: صنعتی امیرکبیر</h3>\n",
    "<h3>نام دانشجو: زهرا احمدی</h3>\n",
    "<h3>استاد: دکتر رضوی</h3>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div style='direction: rtl; text-align: right; font-family: B Nazanin;'>\n",
    "<h2>۱. تحلیل سیستم هایبرید</h2>\n",
    "<p>سیستم:</p>\n",
    "\\[\n",
    "\\dot{x} = \\begin{cases} \n",
    "-x + u & \\text{if } x \\geq 0 \\\\\n",
    "2x + u & \\text{if } x < 0 \n",
    "\\end{cases}\n",
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
    "# شبیه‌سازی سیستم هایبرید\n",
    "def hybrid_system(x, u):\n",
    "    return -x + u if x >= 0 else 2*x + u\n",
    "\n",
    "# پاسخ به شرایط اولیه مختلف\n",
    "x0_values = [-1, 0, 1]\n",
    "t = np.linspace(0, 5, 100)\n",
    "for x0 in x0_values:\n",
    "    sol = solve_ivp(lambda t, x: [hybrid_system(x[0], 0)], [0, 5], [x0], t_eval=t)\n",
    "    plt.plot(t, sol.y[0], label=f'x0={x0}')\n",
    "plt.legend()"
   ]
  }
 ],
 "metadata": {}
}