#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.67])
AC_INIT([project], [1], [reda@eurecom.fr])
AC_CONFIG_SRCDIR([src/lib_foo/foo.c])
AC_CONFIG_HEADERS([config.h])
AM_INIT_AUTOMAKE([foreign])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.
AC_PROG_RANLIB

# Checks for header files.
AC_COMPILE_IFELSE(
	[AC_LANG_PROGRAM([[#include <mistery.h>]], [[mistery_value(1);]])],
	[AC_DEFINE([MISTERY_VALUE_ONEPARAM], [], [IN ORDER TO SELECT FUNCTION WITH ONE PARAMETER])],
	[AC_DEFINE([MISTERY_VALUE_TWOPARAM], [], [IN ORDER TO SELECT FUNCTION WITH TWO PARAMETERS])])

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.
AC_SEARCH_LIBS([mistery_value], [magic voodoo mistery], [], [AC_MSG_ERROR([Libraries not found])])

AC_CONFIG_FILES([Makefile
                 src/Makefile
                 src/lib_foo/Makefile
                 src/main/Makefile])
AC_OUTPUT
