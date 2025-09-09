{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### سری 3: طراحی جبران‌ساز\n",
    "11. طراحی جبران‌ساز پیش‌فاز با:\n",
    "    \\[ \\phi_m = 30^\\circ, \\omega_m = 2 \\text{ rad/s} \\]\n",
    "    پاسخ:\n",
    "    \\[ G_c(s) = \\frac{1 + aTs}{1 + Ts} \\]\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# طراحی جبران‌ساز\n",
    "from control import lead_compensator\n",
    "Gc = lead_compensator(30, 2)  # تقریبی\n",
    "print(\"جبران‌ساز:\", Gc)"
   ]
  }
 ]
}