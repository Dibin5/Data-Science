# ---------- QUERY ----------
msSQL_query = """
SELECT TOP (10)
      [Row ID],
      [Order ID],
      [Order Date],
      [Ship Date],
      [Ship Mode],
      [Customer ID],
      [Customer Name]
FROM [test].[dbo].[order_dibin]
"""
