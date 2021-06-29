# -*- coding: utf-8 -*-
# This script will hold callable and objects both services use


# Clean this up!!!
# Regex for YYYY-MM-DDDD or MM-DDDD-YYYY
proper_dates = (
    r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])|"
    r"^(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])-\d{4}"
)
