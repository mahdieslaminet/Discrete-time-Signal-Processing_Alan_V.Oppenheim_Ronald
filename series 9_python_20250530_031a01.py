{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "## سری ۸: سیستم‌های چندمتغیره\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div dir='rtl'>\n",
    "### ۱. کنترل‌پذیری سیستم\n",
    "**بررسی سیستم $\\dot{x} = Ax + Bu$**\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "A = np.array([[0,1],[-2,-3]])\n",
    "B = np.array([[0],[1]])\n",
    "C = np.array([[1,0]])\n",
    "sys = ct.ss(A,B,C,0)\n",
    "print(\"کنترل‌پذیر:\", ct.ctrb(A,B).shape[1] == np.linalg.matrix_rank(ct.ctrb(A,B)))"
   ]
  }
 ],
 "metadata": {}
}