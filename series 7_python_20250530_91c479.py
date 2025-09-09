{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "## سری ۷: تحلیل پاسخ گذرا و جبرانسازی\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### ۱. زمان نشست و فراجهش\n",
    "**برای سیستم $T(s) = \\frac{9}{s^2+2s+9}$**\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "wn = 3\n",
    "zeta = 1/3\n",
    "os = np.exp(-zeta*np.pi/np.sqrt(1-zeta**2))*100\n",
    "ts = 4/(zeta*wn)\n",
    "print(f\"فراجهش: {os:.1f}%\\nزمان نشست: {ts:.1f} ثانیه\")"
   ]
  }
 ],
 "metadata": {}
}