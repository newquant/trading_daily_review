# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author: zhnlk
from openpyxl.styles import Border, Side, Alignment, Font, NamedStyle


def highlight_style():
    normal = NamedStyle("highlight")
    normal.font = Font(bold=True, size=20)

    # style = CellStyle()
    normal.border = Border(Side(style='thin', color="000000"),
                           Side(style='thin', color="000000"),
                           Side(style='thin', color="000000"),
                           Side(style='thin', color="000000"))

    normal.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    return normal


def normal_style():
    style2 = NamedStyle("normal")
    style2.font = Font(size=12, color="000000")
    # XSSFFont font = (XSSFFont) workbook.CreateFont()
    # font.FontHeight = 400.0
    # style2.SetFont(font)
    style2.alignment = Alignment(horizontal='center', wrap_text=True)
    return style2
